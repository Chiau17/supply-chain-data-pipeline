select 
    order_item_id,
    order_id,
    user_id,
    product_id,
    inventory_item_id,  
    created_at,
    sale_price
from {{ ref('stg_thelook_orderitems') }}
where status = 'Complete'  