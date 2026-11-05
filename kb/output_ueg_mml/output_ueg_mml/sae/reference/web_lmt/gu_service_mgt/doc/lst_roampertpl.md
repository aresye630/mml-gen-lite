# 查询优选漫游模板（LST ROAMPERTPL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询优选漫游模板中运营商的漫游比例。

- 若需要查询“HLR序列号”下全部优选漫游模板ID信息，请输入“HLR序列号”，其他参数不输入。
- 若需要查询某个优选漫游模板中所有运营商的分组信息，请输入“HLR序列号”、“模板ID”和“模板类型”，其他参数不输入。
- 若需要查询某个优选漫游模板中某个国家分组中所有运营商的漫游比例信息，请输入“HLR序列号”、“模板ID”、“模板类型”和“分组ID”，其他参数不输入。
- 若需要查询某个优选漫游模板中某个运营商的漫游比例信息，请输入“HLR序列号”、“模板ID”、“模板类型”、“分组ID”以及“运营商ID”或“运营商名称”，其他参数不输入。

## 注意事项

“运营商名称”和“运营商ID”不能同时输入。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                         |
|:--------|:-------|:-----------------------------|
| HLRSN   | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询优选漫游模板信息。 |
| TPLID   | 模板ID   | 用于指示系统按照哪个模板ID来查询优选漫游模板信息。   |
| TPLTYPE | 模板类型   | 用于指示系统查询哪个类型的优选漫游模板信息。       |
| GRPID   | 分组ID   | 用于指示系统按照哪个分组ID来查询优选漫游模板信息。   |
| OPRID   | 运营商ID  | 用于指示系统按照哪个运营商ID来查询优选漫游模板信息。  |
| OPRNAME | 运营商名称  | 用于指示系统按照哪个运营商名称来查询优选漫游模板信息。  |

## 使用实例

1. 查询“HLRSN”为“1”的全部优选漫游模板ID信息：

   ```
   LST ROAMPERTPL: HLRSN=1;
   ```

   ```
   %%LST ROAMPERTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

   TPLID          TPLTYPE
   1              CS
   1              PS
   1042331216     PS

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”，“模板ID”为“1”，“模板类型”为“PS”的优选漫游模板中所有运营商的分组信息：

   ```
   LST ROAMPERTPL: HLRSN=1, TPLID=1, TPLTYPE=PS;
   ```

   ```
   %%LST ROAMPERTPL: HLRSN=1, TPLID=1, TPLTYPE=PS;%%
   RETCODE = 0 SUCCESS0001:操作成功

   GRPID          GRPNAME
   1              Group1

   Total count = 1

   There is together 1 report

   ---    END
   ```
3. 查询“HLR序列号”为“1”，“模板ID”为“1”，“模板类型”为“PS”，“分组ID”为“1”的国家分组中所有运营商的漫游比例信息：

   ```
   LST ROAMPERTPL: HLRSN=1, TPLID=1, TPLTYPE=PS, GRPID=1;
   ```

   ```
   %%LST ROAMPERTPL: HLRSN=1, TPLID=1, TPLTYPE=PS, GRPID=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                          GRPNAME = Group1
                               CC = 86
                              MCC = 460
                        REJECTNUM = 5
                         OPR1NAME = Peking1
                      OPR1ROAMPRO = 40
                         OPR2NAME = Peking2
                      OPR2ROAMPRO = 30
                         OPR3NAME = Peking3
                      OPR3ROAMPRO = 30

   Total count = 10

   There is together 1 report

   ---    END
   ```
4. 查询“HLR序列号”为“1”，“模板ID”为“1”，“模板类型”为“PS”，“分组ID”为“1”，“运营商ID”为“10”的运营商的漫游比例信息：

   ```
   LST ROAMPERTPL: HLRSN=1, TPLID=1, TPLTYPE=PS, GRPID=1, OPRID=10;
   ```

   ```
   %%LST ROAMPERTPL: HLRSN=1, TPLID=1, TPLTYPE=PS, GRPID=1, OPRID=10;%%
   RETCODE = 0 SUCCESS0001:操作成功

                          GRPNAME = <NULL>
                               CC = 86
                              MCC = 460
                        REJECTNUM = 5
                         OPR1NAME = Peking1
                      OPR1ROAMPRO = 40

   Total count = 6

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET ROAMPERTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释     | 原因分析                                                     | 处理建议                                                                                                                                |
|:--------|:----------|:---------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| ERR1010 | 参数冲突      | 同时输入了“运营商名称”和“运营商ID”两个参数。                                | 根据实际情况，重新输入参数，确保满足“运营商名称”和“运营商ID”不能同时输入。                                                                                            |
| ERR3007 | 记录不存在     | 可能原因如下：需要查询的虚拟HLR中未添加模板。“HLR序列号”和“模板ID”参数对应的优选漫游模板记录不存在。 | 根据可能原因可按如下方法操作：如果需要增加模板，可以通过SET ROAMPERTPL命令为该虚拟HLR增加模板。确保满足“HLR序列号”和“模板ID”参数对应的优选漫游模板数据记录已存在。已存在的优选漫游模板记录可以通过该命令只输入参数“HLR序列号”查询获得。 |
| ERR3097 | HLR序列号未定义 | 参数“HLR序列号”输入错误，实际输入的参数“HLR序列号”未定义。                       | 根据实际情况，重新输入参数“HLR序列号”的取值，确保其取值已被定义。已定义的“HLR序列号”可通过LST HLRSN命令查询。                                                                    |
| ERR3111 | 系统不支持该特性  | 用户级的优选漫游业务功能开关未开启。                                       | 将命令SET MAPCONF中的参数“SUBLEVEL_ROAMPER_SUPP（是否支持用户级的优选漫游业务）”配置为“TRUE”，使UDM支持用户单独签约优选漫游模板，然后再使用此命令查询。                                   |