-- 코드를 입력하세요
SELECT concat('/home/grep/src/',
              b.BOARD_ID, '/',
              g.FILE_ID, 
              g.FILE_NAME,
              g.FILE_EXT) FILE_PATH
    from USED_GOODS_BOARD b
        inner join USED_GOODS_FILE g
        on b.BOARD_ID = g.BOARD_ID
    where b.VIEWS = (select max(VIEWS) from USED_GOODS_BOARD)
    order by  g.FILE_ID desc;