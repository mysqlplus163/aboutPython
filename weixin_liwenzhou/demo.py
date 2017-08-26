#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/8/26

import requests


req = requests.get("https://mp.weixin.qq.com/misc/appmsgcomment?action=list_latest_comment&begin=0&count=20&filtertype=0&day=0&token=1969359283&lang=zh_CN",
                   {
                       "RK":"LG+SnuJ/Q2",
                        "cert":"oeX6a80h9Maf8INtBpC9UhbELmrKp5Sk",
                       "verifysession":"h0182489cf4cdb03cc73b5ead08294e0eba871c49813c558e65a43ee4913cb6930e342a668d2b543a66",
                       "noticeLoginFlag":"1",
                       "remember_acct":"1289287487%40qq.com",
                       "mmad_session":"5ae237640c8a259335cd06b89300589f2153de0888c46e6958d67d34458d060bb7e7d920c33833fe1ef2639e5399f676037e161b886400524c29135a0b248694e53e44a932bbe1b79d164ecdf9d690a81d751b3425b90964a5adc424cb61165411de1c56c245721266e7088080fefde3",
                       "pgv_info":"ssid=s4786023950",
                       "pgv_pvid":"6489148765",
                       "ts_uid":"3416028771",
                       "pgv_pvi":"3430083584",
                       "pgv_si":"s5878551552",
                       "ptui_loginuin":"1289287487",
                       "ptisp":"cm",
                       "ptcz":"0e5a18dec96c7fe3ce63fe8bed051ad86b6a17ccb9daed28e09f8c8ecc77cb1f",
                       "pt2gguin":"o1289287487",
                       "uin":"o1289287487",
                       "skey":"@NcXc1Opuc",
                       "uuid":"7a119399123c8d6f6b19c89d59ae4fb1",
                       "data_bizuin":"3257649313",
                       "data_ticket":"ky2DccVaMUFa1HaZL/E+3Mj7+XkDUqfw86uZZJoB1E/Mbixm2YdmeWonRtYmnMWB",
                       "ua_id":"99V4tG9jOzPaQ5ssAAAAAIZiaf9gXCLxyH8BI66k_I4=",
                       "xid":"844cfcedf75aa9c9872f0c45d4040d62",
                       "openid2ticket_oocgrwsaM28DAGdlP4Xk6HLZzgVM":"9A+jNThoJ999dxJdiezhAsiX8P1BtW/kKZa3G8K1o+c=",
                       "slave_user":"gh_ac1389eb0338",
                       "slave_sid":"RXhqNmNHUUJfOUEzbm9NVTRmdnpKVEtoRG92cWZfcGpETmtrRWdwcnQ2Q3RKWXJRUzQ3d1J3Mnd2cERMeGFWSG1sem11dk1VOFlaNlAzY1hmSUYzakNna3RRVlRIelh0bEc2ekE1VWZGd0NQM1lFQVpMbVRGZEw5NGFBRzhEdWVPSDZzd3Zac0RPelREamtx",
                       "bizuin":"3592010756"
                   }
                   )


print(req.text)
