WITH
  total_revenue as (
    SELECT
      day,
      SUM(bill) as sales
    FROM
      AB
    GROUP BY
      day
  )
SELECT
  CONCAT(ROUND(A.bill * 100.0 / B.sales, 2), '%') as total_per
FROM
  AB as A
  JOIN total_revenue as B ON A.day = B.day
ORDER BY
  1 DESC;

-- WITH 별칭1 AS(
-- ...
-- ), 별칭2 AS(
-- ...
-- ), 별칭3 AS(
-- ...
-- ) ... 가능
