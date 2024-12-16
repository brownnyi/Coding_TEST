WITH DeveloperPlatformSales AS (
    SELECT 
        C.name AS developer,
        B.name AS platform,
        SUM(A.sales_na + A.sales_eu + A.sales_jp + A.sales_other) AS sales
    FROM games A
    JOIN platforms B ON A.platform_id = B.platform_id
    JOIN companies C ON A.developer_id = C.company_id
    GROUP BY C.name, B.name
),
MaxSalesPerDeveloper AS (
    SELECT 
        developer,
        MAX(sales) AS max_sales
    FROM DeveloperPlatformSales
    GROUP BY developer
)
SELECT 
    DPS.developer,
    DPS.platform,
    DPS.sales
FROM DeveloperPlatformSales DPS
JOIN MaxSalesPerDeveloper MSPD
ON DPS.developer = MSPD.developer AND DPS.sales = MSPD.max_sales
ORDER BY DPS.developer, DPS.platform;
