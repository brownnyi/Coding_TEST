WITH daily_sales as (
  SELECT day,
        SUM(bill) as sales
  FROM A
  GROUP BY day
)

SELECT AVG(sales)
FROM daily_sales

-- SELECT AVG(sales)
-- FROM (
--   SELECT day, SUM(bill) as sales
--   FROM A
--   GROUP BY day
-- ) as daily_sales
