SELECT
  m1.measured_at,
  pm10,
  (
    SELECT
      SUM(m2.pm10)
    FROM
      measurements as m2
    WHERE
      m2.measured_at BETWEEN '2022-01-01' AND m1.measured_at
  ) as pm10_running_total
FROM
  measurements as m1
ORDER BY
  measured_at

-- WHERE m2.measured_at <= m1.measured_at 도 가능
