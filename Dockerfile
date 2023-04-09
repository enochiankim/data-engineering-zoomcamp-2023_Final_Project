FROM prefecthq/prefect:2.7.7-python3.9

COPY docker-requirements.txt .

RUN pip install -r docker-requirements.txt --trusted-host pypi.python.org --no-cache-dir

RUN mkdir -p /opt/prefect/data/stocks

COPY flows /opt/prefect/flows
COPY blocks /opt/prefect/blocks
COPY terraform /opt/prefect/terraform
COPY Stock_Data /opt/prefect/Stock_Data