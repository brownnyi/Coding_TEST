SELECT
  id,
  MIN(date) as first_order_date,
  MAX(date) as last_order_date,
  COUNT(DISTINCT date) as cnt_orders,
  SUM(sales) as sum_sales
FROM
  A
GROUP BY
  id


SELECT
  DATE_FORMAT(first_order_date, '%Y-%m-01') as first_order_month,
  COUNT(DISTINCT id)
FROM
  B
GROUP BY
  first_order_month
