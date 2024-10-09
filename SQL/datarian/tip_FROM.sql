SELECT order_week
      , AVG(num_orders_daily) as orders_weekly_v1
      , SUM(num_orders_daily) / 7 as orders_weekly_v2
FROM (
  SELECT order_date
        , DAYNAME(order_date) as order_dayofweek
        , WEEK(order_date) as order_week
        , COUNT(DISTINCT order_id) as num_orders_daily
  FROM orders
  WHERE order_date BETWEEN '2019-01-06' AND '2019-03-16'
  GROUP BY order_date, order_dayofweek, order_week
) as num_orders_daily
GROUP BY order_week

-- orders_weekly_v2는 분모를 7 (일주일은 7일이기 때문에)
-- orders_weekly_v1은 평균을 계산할 때 분모는 집계에 해당하는 것들만, 데이터가 없다면 집계 X
