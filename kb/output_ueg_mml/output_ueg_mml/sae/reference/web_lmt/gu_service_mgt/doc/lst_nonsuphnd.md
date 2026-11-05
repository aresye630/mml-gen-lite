# 查询系统不支持业务的替代功能(LST NONSUPHND)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询系统不支持业务的替代功能，当用户漫游所在的MSC/VLR/MME/S4SGSN不支持用户所签约的ODB、CUG、IST、DIC、ZC和EPC\_ZC业务时，系统使用该MSC/VLR/MME/S4SGSN所支持的业务替代上述业务。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                             |
|:-------|:-------|:---------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询系统不支持业务的替代功能。 |

## 使用实例

查询“HLR序列号”为“1”的HLR的系统不支持业务替代功能：

```
LST NONSUPHND: HLRSN=1;
```

```
%%LST NONSUPHND: HLRSN=1;%%
RETCODE = 0 SUCCESS0001:操作成功

                        ODBAOC = RoamingRestrict
                        ODBOIC = RoamingRestrict
                    ODBOICEXHC = RoamingRestrict
                      ODBENTER = RoamingRestrict
                       ODBINFO = RoamingRestrict
                         ODBSS = NoProcess
                        ODBECT = NoProcess
                       ODBDECT = NoProcess
                       ODBMECT = NoProcess
                        ODBPOS = NoProcess
                        ODBPB1 = NoProcess
                        ODBPB2 = NoProcess
                        ODBPB3 = NoProcess
                        ODBPB4 = NoProcess
                           CUG = RoamingRestrict
                            ZC = RoamingRestrict
                       ISTVMSC = NoProcess
                       ISTGMSC = NoProcess
                      DIC_DICR = RoamingRestrict
                      DIC_DICV = NoProcess
                        EPC_ZC = NoProcess

Total count = 21

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息，各参数含义请参见**SET NONSUPHND**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析       | 处理建议                                                  |
|:--------|:--------|:-----------|:------------------------------------------------------|
| ERR3007 | 记录不存在   | HLR序列号未定义。 | 执行LST HLRSN命令查询出已定义的HLR序列号，然后再执行LST NONSUPHND命令时输入即可。 |