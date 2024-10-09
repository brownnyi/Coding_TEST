WITH daily_sales as (
  SELECT day,
        SUM(total_bill) as sales
  FROM tips
  GROUP BY day
)

SELECT AVG(sales)
FROM daily_sales

-- SELECT AVG(sales)
-- FROM (
--   SELECT day, SUM(total_bill) as sales
--   FROM tips
--   GROUP BY day
-- ) as daily_sales
