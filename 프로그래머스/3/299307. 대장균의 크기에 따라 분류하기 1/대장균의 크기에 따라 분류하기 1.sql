select ID,
    case when SIZE_OF_COLONY <= 100 THEN 'LOW'
    when SIZE_OF_COLONY <= 1000 THEN 'MEDIUM'
    else 'HIGH' 
    end as size
from ECOLI_DATA
order by ID;
    