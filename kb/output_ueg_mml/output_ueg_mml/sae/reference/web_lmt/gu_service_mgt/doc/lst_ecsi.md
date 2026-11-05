# 以格式1查询用户CAMEL信息(LST ECSI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询用户CAMEL信息，以指定的格式返回查询结果。

使用场景限于运营商对返回报文有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称    | 参数描述                                                                  |
|:--------|:--------|:----------------------------------------------------------------------|
| ISDN    | MSISDN  | 此参数用于设置MSISDN号码。 取值范围：E.212格式的编码，6～15位的十进制数字。 说明：必选参数。                |
| PDPTYPE | PDPTYPE | 此参数用于指定CAMEL类型。 取值范围： OCSI TCSI 说明：可选参数。                              |
| OPTION  | OPTION  | 此参数用于设置选择类型。 取值范围： 全部选中 全部清空 全部灰化 OPT EXT 说明：可选参数。 参数复选框中的灰化表示不携带该选项。 |

## 使用实例

查询用户CAMEL信息，以指定数据格式返回。命令如下：

```
LST ECSI: ISDN="877777777777777", PDPTYPE=OCSI, OPTION=OPT-1&EXT-1;
```

```
%%LST ECSI: ISDN="877777777777777", PDPTYPE=OCSI, OPTION=OPT-1&EXT-1%%
RETCODE = 0 SUCCESS0001:Operation is successful

HLR CAMEL SUBSCRIPTION DATA

MSISDN           CSP
877777777777777  

TDPTYPE   TDP    SK         GSA                 DEH    CCH  I  DIALNUM
OCTDP     2      1          8613880000          0      3       
OCTDP     4      1          8613000000          0      3       
OCTDP     2      9999                           0      1       
OCTDP     2      9999                           0      2       

CAMEL SUBSCRIPTION OPTIONS

GCSO   MCSO   SSLO   GC2SO  MC2SO  TIF    GPRSSO    OSMSSO
0      0      0      0      0      0      0         0

GC3SO  MC3SO  GC4SO  MC4SO
0      2      0      0

MMSO   TSMSSO
0      0

EXTENDED CAMEL DATA

EOINCI    EOICK   ETINCI  ETICK
0         0       0       0

Total count = 9

There is together 1 report

---    END
```