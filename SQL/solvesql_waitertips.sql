SELECT day, time, ROUND(AVG(tip),2) as avg_tip, ROUND(AVG(size), 2) as avg_size
FROM TIPS
GROUP BY day, time
ORDER BY 1, 2;
