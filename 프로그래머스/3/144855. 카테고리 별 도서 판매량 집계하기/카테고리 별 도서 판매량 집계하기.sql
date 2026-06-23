select b.CATEGORY, sum(s.SALES) TOTAL_SALES
    from BOOK b inner join BOOK_SALES s on b.BOOK_ID = s.BOOK_ID
    where left(s.SALES_DATE,7) = '2022-01'
    group by b.CATEGORY
    order by b.CATEGORY asc;