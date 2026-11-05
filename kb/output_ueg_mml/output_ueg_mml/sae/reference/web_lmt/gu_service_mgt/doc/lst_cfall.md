# 查询CFALL业务(LST CFALL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

可以查询网络数据库中保存的前转信息。如果前转已登记或已激活时，会将前转号码和基本业务提示给用户；如果前转已登记但未激活，仅提示前转业务的状态。

## 注意事项

IMSI、ISDN是条件可选参数，有且只能有一个参数出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。 可选参数。                                              |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。 可选参数。                                            |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                  |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                |

## 使用实例

查询IMSI号码为460000009123456的用户前转业务的签约情况。例如：

```
LST CFALL: IMSI="460000009123456";
```

```
%%LST CFALL: IMSI="460000009123456";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000009123456
                          ISDN = 2013521

CFU
                           NCS = TRUE
                         TPLID = 2
                           COU = OPERATOR

                           FTN = <NULL>
                           BSG = ALL BS
                        STATUS = PROV

CFB
                           NFS = TRUE
                           NCS = TRUE
                         TPLID = 2
                           COU = OPERATOR

                           FTN = <NULL>
                           BSG = ALL BS
                        STATUS = PROV

CFNRY
                           NFS = FALSE
                           NCS = FALSE
                           COU = SUBSCRIBER

                           FTN = <NULL>
                           BSG = ALL BS
                        STATUS = NOTPROV

CFNRC
                           NCS = TRUE
                         TPLID = 2
                           COU = OPERATOR

                           FTN = <NULL>
                           BSG = ALL BS
                        STATUS = PROV

CFD
                           NFS = FALSE
                           NCS = FALSE
                   SUPINTERCFD = FALSE
                      VALIDCCF = 
                  CFD_SHORTNUM = FALSE

                           FTN = <NULL>
                           BSG = ALL BS
                        STATUS = NOTPROV

Total count = 35

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见呼叫前转类补充业务命令的参数说明。表1列出的是未包含在呼叫前转类补充业务命令参数说明中的输出项。

| 输出项名称   | 输出项解释                                                          |
|:--------|:---------------------------------------------------------------|
| STATUS  | 用于返回用户的呼叫前转状态。 NOTPROV：未签约。PROV：签约。REG：登记。ACT：激活。QUIESCENT：静止。 |