---
id: ''
name: PCF侧业务配置
ne_type: UNC
type: feature
description: 该场景根据整体方案设计需配置1个业务，该业务挂载1个策略，该策略包含2个规则：  * 规则1（PrePcc\_Rule1），详细内容规划如下：   + 条件：RoamingRegion等于Region\_Local   + 动作：下发预定义规则名称“Predefined1”（上下行带宽100 Mbit/s） * 规则2（PrePcc\_Rule2），详细内容规划如下：   + 条件：RoamingRegion不等于Region\_Local   + 动作：下发预定义规则名称“Predefined2”（上下行带宽1 Mbit/s）
risk_level: ''
doc_source: ["网络部署","业务专题","5G PCC之SM策略解决方案","典型业务场景E2E方案设计","基于位置区域的带宽差异化控制方案（预定义）","E2E业务配置","PCF侧业务配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该场景根据整体方案设计需配置1个业务，该业务挂载1个策略，该策略包含2个规则：* 规则1（PrePcc\_Rule1），详细内容规划如下：  + 条件：RoamingRegion等于Region\_Local  + 动作：下发预定义规则名称“Predefined1”（上下行带宽100 Mbit/s）* 规则2（PrePcc\_Rule2），详细内容规划如下：  + 条件：RoamingRegion不等于Region\_Local  + 动作：下发预定义规则名称“Predefined2”（上下行带宽1 Mbit/s）

## 必备事项
前提条件

已通过学习SM策略E2E实现原理、业务配置方法及业务调测方法了解了SM策略的配置原理及方法。
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
    - USRIDENTIFIER: 46000120010****
      USRMSISDN: 861390010****
      USRSTATE: Normal
      USRPAIDTYPE: 'NULL'
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: 'NULL'
      USRSUBNETTYPE: eMBB-SA
    add_psrv_list:
    - USRIDENTIFIER: 46000120010****
      SRVNAME: Location_Service
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录**“UPCF Web UI”**界面。

### 2 配置**“PLMN”。**

### 导航入口为“位置管理 > 位置 > PLMN”。

### PLMN的数据规划如表1所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>位置管理>PLMN”帮助页面。

### **表1** PLMN

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | PLMN1 | 基本信息 | PLMN标识 | PLMN\_1 |

### |  |  | 类型 | Local |

### |  |  | MCC | 460 |

### |  |  | MNC | 003 |

### | PLMN2 | 基本信息 | PLMN标识 | PLMN\_2 |

### |  |  | 类型 | Local |

### |  |  | MCC | 460 |

### |  |  | MNC | 002 |

### 此处MCC/MNC取值为样例自行定义，具体取值请根据实际业务场景。

### 3 配置**“漫游区”**。

### 导航入口为“位置管理 > 位置 > 漫游区”。

### 漫游区的数据规划如表2所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>位置管理>漫游区”帮助页面。

### **表2** 漫游区

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 漫游区 | 基本信息 | 漫游区标识 | Region\_Local |

### |  | PLMN1 | PLMN标识 | PLMN\_1 |

### |  | PLMN2 | PLMN标识 | PLMN\_2 |

### 此业务场景下，Region\_Local表示位置区域为国内，除此之外的所有区域都为国外（漫游区）。

### 4 配置**“条件组”**。

### 导航入口为“策略管理 > 策略 > 条件组”。

#### 4.1 当业务的使用需要设置控制条件时，需要配置条件组。若某规则不配置条件组，表示在同一业务里其他条件都匹配不上时，才触发此规则。

#### 4.2 条件组是一个或多个条件的组合。条件组中的各条件之间可以是“与”的关系，也可以是“或”的关系。条件之间的与/或关系由参数“关系”的取值决定。

### 需要配置两个条件组，用于判断用户在国内或国外（漫游区）接入。条件组的数据规划如表3和表4所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>条件组”帮助页面。

### **表3** 条件组1（用户在漫游区内接入）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组1 | 基本信息 | 名称 | CG\_Local |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Con1 |

### |  |  | 对象属性 | * 对象：SmfSession * 属性：RoamingRegion |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Region\_Local |

### **表4** 条件组2（用户在漫游区外接入）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组2 | 基本信息 | 名称 | CG\_Roaming |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Con2 |

### |  |  | 对象属性 | * 对象：SmfSession * 属性：RoamingRegion |

### |  |  | 操作符 | Not Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Region\_Local |

### 5 配置**“5G动作组”**

### 导航入口为“策略管理 > 策略 > 5G动作组”。

#### 5.1 5G场景下预定义规则的下发是通过5G动作组关联预定义规则/预定义规则组名的方式实现的，与4G不同。

#### 5.2 预定义动作的名称需要提前与对端SMF规划一致，具体规则的实现细节详见SMF（UNC）侧配置与UPF（UDG）侧配置。

### 动作组的数据规划如表5和表6所示。

### **表5** 5G动作组1（用户在漫游区内接入）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组1 | 基本信息 | 名称 | AG\_Local |

### |  |  | 类型 | PredefinedPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：Predefined1 说明：  该参数取值须与SMF/UPF协商一致。 |

### 预定义规则"Predefined1"在对端SMF中配置，其内容为设置用户上行带宽为100 Mbit/s，下行带宽为100 Mbit/s。

### **表6** 5G动作组2（用户在漫游区外接入）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组2 | 基本信息 | 名称 | AG\_Roaming |

### |  |  | 类型 | PredefinedPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：Predefined2 说明：  该参数取值须与SMF/UPF协商一致。 |

### 预定义规则"Predefined2"在对端SMF中配置，其内容为设置用户上行带宽为1 Mbit/s，下行带宽为1 Mbit/s。

### 6 配置**“规则”**。

### 导航入口为“策略管理 > 策略 > 规则”。

### 规则的数据规划如表7和表8所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>规则”帮助页面。

### 此场景下规则的配置仅用于关联5G动作和条件组，共配置两个规则，分别对应用户在漫游区接入和在非漫游区接入的场景。

### **表7** 规则1（用户在漫游区内接入）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | PrePCC\_Rule1 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_Local  说明：  已在表3中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_Local  说明：  已在表5中定义。 |

### **表8** 规则2（用户在漫游区外接入）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则2 | 基本信息 | 名称 | PrePCC\_Rule2 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_Roaming  说明：  已在表4中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_Roaming  说明：  已在表6中定义。 |

### 7 配置**“策略”**。

### 导航入口为“策略管理 > 策略 > 策略”。

### 策略的数据规划如表9所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>策略”。

### **表9** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略 | 基本信息 | 名称 | Policy\_Location |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | * IPCAN\_EST * PLMN\_CH |

### |  | 规则 | 名称 | * PrePCC\_Rule1 * PrePCC\_Rule2 说明：  已在表7和表8中定义。 |

### 8 配置**“业务”**

### 导航入口为“业务管理 > 业务 > 业务”。

### 完成业务配置后，可以配置套餐，即对一组业务进行逻辑组合，统一包装。用户可以订购套餐，订购了套餐即把该套餐下的所有业务都订购，套餐的配置步骤请参见“UPCF产品文档>UPCF WebUI GUI参考>业务管理>套餐”。

### 业务的数据规划如表10所示。

### **表10** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务 | 基本信息 | 名称 | Location\_Service |

### |  |  | 类型 | VALUE\_ADDED\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | Policy\_Location  说明：  已在表9中定义。 |

### 9 **开户**。

### **登录“UPCF PGW Web LMT>UPCF 业务管理”窗口**，将配置完成的业务通过UPCF开户签约系统进行下发。

### 执行**ADD PSUB**增加一个用户。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=9 -->
```

### 10 **业务发放**。

### 在“UPCF PGW Web LMT>UPCF 业务管理”窗口继续执行**ADD PSRV**给用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=10 -->
```

