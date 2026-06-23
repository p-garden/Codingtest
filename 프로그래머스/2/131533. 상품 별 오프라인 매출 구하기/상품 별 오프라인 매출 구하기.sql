select PRODUCT_CODE, sum(p.PRICE*s.SALES_AMOUNT) SALES 
    from PRODUCT p 
        inner join  OFFLINE_SALE s 
        on p.PRODUCT_ID = s.PRODUCT_ID
    group by p.PRODUCT_CODE
    order by SALES desc, PRODUCT_CODE asc;