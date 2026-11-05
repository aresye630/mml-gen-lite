# 增加全局Diameter域（ADD GLBDIAMREALM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于设置IMSI/MSISDN号段与Diameter域信息的映射关系，或指定根据IMSI构造号段的Diameter域信息。

如果不指定IMSI/MSISDN号段，则用于设置系统缺省的Diameter域，或指定系统缺省根据IMSI构造Diameter域。

该配置基于某种应用类型生效。

#### 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为4096。
- 对于每种应用，每个号段只能绑定一次Diameter域相关配置，配置的规格与号段配置规格一致。
- 对于Gx应用，如果全局PccSwitch开关使能并且APN的PccSwitch开关为Inherit时，当PCC用户激活时，首先根据用户IMSI/MSISDN查找号段对应的PCRF组，如果查找到PCRF组且选择到可用PCRF，则发送的CCR-I消息携带Destination-Host AVP；否则继续查找IMSI/MSISDN号段对应的Diameter域相关配置，如果查找到，则发送只携带Destination-Realm AVP的消息，Destination-Realm AVP填写为绑定的Diameter域名或通过IMSI构造，SMF根据域名查找Diameter路由，发送给下一跳DRA，通过DRA寻址Diameter Server。
- 对于Gy应用，如果根据配置无法选择到OCS，且APN下也没有对应的Diameter域相关配置，则查找IMSI/MSISDN号段对应的Diameter域相关配置，如果查找到，则发送只携带Destination-Realm AVP的消息，Destination-Realm AVP填写为绑定的Diameter域或通过IMSI构造，SMF根据域名查找Diameter路由，发送给下一跳DRA，通过DRA寻址Diameter Server。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称                      | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:--------------|:--------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APPLICATION   | Diameter应用                | 可选必选说明：必选参数 参数含义：该参数用于指定全局Diameter域所属的Diameter应用。 数据来源：全网规划 取值范围：枚举类型。 GY：Gy接口应用。GX：Gx接口应用。S6B：S6b接口应用。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| SEGMENTNAME   | IMSI/MSISDN号段名称           | 可选必选说明：可选参数 参数含义：该参数用于指定要与Diameter域绑定的IMSI/MSISDN号段的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD IMSIMSISDNSEG命令配置生成。该配置不能和已有的绑定关系重复，即已有的GLBDIAMREALM未绑定该号段。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PRIORITY      | 优先级                       | 可选必选说明：可选参数 参数含义：该参数用于指定IMSI/MSISDN号段匹配的优先级。 数据来源：本端规划 取值范围：整数类型，取值范围为1～65535。如果不指定号段，该参数配置不生效。 默认值：无 配置原则： 如果不输入IMSI/MSISDN号段名称则UNC会自动将优先级设置为无效值0。如果输入IMSI/MSISDN号段名称则此参数也必须输入。优先级取值越小，表示优先级越高。优先级在相同应用的范围内不能与已有的绑定关系重复，不同应用可以重复。当某号码能够匹配到两个或两个以上的Diameter域时，优先选择优先级别较高的号段对应的Diameter域。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CONSTBYIMSISW | 根据IMSI构造归属地Realm开关        | 可选必选说明：必选参数 参数含义：该参数用于指定是否使能根据IMSI构造Peer的归属地Diameter域名。 数据来源：全网规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：当选择ENABLE时，将通过IMSI构造Diameter域，构造格式为“epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| REALM         | Diameter域名                | 可选必选说明：条件必选参数 前提条件：该参数在“CONSTBYIMSISW”配置为“DISABLE”时为必选参数。 参数含义：该参数用于指定与号段绑定的Diameter域名或者缺省的Diameter域名。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT150控制是否区分大小写。 默认值：无 配置原则： 当根据IMSI构造归属地Realm开关设置为ENABLE时，该参数无效。当根据IMSI构造归属地Realm开关设置为DISABLE时，必须手动指定Diameter域。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| SUPFTNEGOSW   | Supported-Features动态协商开关  | 可选必选说明：条件可选参数 前提条件：该参数在“APPLICATION”配置为“GX”时为可选参数。 参数含义：该参数用于指定是否使能Gx应用的Supported-Features动态协商。 数据来源：对端协商 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：DISABLE 配置原则：该参数在3GPP-EPS接入场景下生效，3GPP-GPRS接入场景下不生效。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| CARRYSUPFEASW | Supported-Feature AVP携带开关 | 可选必选说明：条件可选参数 前提条件：该参数在“SUPFTNEGOSW”配置为“DISABLE”时为可选参数。 参数含义：该参数用于配置是否在CCR-I消息中携带Supported-Feature AVP。 数据来源：全网规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：ENABLE 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| FEATURELIST   | Feature列表                 | 可选必选说明：可选参数 参数含义：该参数用于指定要开启的Supported-Features动态协商参数。 数据来源：对端协商 取值范围：位域类型。 RELEASE8：表示支持3GPP Rel-8 Gx功能。RELEASE9：表示支持3GPP Rel-9 Gx功能。RELEASE10：表示支持3GPP Rel-10 Gx功能。ADC：表示支持应用检测与控制功能。NETLOC：表示支持接入网信息上报功能。PROVAFSIGNALFL：表示支持IMS恢复功能。UMCH：表示支持Usage Monitoring拥塞处理功能。SGW_REST：表示支持SGW恢复功能。CNO_ULI：表示支持基于指定区域的策略控制功能。PENDINGTRANSACTION：表示支持事务等待功能。PCSCF_RESTORATION_ENHANCEMENT：PCSCF故障恢复增强功能。EXTENDED_BW_NR：扩展带宽特性。 默认值：无 配置原则： RELEASE8、RELEASE9和RELEASE10为必选参数，必须至少设置一个。ADC，NETLOC，PROVAFSIGNALFL，UMCH和SGW_REST为可选参数，可以根据实际应用场景配置0个或多个。动态协商关闭时，UNC设置Feature列表默认值为RELEASE8和RELEASE9，并按照所设置的最高协议版本和PCRF进行交互。动态协商使能时，如果不配置Feature列表，UNC按照缺省配置RELEASE8和RELEASE9和PCRF进行协商。动态协商使能时，如果配置Feature列表，则UNC使用实际配置的Feature和PCRF进行协商。UNC会对协商结果进行缓存，按照实际的协商结果与PCRF进行该会话的后续交互，并使用缓存的协商结果发起后续会话与该PCRF的动态协商，以提高协商成功率。不配置此参数时值默认为RELEASE8（0）。 |

#### 使用实例

如果希望将号段imsi\_msisdn\_segment\_1内的用户都在Diameter域pcrf.huawei.com上寻找PCRF以激活动态PCC用户，则可以为Gx应用绑定Diameter域pcrf.huawei.com到指定的号段imsi\_msisdn\_segment\_1：

```
ADD GLBDIAMREALM:APPLICATION=GX,SEGMENTNAME="imsi_msisdn_segment_1",PRIORITY=100,CONSTBYIMSISW=DISABLE,REALM="pcrf.huawei.com",SUPFTNEGOSW=DISABLE;
```