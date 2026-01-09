select sum(b.SCORE)SCORE, b.EMP_NO EMP_NO, a.EMP_NAME EMP_NAME , a.POSITION POSITION , a.EMAIL EMAIL
    from HR_EMPLOYEES a inner join HR_GRADE b on a.EMP_NO = b.EMP_NO
    where b.YEAR = 2022
    group by b.EMP_NO
    order by SCORE desc LIMIT 1;
    