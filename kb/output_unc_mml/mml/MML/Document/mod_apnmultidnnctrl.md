# 修改2B2C漫游双DNN特性APN级的相关功能控制（MOD APNMULTIDNNCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF**

该命令用于修改2B2C漫游双DNN特性APN级的相关功能控制。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:---------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN            | APN名称       | 可选必选说明：必选参数  参数含义：该参数用于指定2B2C漫游双DNN特性的通用DNN会话的APN实例名。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。  默认值：无  配置原则：  该参数使用ADD APN命令配置生成。                                                                                                                                                                                         |
| GETPOLICYFIRST | 在EPS是否先获取策略 | 可选必选说明：可选参数  参数含义：该参数用于指定当PGW-C上开启2B2C漫游双DNN特性开关（即SET SMCOMMFUNC:MULTIDNNSW=Support）时，PGW-C对接PCF时，是否先跟PCF交互获取会话策略，再动态分配UE IP地址。  数据来源：本端规划 取值范围： “INHERIT（继承）”：表示继承SET MULTICTRL配置下GETPOLICYFIRST的取值。“ENABLE（使能）”：表示PGW-C先跟PCF交互获取会话策略，再动态分配UE IP地址。“DISABLE（不使能）”：表示保持原有实现，即PGW-C先动态分配UE IP地址，再跟PCF交互获取会话策略。  默认值：无  配置原则：无                                                                                                                 |
| MULDNNTRIGGER  | 专网会话触发方式    | 可选必选说明：可选参数  参数含义：该参数用于指定专网会话建立的触发方式。  数据来源：本端规划 取值范围： “INHERIT（继承）”：表示继承SET MULTIDNNCTRL配置下MULDNNTRIGGER的取值。“DEFERRED_INITIATE（延迟触发）”：当用户面检测到业务流匹配分流规则时，通知控制面触发专网会话建立。“IMMEDIATE_INITIATE（立即触发）”：接收到PCF下发MulDnnSessRule时，立即触发专网会话建立。  默认值：无  配置原则：  PCF下发的MulDnnSessRule中的triggerCategory优先级高于此配置。                                                                                                                                          |
| UEIPNATPOS     | UE IP地址转换位置 | 可选必选说明：可选参数  参数含义：在通用DNN漫游分流场景下，由于终端不感知专网会话，需要公网/专网UPF将园区上下行报文中的UE IP进行转换，该参数用于指定专网会话中UE IP地址转换所需的UPF。  数据来源：本端规划 取值范围： “INHERIT（继承）”：表示继承SET MULTIDNNCTRL配置下UEIPNATPOS的取值。“DEDDNN_IUPF（专网会话I-UPF）”：由专网会话的I-UPF进行UE IP地址转换。“DEDDNN_PSAUPF（专网会话锚点UPF）”：由专网会话的锚点UPF进行UE IP地址转换。  默认值：无  配置原则：无                                                                                                                                                 |
| DEDDNNIE       | 园区DNN信元携带方式 | 可选必选说明：可选参数  参数含义：该参数用于指定创建专网会话时，通过N16a接口携带园区DNN的信元的方式。  数据来源：本端规划 取值范围： “INHERIT（继承）”：表示继承SET MULTIDNNCTRL配置下DEDDNNIE的取值。“REQUESTDNN（请求DNN）”：通过Nsmf_PDUSession_Create_request中PduSessionCreateData的“dnn”信元携带园区DNN。“SELECTEDDNN（selected DNN）”：通过Nsmf_PDUSession_Create_request中PduSessionCreateData的“dnn”信元携带通用DNN，selectedDnn信元携带园区DNN。  默认值：无  配置原则：无                                                                                     |
| NEARBYACCSW    | 是否支持就近接入    | 可选必选说明：可选参数  参数含义：该参数用于控制SMF使用多园区就近接入功能的开关。当该参数设置为"ENABLE"时，SMF会根据用户签约的智能分流规则中的ServiceDNN是否匹配配置的就近接入关键字（NEARBYKEYWD参数配置）来判断用户是否有就近接入诉求。如果用户有就近接入诉求，SMF会在专网会话建立流程中向UDM获取就近的DNN用于SMF的服务发现和会话建立。  数据来源：本端规划 取值范围： “INHERIT（继承）”：表示继承SET MULTICTRL配置下NEARBYACCSW的取值。“ENABLE（使能）”：支持就近接入“DISABLE（不使能）”：不支持就近接入  默认值：无  配置原则：  业务处理过程中优先应用ADD APNMULTIDNNCTRL配置下NEARBYACCSW的取值，只有当ADD APNMULTIDNNCTRL配置为INHERIT时才继承SET MULTICTRL配置下NEARBYACCSW的取值。 |

## 使用实例

修改“APN名称”为“HUAWEI.COM”的2B2C漫游双DNN特性相关功能控制，在EPS中不先获取策略。

```
MOD APNMULTIDNNCTRL: APN="HUAWEI.COM",GETPOLICYFIRST=DISABLE;
```