-- 코드를 입력하세요
SELECT m.MEMBER_NAME, r.REVIEW_TEXT, r.REVIEW_DATE
    from (select MEMBER_ID, count(*) from REST_REVIEW group by MEMBER_ID order by count(*) desc LIMIT 1) t1     inner join REST_REVIEW r on t1.MEMBER_ID=r.MEMBER_ID 
    inner join MEMBER_PROFILE m on r.MEMBER_ID=m.MEMBER_ID
    order by r.REVIEW_DATE, r.REVIEW_TEXT;
    