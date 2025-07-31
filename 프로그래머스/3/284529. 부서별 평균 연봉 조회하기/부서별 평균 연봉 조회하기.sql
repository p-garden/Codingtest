-- 코드를 작성해주세요
select d.DEPT_ID as 'DEPT_ID',
     d.DEPT_NAME_EN as 'DEPT_NAME_EN',
    round(avg(e.SAL),0) as AVG_SAL
    from HR_EMPLOYEES e
        inner join HR_DEPARTMENT d
        on e.DEPT_ID = d.DEPT_ID
    group by d.DEPT_ID
    order by avg(e.SAL) desc