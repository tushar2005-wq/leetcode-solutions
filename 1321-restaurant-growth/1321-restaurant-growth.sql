# Write your MySQL query statement below
SELECT c1.visited_on,
SUM(c2.amount) as amount,
ROUND(SUM(c2.amount)/7,2) as average_amount
FROM (SELECT DISTINCT visited_on
FROM Customer) c1
JOIN Customer c2
ON DATEDIFF(c1.visited_on,c2.visited_on) BETWEEN 0 AND 6
GROUP BY visited_on
HAVING COUNT(DISTINCT c2.visited_on)=7
ORDER BY visited_on;