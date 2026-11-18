-- 코드를 작성해주세요
SELECT e.EMP_NO , e.EMP_NAME, case when avg(h.SCORE) >= 96 then 'S'
                                    when avg(h.SCORE) >= 90 then 'A'
                                    when avg(h.SCORE) >= 80 then 'B'
                                    else  'C' end GRADE, 
                                case when avg(h.SCORE)>= 96 then (e.SAL*0.2)
                                    when avg(h.SCORE) >= 90 then (e.SAL*0.15)
                                    when avg(h.SCORE) >= 80 then (e.SAL*0.1)
                                    else  0 end BONUS
    FROM HR_DEPARTMENT d inner join HR_EMPLOYEES e
        on d.DEPT_ID=e.DEPT_ID inner join HR_GRADE h
        on e.EMP_NO = h.EMP_NO  
    group by e.EMP_NO 
    order by EMP_NO ; 