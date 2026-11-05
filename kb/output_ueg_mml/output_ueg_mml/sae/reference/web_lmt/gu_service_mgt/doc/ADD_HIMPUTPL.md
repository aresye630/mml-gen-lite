# 增加IMPU基本信息模板(ADD HIMPUTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中添加一个IMPU基本信息模板。

## 注意事项

- “NASS游牧模板ID”参数和“NASS游牧模板名称”参数不能同时存在。
- 添加IMPU模板前，必须先配置拜访网络模板和NASS游牧模板，然后才能在此命令中引用“拜访网络模板ID”、“NASS游牧模板ID”和“NASS游牧模板名称”。
- 当通过**SET HSYSTEMPARA**命令设置“USINGHLRSNFORIMS（是否启用IMS-HSS的分权分域功能）”软参为“TRUE(TRUE)”时，执行该命令时会返回错误。

## 参数说明

| 参数标识      | 参数名称       | 参数说明                                                                                                                                                                                    |
|:----------|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TPLID     | IMPU模板ID   | 可选必选说明：必选参数 参数含义：用于定义IMPU基本信息模板的序号，以方便对IMPU基本信息模板进行查询和引用，配置原则是不能与已有的IMPU基本信息模板的模板ID重复。 取值范围： 0~254 默认值： 无                                                                               |
| TPLNAME   | IMPU模板名称   | 可选必选说明：可选参数 参数含义：该参数用于具体描述一个IMPU基本信息模板，以便于识别。 取值范围： 长度不超过64的字符串，字符串由数字、字母、“.”、“-”或“_”组成。 默认值： 无                                                                                         |
| VNTPLID   | 拜访网络模板ID   | 可选必选说明：可选参数 参数含义：用于指定一个漫游地址ID。该参数必须先在ADD HVNTPL中定义，然后才能在此处引用。 取值范围：0~254 默认值：无 配置原则：ADD HVNTPL命令中“拜访网络模板ID”参数取值范围为0~1024，本参数仅支持引用0~254，超过该范围取值，系统上报“900003245：拜访网络模板ID不存在”错误提示。         |
| NATPLID   | NASS游牧模板ID | 可选必选说明：可选参数 参数含义：用于指定一个NASS游牧模板ID。该参数必须先由ADD HNATPL定义，然后才能在此处引用。 取值范围： 0~67108863 默认值： 无 说明：该参数为255表示无效值。                                                                               |
| NATPLNAME | NASS游牧模板名称 | 可选必选说明：可选参数 参数含义：用于指定一个NASS游牧模板名称。该参数必须先由ADD HNATPL定义，然后才能在此处引用。 取值范围： 长度不超过64的字符串，字符串由数字、字母、“.”、“-”或“_”组成。 默认值： 无                                                                      |
| BAR       | 闭锁标志       | 可选必选说明：必选参数 参数含义：指定IMPU的闭锁状态。 取值范围： FALSE(False)：解除闭锁TRUE(TRUE)：闭锁 默认值： 无                                                                                                               |
| REGAUTH   | 注册权限       | 可选必选说明：必选参数 参数含义：指定IMPU的注册权限。 取值范围： FALSE(False)：不允许注册TRUE(TRUE)：允许注册 默认值： 无                                                                                                            |
| VNCFLAG   | 漫游权限检查     | 可选必选说明：必选参数 参数含义：指定IMPU的漫游权限检查标志。 取值范围： FALSE(False)：取消漫游权限检查TRUE(TRUE)：进行漫游权限检查 默认值： 无                                                                                                 |
| NNCFLAG   | 游牧控制标识     | 可选必选说明：必选参数 参数含义：指定IMPU的游牧控制标志，取值固定为DEACTIVE。 取值范围： DEACTIVE(Deactive) 默认值： 无                                                                                                           |
| SERPRVID  | 服务提供商标识    | 可选必选说明：可选参数 参数含义：指定的Service Provider ID(服务提供商标识) 取值范围： 长度不超过39的字符串 默认值： 无                                                                                                               |
| LRI       | 松路由指示信息    | 可选必选说明：可选参数 参数含义：指定IMPU是否签约松路由指示。 取值范围： LOOSE_ROUTE_NOT_REQUIRED(LOOSE_ROUTE_NOT_REQUIRED)：去签约松路由指示。 LOOSE_ROUTE_REQUIRED(LOOSE_ROUTE_REQUIRED)：签约松路由指示 。 默认值： 无 配置原则：不指定该参数表示去签约松路由指示。 |
| COMMENT   | 模板注释说明     | 可选必选说明：可选参数 参数含义：该参数用于具体描述一个IMPU基本信息模板的注释信息，以便于理解和使用。 取值范围： 长度不超过512的字符串 默认值： 无                                                                                                         |

## 使用实例

1. 增加IMPU基本信息模板。IMPU模板ID：10，IMPU模板名称：IMPU Template，拜访网络模板ID：1，NASS游牧模板ID：1，闭锁标志：FALSE，注册权限：TRUE，漫游权限检查：FALSE，游牧控制标识：DEACTIVE，服务提供商标识：1，松路由指示：LOOSE\_ROUTE\_NOT\_REQUIRED，模板注释说明：IMPU Template For ADD HTPLIMPU：

   ```
   ADD HIMPUTPL: TPLID=10, TPLNAME="IMPU Template", VNTPLID=1, NATPLID=1, BAR=FALSE, REGAUTH=TRUE, VNCFLAG=FALSE, NNCFLAG=DEACTIVE, SERPRVID="1", LRI=LOOSE_ROUTE_NOT_REQUIRED, COMMENT="IMPU Template For ADD HTPLIMPU";
   ```
2. 增加IMPU基本信息模板。IMPU模板ID：10，IMPU模板名称：IMPU Template，拜访网络模板ID：1，NASS游牧模板名称：07550011，闭锁标志：FALSE，注册权限：TRUE，漫游权限检查：FALSE，游牧控制标识：DEACTIVE，服务提供商标识：1，松路由指示：LOOSE\_ROUTE\_NOT\_REQUIRED，模板注释说明：IMPU Template For ADD HTPLIMPU：

   ```
   ADD HIMPUTPL: TPLID=10, TPLNAME="IMPU Template", VNTPLID=1, NATPLNAME="07550011", BAR=FALSE, REGAUTH=TRUE, VNCFLAG=FALSE, NNCFLAG=DEACTIVE, SERPRVID="1", LRI=LOOSE_ROUTE_NOT_REQUIRED, COMMENT="IMPU Template For ADD HTPLIMPU";
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|       错误码 | 错误码解释         | 原因分析                                                                       | 处理建议                                                                       |
|----------:|:--------------|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| 900003245 | 拜访网络模板ID不存在   | “拜访网络模板ID”输入错误，实际输入的参数“拜访网络模板ID”未定义。                                       | 如果输入的“拜访网络模板ID”确定正确，说明实际输入的参数“拜访网络模板ID”未定义，请先通过ADD HVNTPL命令定义“拜访网络地址模板ID”。 |
| 900003524 | 分权分域模式下不支持此命令 | SET HSYSTEMPARA命令的“USINGHLRSNFORIMS（是否启用IMS-HSS的分权分域功能）”软参设置为“TRUE(TRUE)”。 | 无需处理。                                                                      |