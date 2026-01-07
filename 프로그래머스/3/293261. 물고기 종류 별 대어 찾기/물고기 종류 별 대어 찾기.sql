-- 코드를 작성해주세요
SELECT a.ID, b.FISH_NAME, a.LENGTH
    from (FISH_INFO a inner join FISH_NAME_INFO b on a.FISH_TYPE = b.FISH_TYPE)
    where (a.FISH_TYPE , a.length) in (select FISH_TYPE , max(length) from FISH_INFO group by FISH_TYPE)
    order by  a.ID;