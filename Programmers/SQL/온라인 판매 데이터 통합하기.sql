-- https://school.programmers.co.kr/learn/courses/30/lessons/131537

(SELECT DATE_FORMAT(SALES_DATE,"%Y-%m-%d") as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE YEAR(SALES_DATE) = 2022 and MONTH(SALES_DATE) = 3

UNION

SELECT DATE_FORMAT(SALES_DATE,"%Y-%m-%d") as SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE YEAR(SALES_DATE) = 2022 and MONTH(SALES_DATE) = 3)

ORDER BY SALES_DATE, PRODUCT_ID, USER_ID