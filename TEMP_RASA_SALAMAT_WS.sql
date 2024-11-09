CREATE TABLE TEMP_RASA_SALAMAT_WS
(
  NATIONAL_CODE  VARCHAR2(100 BYTE),
  TRACKING_CODE  VARCHAR2(100 BYTE),
  RES            VARCHAR2(3000 BYTE),
  RESULT         CLOB
)
LOB (RESULT) STORE AS BASICFILE (
  TABLESPACE  SYSTEM
  ENABLE      STORAGE IN ROW
  CHUNK       8192
  RETENTION
  NOCACHE
  LOGGING
  STORAGE    (
              INITIAL          64K
              NEXT             1M
              MINEXTENTS       1
              MAXEXTENTS       UNLIMITED
              PCTINCREASE      0
              FREELISTS        1
              FREELIST GROUPS  1
              BUFFER_POOL      DEFAULT
             ))
TABLESPACE USERS
PCTFREE    10
INITRANS   1
MAXTRANS   255
STORAGE    (
            INITIAL          64K
            NEXT             1M
            MINEXTENTS       1
            MAXEXTENTS       UNLIMITED
            PCTINCREASE      0
            BUFFER_POOL      DEFAULT
           )
LOGGING 
NOCOMPRESS 
NOCACHE;


CREATE INDEX RSW_NAT_INDX ON TEMP_RASA_SALAMAT_WS
(NATIONAL_CODE)
LOGGING
TABLESPACE SYSTEM
PCTFREE    10
INITRANS   2
MAXTRANS   255
STORAGE    (
            INITIAL          64K
            NEXT             1M
            MINEXTENTS       1
            MAXEXTENTS       UNLIMITED
            PCTINCREASE      0
            FREELISTS        1
            FREELIST GROUPS  1
            BUFFER_POOL      DEFAULT
           );

CREATE INDEX RSW_TRACK_INDX ON TEMP_RASA_SALAMAT_WS
(TRACKING_CODE)
LOGGING
TABLESPACE SYSTEM
PCTFREE    10
INITRANS   2
MAXTRANS   255
STORAGE    (
            INITIAL          64K
            NEXT             1M
            MINEXTENTS       1
            MAXEXTENTS       UNLIMITED
            PCTINCREASE      0
            FREELISTS        1
            FREELIST GROUPS  1
            BUFFER_POOL      DEFAULT
           );
