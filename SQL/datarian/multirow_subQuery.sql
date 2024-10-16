SELECT *
FROM A
WHERE day in (
  SELECT day
  FROM A
  GROUP BY day
  HAVING SUM(bill) >= 1500
  )
