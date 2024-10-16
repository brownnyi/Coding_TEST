SELECT *
FROM A
WHERE (day, bill) in (
  SELECT day, MAX(bill)
  FROM A
  GROUP BY day
)
#(,)로 묶고 순서 동일하게
