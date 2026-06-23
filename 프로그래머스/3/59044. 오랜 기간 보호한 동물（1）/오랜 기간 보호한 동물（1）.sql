select i.NAME, date_format(i.DATETIME, '%Y-%m-%d %H:%i:%s') DATETIME
    from ANIMAL_INS i
        left join ANIMAL_OUTS o
        on i.ANIMAL_ID = o.ANIMAL_ID
    where o.ANIMAL_ID is null
    order by i.DATETIME asc LIMIT 3;