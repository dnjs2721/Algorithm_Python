-- https://school.programmers.co.kr/learn/courses/30/lessons/157339
SELECT CAR.CAR_ID, CAR.CAR_TYPE, CAST(CAR.daily_fee * (100 - PLAN.discount_rate) / 100 * 30 AS signed integer) as FEE
FROM CAR_RENTAL_COMPANY_CAR as CAR
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY as HISTORY ON CAR.CAR_ID = HISTORY.CAR_ID
    JOIN (SELECT *
          FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN as a
          WHERE a.duration_type = '30일 이상') as PLAN ON CAR.CAR_TYPE = PLAN.CAR_TYPE
WHERE CAR.CAR_TYPE IN ('세단', 'SUV')
    and CAST(CAR.daily_fee * ((100 - PLAN.discount_rate) / 100) * 30 AS signed integer) BETWEEN 500000 and 1999999
GROUP BY CAR.CAR_ID HAVING MAX(HISTORY.END_DATE) < '2022-11-01'
ORDER BY FEE DESC, CAR.car_type ASC, CAR.CAR_ID DESC