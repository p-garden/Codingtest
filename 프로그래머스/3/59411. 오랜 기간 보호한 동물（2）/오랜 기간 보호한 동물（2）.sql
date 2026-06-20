select i.ANIMAL_ID, i.NAME
    from ANIMAL_INS i inner join ANIMAL_OUTS o
        on i.ANIMAL_ID = o.ANIMAL_ID
    order by datediff(o.DATETIME,i.DATETIME) desc
    LIMIT 2;