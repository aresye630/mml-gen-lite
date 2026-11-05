# 启动S1接口过载控制(STR S1OVERLOAD)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

此命令用于启动S1接口过载控制。

#### 注意事项

此命令只用于测试场景。无论当前系统当前是否处于过载状态，执行该命令后，UNC则会立即按设置的控制策略向对应的eNodeB发送OVERLOAD START消息。

执行该命令会导致新接入用户无法附着，已经附着的用户不会受影响。

此配置涉及MME过载控制特性（特性编号：WSFD-104102，license部件编码：LKV2POOLOC02），执行命令请使用**DSP LICENSE**命令确认对应特性license是否得到授权，执行**LST LICENSESWITCH**命令确认特性开关状态为“ENABLE(打开)”。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:-----------|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CTRLPLY    | 过载控制策略     | 可选必选说明：必选参数 参数含义：该参数用于指定一个过载控制策略。 取值范围： “REJECT_ALL_NON_EMERGENCY(Reject all non-emergency MO DT)”：当非紧急移动发起数据传输时，拒绝所有的RRC连接请求，包括RRC建立原因值为“mo-data”和“delayTolerantAccess”的业务消息。“REJECT_ALL_SIGNALLING(Reject all Signalling)”：发信号时拒绝新的RRC连接请求，包括RRC建立原因值为“mo-data”、“mo-signalling”和“delayTolerantAccess”的业务消息。“PERMIT_EMERGENCY_AND_MT(Permit Emergency And MT)”：只允许建立紧急情况RRC连接，包括RRC建立原因值为“emergency”和“mt-Access”的业务消息。“PERMIT_HIGH_PRIORITY_ONLY(Permit High Priority only)”：仅允许接入RRC建立原因值为“highPriorityAccess”和“mt-Access”的业务消息。“REJECT_DELAY_TOLERANT_ACCESS(Reject delay tolerant access)”：仅拒绝RRC建立原因值为“delayTolerantAccess”的业务消息。 默认值：无 |
| BGENODEBID | 起始eNodeB标识 | 可选必选说明：必选参数 参数含义：该参数用于指定起始eNodeB的ID。 取值范围：0～268435455 默认值：无  说明： “EDENODEBID”的值必须大于等于“BGENODEBID”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| EDENODEBID | 终止eNodeB标识 | 可选必选说明：可选参数 参数含义：该参数用于指定终止eNodeB的ID。 取值范围：0～268435455 默认值：无  说明： “EDENODEBID”的值必须大于等于“BGENODEBID”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| REJRATE    | 拒绝比例（%）    | 可选必选说明：可选参数 参数含义：该参数用于指定MME在Overload Start消息中携带的"Traffic Load Reduction Indication"信元的值。"Traffic Load Reduction Indication"信元表示MME指示eNodeB限制指定过载控制策略下用户接入的流控百分比。 取值范围：1～99 默认值：无  说明： 如果不填写系统将按照eNodeB不支持"Traffic Load Reduction Indication"信元处理。                                                                                                                                                                                                                                                                                                                                                                                            |

#### 使用实例

当MME过载时可以通过本命令手动向eNodeB发送Overload Start消息，通知eNodeB拒绝UE新建连接，从而减少对网络的信令冲击。启动S1接口的过载控制策略为Reject all Non-emergency MO DT，起始eNodeB标识为100，终止eNodeB标识为1000，拒绝比例为99的过载控制：

STR S1OVERLOAD: CTRLPLY=REJECT\_ALL\_NON\_EMERGENCY, BGENODEBID=100, EDENODEBID=1000, REJRATE=99;