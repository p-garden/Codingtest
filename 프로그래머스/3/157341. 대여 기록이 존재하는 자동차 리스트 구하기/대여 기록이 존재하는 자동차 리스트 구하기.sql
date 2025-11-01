-- 코드를 입력하세요
SELECT distinct(c.CAR_ID)
    from CAR_RENTAL_COMPANY_CAR c 
    inner join  CAR_RENTAL_COMPANY_RENTAL_HISTORY h on (c.CAR_ID =h.CAR_ID)
    where h.START_DATE LIKE '%-10-%'   and c.CAR_TYPE ='세단'
    order by c.CAR_ID desc;