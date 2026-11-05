# 显示PCC会话信息（DSP PCCSESSINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询指定IMSI、MSISDN或IMEI的会话中所有的承载、PCC规则的安装情况，以及规则的生效失效时间、流量监控、profile-space、PRA等相关信息，适用于PCC用户。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                     |
|:------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| USERIDTYPE  | 用户标识类型 | 可选必选说明：必选参数 参数含义：该参数用于指定需要查询的用户类型。 数据来源：本端规划 取值范围：枚举类型。 IMSI：按IMSI查询用户信息。MSISDN：按MSISDN查询用户信息。IMEI：按IMEI查询用户信息。 默认值：无 配置原则：无                             |
| MSISDN      | MSISDN | 可选必选说明：条件必选参数 前提条件：该参数在“USERIDTYPE”配置为“MSISDN”时为必选参数。 参数含义：该参数用于指定被查询用户的MSISDN号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 默认值：无 配置原则：无            |
| IMSI        | IMSI   | 可选必选说明：条件必选参数 前提条件：该参数在“USERIDTYPE”配置为“IMSI”时为必选参数。 参数含义：该参数用于指定被查询用户的IMSI号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 默认值：无 配置原则：无                |
| IMEI        | IMEI   | 可选必选说明：条件必选参数 前提条件：该参数在“USERIDTYPE”配置为“IMEI”时为必选参数。 参数含义：该参数用于指定被查询用户的IMEI号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～16。每个字符必须为0~9的数字。 默认值：无 配置原则：无                |
| DISPLAYMODE | 显示方式   | 可选必选说明：可选参数 参数含义：该参数用于指定显示用户会话信息的模式。 数据来源：本端规划 取值范围：枚举类型。 SIMPLE：显示用户的会话信息。VERBOSE：显示用户的会话详细信息。USG_MONITORING：显示用户的Usage Monitoring信息。 默认值：SIMPLE 配置原则：无 |

#### 使用实例

- Gx接口：查询IMSI为123011223344551的在线用户的会话信息：

  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551";
  ```

  ```
  RETCODE = 0  操作成功。

  PCC Session 信息
  -----------------------
  结果  =  
  Pcc Session 信息 IMSI 123031500010001 on Pod uncpod-0
  (No:1)
  -----------------------------------------------------------

  承载的QoS信息:
  ---------------------------
  QFI   QCI   Arp.PriorityLevel   Arp.preemptCap      Arp.preemptVuln     
  1     7     2                   May Preempt         Not Preemptable     

  承载的动态规则信息  [QFI:1]
  -----------------------------------------------------
  No    规则名称            规则来源            优先级
  1     rule2               PCRF Created        1000
  (结果个数 = 1)

  ---    END
  ```
- Gx接口：查询IMSI为123011223344551的在线用户的会话详细信息：

  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551", DISPLAYMODE=VERBOSE;
  ```

  ```
  RETCODE = 0  操作成功。

  PCC Session 信息
  -----------------------
  结果  =
  Pcc Session 信息 IMSI 123031500010001 on Pod uncpod-0
  (No:1)
  -----------------------------------------------------------

  Qosflow information :
  ---------------------------
  No   QFI   FiveQI   PriorityLevel   Arp.PriorityLevel   Arp.preemptCap   Arp.preemptVuln   MaxDataBurstVol   AverWindow    Qnc
  1    1     7        0               2                   May Preempt      Preemptable       0                 0             false

  Predefined Rule Information
  ---------------------------
  No   RuleName         Type             PolicyType
  1    any_uptolocalpcc UserProfile Rule PCC
  (结果个数 = 1)

  ---    END
  ```
- Gx接口：查询IMSI为123011223344551的在线用户的Usage Monitoring信息：

  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551", DISPLAYMODE=USG_MONITORING;
  ```

  ```
  RETCODE = 0  操作成功。

  PCC Session 信息
  -----------------------
  结果  =
  Pcc Session 信息 IMSI 123031500010001 on Pod uncpod-0
  (No:1)
  -----------------------------------------------------------

  Qosflow information :
  ---------------------------
  No   QFI   FiveQI   PriorityLevel   Arp.PriorityLevel   Arp.preemptCap   Arp.preemptVuln   MaxDataBurstVol   AverWindow    Qnc
  1    1     7        0               2                   May Preempt      Preemptable       0                 0             false

  Predefined Rule Information
  ---------------------------
  No   RuleName         Type             PolicyType
  1    any_uptolocalpcc UserProfile Rule PCC
  (结果个数 = 1)

  ---    END
  ```
- N7接口：查询IMSI为123011223344551的在线用户的会话信息：

  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551";
  ```

  ```
  RETCODE = 0  操作成功

  PCC会话信息
  -----------
  查询结果  =  
  PCC session information for IMSI 123011223344551 on Pod uncpod-0
  (session id: 5)
  -----------------------------------------

  Qosflow information :
  ---------------------
  No   QFI   FiveQI   PriorityLevel   Arp.PriorityLevel   Arp.preemptCap   Arp.preemptVuln   MaxDataBurstVol   AverWindow    Qnc
  1    1     5        0               3                   Not Preempt      Preemptable       0                 0             false

  Dynamic Rule Information of QosFlow/Bearer [QFI:1] 
  ---------------------------------------------------
  No   RuleName  RuleSource      Priority
  1    PccRule1  PCF created     1

  IPE Session Information
  --------------------
  IPE-Session-Associated-Indicator = false
  (结果个数 = 1)

  ---    END
  ```
- N7接口：查询IMSI为123011223344551的在线用户的会话详细信息：

  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551", DISPLAYMODE=VERBOSE;
  ```

  ```
  RETCODE = 0  操作成功。

  PCC Session 信息
  -----------------------
  结果  =
  Pcc Session 信息 IMSI 123031500010001 on Pod uncpod-0
  (No:1)
  -----------------------------------------------------------

  Qosflow information :
  ---------------------------
  No   QFI   FiveQI   PriorityLevel   Arp.PriorityLevel   Arp.preemptCap   Arp.preemptVuln   MaxDataBurstVol   AverWindow    Qnc
  1    1     5        0               1                   May Preempt      Preemptable       0                 0             false

  Predefined Rule Information
  ---------------------------
  No   RuleName         Type             PolicyType
  1    any_uptolocalpcc UserProfile Rule PCC

  IPE Session Information
  --------------------
  IPE-Session-Associated-Indicator = false
  (结果个数 = 1)

  ---    END
  ```
- N7接口：查询IMSI为123011223344551的在线用户的Usage Monitoring信息：

  ```
  DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="123011223344551", DISPLAYMODE=USG_MONITORING;
  ```

  ```
  RETCODE = 0  操作成功。

  PCC Session 信息
  -----------------------
  结果  =
  Pcc Session 信息 IMSI 123031500010001 on Pod uncpod-0
  (No:1)
  -----------------------------------------------------------

  Qosflow information :
  ---------------------------
  No   QFI   FiveQI   PriorityLevel   Arp.PriorityLevel   Arp.preemptCap   Arp.preemptVuln   MaxDataBurstVol   AverWindow    Qnc
  1    1     5        0               1                   May Preempt      Preemptable       0                 0             false

  Predefined Rule Information
  ---------------------------
  No   RuleName         Type             PolicyType
  1    any_uptolocalpcc UserProfile Rule PCC

  IPE Session Information
  --------------------
  IPE-Session-Associated-Indicator = false
  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

| 输出项名称                            | 输出项解释                                                                                      |
|:---------------------------------|:-------------------------------------------------------------------------------------------|
| No                               | 序号。                                                                                        |
| QFI                              | QosFlow标识。                                                                                 |
| FiveQI                           | QosFlow QoS的5QI。                                                                           |
| PriorityLevel                    | QosFlow QoS的优先级，当优先级是3GPP TS 23.501中标准5QI对应的优先级时显示为0。                                      |
| Arp.PriorityLevel                | ARP优先级。                                                                                    |
| Arp.preemptCap                   | ARP抢占能力。                                                                                   |
| Arp.preemptVuln                  | ARP可被抢占。                                                                                   |
| MaxDataBurstVol                  | 最大数据突发量。                                                                                   |
| AverWindow                       | 平均窗口。                                                                                      |
| Qnc                              | QOS通知控制。                                                                                   |
| RuleName                         | 规则名字。                                                                                      |
| RuleSource                       | 规则来源。                                                                                      |
| Priority                         | 规则优先级。                                                                                     |
| IPE-Session-Associated-Indicator | 指示当前会话是否伴随智能N7会话，为True时表示伴随智能N7会话建立。                                                       |
| PolicyType                       | 策略名称。                                                                                      |
| Type                             | 预定义规则类型，包括UserProfile Rule和Static Rule。当UserProfile存在绑定规则时，输出内容只会显示UserProfile而不会显示所绑定的规则。 |