# Write your MySQL query statement below
-- WITH temp AS (
--      requester_id AS name,
--      COUNT(*) OVER(PARTITION BY accepter_id) AS num
--      ORDER BY num
--      LIMIT 1
-- )
SELECT
    id,
    COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) AS all_friends
GROUP BY id
ORDER BY num DESC
LIMIT 1;
