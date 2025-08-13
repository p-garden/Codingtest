select t2.flavor
    from(select FLAVOR, sum(TOTAL_ORDER) tot
         from july
         group by FLAVOR) t1
    inner join FIRST_HALF t2
    on t1.FLAVOR = t2.FLAVOR
    group by (t2.FLAVOR)
    order by(t1.tot+t2.TOTAL_ORDER) desc
    limit 3;