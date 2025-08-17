-- 코드를 입력하세요
SELECT i.INGREDIENT_TYPE , sum(f.TOTAL_ORDER) as 'TOTAL_ORDER' 
    from  FIRST_HALF f inner join ICECREAM_INFO i on f.flavor = i.flavor
    group by i.ingredient_type 
    order by sum(f.TOTAL_ORDER) asc;