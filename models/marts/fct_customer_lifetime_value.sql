with user_base as(
    select * from {{ref('stg_thelook_users')}}
),
order_items as(
    select * from {{ref("int_active_order_items")}}
)
select u.user_id,
u.country,
u.state,
count(distinct o.order_id) as total_orders,
sum(o.sale_price) as lifetime_spend,
min(o.created_at) as min_date,
max(o.created_at) as max_date
from user_base u
left join order_items o
on u.user_id = o.user_id
group by u.user_id, u.country, u.state