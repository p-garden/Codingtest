-- 코드를 입력하세요
SELECT   O.ANIMAL_ID,
         O.NAME
    FROM ANIMAL_INS I
        right JOIN ANIMAL_OUTS O 
        ON I.ANIMAL_ID = O.ANIMAL_ID
    WHERE I.ANIMAL_ID is null;