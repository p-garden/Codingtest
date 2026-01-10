select b.ANIMAL_ID ANIMAL_ID, b.NAME  NAME
from ANIMAL_INS a right join  ANIMAL_OUTS b on a.ANIMAL_ID = b.ANIMAL_ID
    where a.DATETIME is null;