SELECT COUNT(USER_ID) as USERS
FROM USER_INFO
WHERE DATE_FORMAT(JOINED, '%Y') = '2021' AND AGE BETWEEN 20 AND 29