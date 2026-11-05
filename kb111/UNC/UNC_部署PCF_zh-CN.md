---
id: ''
name: 部署PCF
ne_type: UNC
type: feature
description: 融合计费场景中，当用户的配额由CHF管理时，业务配置中的配额信息由CHF定义，PCF只需定义配额的“名称”、“配额管理归属”和“缺省状态”，且配额的名称需要和CHF上的定义保持一致。PCF通过从CHF中获取到的配额状态向SMF下发相应策略为例，具体场景如表1所示。  **表1** 根据Sy配额的状态控制速率  | Sy配额状态 | UPCF配额状态 | 带宽控制 | | --- | --- | --- | | 0 | Normal | 正常速率，用户会话请求速率，PCF下发预定义规则Rule001。 | | 1 | Level1 | 限速100 Mbps，PCF下发预定义规则Rule002。 | | 2 | Level2 | 限速512 Kbps，PCF下发预定义规则Rule003。 | | 5 | Exhaust | 强制用户下线。 |
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案三：部署NCG且基于服务化接口的纯离线计费组网方案","部署PCF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
融合计费场景中，当用户的配额由CHF管理时，业务配置中的配额信息由CHF定义，PCF只需定义配额的“名称”、“配额管理归属”和“缺省状态”，且配额的名称需要和CHF上的定义保持一致。PCF通过从CHF中获取到的配额状态向SMF下发相应策略为例，具体场景如表1所示。**表1** 根据Sy配额的状态控制速率| Sy配额状态 | UPCF配额状态 | 带宽控制 || --- | --- | --- || 0 | Normal | 正常速率，用户会话请求速率，PCF下发预定义规则Rule001。 || 1 | Level1 | 限速100 Mbps，PCF下发预定义规则Rule002。 || 2 | Level2 | 限速512 Kbps，PCF下发预定义规则Rule003。 || 5 | Exhaust | 强制用户下线。 |

## 必备事项
前提条件

**前提条件**

* 操作员已了解UPCF产品手册的“WHFD-611072 N28接口（基于HTTP协议）策略控制特性描述”。
* 操作已完成配置UPCF与CHF的对接数据。
* N28接口开关已启用，即软参**VRM\_SYSWITCH（Sy接口开关）**已设置为“1”、“2”或“3”。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_psub_list:
      type: items
      properties:
        USRIDENTIFIER:
          name: 'USRIDENTIFIER'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRMSISDN:
          name: 'USRMSISDN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRSTATE:
          name: 'USRSTATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRPAIDTYPE:
          name: 'USRPAIDTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRSTATION:
          name: 'USRSTATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRCONTACTMETHOD:
          name: 'USRCONTACTMETHOD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRBILLCYCLEDATE:
          name: 'USRBILLCYCLEDATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRSUBNETTYPE:
          name: 'USRSUBNETTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_psrv_list:
      type: items
      properties:
        USRIDENTIFIER:
          name: 'USRIDENTIFIER'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNAME:
          name: 'SRVNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVUSAGESTATE:
          name: 'SRVUSAGESTATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVROAMINGTYPE:
          name: 'SRVROAMINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_psub_list:
    - USRIDENTIFIER: 12310381012****
      USRMSISDN: 1234567****
      USRSTATE: Normal
      USRPAIDTYPE: 'NULL'
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: 'NULL'
      USRSUBNETTYPE: eMBB-SA
    add_psrv_list:
    - USRIDENTIFIER: 12310381012****
      SRVNAME: Nchf_Service
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UPCF Web UI界面。

### 2 配置**“配额”**。

### 导航入口为“业务管理 > 业务 > 配额”。

### 配额（Quota）是指一个指定周期内供用户使用的流量或时长，也可指单个会话内供用户使用的时长额度。当业务的使用与流量、时长均相关时，需要配置流量配额和时长配额。

### 配额的数据规划如表3所示，详细参数说明请参见UPCF产品手册上的**“配额参数表”**。

### **表3** 配额

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 配额 | 基本信息 | 名称 | CHF\_Quota |

### |  |  | 配额管理归属 | Sy |

### |  |  | 缺省状态 | Normal |

### |  |  | 单次型配额 | 否 |

### |  | 复位设置 | 结帐模式 | Sy设定 |

### 3 配置“配额状态映射”

### 导航入口为“系统配置管理 > 系统配置 > 配额状态映射”。

### 配额状态映射的数据规划如表4所示，详细参数说明请参见“配额状态映射参数说明”。

### **表4** 配额状态映射

### | 类别 | 参数 | 取值样例 |

### | --- | --- | --- |

### | 配额状态映射 | 协议配额状态 | * 0 * 1 * 2 * 5 说明：  “协议配额状态”的取值不能重复。 |

### |  | 配额状态 | * Normal * Level1 * Level2 * Exhaust |

### 4 配置“条件组”。

### 导航入口为“策略管理 > 策略 > 条件组”。

### 条件组的数据规划如表5所示，详细参数说明请参见“条件组参数说明”。

### **表5** 条件组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组1 | 基本信息 | 名称 | Nchf\_CG\_norm |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Nchf\_C\_norm |

### |  |  | 对象属性 | * 对象：Quota * 属性：QuotaStatus |

### |  |  | 对象实例 | CHF\_Quota  说明：  已在配额中定义。 |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Normal  说明：  “Normal”：表示配额消耗小于Level1。 |

### | 条件组2 | 基本信息 | 名称 | Nchf\_CG\_Lev1 |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Nchf\_C\_Lev1 |

### |  |  | 对象属性 | * 对象：Quota * 属性：QuotaStatus |

### |  |  | 对象实例 | CHF\_Quota  说明：  已在配额中定义。 |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Level1  说明：  “Level1”：表示配额消耗大于等于Level1、但小于Level2。 |

### | 条件组3 | 基本信息 | 名称 | Nchf\_CG\_Lev2 |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Nchf\_C\_Lev2 |

### |  |  | 对象属性 | * 对象：Quota * 属性：QuotaStatus |

### |  |  | 对象实例 | CHF\_Quota  说明：  已在配额中定义。 |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Level2  说明：  “Level2”：表示配额消耗大于等于Level2、但未耗尽。 |

### | 条件组4 | 基本信息 | 名称 | Nchf\_CG\_Exhaust |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Nchf\_C\_Exhaust |

### |  |  | 对象属性 | * 对象：Quota * 属性：QuotaStatus |

### |  |  | 对象实例 | CHF\_Quota  说明：  已在配额中定义。 |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Exhaust  说明：  “Exhaust”：表示配额耗尽。 |

### 5 配置“5G动作组”。

### 导航入口为“策略管理 > 策略 > 5G动作组”。

### 5G动作组的数据规划如表6所示，详细参数说明请参见**5G动作组参数说明**。

### **表6** 5G动作组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组1 | 基本信息 | 名称 | Rule001 |

### |  |  | 类型 | PredefinedPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：Rule001 |

### | 5G动作组2 | 基本信息 | 名称 | Rule002 |

### |  |  | 名称 | PredefinedPccRule |

### |  | 属性 | 类型 | PredefinedPccRule |

### |  |  | pccRuleId | * 类型：Value * 值：Rule002 |

### | 5G动作组3 | 基本信息 | 名称 | Rule003 |

### |  |  | 类型 | PredefinedPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：Rule003 |

### 6 配置“规则”

### 导航入口为“策略管理 > 策略 > 规则”。

### 规则的数据规划如表7所示，详细参数说明请参见“规则参数说明”。

### **表7** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | Nchf\_Predefine\_Rule01 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | Nchf\_CG\_norm  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | Rule001  说明：  已在5G动作组中定义。 |

### | 规则2 | 基本信息 | 名称 | Nchf\_Predefine\_Rule02 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | Nchf\_CG\_Lev1  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | Rule002  说明：  已在5G动作组中定义。 |

### | 规则3 | 基本信息 | 名称 | Nchf\_Predefine\_Rule03 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | Nchf\_CG\_Lev2  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | Rule003  说明：  已在5G动作组中定义。 |

### | 规则4 | 基本信息 | 名称 | Nchf\_R\_Exhaust |

### |  |  | 操作类型 | Term IP-CAN Session |

### |  |  | 信令错误码 | 4001-AUTHENTICATION\_REJECTED |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | Nchf\_CG\_Exhaust  说明：  已在条件组中定义。 |

### 7 配置“策略”。

### 导航入口为“策略管理 > 策略 > 策略”。

### 策略的数据规划如表8所示，详细参数说明请参见“策略参数说明”。

### **表8** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略 | 基本信息 | 名称 | Nchf\_Policy |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | IPCAN\_EST |

### |  | 规则 | 名称 | * Nchf\_Predefine\_Rule01 * Nchf\_Predefine\_Rule02 * Nchf\_Predefine\_Rule03 * Nchf\_R\_Exhaust 说明：  已在规则中定义。 |

### 8 配置“业务”。

### 导航入口为“业务管理 > 业务 > 业务”。

### 业务的数据规划如表9所示，详细参数说明请参见“业务参数说明”。

### **表9** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务 | 基本信息 | 名称 | Nchf\_Service |

### |  |  | 类型 | VALUE\_ADDED\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | Nchf\_Policy  说明：  已在策略中定义。 |

### |  | 配额 | 名称 | CHF\_Quota  说明：  已在配额中定义。 |

### 9 登录PGW Web LMT，选择“**UPCF业务管理”**窗口。

### 10 发放业务。

#### 10.1 执行**ADD PSUB**增加一个用户。

#### “USRIDENTIFIER”的参数类型受软参“VRM\_SUBSRCIPTIONIDTYPE（系统支持的用户类型）”控制，默认为“IMSI”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=10.1 -->
```

#### 10.2 执行**ADD PSRV**给用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=10.2 -->
```

#### **脚本**

#### CLI.txt

