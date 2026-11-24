# Write your MySQL query statement below
SELECT DISTINCT 
      v1.author_id as id
FROM Views AS v1
where v1.author_id=v1.viewer_id
ORDER BY id;