# 以格式2查询ALS用户的ODB数据(LST NALSODB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于以格式2查询用户ALS ODB业务信息，当输入用户的“IMSI”号码时，系统将以指定的格式返回查询结果。

使用场景限于运营商对返回报文格式有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数描述                                                         |
|:-------|:-------|:-------------------------------------------------------------|
| IMSI   | IMSI   | 用于指示系统需要查询哪个IMSI号码的用户的ODB业务信息。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。 |

## 使用实例

查询IMSI号码为“461380000000000”的用户的ODB业务信息，以指定的数据格式返回。命令如下：

```
LST NALSODB: IMSI="461380000000000";
```

```
LST NALSODB: IMSI="461380000000000";%%
RETCODE = 0 SUCCESS0001:Operation is successful

 
   IMSI ... INTERNATIONAL MOBILE SUBSCRIBER IDENTITY ... 461380000000000
   BSERV .. BASIC SERVICE CODE ......................... TD1
                                             
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
                                          
   BCCF ... BARRING OF CHANGING A CALL FORWARDING NUMBER ....... N
                                
COMMAND EXECUTED

Total count = 82

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                 | 处理建议                                                             |
|:--------|:--------|:-------------------------------------|:-----------------------------------------------------------------|
| ERR1004 | 无效的参数值  | 参数“IMSI”的取值不是6～15位十进制数字组成的字符串。       | 根据实际情况，重新输入“IMSI”的取值，确保其取值符合要求。                                  |
| ERR1009 | 参数丢失    | 参数“IMSI”没有输入。                        | 根据实际情况，重新输入参数。                                                   |
| ERR3001 | 用户未开户   | 用户的IMSI号码输入错误，实际输入的参数“IMSI”对应的用户未开户。 | 核实用户的IMSI号码，如果确定输入无误，证明实际输入的参数“IMSI”对应的用户未开户，请先通过ADD SUB命令给用户开户。 |