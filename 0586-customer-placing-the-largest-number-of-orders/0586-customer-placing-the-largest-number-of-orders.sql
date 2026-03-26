-- select distinct(customer_number) from orders
-- where order_number in (select max(order_number) from orders);
-- only 7/19 testcases passes

select customer_number from orders
group by customer_number
order by count(order_number) desc
limit 1;