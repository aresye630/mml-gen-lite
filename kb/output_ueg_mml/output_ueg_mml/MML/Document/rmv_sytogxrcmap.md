# 删除Sy/N28结果码映射（RMV SYTOGXRCMAP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

此命令是高危命令，执行不当会导致Sy/N28结果码与Gx/N7结果码的映射关系不正确，需联系华为技术支持确认后再执行。

该命令用于在UPCF配置数据库中删除一条Sy/N28结果码映射记录。

在该命令中，系统通过“Sy/N28接口结果码”和“PCEF主机名”参数来标识一条Sy/N28结果码映射记录。

## 注意事项

该命令不能删除默认的5条记录。

## 参数说明

| 参数标识     | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:---------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SYRC     | Sy/N28接口结果码 | 可选必选说明：必选参数 参数含义：用于指定要删除的Sy/N28接口消息结果码。 取值范围：RC0(SLATimeOut)RC1(CounterInfoError)RC2(EmptySNR)RC3(DefaultError)RC4(NoAvailableSyLink)RC1001(DIAMETER_MULTI_ROUND_AUTH)RC2002(DIAMETER_LIMITED_SUCCESS)RC3001(DIAMETER_COMMAND_UNSUPPORTED)RC3002(DIAMETER_UNABLE_TO_DELIVER)RC3003(DIAMETER_REALM_NOT_SERVED)RC3004(DIAMETER_TOO_BUSY)RC3005(DIAMETER_LOOP_DETECTED)RC3006(DIAMETER_REDIRECT_INDICATION)RC3007(DIAMETER_APPLICATION_UNSUPPORTED)RC3008(DIAMETER_INVALID_HDR_BITS)RC3009(DIAMETER_INVALID_AVP_BITS)RC3010(DIAMETER_UNKNOWN_PEER)RC4001(DIAMETER_AUTHENTICATION_REJECTED)RC4002(DIAMETER_OUT_OF_SPACE)RC4241(DIAMETER_ERROR_NO_AVAILABLE_POLICY_COUNTERS)RC5001(DIAMETER_AVP_UNSUPPORTED)RC5002(DIAMETER_UNKNOWN_SESSION_ID)RC5003(DIAMETER_AUTHORIZATION_REJECTED)RC5004(DIAMETER_INVALID_AVP_VALUE)RC5005(DIAMETER_MISSING_AVP)RC5006(DIAMETER_RESOURCES_EXCEEDED)RC5007(DIAMETER_CONTRADICTING_AVPS)RC5008(DIAMETER_AVP_NOT_ALLOWED)RC5009(DIAMETER_AVP_OCCURS_TOO_MANY_TIMES)RC5010(DIAMETER_NO_COMMON_APPLICATION)RC5011(DIAMETER_UNSUPPORTED_VERSION)RC5012(DIAMETER_UNABLE_TO_COMPLY)RC5013(DIAMETER_INVALID_BIT_IN_HEADER)RC5014(DIAMETER_INVALID_AVP_LENGTH)RC5015(DIAMETER_INVALID_MESSAGE_LENGTH)RC5016(DIAMETER_INVALID_AVP_BIT_COMBO)RC5017(DIAMETER_NO_COMMON_SECURITY)RC5030(DIAMETER_USER_UNKNOWN)RC5570(DIAMETER_ERROR_UNKNOWN_POLICY_COUNTERS)RC400_0(400DEFAULT)RC400_1(INVALID_API)RC400_2(INVALID_MSG_FORMAT)RC400_3(INVALID_QUERY_PARAM)RC400_4(MANDATORY_IE_INCORRECT)RC400_5(UNSPECIFIED_MSG_FAILURE)RC400_6(MANDATORY_IE_MISSING)RC400_7(USER_UNKNOWN)RC400_8(NO_AVAILABLE_POLICY_COUNTERS)RC403_0(403DEFAULT)RC403_1(MODIFICATION_NOT_ALLOWED)RC404_0(404DEFAULT)RC404_1(SUBSCRIPTION_NOT_FOUND)RC404_2(RESOURCE_URI_STRUCTURE_NOT_FOUND)RC411_0(411DEFAULT)RC411_1(INCORRECT_LENGTH)RC429_0(429DEFAULT)RC429_1(NF_CONGESTION_RISK)RC500_0(500DEFAULT)RC500_1(INSUFFICIENT_RESOURCES)RC500_2(UNSPECIFIED_NF_FAILURE)RC500_3(SYSTEM_FAILURE)RC503_0(503DEFAULT) 默认值：无。 配置原则：无。 |
| HOSTNAME | PCEF主机名     | 可选必选说明：必选参数 参数含义：用于指定要删除的Gx接口对端PCEF的主机名称。 取值范围：长度不超过127字节的字符串。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## 使用实例

- 删除一条Sy结果码映射，“Sy/N28接口结果码”为“RC3001”，“PCEF主机名”为“huawei1.com”。

  ```
  RMV SYTOGXRCMAP: SYRC=RC3001, HOSTNAME="huawei1.com";
  ```

  ```
  %%RMV SYTOGXRCMAP: SYRC=RC3001, HOSTNAME="huawei1.com";%%
  RETCODE = 0  操作成功

  ---    END
  ```

- 删除一条N28结果码映射，“Sy/N28接口结果码”为“RC400\_3”，“PCEF主机名”为“NULL”。

  ```
  RMV SYTOGXRCMAP: SYRC=RC400_3, HOSTNAME="NULL";
  ```

  ```
  %%RMV SYTOGXRCMAP: SYRC=RC400_3, HOSTNAME="NULL";%%
  RETCODE = 0  操作成功

  ---    END
  ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释     | 原因分析               | 处理建议       |
|------:|:----------|:-------------------|:-----------|
| 57654 | 不能删除默认数据。 | 默认映射记录允许修改，但不允许删除。 | 默认数据不允许删除。 |