select count(ID) FISH_COUNT, max(COALESCE(LENGTH, 10)) MAX_LENGTH, FISH_TYPE
    from FISH_INFO
    group by FISH_TYPE
    having avg(COALESCE(LENGTH, 10) ) >= 33
    order by FISH_TYPE;