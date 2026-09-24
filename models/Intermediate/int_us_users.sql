select user_id,
    first_name,
    last_name,
    email,
    age,
    gender,
    state,
    country,
    created_at
from {{ref('stg_thelook_users')}}
where country = 'Brasil'