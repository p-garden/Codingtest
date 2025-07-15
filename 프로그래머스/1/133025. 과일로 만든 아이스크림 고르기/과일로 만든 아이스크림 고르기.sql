select B.FLAVOR
    FROM FIRST_HALF a join ICECREAM_INFO B on a.flavor = b.flavor
    WHERE B.INGREDIENT_TYPE = 'fruit_based' and a.TOTAL_ORDER > 3000
    order by a.TOTAL_ORDER desc