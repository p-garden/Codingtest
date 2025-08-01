-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(p.PRICE*s.SALES_AMOUNT) SALES 
    from PRODUCT p
        inner join (select PRODUCT_ID, sum(SALES_AMOUNT) SALES_AMOUNT 
                    from OFFLINE_SALE 
                    group by PRODUCT_ID) s
        on p.PRODUCT_ID=s.PRODUCT_ID
    group by p.PRODUCT_ID
    order by sum(p.PRICE*s.SALES_AMOUNT) desc, p.PRODUCT_CODE ;