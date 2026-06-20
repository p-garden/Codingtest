select left(PRODUCT_CODE,2) CATEGORY, count(*) as PRODUCTS
    from PRODUCT
    group by CATEGORY
    order by CATEGORY asc;
    