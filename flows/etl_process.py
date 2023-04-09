from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials
import os

@task()
def transform(path: Path):
    """Read Parquet file from local path and perform data cleaning"""
    df = pd.read_parquet(path)
    return df

@task()
def write_bq(df: pd.DataFrame, company: str):
    """Write DataFrame to BigQuery"""
    gcp_credentials_block = GcpCredentials.load("zoomcamp-gcs-credentials")
    project_id = "prefect-de-zoomcamp-376500"
    destination_table = f"{project_id}.stock_data_table.{company}"
    df.to_gbq(
        destination_table=destination_table,
        project_id=project_id,
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        if_exists="append"
    )


@flow()
def etl_gcs_to_bq(company, gcs_path):
    """Main ETL flow to load data into Big Query"""
    df = transform(gcs_path)
    write_bq(df, company=company)


@task(retries=3)
def fetch(dataset_url: str):
    """Download CSV file from URL and return DataFrame"""
    df = pd.read_csv(dataset_url)
    return df

@task()
def write_local(df: pd.DataFrame, dataset_file: str):
    """Write DataFrame to local Parquet file and return file path"""
    df = df.assign(file_name=dataset_file)
    Path(f"Stock_data").mkdir(parents=True, exist_ok=True)
    path = Path(f"Stock_data/{dataset_file}.parquet")
    df.to_parquet(path, compression="gzip")
    return path

@task()
def write_gcs(path: Path):
    """Upload local Parquet file to Google Cloud Storage bucket"""
    gcp_block = GcsBucket.load("zoom-gcs")
    gcp_block.upload_from_path(from_path=path, to_path=path, timeout=120)

@flow(log_prints=True)
def etl_web_to_gcs(company: str):
    """Flow to download CSV file from web URL, write to local Parquet file, and upload to GCS bucket"""
    dataset_file = f"{company}"
    dataset_url = f"https://raw.githubusercontent.com/enochiankim/data-engineering-zoomcamp-2023_Final_Project/main/Stock_Data/Company/{dataset_file}.csv"
    df = fetch(dataset_url)
    path = write_local(df, dataset_file)
    write_gcs(path)
    return path

@flow(log_prints=True)
def etl_parent_flow(companies):
    """Orchestrate ETL process for multiple companies"""
    for company in companies:
        gcs_path = etl_web_to_gcs(company=company)
        etl_gcs_to_bq(company=company, gcs_path=gcs_path)

if __name__ == "__main__":
    companies = ["Amazon", "Apple", "Facebook", "Google", "Netflix"]
    etl_parent_flow(companies)
