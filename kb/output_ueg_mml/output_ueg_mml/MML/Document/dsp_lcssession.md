# 显示LCS会话信息（DSP LCSSESSION）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于显示LCS的会话信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                                                            |
|:----------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUERYTYPE | 查询方式   | 可选必选说明：必选参数 参数含义：该参数用于指定查询会话的方式。 数据来源：全网规划 取值范围： MSISDN：指定待查询用户的MSISDN号。IMSI：指定待查询用户的IMSI号。 默认值：无 配置原则：该参数配置为MSISDN时，指定按照MSISDN方式查询会话；该参数配置为IMSI时，指定按照IMSI查询会话。 |
| NFTYPE    | NF类型   | 可选必选说明：必选参数 参数含义：该参数用于指定NF类型。 数据来源：全网规划 取值范围： NfLMF：NfLMF。NfGMLC：NfGMLC。 默认值：无 配置原则：该参数配置为NfGMLC时，指定查询GMLC上的会话；该参数配置为NfLMF时，指定查询LMF上的会话。                        |
| MSISDN    | MSISDN | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“MSISDN”时为必选参数。 参数含义：该参数用于指定用户的MSISDN信息。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～15。 默认值：无 配置原则：无                                    |
| IMSI      | IMSI   | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“IMSI”时为必选参数。 参数含义：该参数用于指定用户的IMSI信息。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～15。 默认值：无 配置原则：无                                        |

#### 使用实例

查询LMF的会话信息：

```
DSP LCSSESSION: QUERYTYPE=MSISDN, NFTYPE=NfLMF, MSISDN="8613901361234";
```

```
RETCODE = 0  操作成功

LCS会话信息
-----------------------
Result  =  
-------------------------------

LCS Context on Pod: lcs-e-pod-d6c54755d-s428l
-----------------------------------------
                                     IMSI = 14456789012342
                                   MSISDN = 8613901361234
                         Active TimeStamp = 03:52:25 02/05/2024(MM/DD/YYYY)
                       Reporting Interval = 10240s

                                      MCC = 460  
                                      MNC = 00   
                               NR Cell ID = 1bf4e0028
                            gNB ID Length = 24   
                                 gNB Type = Small Cell

                           AMF InstanceID = AMF_Instance_0
                     AMF SCP ModeD Switch = false    
                        AMF Correlationid = 12   
                         LMF Address IPV4 = 192.168.0.0:33000
                   LMF Local NFInstanceId = 3863cb65-6f9f-4fa5-9efb-ee39fbb9be98

                        User Trace Switch = false    
  Positioning Deactivation Message Switch = false    
                      TRP Function Switch = false
(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称                                     | 输出项解释                                       |
|:------------------------------------------|:--------------------------------------------|
| IMSI                                      | 国际移动用户标识。                                   |
| MSISDN                                    | 用户的MSISDN号。                                 |
| Active TimeStamp                          | 用户发起定位的时间。                                  |
| Reporting Interval                        | 周期性定位的上报周期。                                 |
| MCC                                       | PLMN的移动国家码部分，由3位数字组成。                       |
| MNC                                       | PLMN的移动网络码部分，由2位或3位数字组成。                    |
| NR Cell ID                                | UE当前所驻留的小区。                                 |
| gNB ID Length                             | UE当前所驻留的基站标识长度。                             |
| gNB Type                                  | UE当前所驻留的基站类型，Small Cell代表小站，Macro Cell代表宏站。 |
| AMF InstanceID                            | 用户接入的AMF实例ID。                               |
| AMF SCP ModeD Switch                      | AMF是否使能SCP功能。                               |
| AMF Correlationid                         | AMF分配的定位会话ID。                               |
| LMF Address IPV4                          | LMF的IPV4地址。                                 |
| LMF Address IPV6                          | LMF的IPV6地址。                                 |
| LMF Local NFInstanceId                    | LMF的实例ID。                                   |
| User Trace Switch                         | 用户的LCS跟踪开关是否开启。                             |
| Positioning Deactivation Message Switch   | LMF发送Positioning Deactivation消息开关是否开启。      |
| Macro Cell One Dimension Algorithm Switch | 宏站一维算法定位开关是否开启。                             |
| TRP Function Switch                       | TRP获取功能开关是否开启。                              |
| GMLC Address IPV4                         | GMLC的IPV4地址。                                |
| GMLC Address IPV6                         | GMLC的IPV6地址。                                |
| Subscription ID                           | 周期性定位返回给LCS Client的订阅ID，标记已创建的订阅请求。         |