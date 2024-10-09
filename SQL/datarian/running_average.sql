SELECT
  measured_at,
  pm10,
  (
    SELECT
      AVG(m2.pm10)
    FROM
      measurements as m2
    WHERE
      m2.measured_at BETWEEN DATE_SUB(m1.measured_at, INTERVAL 1 DAY) AND DATE_ADD(m1.measured_at, INTERVAL 1 DAY)
  ) as pm10_running_average
FROM
  measurements as m1
