# 删除ARP策略参数配置(RMV ARPPARA)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN**

该命令用于删除ARP策略参数配置。

#### 注意事项

删除ARP策略组的最后一条记录前，请先通过**RMV ARPRANGE**命令删除被应用的APR策略组记录。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:--------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GROUPID | ARP策略组 | 可选必选说明：必选参数 参数含义：该参数用于指定ARP策略组。 数据来源：整网规划 取值范围：“G1(自定义组1)”“G2(自定义组2)”“G3(自定义组3)”“G4(自定义组4)”“G5(自定义组5)”“G6(自定义组6)”“G7(自定义组7)”“G8(自定义组8)”“G9(自定义组9)” 默认值：无  说明： 删除ARP策略组的最后一条记录前，请先通过RMV ARPRANGE命令删除被应用的APR策略组记录。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| USRPRI  | 用户级别   | 可选必选说明：必选参数 参数含义：该参数用于指定用户级别，根据用户协商QoS属性中的分配保留优先级（Allocation/Retention Priority）确定。 数据来源：整网规划 取值范围：“ALL(所有用户)”：所有用户“HIGHLEVELUSER(高端用户)”：核心网侧协商的ARP为1。“NORMALUSER(普通用户)”：核心网侧协商的ARP为2。“LOWLEVELUSER(低端用户)”：核心网侧协商的ARP为3。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SRVLVL  | 业务级别   | 可选必选说明：必选参数 参数含义：该参数用于指定业务级别。根据用户PDP上下文QoS中的流量等级（Traffic class），下行保证速率（Guaranteed bit rate for downlink）和发送控制优先级（Traffic handling priority）确定。 数据来源：整网规划 取值范围：“ALL(所用业务级别)”：所有业务级别。“CONVERSATION(Conversation)”：流量等级为Conversational class。“STREAMINGGBRMORE25KBPS(StreamingGBRMore25kbps)”：流量等级为Streaming class，下行保证速率大于等于25kbit/s。“STREAMINGGBRLESS24KBPS(StreamingGBRLess24kbps)”：流量等级为Streaming class，下行保证速率小于25kbit/s。“INTERACTIVETRAFFICPRI1(InteractiveTrafficPri1)”：流量等级为Interactive class，发送控制优先级为1。“INTERACTIVETRAFFICPRI2(InteractiveTrafficPri2)”：流量等级为Interactive class，发送控制优先级为2。“INTERACTIVETRAFFICPRI3(InteractiveTrafficPri3)”：流量等级为Interactive class，发送控制优先级为3。“BACKGROUND(Background)”：流量等级为Background class。 默认值：无 |

#### 使用实例

| 记录号   | ARP策略组    | 用户级别   | 业务级别                   |   承载优先级 | 抢占性    | 被抢占性   | 排队属性   |
|:------|:----------|:-------|:-----------------------|--------:|:-------|:-------|:-------|
| 记录1   | G1(自定义组1) | 高端用户   | Conversation           |       4 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 记录2   | G1(自定义组1) | 高端用户   | StreamingGBRMore25Kbps |       5 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 记录3   | G1(自定义组1) | 高端用户   | StreamingGBRLess24Kbps |       5 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 记录4   | G1(自定义组1) | 高端用户   | InteractiveTrafficPri1 |       6 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 记录5   | G1(自定义组1) | 高端用户   | InteractiveTrafficPri2 |       6 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 记录6   | G1(自定义组1) | 高端用户   | InteractiveTrafficPri3 |       6 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 记录7   | G1(自定义组1) | 高端用户   | Background             |       7 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 记录8   | G1(自定义组1) | 普通用户   | Conversation           |       7 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 记录9   | G1(自定义组1) | 普通用户   | StreamingGBRMore25Kbps |       8 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 记录10  | G1(自定义组1) | 普通用户   | StreamingGBRLess24Kbps |       8 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 记录11  | G1(自定义组1) | 普通用户   | InteractiveTrafficPri1 |       9 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 记录12  | G1(自定义组1) | 普通用户   | InteractiveTrafficPri2 |       9 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 记录13  | G1(自定义组1) | 普通用户   | InteractiveTrafficPri3 |       9 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 记录14  | G1(自定义组1) | 普通用户   | Background             |      10 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 记录15  | G1(自定义组1) | 低端用户   | Conversation           |      10 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 记录16  | G1(自定义组1) | 低端用户   | StreamingGBRMore25Kbps |      11 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 记录17  | G1(自定义组1) | 低端用户   | StreamingGBRLess24Kbps |      11 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 记录18  | G1(自定义组1) | 低端用户   | InteractiveTrafficPri1 |      12 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 记录19  | G1(自定义组1) | 低端用户   | InteractiveTrafficPri2 |      12 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 记录20  | G1(自定义组1) | 低端用户   | InteractiveTrafficPri3 |      12 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 记录21  | G1(自定义组1) | 低端用户   | Background             |      13 | 不触发抢占  | 允许抢占   | 不允许排队  |

1. 系统预先配置记录如表1。

   删除指定ARP策略组G1下的所有记录，记录1–记录21被删除。

   RMV ARPPARA: GROUPID=G1, USRPRI=ALL, SRVLVL=ALL;
2. 系统预先配置记录如表1。

   删除指定ARP策略组G1下的指定业务级别为CONVERSATION的所有记录，记录1、记录8、记录15被删除。

   RMV ARPPARA: GROUPID=G1, USRPRI=ALL, SRVLVL=CONVERSATION;
3. 系统预先配置记录如表1。

   删除指定ARP策略组G1下的指定用户级别为高端用户的所有记录，记录1–记录7被删除。

   RMV ARPPARA: GROUPID=G1, USRPRI=HIGHLEVELUSER, SRVLVL=ALL;
4. 系统预先配置记录如表1。

   删除指定ARP策略组G1下的指定用户级别为高端用户和指定业务级别为InteractiveTrafficPri2的记录、记录5被删除。

   RMV ARPPARA: GROUPID=G1, USRPRI=HIGHLEVELUSER, SRVLVL=INTERACTIVETRAFFICPRI2;