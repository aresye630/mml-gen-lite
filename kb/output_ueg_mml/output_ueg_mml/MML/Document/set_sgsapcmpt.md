# 设置SGsAP协议兼容性(SET SGSAPCMPT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于设置SGsAP接口协议兼容性开关参数。

#### 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称                     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:---------------|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TAI            | TAI                      | 可选必选说明：可选参数 参数含义：该参数用于指定SGsAP-LOCATION-UPDATE-REQUEST消息中新增信元跟踪区是否携带。 数据来源：根据对端MSC支持能力配置 取值范围：“NOT_CARRY(不携带)”“PRO_DEFINE(按协议定义携带)” 系统初始设置值：“PRO_DEFINE(按协议定义携带)”。                                                                                                                                                                                                                                                                                           |
| ECGI           | E-CGI                    | 可选必选说明：可选参数 参数含义：该参数用于指定SGsAP-LOCATION-UPDATE-REQUEST消息中新增信元E-CGI是否携带。 数据来源：根据对端MSC支持能力配置 取值范围：“NOT_CARRY(不携带)”“PRO_DEFINE(按协议定义携带)” 系统初始设置值：“PRO_DEFINE(按协议定义携带)”。                                                                                                                                                                                                                                                                                         |
| NRI            | TMSI based NRI container | 可选必选说明：可选参数 参数含义：该参数用于指定SGsAP-LOCATION-UPDATE-REQUEST消息中是否携带信元TMSI based NRI container信元。该信元由UE在Attach Request或TAU Request消息中发送给MME，MME将此信元透传给MSC，在MSC POOL组网下，MSC判断此NRI是否为本MSC分配，若非本MSC分配，则向HLR重新获取用户上下文，以防止一些异常场景下，HLR上的VLR信息没有被更新，导致用户的被叫业务故障。 数据来源：本端规划 取值范围：“NOT_CARRY(不携带)”“PRO_DEFINE(按协议定义携带)” 系统初始设置值：“NOT_CARRY(不携带)” 配置原则：如果CS域是MSC POOL组网，并且对端MSC支持SGsAP-LOCATION-UPDATE-REQUEST消息中TMSI based NRI container信元的处理，建议将开关设置为“PRO_DEFINE(按协议定义携带)”。 |
| SPECLAI        | 设置特殊LAI                  | 可选必选说明：可选参数 参数含义：本参数用于指定是否设置特殊的LAI。MSC POOL组网，当UE未携带有效的TMSI based NRI container信元时，若MME判断UE注册的MSC发生改变，MME将在Old LAI信元中携带一个特殊的LAI给MSC。MSC收到携带特殊LAI的SGsAP-LOCATION-UPDATE-REQUEST消息后将去HSS重新获取用户上下文，以防止一些异常场景下，HLR上的VLR信息没有被更新，导致用户的被叫业务故障。 数据来源：全网规划 取值范围：“NO(否)”“YES(是)” 系统初始设置值：“NO(否)” 配置原则：如果对端MSC支持SGsAP-LOCATION-UPDATE-REQUEST消息中特殊LAI的识别和处理，建议设置为“YES(是)”。                                                                                             |
| SPECLAIVAL     | LAI                      | 可选必选说明：条件必选参数 参数含义：该参数用于指定在SGsAP-LOCATION-UPDATE-REQUEST消息中携带的特殊LAI。 前提条件：该参数在“SPECLAI(设置特殊LAI)”参数设置为“YES(是)”时，需要配置。 数据来源：全网规划 取值范围：9～10位十六进制字符串 系统初始设置值：无 配置原则：该LAI不在网络中被广播，且不与任何MSC相对应。                                                                                                                                                                                                                                                                   |
| UEUNREACHCAUSE | UE不可达原因值                 | 可选必选说明：可选参数 参数含义：该参数用于在因UE进入了PSM/eDRX状态而不能被寻呼时，MME向MSC发送的SGsAP-UE-UNREACHABLE消息中SGs cause的取值。 数据来源：全网规划 取值范围：“UE_UNREACHABLE(UE不可达)”“UE_TEMPORARILY_UNREACHABLE(UE暂时不可达)” 系统初始设置值：“UE_TEMPORARILY_UNREACHABLE(UE暂时不可达)”。 配置原则：该参数建议使用系统初始设置值“UE_TEMPORARILY_UNREACHABLE(UE暂时不可达)”。                                                                                                                                                                          |

#### 使用实例

- 设置“TAI”为“按协议定义携带”，“E-CGI”为“不携带”:

  SET SGSAPCMPT: TAI=PRO\_DEFINE, ECGI=NOT\_CARRY;
- 设置“NRI”为“按协议定义携带”，“SPECLAI”为“YES(是)”，“SPECLAIVAL”为“123033201”:

  SET SGSAPCMPT: NRI=PRO\_DEFINE, SPECLAI=YES, SPECLAIVAL="123033201";