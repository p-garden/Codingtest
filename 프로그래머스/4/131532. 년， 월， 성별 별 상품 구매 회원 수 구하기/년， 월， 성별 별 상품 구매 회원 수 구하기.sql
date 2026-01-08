-- 코드를 입력하세요
SELECT YEAR(b.SALES_DATE) as YEAR, MONTH(b.SALES_DATE) as MONTH, a.GENDER, count(DISTINCT b.USER_ID) as USERS
    from USER_INFO a right join ONLINE_SALE b on a.USER_ID = b.USER_ID
    where GENDER is not null
    group by YEAR , MONTH , GENDER
    order by YEAR , MONTH , GENDER;