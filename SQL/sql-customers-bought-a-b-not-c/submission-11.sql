-- Write your query below
with x as (select customer_id from orders group by customer_id
having sum(case when product_name = 'A' then 1 else 0 end ) >0 and sum(case when product_name='B' then 1 else 0 end)>0 and sum(case when product_name='C' then 1 else 0 end)=0 
)

select * from customers where customer_id in (select customer_id from x) order by customer_name;