{{ config(materialized='table') }}

select
    Company,
    Stock_Symbol
from {{ source('faang_stock_data', 'Stock_Symbol') }}