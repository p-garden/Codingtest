-- 코드를 입력하세요
SELECT i.NAME, i.DATETIME
    FROM ANIMAL_INS i left join ANIMAL_OUTS o
        on i.ANIMAL_ID = o.ANIMAL_ID
    where o.ANIMAL_ID IS NULL
    order by i.DATETIME asc LIMIT 3;