# 以格式2修改CAMEL数据(MOD NCAMEL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于修改CAMEL数据。

使用场景限于运营商对命令格式有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称       | 参数描述                                                   |
|:---------|:-----------|:-------------------------------------------------------|
| IMSI     | IMSI       | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，为6～15位的十进制数。 说明：可选参数。   |
| ISDN     | MSISDN     | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，为1～15位的十进制数。 说明：可选参数。 |
| OCSI_DP  | OCSI DP值   | 该参数用于设置OCSI的DP值。 取值范围： COLLECTINFOROUTESELFAIL 默认值：无。  |
| OCSI_SCP | OCSI SCP地址 | 该参数用于设置OCSI的SCP地址。 取值范围：E.164格式的地址，为1～15位的十进制数。 默认值：无。 |
| OCSI_SK  | OCSI 业务键   | 该参数用于设置OCSI业务键。 取值范围：0～2147483647。 默认值：无。              |
| TCSI_DP  | TCSI DP值   | 该参数用于设置TCSI的DP值。 取值范围： TAATBUSYTNOANSWER 默认值：无。        |
| TCSI_SCP | TCSI SCP地址 | 该参数用于设置TCSI的SCP地址。 取值范围：E.164格式的地址，为1～15位的十进制数。 默认值：无。 |
| TCSI_SK  | TCSI 业务键   | 该参数用于设置TCSI业务键。 取值范围：0～2147483647。 默认值：无。              |

## 使用实例

为IMSI号码为111111111111111的用户修改CAMEL数据，“OCSI DP值”修改为“COLLECTINFO”，“OCSI SCP地址”修改为“8613911111”，“OCSI 业务键”修改为“5”。命令如下：

```
MOD NCAMEL: IMSI="111111111111111", OCSI_DP=COLLECTINFO, OCSI_SCP="8613911111", OCSI_SK=5;
```

```
%%MOD NCAMEL: IMSI="111111111111111", OCSI_DP=COLLECTINFO, OCSI_SCP="8613911111", OCSI_SK=5;%%
RETCODE = 0 SUCCESS0001:Operation is successful

There is together 1 report

---    END
```