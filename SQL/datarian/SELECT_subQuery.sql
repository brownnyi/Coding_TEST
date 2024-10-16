SELECT day, bill, CONCAT(ROUND(bill * 100.0 / (SELECT SUM(bill) FROM A),2), '%') as pct
FROM A
ORDER BY 2 DESC;
