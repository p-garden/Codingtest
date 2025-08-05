-- 코드를 입력하세요
SELECT p.PRODUCT_ID,
    p.PRODUCT_NAME	,
    sum(o.AMOUNT * p.PRICE) TOTAL_SALES
    from FOOD_ORDER o
        inner join FOOD_PRODUCT p
        on o.PRODUCT_ID=p.PRODUCT_ID
    where left(o.PRODUCE_DATE,7)= '2022-05'
    group by p.PRODUCT_ID
    order by sum(o.AMOUNT * p.PRICE) desc,  p.PRODUCT_ID;