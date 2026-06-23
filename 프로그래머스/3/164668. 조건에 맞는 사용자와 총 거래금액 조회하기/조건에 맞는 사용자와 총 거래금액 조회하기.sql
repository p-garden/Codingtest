select u.USER_ID, u.NICKNAME, sum(b.PRICE) TOTAL_SALES
    from USED_GOODS_BOARD b 
        inner join USED_GOODS_USER u 
        on b.WRITER_ID=u.USER_ID
    where WRITER_ID in (
                    select WRITER_ID 
                    from USED_GOODS_BOARD 
                    where STATUS = 'DONE'
                    group by WRITER_ID
                    having sum(PRICE)>=700000)
        and STATUS = 'DONE'
    group by USER_ID
    order by TOTAL_SALES asc;