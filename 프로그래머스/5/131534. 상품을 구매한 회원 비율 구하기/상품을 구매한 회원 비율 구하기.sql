-- 코드를 입력하세요
SELECT left(s.SALES_DATE,4 ) YEAR,
    substring(s.SALES_DATE,6,2) MONTH,
    count(distinct s.USER_ID) PURCHASED_USERS,
    round (count(distinct s.USER_ID) /
    (SELECT COUNT(DISTINCT USER_ID) 
        FROM USER_INFO
        WHERE LEFT(JOINED, 4) = '2021'),1) AS PURCHASED_RATIO
    FROM  ONLINE_SALE s
        INNER JOIN USER_INFO u 
        ON s.USER_ID = u.USER_ID
    WHERE LEFT(u.JOINED, 4) = '2021'
    group by left(s.SALES_DATE,4 ), substring(s.SALES_DATE, 6,2)