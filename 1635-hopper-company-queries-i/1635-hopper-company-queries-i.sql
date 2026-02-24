# Write your MySQL query statement below

with recursive cte as (
    select '2019-12-01' as month_all from dual
    union all
    select date_add(month_all, interval 1 month) as month_all from cte
    where month_all<'2020-12-01'
), 

passenger as (
SELECT 
    left(c.requested_at ,7) as requested_at,
    count(distinct d.ride_id) as accepted_rides
FROM Rides c
inner join AcceptedRides d
on c.ride_id = d.ride_id 
group by 1
),

driver_count as (
SELECT 
    a.month_all as driver_month,
    count(b.driver_id) over(order by a.month_all) as active_drivers
FROM cte a
left join DRIVERS b
on left(a.month_all,7) = left(b.JOIN_DATE,7))


-- select * from driver_count

select 
    month(driver_month) as month, 
    active_drivers,
    coalesce(accepted_rides,0) as accepted_rides 
from driver_count a
left join passenger b
on left(a.driver_month,7) = requested_at
where year(driver_month)=2020
group by 1,2,3