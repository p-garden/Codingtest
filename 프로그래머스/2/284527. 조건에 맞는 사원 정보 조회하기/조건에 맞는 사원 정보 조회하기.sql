select  sum(g.SCORE) SCORE, e.EMP_NO, e.EMP_NAME,e.POSITION, e.EMAIL
    from HR_DEPARTMENT h inner join 
        HR_EMPLOYEES e on h.DEPT_ID = e.DEPT_ID inner join
        HR_GRADE g on e.EMP_NO=g.EMP_NO
    group by EMP_NO
    order by SCORE desc LIMIT 1;