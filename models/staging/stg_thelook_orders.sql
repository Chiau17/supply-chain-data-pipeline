select order_id,
user_id,
status,
created_at,
shipped_at,
delivered_at,
returned_at
from {{source('thelook_ecommerce','orders')}}