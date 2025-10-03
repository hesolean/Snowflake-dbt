{{ config(materialized='table')}}

WITH COUNTRIES AS (
    SELECT 
        ID,
        NUMBER,
        STREET,
        CITY,
        POSTCODE,
        COUNTRY
    FROM {{ source('WW_Adress_Data', 'OPENADDRESS')}}
    WHERE COUNTRY='us'
)

SELECT * FROM COUNTRIES
