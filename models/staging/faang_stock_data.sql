{{ config(materialized='table') }}

select
    Date,
    Open,
    High,
    Low,
    Close,
    Adj_Close,
    Volume,
    file_name
from {{ source('faang_stock_data', 'faang_stock_data_partitioned') }}