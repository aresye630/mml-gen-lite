# 以格式2查询ODB数据(LST NODBDAT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询用户的ODB数据，以指定的格式返回查询结果。

使用场景限于运营商对返回报文格式有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数描述                                                   |
|:-------|:-------|:-------------------------------------------------------|
| IMSI   | IMSI   | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，为6～15位的十进制数。 说明：可选参数。   |
| ISDN   | MSISDN | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，为1～15位的十进制数。 说明：可选参数。 |

## 使用实例

查询用户的ODB数据，以指定的数据格式返回。命令如下：

```
LST NODBDAT: IMSI="461380000000000";
```

```
%%LST NODBDAT: IMSI="461380000000000";%%
RETCODE = 0 SUCCESS0001:Operation is successful

 
   IMSI ... INTERNATIONAL MOBILE SUBSCRIBER IDENTITY ... 461380000000000
                                             
            OPERATOR DETERMINED BARRING DATA :
   
   BAOC ... BARRING OF ALL OUTGOING CALLS ...................... N
   BOIC ... BARRING OF OUTGOING INTERNATIONAL CALLS ............ N
   BOIH ... BARRING OF OUTGOING INTERNATIONAL CALLS
            EXCEPT THOSE DIRECTED TO THE HOME PLMN COUNTRY ..... N
   BORO ... BARRING OF OUTGOING CALLS WHEN ROAMING
            OUTSIDE THE HOME PLMN COUNTRY ...................... N
   BOZ .... BARRING OF OUTGOING INTER-ZONAL CALLS .............. N
   BOZH ... BARRING OF OUTGOING INTER-ZONAL CALLS EXCEPT
            THOSE DIRECTED TO THE HOME PLMN COUNTRY ............ N
   BOZIH .. BARRING OF OUTGOING INTERNATIONAL CALLS EXCEPT
            THOSE DIRECTED TO THE HOME PLMN COUNTRY
            AND
            BARRING OF OUTGOING INTER-ZONAL CALLS .............. N
   ROAM ... CBO ACTIVE ONLY WHEN ROAMING ....................... N
                                          
   BAPRE .. BARRING OF PREMIUM RATE CALLS (ENTERTAINMENT) ...... N
   BAPRI .. BARRING OF PREMIUM RATE CALLS (INFORMATION) ........ N
   ROAM ... BAPR ACTIVE ONLY WHEN ROAMING ...................... N
                                          
   BAIC ... BARRING OF ALL INCOMING CALLS ...................... N
   BIRN ... BARRING OF INCOMING CALLS WHEN ROAMING
            OUTSIDE THE HOME PLMN .............................. N
   BIRO ... BARRING OF INCOMING CALLS WHEN ROAMING
            OUTSIDE THE HOME PLMN COUNTRY ...................... N
   BIRZ ... BARRING OF INCOMING CALLS WHEN ROAMING
            OUTSIDE THE ZONE OF THE HOME PLMN COUNTRY .......... N
                                          
   BOS1 ... OPERATOR SPECIFIC BARRING CATEGORY 1 ............... N
   BOS2 ... OPERATOR SPECIFIC BARRING CATEGORY 2 ............... N
   BOS3 ... OPERATOR SPECIFIC BARRING CATEGORY 3 ............... N
   BOS4 ... OPERATOR SPECIFIC BARRING CATEGORY 4 ............... N
                                          
   BASS ... BARRING OF SUPPLEMENTARY SERVICE MANAGEMENT ........ N
   ROAM ... BASS ACTIVE ONLY WHEN ROAMING ...................... N
                                          
   BR ..... BARRING OF REGISTRATION OF ANY FORWARDED-TO NUMBER . N
   BRI .... BARRING OF REGISTRATION OF INTERNATIONAL
            FORWARDED-TO NUMBER ................................ N
   BRIH ... BARRING OF REGISTRATION OF INTERNATIONAL
            FORWARDED-TO NUMBER EXCEPT TO A NUMBER WITHIN
            THE HOME PLMN COUNTRY .............................. N
   BRZ .... BARRING OF REGISTRATION OF INTER-ZONAL
            FORWARDED-TO NUMBER ................................ N
   BRZH ... BARRING OF REGISTRATION OF INTER-ZONAL
            FORWARDED-TO NUMBER EXCEPT TO A NUMBER WITHIN
            THE HOME PLMN COUNTRY .............................. N
                                          
   BI ..... BARRING OF INVOCATION OF ANY CALL TRANSFER ......... N
   BIC .... BARRING OF INVOCATION OF CALL TRANSFER
            WHERE AT LEAST ONE OF THE TWO CALLS IS A CALL
            CHARGED TO THE SERVED SUBSCRIBER ................... N
   BICI ... BARRING OF INVOCATION OF CALL TRANSFER
            WHERE AT LEAST ONE OF THE TWO CALLS IS A CALL
            CHARGED TO THE SERVED SUBSCRIBER AT
            INTERNATIONAL RATES ................................ N
   BICZ ... BARRING OF INVOCATION OF CALL TRANSFER
            WHERE AT LEAST ONE OF THE TWO CALLS IS A CALL
            CHARGED TO THE SERVED SUBSCRIBER AT
            INTER-ZONAL RATES .................................. N
   BICB ... BARRING OF INVOCATION OF CALL TRANSFER
            WHERE BOTH CALLS ARE CALLS CHARGED TO
            THE SERVED SUBSCRIBER .............................. N
   BIM .... BARRING OF INVOCATION OF CALL TRANSFER
            WHEN THERE IS AN EXISTING TRANSFERRED CALL
            FOR THE SERVED SUBSCRIBER IN THE SAME MSC/VLR ...... N
   ROAM ... BICT ACTIVE ONLY WHEN ROAMING ...................... N
                                          
   BOSCF1 . OPERATOR SPECIFIC BARRING OF CF
            REGISTRATION CATEGORY 1 ............................ N
   BOSCF2 . OPERATOR SPECIFIC BARRING OF CF
            REGISTRATION CATEGORY 2 ............................ N
   BOSCF3 . OPERATOR SPECIFIC BARRING OF CF
            REGISTRATION CATEGORY 3 ............................ N
   BOSCF4 . OPERATOR SPECIFIC BARRING OF CF
            REGISTRATION CATEGORY 4 ............................ N
                                          
   BAPS ... BARRING OF ALL PACKET ORIENTED SERVICES ............ N
   BPSH ... BARRING OF PACKET ORIENTED SERVICES FROM ACCESS
            POINTS THAT ARE WITHIN THE HPLMN WHILST THE
            SUBSCRIBER IS ROAMING IN A VPLMN ................... N
   BPSV ... BARRING OF PACKET ORIENTED SERVICES FROM ACCESS
            POINTS THAT ARE WITHIN THE ROAMED TO VPLMN ......... N
   BPSR ... BARRING OF ALL PACKET ORIENTED SERVICES WHILST
            THE SUBSCRIBER IS ROAMING IN A VPLMN ............... N
                                          
   BCCF ... BARRING OF CHANGING A CALL FORWARDING NUMBER ....... N
                                
COMMAND EXECUTED

Total count = 90

There is together 1 report

---    END
```