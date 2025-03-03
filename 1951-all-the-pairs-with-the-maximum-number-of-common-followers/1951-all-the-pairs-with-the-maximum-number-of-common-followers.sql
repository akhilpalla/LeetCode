# Write your MySQL query statement below
with

common_followers as (
  select
    r1.user_id as user1_id,
    r2.user_id as user2_id,
    count(*) as cnt_followers,
    max(count(*)) over () as max_cnt_followers
  from
    relations r1
  inner join
    relations r2
    on r1.user_id < r2.user_id
    and r1.follower_id = r2.follower_id
  group by
    user1_id,
    user2_id
)

select
  user1_id,
  user2_id
from
  common_followers
where
  cnt_followers = max_cnt_followers
;