WITH RankedActivity AS (
    SELECT
        player_id,
        event_date,
        ROW_NUMBER() OVER (
            PARTITION BY player_id
            ORDER BY event_date ASC
        ) AS rn
    FROM Activity
)
SELECT player_id, event_date AS first_login
FROM RankedActivity
WHERE rn = 1;