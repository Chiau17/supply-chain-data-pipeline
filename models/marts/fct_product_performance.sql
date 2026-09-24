select product_id,
count(product_id) as sales_qty,
sum(sale_price) as sales_amount
from {{ref('int_active_order_items')}}
group by product_id
