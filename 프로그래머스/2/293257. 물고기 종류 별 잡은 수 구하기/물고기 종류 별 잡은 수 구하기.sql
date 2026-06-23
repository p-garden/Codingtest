select count(*) FISH_COUNT, n.FISH_NAME
    from FISH_INFO i inner join FISH_NAME_INFO n on i.FISH_TYPE = n.FISH_TYPE
    group by i.FISH_TYPE
    order by FISH_COUNT desc;