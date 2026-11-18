select t2. FLAVOR
    from FIRST_HALF t1 inner join (select FLAVOR, sum(TOTAL_ORDER) TOTAL_ORDER from JULY group by FLAVOR) t2 on t1.FLAVOR=t2.FLAVOR
    group by t2.FLAVOR
    order by (t1.TOTAL_ORDER+t2.TOTAL_ORDER) desc
    LIMIT 3;