# 根据模板信息新增PUSI用户数据(ADD HTPLPUSI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中，利用PUSI的相关的Service Profile模板，PUSI模板，增加一个PUSI用户。

该命令的参数索引关系如图1所示。

**图1** 命令的参数索引关系图

## 注意事项

当通过**SET HSYSTEMPARA**命令设置“USINGHLRSNFORIMS（是否启用IMS-HSS的分权分域功能）”软参为“TRUE(TRUE)”时，执行该命令时会返回错误。

## 参数说明

| 参数标识      | 参数名称               | 参数说明                                                                                                                                                                                                                                                                     |
|:----------|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PISI      | PISI               | 用于指定新增PUSI关联的PISI，必选通过操作ADD HPSI/ADD HTPLPSI增加，才能在此处索引。要求输入的PISI值符合NAI格式，字母区分大小写。                                                                                                                                                                                        |
| PUSI      | PUSI               | 用于指定一个需要根据模板信息新增PUSI用户的PUSI。要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围： 长度不超过127的字符串 缺省值： 无                                                                                                                                                                             |
| PUSITYPE  | PUSI的类型            | 用于标识新增PUSI的类型，当取值为DPUSI，表示新增的PUSI为非通配型；当取值为WPUSI，表示新增的PUSI为通配型。当PUSI为通配型时，PUSI的格式必须符合@符之前是“!.*!”，例如sip:chatlist_!.*!@huawei.com。 取值范围： DPUSI(DPUSI)WPUSI(WPUSI) 缺省值： 无 说明：系统允许的通配IMPU和通配PUSI数量最大为120000个。当前系统限制一个PISI下只能添加一条WPUSI记录，请通过ADD HPSI/ADD HTPLPSI指令添加WPUSI类型记录 |
| SPTPLID   | ServiceProfile模板ID | 用于唯一标识一个Service Profile模板，通过ADD HSPTPL定义，然后才能在此处索引。 取值范围：0～254 默认值：无 配置原则：ADD HSPTPL命令中“Service Profile模板ID”参数取值范围为0~1024，本参数仅支持引用0~254，超过该范围取值，系统上报“900003240：SP模板ID不存在”错误提示。                                                                                           |
| PUSITPLID | PUSI基本信息模板ID       | 用于唯一标识一个PUSI模板，通过ADD HPUSITPL定义，然后才能在此处索引。 取值范围：0～254 默认值：无                                                                                                                                                                                                              |

## 使用实例

根据模板信息新增PUSI用户数据。PISI：pisiinfo，PUSI：sip:pusiinfo@huawei.com，PUSI的类型：DPUSI, ServiceProfile模板ID：1, PUSI基本信息模板ID：1。

```
ADD HTPLPUSI: PISI="pisiinfo", PUSI="sip:pusiinfo@huawei.com", PUSITYPE=DPUSI, SPTPLID=1, PUSITPLID=1;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|       错误码 | 错误码解释         | 原因分析                                                                       | 处理建议                                                        |
|----------:|:--------------|:---------------------------------------------------------------------------|:------------------------------------------------------------|
| 900003240 | SP模板ID不存在     | 输入的Service Profile模板ID在系统中未定义。                                             | 根据实际情况，重新输入Service Profile模板ID，确保输入的Service Profile模板ID已定义。 |
| 900003524 | 分权分域模式下不支持此命令 | SET HSYSTEMPARA命令的“USINGHLRSNFORIMS（是否启用IMS-HSS的分权分域功能）”软参设置为“TRUE(TRUE)”。 | 无需处理。                                                       |