# 停止S1接口过载控制(STP S1OVERLOAD)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

此命令用于停止S1接口过载控制，用于发送overload stop消息给eNodeB。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称       | 参数说明                                                                                                                                                                                                        |
|:-----------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ENODERANGE | eNodeB范围   | 可选必选说明：可选参数 参数含义：该参数用于指定一个eNodeB范围。 取值范围： “ALL_ENODEB(所有eNodeB)”“SPECIFY_ENODEB(指定eNodeB)” 默认值：“SPECIFY_ENODEB(指定eNodeB)”  说明： ALL_ENODEB：用于所有eNodeB强制停止系统自动触发的过载控制流程。SPECIFY_ENODEB：设定停止S1接口过载控制的eNodeB范围。 |
| BGENODEBID | 起始eNodeB标识 | 可选必选说明：条件必选参数 参数含义：该参数用于指定起始eNodeB的ID。 前提条件：该参数在“ENODERANGE”参数配置为“SPECIFY_ENODEB(指定eNodeB)”时生效。 取值范围：0～268435455 默认值：无  说明： “EDENODEBID”必须大于等于“BGENODEBID”。                                                 |
| EDENODEBID | 终止eNodeB标识 | 可选必选说明：条件可选参数 参数含义：该参数用于指定终止eNodeB的ID。 前提条件：该参数在“ENODERANGE”参数配置为“SPECIFY_ENODEB(指定eNodeB)”时生效。 取值范围：0～268435455 默认值：无  说明： “EDENODEBID”必须大于等于“BGENODEBID”。                                                 |

#### 使用实例

停止一个eNodeB范围为SPECIFY\_ENODEB(指定eNodeB)，起始eNodeB标识为100，终止eNodeB标识为1000的S1接口过载控制：

STP S1OVERLOAD: ENODERANGE=SPECIFY\_ENODEB, BGENODEBID=100, EDENODEBID=1000;