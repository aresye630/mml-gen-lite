# 查询SS业务(LST SS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作是用来查询用户签约的所有补充业务。

## 注意事项

IMSI、ISDN是条件可选参数，此操作中，有且只能有一个参数出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                    |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                  |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                  |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                |

## 使用实例

查询IMSI号码为460000009123456的用户的补充业务签约情况。例如：

```
LST SS: IMSI="460000009123456";
```

```
%%LST SS: IMSI="460000009123456";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000009123456
                          ISDN = 2013521
                          CLIP = NOTPROV
                  CLIPOVERRIDE = TRUE
                          CNAP = PROV
                  CNAPOVERRIDE = TRUE
                          CLIR = NOTPROV
                      CLIRMODE = PERMANENT
                          COLP = PROV
                  COLPOVERRIDE = TRUE
                          COLR = NOTPROV
                          HOLD = PROV
                          MPTY = PROV
                           ECT = PROV
                           CFU = PROV
                           CFB = PROV
                         CFNRY = NOTPROV
                         CFNRC = PROV
                           CFD = NOTPROV
                            CW = PROV
                          BAOC = NOTPROV
                          BOIC = NOTPROV
                      BOICEXHC = NOTPROV
                          BORO = NOTPROV
                          BAIC = NOTPROV
                       BICROAM = NOTPROV
                         CBCOU = SUBSCRIBER
                          AOCC = NOTPROV
                          AOCI = NOTPROV
                          UUS1 = NOTPROV
                          UUS2 = NOTPROV
                          UUS3 = NOTPROV
             plmn-specificSS-1 = NOTPROV
             plmn-specificSS-2 = NOTPROV
             plmn-specificSS-3 = NOTPROV
             plmn-specificSS-4 = NOTPROV
             plmn-specificSS-5 = NOTPROV
             plmn-specificSS-6 = NOTPROV
             plmn-specificSS-7 = NOTPROV
             plmn-specificSS-8 = NOTPROV
             plmn-specificSS-9 = NOTPROV
             plmn-specificSS-A = NOTPROV
             plmn-specificSS-B = NOTPROV
             plmn-specificSS-C = NOTPROV
             plmn-specificSS-D = NOTPROV
             plmn-specificSS-E = NOTPROV
             plmn-specificSS-F = NOTPROV
            allplmn-specificSS = NOTPROV
                            MC = PROV
                         EMLPP = PROV
                          CCBS = PROV
                    CCBSTARGET = PROV

Total count = 52

There is together 1 report

---    END
```