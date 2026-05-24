# Write your MySQL query statement below
with seasonal as (

SELECT
    products.category,
    SUM(sales.quantity) AS total_quantity,
    SUM(sales.quantity * sales.price) AS total_revenue,

    CASE
        WHEN MONTH(sales.sale_date) IN (12, 1, 2) THEN 'Winter'
        WHEN MONTH(sales.sale_date) IN (3, 4, 5) THEN 'Spring'
        WHEN MONTH(sales.sale_date) IN (6, 7, 8) THEN 'Summer'
        WHEN MONTH(sales.sale_date) IN (9, 10, 11) THEN 'Fall'
    END AS season

FROM sales

JOIN products
    ON sales.product_id = products.product_id

GROUP BY
    products.category,
    season
),
ranked as (
    select season, category,total_quantity,total_revenue,
    row_number() over(partition by season order by total_quantity desc , total_revenue desc) as ran
    from seasonal
)

select 
season,
category,
total_quantity,
total_revenue
from ranked
where ran=1
order by season

