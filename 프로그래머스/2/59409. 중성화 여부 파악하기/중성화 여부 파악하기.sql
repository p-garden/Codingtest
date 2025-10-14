-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
    case when (SEX_UPON_INTAKE REGEXP ('Neutered|Spayed')) THEN 'O'
    else  'X' end as 중성화
    from ANIMAL_INS;