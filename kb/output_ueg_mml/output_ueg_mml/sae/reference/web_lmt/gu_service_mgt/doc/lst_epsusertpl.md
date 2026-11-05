# 查询EPS用户模板（LST EPSUSERTPL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询EPS用户模板的信息：

- 若需要查询全部的EPS用户模板数据，请输入“HLR序列号”，其他参数不输入。
- 若需要查询某个模板ID的EPS用户模板数据的详细信息，请输入“HLR序列号”和“模板ID”。

## 注意事项

仅输入“HLR序列号”查询所有的模板数据时，会导致PGW模块的CPU占用率升高，因此推荐输入“HLR序列号”和“模板ID”精确查询模板数据。当必须查询所有的模板数据时，请在低话务量时执行。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                       |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询EPS用户模板数据，该参数必须选择。                                                                                                                                                                                                                                                                                      |
| TPLID  | 模板ID   | 用于指示系统按照哪个模板ID来查询EPS用户模板数据；若不输入，则表示查询所有的EPS用户模板数据。                                                                                                                                                                                                                                                                         |
| SAVEAS | 保存文件名  | 用于标识保存查询结果的文件名称。 当查询结果的记录数超过5000条时必须输入该参数，将查询结果保存在文件中，否则会报错“ERR4102：查询结果已经超过5000条，需要指定保存文件名进行查询”。 取值范围：长度不超过20的字符串。 默认值：无 说明：“保存文件名”参数指定的文件存放在主备PGW模块所在容器上，容器目录为“/opt/pgw/pgwtmpfile/SYSHLRSN+OPNAME”。SYSHLRSN默认为3位数字，不足3位时前面补0。如：SYSHLRSN=1，OPNAME=admin时，最后一层目录为001admin。 保存文件名参数指定的文件，可以通过“PGW Web LMT”界面右上角的“文件管理器”下载。 |

## 使用实例

1. 查询“HLR序列号”为“1”的所有EPS用户模板信息：

   ```
   LST EPSUSERTPL: HLRSN=1;
   ```

   ```
   %%LST EPSUSERTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  1            EPSUSERTPL_1
                  2            EPSUSERTPL_2
                  3            EPSUSERTPL_3

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”，“模板ID”为“3”的EPS用户模板信息：

   ```
   LST EPSUSERTPL: HLRSN=1, TPLID=3;
   ```

   ```
   %%LST EPSUSERTPL: HLRSN=1, TPLID=3;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            TPLID = 3
                          TPLNAME = EPSUSERTPL_3
                            APNOI = huawei
                        AMBRMAXUL = 50000
                        AMBRMAXDL = 5000
                  RATFREQSELPRIID = 130
                      ACTIVETIMER = 10
                  EUTRANEDRXCYCLE = 10
                   NBIOTEDRXCYCLE = 10
                      RAUTAUTIMER = 10
                   AMBRMAXUL_UNIT = bps
                   AMBRMAXDL_UNIT = bps
                    EPCNOTALLOWED = FALSE
                    NGCNOTALLOWED = TRUE
                            WBPTW = 15
                            NBPTW = 15
                           CNTXID = 1
                   EPSAPNQOSTPLID = 1
                      DEFAULTFLAG = TRUE
                 DEFAULTNONIPFLAG = FALSE

   Total count = 19

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**ADD EPSUSERTPL**

命令的参数说明。表1列出的是未包含在

**ADD EPSUSERTPL**

命令参数说明中的输出项。

| 输出项名称            | 输出项解释                                                              |
|:-----------------|:-------------------------------------------------------------------|
| DEFAULTNONIPFLAG | 用于标识该命令报文中的CNTXID对应的APN是否为NB-IoT用户的默认APN。TRUE：默认APNFALSE：非默认APN    |
| DEFAULTFLAG      | 用于标识该命令报文中的CNTXID对应的PDN上下文是否为默认PDN上下文。TRUE：默认PDN上下文FALSE：非默认PDN上下文 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释                        | 原因分析                           | 处理建议                                                                                         |
|:--------|:-----------------------------|:-------------------------------|:---------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义                        | “HLR序列号”和“模板ID”参数对应的模板数据记录不存在。 | 根据实际情况，重新输入参数，确保“HLR序列号”和“模板ID”参数对应的模板数据记录已存在。已存在的模板数据记录可以通过LST EPSUSERTPL命令仅输入“HLR序列号”参数查询。 |
| ERR4102 | 查询结果已经超过5000条，需要指定保存文件名进行查询。 | 查询结果超过5000条，但未输入参数“保存文件名”。     | 输入参数“保存文件名”，将查询结果保存在文件中。                                                                     |