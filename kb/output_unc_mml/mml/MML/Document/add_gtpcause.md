# 增加GTP原因值(ADD GTPCAUSE)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

- 此命令用于增加一条记录，规定了当相应GTP版本消息携带了特定拒绝原因值，将进行P-GW/GGSN重选。
- UNC在以下流程中根据消息中返回的Cause值及Cause值在该表1中的配置，判断是否将该P-GW/GGSN进行网元重选流程。

  - E-UTRAN发起的附着流程和UE请求的PDN连接流程，收到S-GW返回的Create Session Response消息，且消息中携带远端(P-GW)带回的特定拒绝原因值。
  - UE发起的PDP一次激活流程，收到GGSN返回的Create PDP Context Response消息。

#### 注意事项

- 此命令最大记录数为255。

- 此命令执行后立即生效。

- 操作过程或操作后不会引起业务、OM的中断或指标下降。

拒绝原因值有推荐值，参考如下推荐配置表：

| GTP版本   |   拒绝原因值(decimal) | 拒绝原因含义                                 |
|:--------|-----------------:|:---------------------------------------|
| GTPv2   |               72 | System failure                         |
| GTPv2   |               73 | No resources available                 |
| GTPv2   |               84 | All dynamic addresses are occupied     |
| GTPv2   |               91 | No memory available                    |
| GTPv2   |              100 | Remote peer not responding             |
| GTPv0v1 |              204 | System failure                         |
| GTPv0v1 |              199 | No resources available                 |
| GTPv0v1 |              212 | No memory is available                 |
| GTPv0v1 |              211 | All dynamic PDP addresses are occupied |
| GTPv0v1 |              240 | Private Cause: GGSN not responding     |
| GTPv0v1 |              200 | Service not supported                  |
| GTPv0v1 |              219 | Missing or unknown APN                 |
| GTPv0v1 |              220 | Unknown PDP address or PDP type        |

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                 |
|:-----------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GTPVERSION | GTP版本  | 可选必选说明：必选参数 参数含义：该参数用于指定原因值的所属GTP版本。 数据来源：整网规划 取值范围：“GTPV0V1（GTPv0v1）”：表示配置的原因值属于GTPv0v1。“GTPV2（GTPv2）”：表示配置的原因值属于GTPv2。 默认值：无                                                       |
| REJCAUSE   | 拒绝原因值  | 可选必选说明：必选参数 参数含义：该参数用于指定拒绝原因值。 数据来源：整网规划 取值范围：1～255 默认值：无 配置原则：当“GTPVERSION”参数配置为“GTPV0V1”时，“REJCAUSE”取值范围为194～226和234～240，当“GTPVERSION”参数配置为“GTPV2”时，“REJCAUSE”取值范围为64～112和130～239。 |

#### 使用实例

增加一条GTP原因值记录，GTP版本为“GTPv0v1”，拒绝原因值为194：

ADD GTPCAUSE: GTPVERSION=GTPV0V1, REJCAUSE=194;