# 查询优化GPRS/EPS模板(LST OPTGPRSTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此操作用于查询优化GPRS/EPS模板。

## 注意事项

- 如果没有指定TPLID，显示所有的优化GPRS/EPS模板ID和相关数据。
- 仅输入“HLR序列号”查询所有的模板数据时，会导致PGW模块的CPU占用率升高，因此推荐输入“HLR序列号”和“模板ID”精确查询模板数据。当必须查询所有的模板数据时，请在低话务量时执行。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                       |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | HLR序列号，有效值域为1～255，在PGW支持容灾功能或虚拟HLR功能时设置。                                                                                                                                                                                                                                                                                   |
| TPLID  | 模板ID   | 模板号，0～65534。                                                                                                                                                                                                                                                                                                               |
| SAVEAS | 保存文件名  | 用于标识保存查询结果的文件名称。 当查询结果的记录数超过5000条时必须输入该参数，将查询结果保存在文件中，否则会报错“ERR4102：查询结果已经超过5000条，需要指定保存文件名进行查询”。 取值范围：长度不超过20的字符串。 默认值：无 说明：“保存文件名”参数指定的文件存放在主备PGW模块所在容器上，容器目录为“/opt/pgw/pgwtmpfile/SYSHLRSN+OPNAME”。SYSHLRSN默认为3位数字，不足3位时前面补0。如：SYSHLRSN=1，OPNAME=admin时，最后一层目录为001admin。 保存文件名参数指定的文件，可以通过“PGW Web LMT”界面右上角的“文件管理器”下载。 |

## 使用实例

1. 查询“HLR序列号”为“1”的所有优化GPRS/EPS模板信息，命令如下：

   ```
   LST OPTGPRSTPL: HLRSN=1;
   ```

   ```
   %%LST OPTGPRSTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  10           testoptgprstpl
                  100          EPS_OPTGPRSTPL

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“148”，“模板ID”为“100”的优化GPRS/EPS模板信息，命令如下：

   ```
   LST OPTGPRSTPL: HLRSN=148, TPLID=100;
   ```

   ```
   %%LST OPTGPRSTPL: HLRSN=148, TPLID=100;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 148
                            TPLID = 100
                          TPLNAME = NULL
                           CNTXID = 1
                         APN_TYPE = EPS_APN
                         APNTPLID = 100
                   DEFAULTCFGFLAG = TRUE
                     WILDCARDFLAG = FALSE
                     EPS_QOSTPLID = 100
                            VPLMN = FALSE
                          PDPTYPE = IPV4IPV6
                           CHARGE = NORMAL
                     NONIPAPNFLAG = FALSE
                     PERMANENTIND = TRUE                      
                           CNTXID = 2
                         APN_TYPE = EPS_APN
                         APNTPLID = 200
                   DEFAULTCFGFLAG = TRUE
                     WILDCARDFLAG = FALSE
                     EPS_QOSTPLID = 100
                            VPLMN = FALSE
                          PDPTYPE = IPV4IPV6
                           CHARGE = NORMAL
                     NONIPAPNFLAG = TRUE
                     PERMANENTIND = TRUE
   Total count = 25

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释                        | 原因分析                       | 处理建议                     |
|:--------|:-----------------------------|:---------------------------|:-------------------------|
| ERR4102 | 查询结果已经超过5000条，需要指定保存文件名进行查询。 | 查询结果超过5000条，但未输入参数“保存文件名”。 | 输入参数“保存文件名”，将查询结果保存在文件中。 |