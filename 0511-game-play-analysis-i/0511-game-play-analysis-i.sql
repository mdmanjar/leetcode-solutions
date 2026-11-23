# Write your MySQL query statement below
SELECT DISTINCT
    player_id,
    FIRST_VALUE(event_date) OVER (
        PARTITION BY player_id
        ORDER BY event_date ASC
    ) AS first_login
FROM Activity;