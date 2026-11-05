# 查询格式1用户数据(LST SUBBYFORMAT1)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询格式1的用户数据信息。

## 注意事项

- “IMSI”和“MSISDN”是可选参数，必须有且只能有一个参数出现。
- 该命令不支持批处理，不支持查询多IMSI业务。
- ALS(Alternative Line Service)业务只支持主号码查询。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                 |
|:-------|:-------|:-------------------------------------------------------------------------------------|
| IMSI   | IMSI   | 可选必选说明：可选参数 参数含义：用于标识系统按照哪个“IMSI”来查询用户的签约数据。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。 配置原则：无。   |
| ISDN   | MSISDN | 可选必选说明：可选参数 参数含义：用于标识系统按照哪个“MSISDN”来查询用户的签约数据。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 配置原则：无。 |

## 使用实例

查询“IMSI”为“460000000030101”的用户数据信息。

```
LST SUBBYFORMAT1: IMSI="460000000030101";
```

```
%%LST SUBBYFORMAT1: IMSI="460000000030101";%%
RETCODE = 0 SUCCESS0001:Operation is successful
                          IMSI = 460000000030101
                          ISDN = 8613855660303
                        AMBRUP = 111
                    AMBRUPUNIT = bps
                        AMBRDW = 111
                    AMBRDWUNIT = bps
                    SMDATALIST = [{"SNSSAI":"111","ISDEFAULTSNSSAI":true,"DNNDATALIST":[{"DNN":"111","ISDEFAULTDNN":true,"DNNQOSTPLID":111}]}]
                         AMFID = FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF
                  REGISTERTIME = 20220803071329
                      VOLTETAG = false
                          IMPI = TC_IDR_001_011_impi_2@huawei.com
                      IMPULIST = ["sip:460000000030101@huawei.com","tel:+460000000030101","sip:TC_IDR_001_011_impu_1_1@huawei.com"]
                      SIFCLIST = [72]
                         STNSR = 000
                     SCSCFLIST = ["sip:scscf@huawei.com"]
                            IC = false
                            OC = false
                      GPRSLOCK = false
                       EPSLOCK = false
                       NGSLOCK = false
                       VLRLIST = 86189
                      SGSNLIST = 86136
                DIAMNODETPL_ID = 0
                 NGCNODETPL_ID = 111
                         ODBIC = NOBIC
                         ODBOC = NOBOC
                       ODBROAM = NOBAR
                         ODBSS = false
                        ODBPOS = NOBPOS
                          CLIP = NOTPROV
                          CLIR = NOTPROV
                          COLP = NOTPROV
                          COLR = NOTPROV
                          HOLD = NOTPROV
                          MPTY = NOTPROV
                           CFU = [{"FTN":"911391111","BSG":"TS1X","STATUS":"ACT"}]
                           CFB = [{"FTN":"911391112","BSG":"BS2X","STATUS":"ACT"}]
                         CFNRY = [{"FTN":"911391119","BSG":"BS3X","STATUS":"ACT"}]
                         CFNRC = [{"FTN":"911391112","BSG":"BS2X","STATUS":"ACT"}]
                            CW = [{"BSG":"TS1X","STATUS":"ACT"}]
                          TCSI = 84
                          OCSI = 111
                        VLRNUM = 86116211
                        MSCNUM = 86116211
                       SGSNNUM = 86116221
                       MMEHOST = saehss1.huawei.com
                          BOIC = [{"BSG":"TS6X","STATUS":"ACT"}]
                      IP_SM_GW = 8613955555
               RATFREQSELPRIID = 1
                     RFSPINDEX = 111
Total count = 50
There is together 1 report
---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释   | 原因分析                                                    | 处理建议                                                        |
|------:|:--------|:--------------------------------------------------------|:------------------------------------------------------------|
|  1010 | 参数冲突    | 同时输入了“IMSI”和“MSISDN”参数。                                 | 根据实际情况，输入“IMSI”和“MSISDN”两者之一。                               |
|  3001 | 用户未开户   | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数 “IMSI”或“MSISDN”对应的用户未开户。 | 核实用户的“IMSI”号码或“MSISDN”号码。如果输入有误，重新输入正确的“IMSI”号码或“MSISDN”号码。 |