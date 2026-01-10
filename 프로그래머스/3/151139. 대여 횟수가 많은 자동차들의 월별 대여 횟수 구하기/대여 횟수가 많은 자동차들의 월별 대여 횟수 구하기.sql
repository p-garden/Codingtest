select MONTH(START_DATE) MONTH, CAR_ID, count(*) RECORDS 
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE BETWEEN '2022-08-01' AND '2022-10-31' and
       CAR_ID in (select CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                  where START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
                  group by CAR_ID
                  having count(*) >=5
       )
    group by MONTH, CAR_ID
    order by MONTH , CAR_ID desc;