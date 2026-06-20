select ANIMAL_ID, NAME,DATE_Format(DATETIME, '%Y-%m-%d') 날짜
    from ANIMAL_INS
    order by ANIMAL_ID;