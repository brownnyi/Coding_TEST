SELECT *
FROM tips
WHERE (day, total_bill) in (
  SELECT day, MAX(total_bill)
  FROM tips
  GROUP BY day
)
#(,)로 묶고 순서 동일하게
