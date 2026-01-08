WITH RECURSIVE TIME_TABLE AS (
    SELECT 0 AS HOUR        -- 시작 숫자 (0시)
    UNION ALL
    SELECT HOUR + 1         -- 1씩 증가
    FROM TIME_TABLE
    WHERE HOUR < 23         -- 23시까지 반복
)

select T.HOUR as HOUR, count(a.ANIMAL_ID) as 'COUNT'
    from TIME_TABLE T left join ANIMAL_OUTS a on T.HOUR = HOUR(a.DATETIME)
    group by T.HOUR
    order by T.HOUR;
