# Write your MySQL query statement below


select Signups.user_id, 
  case
    when Confirmations.action is null then 0.00
    else round(sum(case when Confirmations.action="confirmed" then 1 else 0 End)/count(*),2)
  End as confirmation_rate
from Signups
left join confirmations
on Signups.user_id=Confirmations.user_id
group by Signups.user_id
order by Confirmations.user_id