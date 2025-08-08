-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.NAME
    from  ANIMAL_INS I
        inner join ANIMAL_OUTS O
        on I.ANIMAL_ID = O.ANIMAL_ID
    where O.DATETIME < I.DATETIME
    order by I.DATETIME