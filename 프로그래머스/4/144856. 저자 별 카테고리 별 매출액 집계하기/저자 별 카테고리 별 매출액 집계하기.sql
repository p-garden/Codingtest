-- 코드를 입력하세요
SELECT  b.AUTHOR_ID AUTHOR_ID , b.AUTHOR_NAME AUTHOR_NAME , a.CATEGORY CATEGORY, 
        sum(a.PRICE * c.SALES) TOTAL_SALES
from BOOK_SALES c left join BOOK a on c.BOOK_ID = a.BOOK_ID
            left join AUTHOR b on a.AUTHOR_ID = b.AUTHOR_ID
where left(c.SALES_DATE,7) = '2022-01'
group by b.AUTHOR_ID , a.CATEGORY
order by AUTHOR_ID asc , CATEGORY desc