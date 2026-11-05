# 查询NGC漫游限制模板操作(LST NGCRRNODETPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在数据库中查询NGC漫游限制模板。

- 若需要查询全部的NGC漫游限制模板数据，请输入“HLR序列号”参数，其他参数不输入。
- 若需要查询某条NGC漫游限制模板数据且不返回详细信息，请同时输入“HLR序列号”和“模板ID”参数，“是否显示详细信息”参数设置为“FALSE”。
- 若需要查询某条NGC漫游限制模板数据且返回详细信息，请同时输入“HLR序列号”和“模板ID”参数，“是否显示详细信息”参数设置为“TRUE”。

## 注意事项

- 输入“HLR序列号”查询所有的NGC漫游限制模板数据时，会导致PGW模块的CPU占用率升高，请在系统低话务量时执行。
- 当单条NGC漫游限制模板关联多个NGC漫游限制区域模板时，查询或保存此NGC漫游限制模板会引起PGW模块的CPU占用率升高，请在系统低话务量时执行。

## 参数说明

| 参数标识    | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                |
|:--------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN   | HLR序列号   | 可选必选说明：必选参数 参数含义：用于指示系统按照哪个HLR序列号来查询NGC漫游限制模板数据。 取值范围：1～255 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                            |
| TPLID   | 模板ID     | 可选必选说明：可选参数 参数含义：用于指示系统按照哪个模板ID来查询NGC漫游限制模板数据；若不输入，则表示查询所有的NGC漫游限制模板数据。 取值范围：1～2147483646 默认值：无 配置原则：无                                                                                                                                                                                                                                                              |
| DETAIL  | 是否显示详细信息 | 可选必选说明：可选参数 参数含义：用于指示系统是否显示NGC漫游限制模板中漫游限制区域模板配置的详细信息。 取值范围： TRUE：以Json字符串格式显示漫游限制模板中漫游限制区域模板配置的详细信息。FALSE：查询结果仅显示漫游限制区域模板ID。 默认值：FALSE 配置原则：无                                                                                                                                                                                                                       |
| SAVEAS  | 保存文件名    | 可选必选说明：可选参数 参数含义：用于标识保存查询结果的文件名称。当查询结果的NGC漫游限制模板信息超过999个时必须输入该参数，将查询结果保存在文件中，否则会报错“ERR4153：报文数量超过上限，需要指定保存文件名进行查询”。 取值范围：长度不超过20的字符串。 默认值：无 配置原则： “保存文件名”和“模板ID”必须同时输入。“保存文件名”参数指定的文件存放在主备PGW模块所在容器上，容器目录为“/opt/pgw/pgwtmpfile/SYSHLRSN+OPNAME”。SYSHLRSN默认为3位数字，不足3位时前面补0。如：SYSHLRSN=1，OPNAME=admin时，最后一层目录为001admin。保存文件名参数指定的文件，可以通过“PGW Web LMT”界面右上角的“文件管理器”下载。 |
| PROCESS | 限制流程     | 可选必选说明：条件可选参数 参数含义：用于标识本命令要根据哪个限制流程查询限制模板。 取值范围： AMFREGISTERAUTHENTICATIONSMFREGISTERSMSFREGISTERALL 默认值：AMFREGISTER 配置原则： 仅当“是否显示详细信息”参数取值为“TRUE”时该参数有效。该参数取值为“ALL”时，报文中参数“AMFIDLIST”中bool类型参数取值的大小写格式由SET UDMSERV命令中MML报文控制参数的“bit0”进行控制。                                                                                                                         |

## 使用实例

1. 查询“HLR序列号”为“1”的NGC漫游限制模板信息：

   ```
   LST NGCRRNODETPL: HLRSN=1;
   ```

   ```
   %%LST NGCRRNODETPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  1            TEMP1
                  2            TEMP2

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”，“模板ID”为“1”的NGC漫游限制模板信息，且不返回详细信息：

   ```
   LST NGCRRNODETPL: HLRSN=1, TPLID=1, DETAIL=FALSE;
   ```

   ```
   %%LST NGCRRNODETPL: HLRSN=1, TPLID=1, DETAIL=FALSE;%%
   RETCODE = 0 SUCCESS0001:操作成功

                           TPLID = 1
                         TPLNAME = TEMP1
                    DEFFAULTRULE = RESTRICT
              DEFNGCSERRESTTPLID = 2 
                  DEFNGCRSITPLID = 4
                     RRAREATPLID = 1
                            RULE = RESTRICT
                 NGCSERRESTTPLID = 1 
                     NGCRSITPLID = 3 

   Total count = 9

   There is together 1 report

   ---    END
   ```
3. 查询“HLR序列号”为“1”，“模板ID”为“1”的NGC漫游限制模板信息，返回详细信息且“限制流程”为“ALL”：

   ```
   LST NGCRRNODETPL: HLRSN=1, TPLID=1, DETAIL=TRUE, PROCESS=ALL;
   ```

   ```
   %%LST NGCRRNODETPL: HLRSN=1, TPLID=1, DETAIL=TRUE, PROCESS=ALL;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            TPLID = 1
                          TPLNAME = TEMP1
                     DEFFAULTRULE = PERMISSION
                  AUTHDEFAULTRULE = PERMISSION
                   SMFDEFAULTRULE = PERMISSION
                  SMSFDEFAULTRULE = PERMISSION
               DEFNGCSERRESTTPLID = 101
                   DEFNGCRSITPLID = 101
                        AMFIDLIST = [{"AMFIDTYPE":"AMFREGION","PLMN":"11111","AMFREGION":2,"AMFREGISTER":true,"AUTHENTICATION":false,"SMFREGISTER":false,"SMSFREGISTER":false,"NGCSERRESTTPLID":100,"NGCRSITPLID":99,"RULE":"PERMISSION"}]

   Total count = 9

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD NGCRRNODETPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释                   | 原因分析                                 | 处理建议                                                                                                                            |
|:--------|:------------------------|:-------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在                   | “HLR序列号”和“模板ID”对应的NGC漫游限制模板数据记录不存在。  | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”的组合，可通过LST HLRSN命令查询已定义的“HLR序列号”，使用本命令输入已定义“HLR序列号”参数，其他参数不输入，查询已定义“HLR序列号”和“模板ID”的NGC漫游限制模板数据记录。 |
| ERR3097 | HLR序列号未定义               | 输入的“HLR序列号”未定义。                      | 根据实际情况，重新输入参数“HLR序列号”的取值，确保其取值已被定义。已定义的“HLR序列号”可通过LST HLRSN命令查询。                                                                |
| ERR4153 | 报文数量超过上限，需要指定保存文件名进行查询。 | NGC漫游限制模板信息的数量超过了999个，但未输入参数“保存文件名”。 | 输入参数“模板ID”和“保存文件名”，将查询结果保存在文件中。                                                                                                 |