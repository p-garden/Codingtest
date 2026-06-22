select MCDP_CD 진료과코드, count(MCDP_CD) 5월예약건수
    from APPOINTMENT
    where left(APNT_YMD,7) = '2022-05'
    group by MCDP_CD
    order by 5월예약건수 asc, 진료과코드 asc;