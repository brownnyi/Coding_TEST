-------테이블 만들기---------
CREATE TABLE TEST_TIME (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    NAME VARCHAR(50),
    TIME INT
);

--------데이터 삽입---------
INSERT INTO TEST_TIME (NAME, TIME) VALUES
('Alice', 23),
('Bob', 27),
('Charlie', 34),
('David', 19),
('Eve', 42),
('Frank', 15),
('Grace', 55),
('Heidi', 65),
('Ivan', 72),
('Judy', 8);

-------코드--------
SELECT
    CASE
        WHEN TIME < 5 THEN '5분 미만'
        ELSE CONCAT(FLOOR(TIME / 5) * 5, '분 이상 ~ ', FLOOR(TIME / 5) * 5 + 5, '분 미만')
    END AS TIME_GROUP,
    COUNT(*) AS count
FROM
    TEST_TIME
GROUP BY
    TIME_GROUP
ORDER BY
    MIN(FLOOR(TIME / 5) * 5);
