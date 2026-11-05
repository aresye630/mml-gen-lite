# 设置VoPS配置（SET NGIMSVOPS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

该命令用于设置AMF是否支持PS域IMS语音。

## 注意事项

- 该命令对于已注册用户将在下次注册流程或者移动性注册流程生效。

- 该命令与ADD NGVOICEDEPLOY命令配合控制用户的PS域IMS语音业务策略。对于某一用户如果配置了ADD NGVOICEDEPLOY，ADD NGVOICEDEPLOY命令优先级高于SET NGIMSVOPS。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| AMFHOMO   | DCVOPS   | RADIOCHKSEQ    | SRRLSCAUSE   | UES1MODE   |
|:----------|:---------|:---------------|:-------------|:-----------|
| SUPPORT   | SUPPORT  | BEFORECTXSETUP | NORMALCAUSE  | OFF        |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识        | 参数名称                   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:------------|:-----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AMFHOMO     | AMF是否支持IMS语音           | 可选必选说明：可选参数  参数含义：该参数用于指定AMF侧的所有跟踪区是否都支持PS域IMS语音能力。  数据来源：全网规划 取值范围： “NOT_SUPPORT（不支持）”：不支持“SUPPORT（支持）”：支持“UNSPECIFIED（未指定）”：表示接入网络的PS域IMS语音能力未知，AMF需要向NG-RAN侧发UE RADIO CAPABILITY CHECK REQUEST消息获取UE的IMS VoPS支持能力。最终根据UE能力和“DCVOPS（Data Centric类型终端支持VoPS）”参数的配置来决策PS域IMS语音能力。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGIMSVOPS查询当前参数配置值。  配置原则：无                                                                                                        |
| DCVOPS      | Data Centric类型终端支持VoPS | 可选必选说明：可选参数  参数含义：该参数用于指定Data Centric类型终端是否都支持IMS语音能力。  数据来源：全网规划 取值范围： “NOT_SUPPORT（不支持）”：不支持“SUPPORT（支持）”：支持  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGIMSVOPS查询当前参数配置值。  配置原则：  当运营商不允许Data Centric终端使用5G语音功能时，设置为NOT_SUPPORT; 当运营商允许Data Centric终端使用5G语音功能时，设置为SUPPORT。该参数在"AMFHOMO"配置为"SUPPORT"或"UNSPECIFIED"时生效。                                                                                                                                       |
| RADIOCHKSEQ | 用户无线能力检查时序             | 可选必选说明：该参数在"AMFHOMO"配置为"UNSPECIFIED"时为条件可选参数。  参数含义：该参数用于配置AMF发送INITIAL CONTEXT SETUP REQUEST或者HANDOVER REQUEST驱动基站建立安全上下文和发送UE RADIO CAPABILITY CHECK REQUEST查询UE无线能力两种消息的先后顺序。  数据来源：全网规划 取值范围： “BEFORECTXSETUP（先查询UE无线能力）”：在AMF驱动基站建立安全上下文之前查询UE无线能力。“AFTERCTXSETUP（后查询UE无线能力）”：在AMF驱动基站建立安全上下文之后查询UE无线能力。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGIMSVOPS查询当前参数配置值。  配置原则：  安全上下文建立之前，空口没有加密和完整性保护，此时通过空口查询UE无线能力可能导致查询失败或者查询结果不可信。建议配置为AFTERCTXSETUP。 |
| SRRLSCAUSE  | 连接态下去激活用户面原因值          | 可选必选说明：可选参数  参数含义：该参数用于控制在连接态下，AMF收到initial UE类型的服务请求和移动性注册消息时，发送给SMF的去激活用户面消息中携带的原因值。  数据来源：全网规划 取值范围： “NORMALCAUSE（正常释放）”：表示NgApCause组为NAS，NgApCause值为normal-release；“USERINACTIVITY（用户不活动）”：表示NgApCause组为Radio Network Layer，NgApCause值为user-inactivity；  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGIMSVOPS查询当前参数配置值。  配置原则：  当需要SMF保留GBR类型QoS Flow时，建议将该参数设置为“USERINACTIVITY(用户不活动)”。                                                                     |
| UES1MODE    | 是否检查用户S1Mode能力         | 可选必选说明：可选参数  参数含义：该参数用于指定是否检查用户的S1Mode能力，开启后只有支持S1Mode的UE才允许使用IMS VoPS业务。该能力来源于UE在Registration request消息中携带的5GMM capability信元。  数据来源：全网规划 取值范围： “OFF（关闭）”：关闭“ON（开启）”：开启  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGIMSVOPS查询当前参数配置值。  配置原则：  在Pool迁移场景中，该参数不生效，使用AMF软参DWORD12 BIT12进行控制。                                                                                                                                                                      |

## 使用实例

设置AMF全部支持PS域IMS语音，执行如下命令：

```
SET NGIMSVOPS: AMFHOMO=SUPPORT, DCVOPS=SUPPORT;
```