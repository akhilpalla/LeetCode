select product_id ,
    sum(IF(store='store1' , price , NULL)) as store1,
    sum(IF(store='store2' , price , NULL))  as store2,
    sum(IF(store='store3' , price , NULL))  as store3
from Products
group by product_id