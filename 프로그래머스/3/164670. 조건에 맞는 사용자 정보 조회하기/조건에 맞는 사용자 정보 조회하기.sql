-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME,concat(u.CITY,' ', u.STREET_ADDRESS1,' ', u.STREET_ADDRESS2) 전체주소, concat(substr(u.TLNO,1,3),'-', substr(u.TLNO,4,4), '-',substr(u.TLNO,8,4)) 전화번호
    FROM USED_GOODS_BOARD b inner join USED_GOODS_USER u
        on b.WRITER_ID = u.USER_ID
    group by b.WRITER_ID
    having count(b.WRITER_ID) >= 3
    order by USER_ID desc;