select ANIMAL_ID,  NAME
    from ANIMAL_INS
    where NAME LIKE lower('%el%') and ANIMAL_TYPE = 'Dog'
    order by NAME, ANIMAL_ID;