SELECT
  customer_id,
  MIN(order_date) as first_order_date,
  MAX(order_date) as last_order_date,
  COUNT(DISTINCT order_date) as cnt_orders,
  SUM(sales) as sum_sales
FROM
  records
GROUP BY
  customer_id
