# Write your MySQL query statement below
SELECT 
      u.name as `name`,
      SUM(CASE WHEN r.distance IS NOT NULL THEN r.distance ELSE 0 END) as 'travelled_distance'
FROM Users  AS u
LEFT JOIN Rides r
ON u.id=r.user_id
GROUP by u.id
ORDER BY SUM(r.distance) DESC,u.name ASC;