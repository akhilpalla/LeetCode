# Write your MySQL query statement below
with TopInvoices as
(select 
pu.invoice_id,
rank() over (order by sum(pu.quantity * pr.price) desc, invoice_id ) as my_rank
from Purchases pu
join Products pr
on pu.product_id = pr.product_id
group by pu.invoice_id)

, TopInvoice as
(select
*
from TopInvoices
where my_rank = 1)

select
pu.product_id,
pu.quantity,
pu.quantity * pr.price as price
from TopInvoice ti
join Purchases pu
on ti.invoice_id = pu.invoice_id
join Products pr
on pu.product_id = pr.product_id