select
    id as user_id,
    first_name,
    last_name,
    email,
    age,
    gender,
    state,
    country,
    created_at
from {{source('thelook_ecommerce','users')}}
/*from `bigquery-public-data.thelook_ecommerce.users`
*/