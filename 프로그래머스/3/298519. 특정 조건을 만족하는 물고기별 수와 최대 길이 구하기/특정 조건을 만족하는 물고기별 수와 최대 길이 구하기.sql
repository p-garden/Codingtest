select count(ID) FISH_COUNT, max(LENGTH) MAX_LENGTH, FISH_TYPE
    from FISH_INFO
    group by FISH_TYPE
    having avg(coalesce(LENGTH,10))> 33.0
    order by FISH_TYPE asc;