SELECT SUBSTR(PRODUCT_CODE,1,2) as CATEGORY, COUNT(*) as PRODUCT #LEFT, MID도 가능
FROM PRODUCT
GROUP BY SUBSTR(PRODUCT_CODE, 1, 2)
ORDER BY 1; 
