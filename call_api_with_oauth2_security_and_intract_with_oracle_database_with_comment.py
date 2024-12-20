#call api with oauth2 security and intract with oracle database
#author : m.dehghan


#install new libraries
pip install oracledb


#import needed libraries
import requests
import pandas as pd
import cx_Oracle
import json
import oracledb


#calculate string value length function
def len_str(v_str):
    i = 0
    for char in v_str:
        i += 1
    return i


#get token code from api token method
def fnc_get_rasa_token():
    credits = ("Api credits keys")
    d={'username':"your username",'password':"your password",'grant_type':'password'}
    r = requests.post("Api token method address")
    rj = r.json()
    tok=rj['access_token']
    return tok


#call Api
def fnc_call_rasa_salamat(lv_national_code,lv_tracking_code):
    tok = fnc_get_rasa_token()
    t={'Content-Type':'application/json',
    'Authorization':'Bearer '+tok}
    if len_str(str(lv_national_code)) == 10:
        nat_code = str(lv_national_code)
    if len_str(str(lv_national_code)) == 9:
        nat_code = '0' + str(lv_national_code)
    if len_str(str(lv_national_code)) == 8:
        nat_code = '00' + str(lv_national_code)
    if len_str(str(lv_national_code)) == 7:
        nat_code = '000' + str(lv_national_code)
    if len_str(str(lv_national_code)) == 6:
        nat_code = '0000' + str(lv_national_code)
    if len_str(str(lv_national_code)) == 5:
        nat_code = '00000' + str(lv_national_code)
         if len_str(str(lv_tracking_code)) == 5:
        track_code = str(lv_tracking_code)
    if len_str(str(lv_tracking_code)) == 4:
        track_code = '0' + str(lv_tracking_code)
    if len_str(str(lv_tracking_code)) == 3:
        track_code = '00' + str(lv_tracking_code)
    if len_str(str(lv_tracking_code)) == 2:
        track_code = '000' + str(lv_tracking_code)
    d = {
        "insurerCompanyCode": "32",
         "organizationCode": "14",
         "nationalCode": nat_code,
         "userId": '',
         "printCodes": [track_code]
        }
    c = json.dumps(d)
    r_test = requests.post("Api address",headers=t,data=c)
    return r_test.json()
    
 
#connect to oracle database and get data from table
rasa_tns = cx_Oracle.makedsn("your host address or ip", "your database port", service_name="your database service name")
conn = cx_Oracle.connect(user=r'sys', password="your database password", dsn=rasa_tns,mode=cx_Oracle.SYSDBA,encoding="UTF-8",nencoding="UTF-8")
cur = conn.cursor()
SQL_SELECT = 'select national_code,tracking_code from sys.TEMP_RASA_SALAMAT_WS_V2 where result is null order by national_code asc fetch first 100000 rows only'
cur.execute(SQL_SELECT)
rows = cur.fetchall()
df1 = pd.DataFrame(rows,columns=['nat','rah'])

#call Api and update results into database
for i in range(len(df1)):
    r = fnc_call_rasa_salamat(df1['nat'][i],df1['rah'][i])
    json_string = json.dumps(r,ensure_ascii=False)
    SQL_Load = """update  sys.TEMP_RASA_SALAMAT_WS_V2 set result = :1 where national_code = :2 and tracking_code = :3"""
    cur.execute(SQL_Load,[json_string,df1['nat'][i],df1['rah'][i]])


    conn.commit()
    
cur.close()
conn.close()




