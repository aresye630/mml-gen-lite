# 查询透明数据(LST HREPDATA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中查询IMPU指定类型和指定ServiceIndication的透明数据或者查询PUSI中指定ServiceIndication的透明数据。

通过**LST HREPDATA**命令查询的透明数据包含业务一致性同步的透明数据。

**说明** 

- 业务数据一致性功能开启后，IMS侧的部分透明数据从HLR动态数据获取，转换后下发到IMS域，这部分数据不在IMS域存储，IMS导出数据时不会导出业务数据一致性同步的透明数据。因此，执行**LST HREPDATA**命令查询的透明数据与IMS导出数据获取的透明数据不完全一致。
- 业务数据一致性功能是否开启通过如下命令查询：

  ```
  LST INSP: INSPT=HSS9860, INSPN=VOLTE_DATA_SYN_SWITCH;
  ```

## 注意事项

- 参数IMPU和参数PUSI必须存在且只能存在一个。
- 当参数IMPU存在时，REPTYPE必须存在，参数PUSI存在时，REPTYPE不能存在。
- 当“SH\_ALIASREPDATA\_SUPPORT\_DATAREFERENCE0”参数（可以通过命令LST HSYSTEMPARA查询）取值为“TRUE”时，“REPTYPE”参数必须为普通透明数据类型。

## 参数说明

| 参数标识    | 参数名称                   | 参数说明                                                                                                                         |
|:--------|:-----------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| IMPU    | IMPU                   | 用于指示系统需要查询哪个IMPU对应的透明数据。要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                                     |
| PUSI    | PUSI                   | 用于指示系统需要查询哪个PUSI对应的透明数据。要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                                     |
| REPTYPE | 透明数据的类型                | 用于指定待查询透明数据的类型。 取值范围： ALIASREPDATA(Aliasrepository data)：表示该透明数据类型为别名透明数据。REPDATA(repository data)：表示该透明数据的类型为普通透明数据。 缺省值： 无 |
| SRVIND  | 透明数据的ServiceIndication | 用于指示系统需要查询哪个ServiceIndication对应的透明数据。 取值范围： 长度不超过127的字符串 缺省值： 无                                                              |

## 使用实例

查询PUSI的透明数据。PUSI：sip:pusiinfo@huawei.com，透明数据的ServiceIndication：10。

```
LST HREPDATA: PUSI="sip:pusiinfo@huawei.com", SRVIND="10";
```

```
%%LST HREPDATA: PUSI="sip:pusiinfo@huawei.com", SRVIND="10";%%
RETCODE = 0 SUCCESS0001:Operation is successful

REPDATA                                                                                                                                                                                             REPTYPE
<?xml version="1.0" encoding="UTF-8"?><Sh-Data><RepositoryData><ServiceIndication>10</ServiceIndication><SequenceNumber>0</SequenceNumber><ServiceData>SH_RSI_DATA</ServiceData></RepositoryData></Sh-Data> 1

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各输出项含义请参见**SET HREPDATA**。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|       错误码 | 错误码解释                       | 原因分析                                                                                      | 处理建议                                                                                                        |
|----------:|:----------------------------|:------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| 900001008 | 参数不足                        | “IMPU”或“PUSI”参数和“透明数据的ServiceIndication”均未输入或仅输入了一个。                                      | “IMPU”或“PUSI”参数和“透明数据的ServiceIndication”参数需同时输入。                                                            |
| 900001009 | 参数冲突                        | 可能原因为如下之一： “IMPU”和“PUSI”两个参数同时输入。“PUSI”和“透明数据的类型”参数同时输入。“IMPU”参数输入时，“透明数据的类型”参数未输入。       | 根据实际情况，重新输入参数，确保满足以下几点： 参数“IMPU”和参数“PUSI”必须存在且只能存在一个。参数“PUSI”存在时，“透明数据的类型”不能存在。参数“IMPU”存在时，“透明数据的类型”必须存在。   |
| 900003060 | 请求消息中的IMPU不存在               | “IMPU”参数取值实际不存在，即用户对应的IMPU未开户。                                                            | 需要重新输入“IMPU”，使用LST HSUB命令查询已存在的IMPU后，重新确认要查询的IMPU值。                                                         |
| 900003092 | PUSI不存在                     | “PUSI”参数取值实际不存在，即对应的PSI用户未开户。                                                             | 需要重新输入“PUSI”，使用LST HPSI命令查询已存在的PUSI后，重新确认要查询的PUSI值。                                                         |
| 900003197 | 指定ServiceIndication的透明数据不存在 | “透明数据的ServiceIndication”参数对应的IMPU用户的透明数据不存在。                                              | 重新输入“透明数据的ServiceIndication”参数，确保该参数对应的透明数据已经存在。                                                            |
| 900003246 | IMPU不属于别名IMPUs              | “透明数据的类型”参数输入为“ALIASREPDATA”。                                                             | 重新输入参数，确保该参数取值为“REPDATA”。                                                                                   |
| 900003476 | 透明数据类型不合法                   | 当SET HSYSTEMPARA命令中的参数“别名透明数据是否支持datareference为0”设置为“TRUE”时，“透明数据的类型”参数设置为“ALIASREPDATA”。 | 当SET HSYSTEMPARA命令中的参数“别名透明数据是否支持datareference为0”设置为“TRUE”时，“透明数据的类型”参数不能设置为“ALIASREPDATA”，仅可以取值为“REPDATA”。 |
|      1001 | 无效的命令                       | 该命令名称输入不正确。                                                                               | 重新输入正确的命令名称。                                                                                                |
| 900001004 | 无效的参数名                      | 该命令中的一个或多个参数标识输入不正确。                                                                      | 重新输入正确的参数标识。                                                                                                |
| 900001007 | 无效的参数值                      | 输入的参数取值不符合参数的取值范围及规范要求。                                                                   | 重新输入参数取值，确保符合参数取值范围及规范要求。                                                                                   |
| 900001010 | 参数重复                        | 重复输入该命令中的任意参数。                                                                            | 核实输入的命令，若命令中任意参数输入两次以上，则删除多余的重复参数后，重新执行该命令。                                                                 |