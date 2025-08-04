-- 코드를 입력하세요
SELECT sub.NAME, sub.DATETIME
    from (select I.ANIMAL_ID, I.NAME, I.DATETIME, O.DATETIME as 'outtime'
          from ANIMAL_INS I
        left join ANIMAL_OUTS O
        on I.ANIMAL_ID = O.ANIMAL_ID
        where O.DATETIME is null) as sub
    order by sub.DATETIME
    limit 3;