# 设置AMF RedCap功能（SET AMFREDCAPFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

该命令用于设置AMF RedCap功能参数。

## 注意事项

- 在用户的下一次移动性流程中生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| REDCAPSW   | RATCMPTSW                |
|:-----------|:-------------------------|
| NO         | UDM-1&PCF-1&SMSF-1&SMF-1 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识       | 参数名称         | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:-----------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REDCAPSW   | RedCap功能开关   | 可选必选说明：可选参数  参数含义：该参数用于控制AMF是否支持RedCap功能。如果该参数设置为“YES（是）”，AMF识别RedCap用户，按照协议定义进行接入和移动性管理；如果该参数设置为“NO（否）”，RedCap用户按照普通NR用户正常接入。  数据来源：全网规划 取值范围： “YES（是）”：是“NO（否）”：否  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFREDCAPFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| RATCMPTSW  | RatType兼容性开关 | 可选必选说明：该参数在"REDCAPSW"配置为"YES"时为条件可选参数。  参数含义：该参数用于指定支持识别NR_REDCAP的网元类型。  数据来源：全网规划 取值范围： “UDM（UDM）”：UDM支持识别NR_REDCAP。“PCF（PCF）”：PCF支持识别NR_REDCAP。“SMSF（SMSF）”：SMSF支持识别NR_REDCAP。“SMF（SMF）”：SMF支持识别NR_REDCAP。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFREDCAPFUNC查询当前参数配置值。  配置原则：  如果指定网元支持识别NR_REDCAP，AMF在和指定网元的服务化请求消息中携带NR_REDCAP作为RatType，否则携带NR作为RatType。  AMF和UDM之间的RatType兼容性控制同时受本参数和ADD AMFN8CMPTPLCY命令的REDCAPRAT参数控制，ADD AMFN8CMPTPLCY支持按号段配置N8接口的兼容性策略，且ADD AMFN8CMPTPLCY优先级更高。                                                                                                                                                                                                                                                                                        |
| NTYSMFPLCY | 空闲态会话通知SMF策略 | 可选必选说明：可选参数  参数含义：该参数用于控制AMF向空闲态PDU会话关联的SMF通知RatType的策略。  数据来源：全网规划 取值范围： “IMMEDIATELY_NOTIFY_ON_CHANGE（变更时立即通知）”：在RatType变化的移动性流程中，如果存在Nsmf_PDUSession_UpdateSMContext Request消息，则跟随该消息随路通知SMF RatType变更，否则单独发送Nsmf_PDUSession_UpdateSMContext Request消息通知SMF RatType变更。“CHANNEL_ASSOCIATED_NOTIFY（随路通知）”：在激活用户面的Nsmf_PDUSession_UpdateSMContext Request消息中会无条件（无论RatType是否变更）携带当前RatType。同时在RatType变化的移动性流程中，如果存在Nsmf_PDUSession_UpdateSMContext Request消息，则跟随该消息随路通知SMF RatType变更。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFREDCAPFUNC查询当前参数配置值。  配置原则： 该参数不受“RedCap功能开关”控制，“RedCap功能开关”由开变为关，会导致用户的RatType发生变化，虽然“RedCap功能开关”关闭，AMF仍然会按照本参数配置的通知策略通知SMF RatType变更。“IMMEDIATELY_NOTIFY_ON_CHANGE(变更时立即通知)”方式时效性更好，用户RatType变化时所有会话关联的SMF都可以及时收到变更通知，但会增加AMF和SMF之间的消息交互，增加系统开销。 |

## 使用实例

开启AMF的RedCap功能，仅UDM不支持识别NR\_RedCap，向空闲态PDU会话关联的SMF立即通知RatType变更执行如下命令：

```
SET AMFREDCAPFUNC:REDCAPSW=YES,RATCMPTSW=UDM-0&PCF-1&SMSF-1&SMF-1,NTYSMFPLCY=IMMEDIATELY_NOTIFY_ON_CHANGE-1&CHANNEL_ASSOCIATED_NOTIFY-0;
```