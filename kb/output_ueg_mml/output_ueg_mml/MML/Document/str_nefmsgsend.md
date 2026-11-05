# 启动向NEF发送消息（STR NEFMSGSEND）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF**

该命令用于启动向NEF发送消息。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                            |
|:-------------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI         | 用户标识    | 可选必选说明：必选参数  参数含义：该参数用于指定用户标识。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是5~15。  默认值：无  配置原则：无                                                                                                                                                                                                                               |
| PDUSESSIONID | PDU会话ID | 可选必选说明：必选参数  参数含义：该参数用于指定PDU会话。  数据来源：本端规划  取值范围：整数类型，取值范围是1~15。  默认值：无  配置原则：无                                                                                                                                                                                                                                 |
| MSGTYPE      | 报告类型    | 可选必选说明：必选参数  参数含义：该参数用于指定报告类型。  数据来源：本端规划 取值范围： Nnef_PFDManagement_Fetch（SMF获取PFD应用资源）Nnef_PFDManagement_Subscribe（SMF订阅PFD资源）Nnef_PFDManagement_Unsubscribe（SMF去订阅PFD资源）Nnef_SMContext_Create（SMF向NEF发起创建会话上下文）Nnef_SMContext_Delete（SMF向NEF发起删除会话上下文）Nnef_SMContext_Delivery（SMF向NEF发起传递会话上下文）  默认值：无  配置原则：无 |
| APPID        | 应用标识    | 可选必选说明：该参数在"MSGTYPE"配置为"Nnef_PFDManagement_Fetch"、"Nnef_PFDManagement_Subscribe"时为条件必选参数。  参数含义：该参数用于指定应用标识。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~100。  默认值：无  配置原则：无                                                                                                                                                |
| NEFID        | NEF标识   | 可选必选说明：该参数在"MSGTYPE"配置为"Nnef_SMContext_Create"时为条件必选参数。  参数含义：该参数用于指定网络能力开放功能网元标识。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~36。  默认值：无  配置原则：  本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。                                                                                                                         |

## 使用实例

启动向NEF发送消息时使用该命令。
1. SMF获取PFD应用资源：
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef\_PFDManagement\_Fetch,APPID="001"
2. SMF订阅PFD资源：
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef\_PFDManagement\_Subscribe,APPID="001";
3. SMF去订阅PFD资源：
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef\_PFDManagement\_Unsubscribe;
4. SMF向NEF发起创建会话上下文：
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef\_SMContext\_Create,NEFID="nef001";
5. SMF向NEF发起删除会话上下文：
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef\_SMContext\_Delete;
6. SMF向NEF发起传递会话上下文：
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef\_SMContext\_Delivery;

```
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef_PFDManagement_Fetch,APPID="001";
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef_PFDManagement_Subscribe,APPID="001";
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef_PFDManagement_Unsubscribe;
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef_SMContext_Create,NEFID="nef001";
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef_SMContext_Delete;
STR NEFMSGSEND:IMSI="123031700100001",PDUSESSIONID=5,MSGTYPE=Nnef_SMContext_Delivery;
```