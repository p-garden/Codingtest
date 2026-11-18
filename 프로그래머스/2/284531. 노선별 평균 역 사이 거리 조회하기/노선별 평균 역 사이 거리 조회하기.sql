-- 코드를 작성해주세요
SELECT ROUTE, concat(round(sum(D_BETWEEN_DIST),1),'km') TOTAL_DISTANCE, concat (round(avg(D_BETWEEN_DIST),2) ,'km') AVERAGE_DISTANCE
    FROM SUBWAY_DISTANCE
    group by ROUTE
    order by sum(D_BETWEEN_DIST) desc;