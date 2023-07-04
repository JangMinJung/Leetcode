# Write your MySQL query statement below
select stock_name, 
    sum(case
            when operation="buy" then -price
            else price
    End) as capital_gain_loss 
from Stocks
group by stock_name