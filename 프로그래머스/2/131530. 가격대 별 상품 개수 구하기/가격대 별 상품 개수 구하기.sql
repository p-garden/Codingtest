select (floor (PRICE / 10000))* 10000 PRICE_GROUP , count(*) PRODUCTS
    from PRODUCT
    group by (floor (PRICE / 10000))
    order by PRICE_GROUP asc
    