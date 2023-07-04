# Write your MySQL query statement below
SELECT 
  CAST(score as DECIMAL(16,2)) AS score, 
  DENSE_RANK() OVER(ORDER BY score DESC) AS "rank"
    
FROM Scores
