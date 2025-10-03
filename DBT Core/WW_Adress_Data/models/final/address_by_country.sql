{% set countries = var('country_list') %}


SELECT 
    ID,
    NUMBER,
    STREET,
    CITY,
    POSTCODE,
    COUNTRY
FROM {{ source('WW_Adress_Data', 'OPENADDRESS') }}
WHERE COUNTRY IN (
    {% for country in countries %}
        '{{ country }}'{% if not loop.last %}, {% endif %}
    {% endfor %}
)
