SELECT day, total_bill, CONCAT(ROUND(total_bill * 100.0 / (SELECT SUM(total_bill) FROM tips),2), '%') as pct
FROM tips
ORDER BY 2 DESC;
