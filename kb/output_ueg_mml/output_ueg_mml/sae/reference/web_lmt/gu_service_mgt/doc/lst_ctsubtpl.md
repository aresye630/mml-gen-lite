# 以格式2查询用户开户模板(LST CTSUBTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此命令用于查询用户开户模板数据。

使用场景限于运营商对返回报文有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                     |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 可选必选说明：必选参数。 参数含义：用于指示系统按照哪个HLR序列号来查询用户开户模板信息。该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。 取值范围：1～255 默认值：无。 配置原则：无。  |
| TPLID  | 模板ID   | 可选必选说明：必选参数。 参数含义：用于指示系统按照哪个模板ID来查询用户开户模板信息。该参数必须先由ADD SUBTPL命令定义，然后才能在此处引用。 取值范围：1～65534 默认值：无。 配置原则：无。 |

## 使用实例

查询“HLR序列号”为“1”，“模板ID”为“10”的用户开户模板信息，以特定的数据格式返回：

```
LST CTSUBTPL: HLRSN=1, TPLID=10;
```

```
%%LST CTSUBTPL: HLRSN=1, TPLID=10;%%
RETCODE = 0 SUCCESS0001:操作成功

                         TPLID = 10
                           NAM = BOTH
                     EPSODBPOS = NOBPOS
                        ODBPB1 = FALSE
                        ODBPB2 = FALSE
                        ODBPB3 = FALSE
                        ODBPB4 = FALSE
                     AMBRMAXUP = 10000
                    AMBRUPUNIT = kbps
                     AMBRMAXDL = 20000
                    AMBRDLUNIT = kbps
APNDATALIST
                        CNTXID = 1
                           APN = abc.com
                DEFAULTCFGFLAG = TRUE
                  EPS_QOSTPLID = 10
                       PDPTYPE = IPV6
                         VPLMN = TRUE
                IW5GSINDICATOR = TRUE
                  NONIPAPNFLAG = FALSE

Total count = 19

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**LST SUB**输出结果项说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                   | 处理建议                                      |
|:--------|:--------|:-----------------------|:------------------------------------------|
| ERR3003 | 模板未定义   | 用户输入的“模板ID”对应的模板信息未添加。 | 执行LST SUBTPL命令查询已添加的模板信息，根据查询结果重新输入参数。    |
| ERR3097 | 记录不存在   | “HLR序列号”未定义。           | 执行LST HLRSN命令查询已定义的“HLR序列号”，根据查询结果重新输入参数。 |