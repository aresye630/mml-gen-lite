---
id: ''
name: 套餐配置
ne_type: UNC
type: feature
description: 基于已完成配置的业务1与业务2，进行“套餐”配置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G PCC之SM策略解决方案","典型业务场景E2E方案设计","基于多业务场景的策略控制（动态）","E2E业务配置","套餐配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
基于已完成配置的业务1与业务2，进行“套餐”配置。

## 必备事项
前提条件

* 完成业务1配置与业务2配置。
* 已通过学习SM策略E2E实现原理、业务配置方法及业务调测方法了解了SM策略的配置原理及方法。
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
    add_psrvpkg_list:
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
        SRVPKGROAMINGTYPE:
          name: 'SRVPKGROAMINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVPKGCONTACTMETHOD:
          name: 'SRVPKGCONTACTMETHOD'
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
    add_psrvpkg_list:
    - USRIDENTIFIER: 46000120010****
      SRVNAME: Flow_Package
      SRVPKGROAMINGTYPE: 'NULL'
      SRVPKGCONTACTMETHOD: None
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录**“UPCF Web UI”**界面。

### 2 配置“互斥组”。

### 导航入口为“业务管理 > 业务 > 互斥组”。

### 根据单业务1与单业务2之间的逻辑关系判断，两个业务的互斥关系为激活+替换，配额的数据规划如表1所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>业务管理>互斥组”帮助页面。

### 新增加的互斥组，仅对后续签约生效，对已签约业务不生效。即增加互斥组时，若两个或多个业务已经被同一用户订购，则互斥组不生效。

### 互斥组的“名称”、“类型”、“互斥操作”、“累积属性”配置后不允许修改，可为互斥组增加或删除相应的业务，其他参数可修改，参数修改后立即生效。

### 业务关联到激活互斥组中，如果业务已经激活，那么只能被更高优先级的新业务互斥去激活，不能被已激活的业务互斥去激活。

### **表1** 互斥组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 互斥组 | 基本信息 | 名称 | Mutex\_FUP\_Holiday |

### |  |  | 类型 | 激活 |

### |  |  | 互斥操作 | 替换 |

### |  | 业务 | 名称 | * Service\_FUP * Service\_Holiday 说明：  已在表18和表16中定义。 |

### 3 配置“套餐”。

### 导航入口为“业务管理 > 套餐”。

### 配额的数据规划如表2所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>业务管理>套餐”帮助页面。

### **表2** 套餐

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 套餐 | 基本信息 | 名称 | Flow\_Package |

### |  | 业务 | 名称 | * Service\_FUP * Service\_Holiday 说明：  已在表18和表16中定义。 |

### 4 “开户”。

### 登录**“UPCF PGW Web LMT>UPCF 业务管理”**窗口，将配置完成的业务通过UPCF开户签约系统进行下发。

### 执行**ADD PSUB**增加一个用户。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=4 -->
```

### 5 “套餐发放”。

### 在“UPCF PGW Web LMT>UPCF 业务管理”窗口继续执行**ADD PSRVPKG**给用户签约套餐。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrvpkg_list的变量区（command: ADD PSRVPKG） -#}
<!-- MISSING_MACRO: command=ADD PSRVPKG list_name=add_psrvpkg_list step_id=5 -->
```

