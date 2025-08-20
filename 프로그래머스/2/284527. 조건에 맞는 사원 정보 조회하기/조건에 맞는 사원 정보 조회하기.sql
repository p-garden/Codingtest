-- 코드를 작성해주세요
-- 코드를 작성해주세요
select  sum(score) as 'SCORE', EMP_NO,EMP_NAME,POSITION,EMAIL
    from HR_EMPLOYEES E join HR_GRADE G using (EMP_NO)
    group by EMP_NO
    order by sum(score) desc
    limit 1;