-- 코드를 입력하세요
SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
    from ( select PRODUCT_NAME, CATEGORY, PRICE, rank() over(partition by CATEGORY order by PRICE desc) as ranking
          from FOOD_PRODUCT) as sub
    where ranking =1 and CATEGORY in ('과자', '국', '김치' ,'식용유')
    order by MAX_PRICE desc;