# 设置AMF与PCF消息交互处理策略（SET AMFPCFPRCSSPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

该命令用于设置AMF与PCF之间消息的处理策略。

通过本命令可以灵活调整AMF与PCF网元交互时的处理策略。例如：AMF创建AM策略偶联过程中，收到PCF发送的Npcf\_AMPolicyControl\_UpdateNotify Request消息，为避免双方死锁，可以将CRTCFLUPDNTF设置为PENDING。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TMNTAFTCRT   | CRTCFLUPDNTF   |
|:-------------|:---------------|
| NO_CHECK     | PREEMPT        |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称                        | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------|:----------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TMNTAFTCRT   | AMF收到Termination处理策略        | 可选必选说明：可选参数  参数含义：该参数用于指示AMF创建AM策略偶联后收到AM-PCF发送的Npcf_AMPolicyControl_AmPolicyAssociationTerminateNotify Request消息的处理策略。  数据来源：全网规划 取值范围： NO_CHECK（不校验偶联ID）CHECK（校验偶联ID）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPCFPRCSSPLCY查询当前参数配置值。  配置原则：  当本参数设置为“CHECK”时，AMF会校验AM-PCF发送的Npcf_AMPolicyControl_AmPolicyAssociationTerminateNotify Request中偶联ID和本地上下文保存的偶联ID是否一致，当偶联ID不一致时，AMF回复404 Not Found；当偶联ID一致时，AMF回复204 No Content。  当本参数设置为“NO_CHECK”时，AMF不会校验AM-PCF发送的Npcf_AMPolicyControl_AmPolicyAssociationTerminateNotify Request中偶联ID，AMF回复204 No Content。                                                                                                                                                                                                                                                      |
| CRTCFLUPDNTF | 创建AM策略偶联时收到UpdateNotify处理策略 | 可选必选说明：可选参数  参数含义：该参数用于指示AMF发送Npcf_AMPolicyControl_Create Request消息后收到Npcf_AMPolicyControl_UpdateNotify Request消息的处理策略。  数据来源：全网规划 取值范围： “PREEMPT（抢占）”：AMF进行抢占处理，此实现为原有实现，会导致AMF后续不处理Npcf_AMPolicyControl_Create Response。“DISCARD（丢弃）”：AMF丢弃Npcf_AMPolicyControl_UpdateNotify Request消息。“PENDING（AMF响应状态码400 Bad Request）”：AMF向PCF响应状态码400 Bad Request，cause为PENDING_TRANSACTION。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFPCFPRCSSPLCY查询当前参数配置值。  配置原则：  当本参数设置为“PENDING”时，AMF向PCF响应状态码400 Bad Request，cause为PENDING_TRANSACTION。  当本参数设置为“DISCARD”时， AMF丢弃Npcf_AMPolicyControl_UpdateNotify Request并继续等待Npcf_AMPolicyControl_Create Response，设置此选项时需要考虑对端AM-PCF是否会优先处理Npcf_AMPolicyControl_Create Request消息，否则容易造成双方死锁。  当本参数设置为“PREEMPT”时，AMF进行抢占处理，此实现为原有实现，会导致AMF后续没有处理Npcf_AMPolicyControl_Create Response。 |

## 使用实例

设置AMF需要校验PCF发送的Npcf\_AMPolicyControl\_AmPolicyAssociationTerminateNotify Request消息中偶联ID与用户中上下文保存的偶联ID是否一致，执行如下命令：

```
SET AMFPCFPRCSSPLCY:TMNTAFTCRT=CHECK;
```