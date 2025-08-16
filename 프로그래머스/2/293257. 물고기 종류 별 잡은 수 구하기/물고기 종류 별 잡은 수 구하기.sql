-- 코드를 작성해주세요
select count(*) as 'FISH_COUNT', N.FISH_NAME as 'FISH_NAME'
    from FISH_INFO I left join FISH_NAME_INFO N using(FISH_TYPE)
    group by N.FISH_NAME
    order by count(*) desc;