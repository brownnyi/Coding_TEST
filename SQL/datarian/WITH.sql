WITH
  total_revenue as (
    SELECT
      day,
      SUM(total_bill) as sales
    FROM
      tips
    GROUP BY
      day
  )
SELECT
  CONCAT(ROUND(A.total_bill * 100.0 / B.sales, 2), '%') as total_per
FROM
  tips as A
  JOIN total_revenue as B ON A.day = B.day
ORDER BY
  1 DESC;
