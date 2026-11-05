# 修改Diameter数据字典中的AVP参数(MOD DMAVPDICT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

该命令用于修改Diameter数据字典中的AVP参数。

当MME与HSS之间的协议版本不一致导致的对接失败时，可以执行此命令来修改Diameter数据字典中的AVP参数以解决HSS无法识别UNC发送的ULR消息的RAT-Type的信元问题。

#### 注意事项

该命令执行后立即生效。

该命令只适用于“S6a/S6d”接口的AVP。

该命令修改涉及参数AVPNAME、AVPCODE、VENDORID时，如果与现有记录不一样会插入新记录，记录最大规格为128条。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识     | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:---------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DICTNAME | 字典名称     | 可选必选说明：可选参数 参数含义：该参数用于指定Diameter数据字典名称。 数据来源：整网规划 取值范围：0~65535 默认值：无  说明： “S6a/S6d”接口对应的字典名称固定取值为6。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| AVPNAME  | 信元名称     | 可选必选说明：必选参数 参数含义：该参数用于指定信元名称。 数据来源：整网规划 取值范围：0~65535 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AVPCODE  | 信元编码     | 可选必选说明：必选参数 参数含义：该参数用于指定信元编码。 数据来源：整网规划 取值范围：0~4294967294 默认值：无  说明： AVP代码连同Vendor-ID字段一起来唯一地标识属性。代码1~255保留，用于保证和RADIUS向后兼容。255以上的代码为Diameter所用，由IANA分配。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| VENDORID | Vendor标识 | 可选必选说明：必选参数 参数含义：该参数用于指定厂商ID字段。 数据来源：整网规划 取值范围：0~4294967294 默认值：无  说明： 厂商ID字段为可选字段，当“V”比特设置为1时才出现。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AVPTYPE  | 信元类型     | 可选必选说明：必选参数 参数含义：该参数用于指定信元类型。 数据来源：整网规划 取值范围：“DIAM_AVP_TYPE_UINT32(DIAM_AVP_TYPE_UINT32)”“DIAM_AVP_TYPE_UINT64(DIAM_AVP_TYPE_UINT64)”“DIAM_AVP_TYPE_INT32(DIAM_AVP_TYPE_INT32)”“DIAM_AVP_TYPE_INT64(DIAM_AVP_TYPE_INT64)”“DIAM_AVP_TYPE_OCTETSTR(DIAM_AVP_TYPE_OCTETSTR)”“DIAM_AVP_TYPE_ENUM(DIAM_AVP_TYPE_ENUM)”“DIAM_AVP_TYPE_DIAMIDENT(DIAM_AVP_TYPE_DIAMIDENT)”“DIAM_AVP_TYPE_DIAMURI(DIAM_AVP_TYPE_DIAMURI)”“DIAM_AVP_TYPE_GROUP(DIAM_AVP_TYPE_GROUP)”“DIAM_AVP_TYPE_TIME(DIAM_AVP_TYPE_TIME)”“DIAM_AVP_TYPE_ADDRESS(DIAM_AVP_TYPE_ADDRESS)”“DIAM_AVP_TYPE_UTF8STR(DIAM_AVP_TYPE_UTF8STR)”“DIAM_AVP_TYPE_IPFILTERRULE(DIAM_AVP_TYPE_IPFILTERRULE)”“DIAM_AVP_TYPE_QOSFILTERRULE(DIAM_AVP_TYPE_QOSFILTERRULE)”“DIAM_AVP_TYPE_OLD_IPV4(DIAM_AVP_TYPE_OLD_IPV4)”“DIAM_AVP_TYPE_FLOAT32(DIAM_AVP_TYPE_FLOAT32)”“DIAM_AVP_TYPE_FLOAT64(DIAM_AVP_TYPE_FLOAT64)”“DIAM_AVP_TYPE_LAST(DIAM_AVP_TYPE_LAST)” 默认值：无 |
| AVPFLAG  | 信元标记     | 可选必选说明：必选参数 参数含义：该参数用于指定AVP标志。 数据来源：整网规划 取值范围：“DIAM_AVP_FLAG_MAY_M_PRESENT(DIAM_AVP_FLAG_MAY_M_PRESENT)”“DIAM_AVP_FLAG_P_PRESENT(DIAM_AVP_FLAG_P_PRESENT)”“DIAM_AVP_FLAG_M_PRESENT(DIAM_AVP_FLAG_M_PRESENT)”“DIAM_AVP_FLAG_V_PRESENT(DIAM_AVP_FLAG_V_PRESENT)” 默认值：无  说明： DIAM_AVP_FLAG_V_PRESENT：表明了AVP头部是否包括可选字段Vendor-ID。设为1时，表示AVP编码属于厂商专用的地址空间。DIAM_AVP_FLAG_M_PRESENT：表示了是否需要支持该AVP。如果Diameter节点接收到的消息的AVP“M”比特设置为1又无法被识别，该消息将被拒绝。Diameter中继代理和重定向代理不能拒绝带有无法识别的“M”位的AVP。DIAM_AVP_FLAG_P_PRESENT：设为1时，表示需要端到端的安全加密。DIAM_AVP_FLAG_MAY_M_PRESENT：表示发送消息时AVP Header中的M bit不置位，接收消息时不检查AVP Header中的M bit。                                                                                                                                                                                                                                                                                                  |

#### 使用实例

修改Diameter数据字典:

MOD DMAVPDICT: AVPNAME=129, AVPCODE=1032, VENDORID=10415, AVPTYPE=DIAM\_AVP\_TYPE\_ADDRESS, AVPFLAG=DIAM\_AVP\_FLAG\_MAY\_M\_PRESENT-0&DIAM\_AVP\_FLAG\_M\_PRESENT-0&DIAM\_AVP\_FLAG\_P\_PRESENT-0;