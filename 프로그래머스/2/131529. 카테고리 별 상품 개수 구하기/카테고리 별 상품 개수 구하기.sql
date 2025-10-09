-- 코드를 입력하세요
SELECT LEFT(PRODUCT_CODE,2) as PRODUCT_CODE , count(*) as PRODUCTS
    from PRODUCT
    group by LEFT(PRODUCT_CODE,2)
    order by PRODUCT_CODE asc;