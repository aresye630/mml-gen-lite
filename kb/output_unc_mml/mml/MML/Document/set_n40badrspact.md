# 设置N40接口收到错误响应时的处理动作（SET N40BADRSPACT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于设置N40接口收到错误响应时的处理动作。

## 注意事项

- 该命令执行后立即生效。

- 当N40接口收到的错误响应同时包含多种错误类型时，错误处理的优先级从高到低依次为：ErrTypeNoMatchHttpCode、ErrTypeErrSeqNum、ErrTypeWrongLocation、ErrTypeNoUpfId、ErrTypePushedRgStateDiffWithSess、ErrTypeInvalidRgLevRC、ErrTypeFuiRedirectWithoutServer、ErrTypeRedirectAddrInvalid、ErrTypeRedirectWithoutAddr、ErrTypeInvalidFuaType、ErrTypeEventRgButRspMeteringNoEvent、ErrTypeErrMetering、ErrTypeGsuWithOnlyUpOrDnVolume、ErrTypeGsuWithZeroTimeQuota、ErrTypeGsuForMeteringZero、ErrTypeNotRspReportRg、ErrTypeGsuNotMatchRsu。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| BADRSPTYPE                          | BADRSPACT   |
|:------------------------------------|:------------|
| ErrTypeNoUpfId                      | INHERIT     |
| ErrTypeErrMetering                  | INHERIT     |
| ErrTypeNotRspReportRg               | INHERIT     |
| ErrTypeGsuNotMatchRsu               | INHERIT     |
| ErrTypeNoMatchHttpCode              | INHERIT     |
| ErrTypeErrSeqNum                    | INHERIT     |
| ErrTypePushedRgStateDiffWithSess    | INHERIT     |
| ErrTypeInvalidRgLevRC               | INHERIT     |
| ErrTypeFuiRedirectWithoutServer     | INHERIT     |
| ErrTypeRedirectAddrInvalid          | INHERIT     |
| ErrTypeRedirectWithoutAddr          | INHERIT     |
| ErrTypeInvalidFuaType               | INHERIT     |
| ErrTypeEventRgButRspMeteringNoEvent | INHERIT     |
| ErrTypeGsuWithOnlyUpOrDnVolume      | INHERIT     |
| ErrTypeGsuWithZeroTimeQuota         | INHERIT     |
| ErrTypeGsuForMeteringZero           | INHERIT     |
| ErrTypeWrongLocation                | INHERIT     |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识       | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:-----------|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BADRSPTYPE | BADRSP错误原因 | 可选必选说明：必选参数  参数含义：该参数用于指定错误响应原因。  数据来源：本端规划 取值范围： “ErrTypeNoUpfId（多UPF场景下，CHF响应携带的UPFID为空）”：多UPF场景下，CHF响应携带的UPFID为空。“ErrTypeErrMetering（CHF响应的配额类型发生了变化）”：CHF响应的配额类型发生了变化。“ErrTypeNotRspReportRg（CHF响应未携带特定的RG信息）”：CHF响应未携带特定的RG信息。“ErrTypeGsuNotMatchRsu（CHF响应未正确下发特定RG的配额）”：CHF响应未正确下发特定RG的配额。“ErrTypeNoMatchHttpCode（CHF的HTTP响应类型与请求类型不一致）”：CHF的HTTP响应类型与请求类型不一致。“ErrTypeErrSeqNum（CHF响应携带了错误的InvocationSequenceNumber）”：CHF响应携带了错误的InvocationSequenceNumber。“ErrTypePushedRgStateDiffWithSess（CHF推送的RG在线离线状态与SMF上下文中记录的不一致）”：CHF推送的RG在线离线状态与SMF上下文中记录的不一致。“ErrTypeInvalidRgLevRC（CHF响应的RG级ResultCode不合法）”：CHF响应的RG级ResultCode不合法。合法的ResultCode有：ResultCodeSUCCESS、ResultCodeEND_USER_SERVICE_DENIED、ResultCodeQUOTA_MANAGEMENT_NOT_APPLICABLE、ResultCodeQUOTA_LIMIT_REACHED、ResultCodeEND_USER_SERVICE_REJECTED、ResultCodeUSER_UNKNOWN、ResultCodeRATING_FAILED、ResultCodeQUOTA_MANAGEMENT“ErrTypeFuiRedirectWithoutServer（CHF下发了FUI重定向动作，但没有下发重定向服务器信息）”：CHF下发了FUI重定向动作，但没有下发重定向服务器信息。“ErrTypeRedirectAddrInvalid（CHF下发了非法的重定向地址类型）”：CHF下发了非法的重定向地址类型。“ErrTypeRedirectWithoutAddr（CHF下发了FUI重定向动作，但没有下发重定向服务器的地址信息）”：CHF下发了FUI重定向动作，但没有下发重定向服务器的地址信息。“ErrTypeInvalidFuaType（CHF下发了不被支持的FUA类型）”：CHF下发了不被支持的FUA类型。支持的FUA类型有：FinalUnitActionTERMINATE、FinalUnitActionREDIRECT。“ErrTypeEventRgButRspMeteringNoEvent（CHF下发的RG的配额类型不支持事件计费，和SMF本地配置不一致）”：CHF下发的RG的配额类型不支持事件计费，和SMF本地配置不一致。“ErrTypeGsuWithOnlyUpOrDnVolume（CHF下发的流量配额格式错误）”：CHF下发的流量配额格式错误。“ErrTypeGsuWithZeroTimeQuota（CHF下发的时长配额为0）”：CHF下发的时长配额为0。该动作配置仅当SET N40QUOTACTRL配置为Terminate时有效。“ErrTypeGsuForMeteringZero（CHF响应携带GSU但是无有效时长流量/事件配额）”：CHF响应携带GSU但是无有效时长流量/事件配额。该场景仅会在RG新业务上报流程中命中。“ErrTypeWrongLocation（ModelC/D场景，CHF响应未携带location）”：ModelC/D场景，CHF响应未携带location。  默认值：无。  配置原则：无 |
| BADRSPACT  | BADRSP处理动作 | 可选必选说明：可选参数  参数含义：该参数用于指定错误响应的处理动作。  数据来源：本端规划 取值范围： “INHERIT（继承）”：处理动作继承自SET CNVRGDCHGPARA的BADRSPACT配置。“TERMINATE（去活会话）”：去活PDU会话。“CONTINUE（允许业务继续进行）”：允许业务继续进行，不再进行配额管理。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40BADRSPACT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## 使用实例

设置N40接口收到CHF响应携带了不合法的RG级ResultCode时去活会话。

```
SET N40BADRSPACT: BADRSPTYPE=ErrTypeInvalidRgLevRC, BADRSPACT=TERMINATE;
```