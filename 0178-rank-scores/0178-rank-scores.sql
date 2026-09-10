# Write your MySQL query statement below
select score,sort_rank as `rank`
FROM(
    select score,
    dense_rank() over (order by score desc) as sort_rank
    FROM Scores
) AS sorted_score
ORDER BY score desc;



