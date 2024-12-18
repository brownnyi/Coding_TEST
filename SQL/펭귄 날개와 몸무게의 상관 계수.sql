SELECT 
    species,
    ROUND(
        (COUNT(*) * SUM(flipper_length_mm * body_mass_g) - SUM(flipper_length_mm) * SUM(body_mass_g)) /
        (SQRT((COUNT(*) * SUM(POWER(flipper_length_mm, 2)) - POWER(SUM(flipper_length_mm), 2)) * 
              (COUNT(*) * SUM(POWER(body_mass_g, 2)) - POWER(SUM(body_mass_g), 2)))),
        3
    ) AS corr
FROM 
    penguins
WHERE 
    flipper_length_mm IS NOT NULL AND body_mass_g IS NOT NULL
GROUP BY 
    species;
