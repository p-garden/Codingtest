select i.INGREDIENT_TYPE, sum(h.TOTAL_ORDER) TOTAL_ORDER
    from FIRST_HALF h inner join ICECREAM_INFO i on h.FLAVOR = i.FLAVOR
    group by i.INGREDIENT_TYPE
    order by TOTAL_ORDER asc;