# Write your MySQL query statement below
select product_id, new_price  as price
from Products
where change_date='2019-08-16'

union all

select product_id, new_price  as price
from Products
where (change_date,product_id) in(
    select max(change_date),product_id
    from Products
    where change_date<'2019-08-16'
    group by product_id
)
and product_id not in(
    select product_id
    from Products 
    where change_date = '2019-08-16'
)

union all

select product_id, 10 as price
from Products
where change_date>'2019-08-16' and 
product_id not in(select product_id
    from Products
    where change_date<='2019-08-16'
    )
group by product_id