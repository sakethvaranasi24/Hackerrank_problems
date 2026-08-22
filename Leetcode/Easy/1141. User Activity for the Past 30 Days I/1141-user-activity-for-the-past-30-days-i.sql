# Write your MySQL query statement below

SELECT activity_date as 'day',count(DISTINCT user_id) as 'active_users'
from activity
where activity_date BETWEEN date_sub('2019-07-27',interval 29 day) and '2019-07-27'
GROUP BY
 activity_date;