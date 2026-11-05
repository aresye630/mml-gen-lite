# 添加Sy/N28结果码映射（ADD SYTOGXRCMAP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在UPCF配置数据库中增加一条Sy/N28结果码映射记录。

该命令的使用场景为：

- OCS/CHF收到UPCF发送的Sy/N28请求消息后，返回的结果有三种：
  - 返回成功的Sy/N28响应消息
  - 不返回Sy/N28响应消息或Sy/N28响应消息超时
  - 返回携带错误码的Sy/N28响应消息

  **说明** 

  此场景下：

  - Sy请求消息为SLR，Sy响应消息为SLA。
  - N28请求消息为Nchf\_SpendingLimitControl\_Subscribe Request，N28响应消息为Nchf\_SpendingLimitControl\_Subscribe Response。
- 当OCS/CHF上配额状态发生变化，OCS/CHF主动向UPCF发送Sy/N28请求消息更新用户配额状态。Sy/N28请求消息的异常状态有如下两种情况：
  - 成功的Sy/N28请求消息，但消息中部分或全部配额信息处理失败。
  - 未携带任何配额信息的Sy/N28请求消息。

  **说明** 

  此场景下：

  - Sy请求消息为SNR，Sy响应消息为SNA。
  - N28请求消息为Nchf\_SpendingLimitControl\_Notify Request，N28响应消息为Nchf\_SpendingLimitControl\_Notify Response。

客户要求UPCF能够根据Sy/N28消息情况对Gx/N7会话进行处理：

- 使用此命令可以建立Sy结果码与Gx结果码的映射关系，从而实现基于Sy结果码控制Gx会话响应的目的。
- 使用此命令可以建立N28结果码与Gx结果码的映射关系，从而实现基于N28结果码控制Gx会话响应的目的。
- 使用此命令可以建立N28结果码与N7结果码的映射关系，从而实现基于N28结果码控制N7会话响应的目的。

Sy/N28结果码映射有5条默认记录，如表1所示：

| Sy/N28接口结果码            | CCA消息结果码                 | CreateResponse结果码   | RAR/UpdateNotify消息原因码      |   PCEF主机名 |   是否默认记录 |
|:-----------------------|:-------------------------|:--------------------|:---------------------------|----------:|---------:|
| RC0(SLATimeOut)        | RC2001(DIAMETER_SUCCESS) | RC201(Created)      | RC9999(Keep Session Alive) |       nan |        1 |
| RC1(CounterInfoError)  | RC2001(DIAMETER_SUCCESS) | RC201(Created)      | RC9999(Keep Session Alive) |       nan |        1 |
| RC2(EmptySNR)          | RC2001(DIAMETER_SUCCESS) | RC201(Created)      | RC9999(Keep Session Alive) |       nan |        1 |
| RC3(DefaultError)      | RC2001(DIAMETER_SUCCESS) | RC201(Created)      | RC9999(Keep Session Alive) |       nan |        1 |
| RC4(NoAvailableSyLink) | RC2001(DIAMETER_SUCCESS) | RC201(Created)      | RC9999(Keep Session Alive) |       nan |        1 |

**说明** 

- 以上默认数据允许修改Gx接口CCA消息结果码、N7接口CreateResponse结果码、Gx/N7接口RAR/UpdateNotify消息原因码、Gx接口PCEF主机名，不允许删除记录。
- 默认记录当中的“RC2(EmptySNR)”结果码映射仅适用于Sy接口。由于“RC2(EmptySNR)”在N28接口当中不属于合法消息，UPCF会直接给CHF回复携带“400 Bad Request”的响应消息而不会进行结果码映射。
- 默认记录当中的“RC4(NoAvailableSyLink)”结果码映射，应用于UPCF根据系统配置和签约信息需要创建Sy会话时获取不到可用的Sy链路的场景；通过修改SYRC=RC4的记录，指定Gx接口需要返回的结果码。
- 该命令的最大记录条数为301条（包括5条默认记录）。

## 注意事项

- 在处理Sy错误码场景时，如果映射结果不是RC2001(DIAMETER\_SUCCESS)或RC9999(Keep Session Alive)，则要求PCEF释放该Gx会话。为了保证VoLTE和VoWIFI会话在处理中不受影响，只释放APN类型为Force-Sy-APN的Gx会话。当所有APN类型为Force-Sy-APN的Gx会话都被释放后，UPCF会自动释放Sy会话。
- Sy/N28错误码映射不支持用户多Gx会话的场景。
- Sy/N28错误码映射不支持主从或企业用户场景。

## 参数说明

| 参数标识            | 参数名称                  | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:----------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SYRC            | Sy/N28接口结果码           | 可选必选说明：必选参数 参数含义：用于指定要进行转换的Sy/N28接口结果码。 取值范围：RC0(SLATimeOut)：表示UPCF在给OCS/CHF发出Sy/N28请求后未收到Sy/N28响应消息或Sy/N28响应消息超时。RC1(CounterInfoError)：表示UPCF收到OCS/CHF发送的成功Sy/N28消息，但消息中部分或全部配额信息处理失败。配额信息处理失败包括以下场景：该配额在UPCF未定义。该配额在UPCF已定义，但不是Sy类型配额。该配额在UPCF被组业务关联，但是用户在UPCF未加入任何组。该配额未关联业务。 RC2(EmptySNR)：表示UPCF收到OCS/CHF发送的Sy/N28请求消息未携带配额信息。RC3(DefaultError)：表示UPCF收到未定义结果码映射关系的Sy/N28错误码。RC4(NoAvailableSyLink)：表示UPCF向OCS发送Sy请求消息时无可用的链路。RC1001(DIAMETER_MULTI_ROUND_AUTH)RC2002(DIAMETER_LIMITED_SUCCESS)RC3001(DIAMETER_COMMAND_UNSUPPORTED)RC3002(DIAMETER_UNABLE_TO_DELIVER)RC3003(DIAMETER_REALM_NOT_SERVED)RC3004(DIAMETER_TOO_BUSY)RC3005(DIAMETER_LOOP_DETECTED)RC3006(DIAMETER_REDIRECT_INDICATION)RC3007(DIAMETER_APPLICATION_UNSUPPORTED)RC3008(DIAMETER_INVALID_HDR_BITS)RC3009(DIAMETER_INVALID_AVP_BITS)RC3010(DIAMETER_UNKNOWN_PEER)RC4001(DIAMETER_AUTHENTICATION_REJECTED)RC4002(DIAMETER_OUT_OF_SPACE)RC4241(DIAMETER_ERROR_NO_AVAILABLE_POLICY_COUNTERS)RC5001(DIAMETER_AVP_UNSUPPORTED)RC5002(DIAMETER_UNKNOWN_SESSION_ID)RC5003(DIAMETER_AUTHORIZATION_REJECTED)RC5004(DIAMETER_INVALID_AVP_VALUE)RC5005(DIAMETER_MISSING_AVP)RC5006(DIAMETER_RESOURCES_EXCEEDED)RC5007(DIAMETER_CONTRADICTING_AVPS)RC5008(DIAMETER_AVP_NOT_ALLOWED)RC5009(DIAMETER_AVP_OCCURS_TOO_MANY_TIMES)RC5010(DIAMETER_NO_COMMON_APPLICATION)RC5011(DIAMETER_UNSUPPORTED_VERSION)RC5012(DIAMETER_UNABLE_TO_COMPLY)RC5013(DIAMETER_INVALID_BIT_IN_HEADER)RC5014(DIAMETER_INVALID_AVP_LENGTH)RC5015(DIAMETER_INVALID_MESSAGE_LENGTH)RC5016(DIAMETER_INVALID_AVP_BIT_COMBO)RC5017(DIAMETER_NO_COMMON_SECURITY)RC5030(DIAMETER_USER_UNKNOWN)RC5570(DIAMETER_ERROR_UNKNOWN_POLICY_COUNTERS)RC400_0(400DEFAULT)RC400_1(INVALID_API)RC400_2(INVALID_MSG_FORMAT)RC400_3(INVALID_QUERY_PARAM)RC400_4(MANDATORY_IE_INCORRECT)RC400_5(UNSPECIFIED_MSG_FAILURE)RC400_6(MANDATORY_IE_MISSING)RC400_7(USER_UNKNOWN)RC400_8(NO_AVAILABLE_POLICY_COUNTERS)RC403_0(403DEFAULT)RC403_1(MODIFICATION_NOT_ALLOWED)RC404_0(404DEFAULT)RC404_1(SUBSCRIPTION_NOT_FOUND)RC404_2(RESOURCE_URI_STRUCTURE_NOT_FOUND)RC411_0(411DEFAULT)RC411_1(INCORRECT_LENGTH)RC429_0(429DEFAULT)RC429_1(NF_CONGESTION_RISK)RC500_0(500DEFAULT)RC500_1(INSUFFICIENT_RESOURCES)RC500_2(UNSPECIFIED_NF_FAILURE)RC500_3(SYSTEM_FAILURE)RC503_0(503DEFAULT) 默认值：无。 配置原则：当本参数配置为“RC3006”时，结果码映射不会生效。  说明： 当控制Sy消息重发次数的软参“VRM_SYRESENDTIMES”取值不为0时，该处描述的SLA消息超时是指尝试次数达到重发次数后依然超时的场景，例如当软参“VRM_SYRESENDTIMES”取值为3时，尝试了3次均超时才根据SLA超时场景配置控制Gx会话响应；如果前两次超时，最后一次响应成功，则按照收到成功的SLA响应处理。DRA组网下，路由重选软参“VRM_DIAMFAILOVERSWITCH”打开后，配置的RC3002和RC3005不支持进行错误码映射，直接通过Gx消息返回2001。 |
| CCARC           | CCA消息结果码              | 可选必选说明：必选参数 参数含义：用于指定Sy/N28接口消息结果码要转换成的Gx接口CCA消息结果码。 取值范围：RC2001(DIAMETER_SUCCESS)RC1001(DIAMETER_MULTI_ROUND_AUTH)RC2002(DIAMETER_LIMITED_SUCCESS)RC3001(DIAMETER_COMMAND_UNSUPPORTED)RC3002(DIAMETER_UNABLE_TO_DELIVER)RC3003(DIAMETER_REALM_NOT_SERVED)RC3004(DIAMETER_TOO_BUSY)RC3005(DIAMETER_LOOP_DETECTED)RC3006(DIAMETER_REDIRECT_INDICATION)RC3007(DIAMETER_APPLICATION_UNSUPPORTED)RC3008(DIAMETER_INVALID_HDR_BITS)RC3009(DIAMETER_INVALID_AVP_BITS)RC3010(DIAMETER_UNKNOWN_PEER)RC4001(DIAMETER_AUTHENTICATION_REJECTED)RC4002(DIAMETER_OUT_OF_SPACE)RC5001(DIAMETER_AVP_UNSUPPORTED)RC5002(DIAMETER_UNKNOWN_SESSION_ID)RC5003(DIAMETER_AUTHORIZATION_REJECTED)RC5004(DIAMETER_INVALID_AVP_VALUE)RC5005(DIAMETER_MISSING_AVP)RC5006(DIAMETER_RESOURCES_EXCEEDED)RC5007(DIAMETER_CONTRADICTING_AVPS)RC5008(DIAMETER_AVP_NOT_ALLOWED)RC5009(DIAMETER_AVP_OCCURS_TOO_MANY_TIMES)RC5010(DIAMETER_NO_COMMON_APPLICATION)RC5011(DIAMETER_UNSUPPORTED_VERSION)RC5012(DIAMETER_UNABLE_TO_COMPLY)RC5013(DIAMETER_INVALID_BIT_IN_HEADER)RC5014(DIAMETER_INVALID_AVP_LENGTH)RC5015(DIAMETER_INVALID_MESSAGE_LENGTH)RC5016(DIAMETER_INVALID_AVP_BIT_COMBO)RC5017(DIAMETER_NO_COMMON_SECURITY)RC5030(DIAMETER_USER_UNKNOWN)RC5140(DIAMETER_ERROR_INITIAL_PARAMETERS)RC5141(DIAMETER_ERROR_TRIGGER_EVENT)RC5142(DIAMETER_PCC_RULE_EVENT)RC5143(DIAMETER_ERROR_BEARER_NOT_AUTHORIZED)RC5144(DIAMETER_ERROR_TRAFFIC_MAPPING_INFO_REJECTED)RC5147(DIAMETER_ERROR_CONFLICTING_REQUEST) 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RARRC           | RAR/UpdateNotify消息原因码 | 可选必选说明：必选参数 参数含义：用于指定Sy/N28接口消息结果码要转换成的Gx接口RAR消息原因码，N28接口消息结果码要转换N7接口的UpdateNotify消息原因码。 取值范围：RC0(UNSPECIFIED_REASON)RC1(UE_SUBSCRIPTION_REASON)RC2(INSUFFICIENT_SERVER_RESOURCES)RC9999(Keep Session Alive) 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| N7RC            | CreateResponse结果码     | 可选必选说明：可选参数 参数含义：用于指定N28接口消息结果码要转换成的N7接口CreateResponse结果码。 取值范围： RC201(Created)RC400_1(USER_UNKNOWN)RC400_2(ERROR_INITIAL_PARAMETERS)RC403_1(POLICY_CONTEXT_DENIED)RC403_2(Forbidden)RC404(NOT_FOUND)NULL 默认值：NULL。 配置原则： 如果执行ADD SYTOGXRCMAP命令时未配置此参数，系统默认给此参数赋值为“NULL”。“CreateResponse结果码”和“PCEF主机名”不能同时设置为非NULL。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| HOSTNAME        | PCEF主机名               | 可选必选说明：必选参数 参数含义：用于标识Gx接口对端PCEF的主机名称。 取值范围：长度不超过127字节的字符串。 默认值：NULL。 配置原则： 如果此参数配置不为“NULL”，则与此参数值匹配的记录才进行错误码映射，不匹配的记录不进行错误码映射。如果此参数配置为“NULL”，则默认所有对端PCEF均进行错误码映射。“CreateResponse结果码”和“PCEF主机名”不能同时设置为非NULL。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ISDEFAULTRECORD | 是否默认记录                | 可选必选说明：可选参数 参数含义：用于标识该条记录是否为系统内置默认记录，不允许变更。 取值范围：0~1。 默认值：0。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## 使用实例

- 如果OCS收到UPCF发送的SLR消息后，发现对于此用户无有效的配额，则OCS会向UPCF返回携带4241 DIAMETER\_ERROR\_NO\_AVAILABLE\_POLICY\_COUNTERS错误码的SLA消息。若需要UPCF在收到该错误码后，强制用户下线，则需要执行以下配置过程：

  添加一条Sy结果码映射，“Sy/N28接口结果码”为“RC4241”，“CCA消息结果码”为“RC5005”，“RAR/UpdateNotify消息原因码”为“RC0”，“PCEF主机名”为“NULL”。

  ```
  ADD SYTOGXRCMAP: SYRC=RC4241, CCARC=RC5005, RARRC=RC0, HOSTNAME="NULL";
  ```

  ```
  %%ADD SYTOGXRCMAP: SYRC=RC4241, CCARC=RC5005, RARRC=RC0, HOSTNAME="NULL";%%
  RETCODE = 0  操作成功

  ---    END
  ```
- 如果OCS收到UPCF发送的SLR消息后，发现对于此用户无有效的配额，则OCS会向UPCF返回携带4241 DIAMETER\_ERROR\_NO\_AVAILABLE\_POLICY\_COUNTERS错误码的SLA消息。若需要UPCF在收到该错误码后，不强制用户下线，则需要执行以下配置过程：

  添加一条Sy结果码映射，“Sy/N28接口结果码”为“RC4241”，“CCA消息结果码”为“RC2001”，“RAR/UpdateNotify消息原因码”为“RC9999”，“PCEF主机名”为“NULL”。

  ```
  ADD SYTOGXRCMAP: SYRC=RC4241, CCARC=RC2001, RARRC=RC9999, HOSTNAME="NULL";
  ```

  ```
  %%ADD SYTOGXRCMAP: SYRC=RC4241, CCARC=RC2001, RARRC=RC9999, HOSTNAME="NULL";%%
  RETCODE = 0  操作成功

  ---    END
  ```
- 如果CHF收到UPCF发送的Nchf\_SpendingLimitControl\_Subscribe Request消息后，发现对于此用户无有效的配额，则CHF会向UPCF返回携带400 Bad Request（原因值为“NO\_AVAILABLE\_POLICY\_COUNTERS”）错误码的Nchf\_SpendingLimitControl\_Subscribe Response消息。若需要UPCF在收到该错误码后，不强制用户下线，则需要执行以下配置过程：

  添加一条N28结果码映射，“Sy/N28接口结果码”为“RC400\_8”，“CCA消息结果码”为“RC2001”，“RAR/UpdateNotify消息原因码”为“RC9999”，“CreateResponse结果码”为“RC201”，“PCEF主机名”为“NULL”。

  ```
  ADD SYTOGXRCMAP: SYRC=RC400_8, CCARC=RC2001, RARRC=RC9999, N7RC=RC201, HOSTNAME="NULL";
  ```

  ```
  %%ADD SYTOGXRCMAP: SYRC=RC400_8, CCARC=RC2001, RARRC=RC9999, N7RC=RC201, HOSTNAME="NULL";%%
  RETCODE = 0  操作成功

  ---    END
  ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|   错误码 | 错误码解释                                   | 原因分析                                       | 处理建议                                                                                                                                |
|------:|:----------------------------------------|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| 57655 | SYTOGXRCMAP已经达到最大数限制。                   | 映射记录数已达到最大数限制。                             | 执行LST SYTOGXRCMAP查询所有已存在映射记录，执行RMV SYTOGXRCMAP删除不需要的映射记录，再执行ADD SYTOGXRCMAP命令添加映射记录。                                                |
| 57656 | 对象已存在， 不能增加相同的对象。                       | 历史操作中，已添加该Sy/N28接口结果码的映射记录。                | 执行LST SYTOGXRCMAP查询该Sy/N28接口结果码是否已经存在映射记录，并检查该映射关系是否和要添加的映射记录一致。如果一致，则无需再执行ADD SYTOGXRCMAP命令；如果不一致，则执行MOD SYTOGXRCMAP命令修改为要添加的映射记录。 |
| 58048 | CreateResponse结果码和PCEF主机名称不能同时设置为非NULL。 | “CreateResponse结果码”和“PCEF主机名”同时设置了非NULL取值。 | 执行本命令时 “CreateResponse结果码”和“PCEF主机名”不同时配置非NULL取值。                                                                                   |
| 58272 | 不允许添加ISDEFAULTRECORD为1的记录。              | 该命令不允许添加“是否默认记录”为“1”的记录。                   | 输入“是否默认记录”的取值为“0”，重新执行本命令。                                                                                                          |