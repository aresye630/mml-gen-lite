---
id: ''
name: 配置高危命令二次授权
ne_type: UNC
type: feature
description: 为了避免操作员一个人执行高危命令时，由于个人疏忽、误操作产生严重事故，系统提供了对高危命令的二次授权能力，即操作员执行被二次授权的高危命令时必须经过二次授权用户的授权确认，保证操作安全。  在开局或日常维护过程中，系统默认关闭高危命令二次授权功能，建议用户对高危命令开通二次授权功能，并配置二次授权用户和二次授权命令。被添加到二次授权命令列表中的命令，在执行时均需经过二次授权用户的授权确认。  高危命令二次授权功能同时支持在网元OM Portal或者网管进行配置操作，本章节主要以OM Portal操作为例介绍。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","配置高危命令二次授权"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为了避免操作员一个人执行高危命令时，由于个人疏忽、误操作产生严重事故，系统提供了对高危命令的二次授权能力，即操作员执行被二次授权的高危命令时必须经过二次授权用户的授权确认，保证操作安全。在开局或日常维护过程中，系统默认关闭高危命令二次授权功能，建议用户对高危命令开通二次授权功能，并配置二次授权用户和二次授权命令。被添加到二次授权命令列表中的命令，在执行时均需经过二次授权用户的授权确认。高危命令二次授权功能同时支持在网元OM Portal或者网管进行配置操作，本章节主要以OM Portal操作为例介绍。

## 必备事项
前提条件

在普通域，使用admin用户登录OM Portal。

在扩展域，使用系统管理员权限用户登录OM Portal。如果登录OM Portal用户无系统管理员权限，请在OM Portal的“安全 > 用户管理 > 角色”为用户添加系统管理员权限。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_secauth_list:
      type: items
      properties:
        STATUS:
          name: '二次授权状态'
          type: string
          enum:
          - OFF
          - ON
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMESWITCH:
          name: '是否打开免二次授权时间段'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_usrsecauth_list:
      type: items
      properties:
        USRNAME:
          name: '用户名称'
          type: string
          maxLength: 100
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_secauthmem_list:
      type: items
      properties:
        MEID:
          name: '网元ID'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        COMMAND:
          name: '命令名称'
          type: string
          maxLength: 80
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_secauth_list:
    - STATUS: ON
      TIMESWITCH: NO
    add_usrsecauth_list:
    - USRNAME: 'User01'
    add_secauthmem_list:
    - MEID: 0
      COMMAND: 'LST ME'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 选择“应用管理 > MML”，选择需要执行MML的应用窗口。

### 2 执行**SET SECAUTH**命令开启二次授权功能开关。

```jinja2
{%- for item in set_secauth_list -%}
    SET SECAUTH:
    {#- --- 必选参数 --- -#}
    STATUS={{item.STATUS}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：STATUS=ON 时可选 --- -#}
    {%- if item.STATUS == 'ON' -%}
        {%- if item.TIMESWITCH is not none -%}
            TIMESWITCH={{item.TIMESWITCH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 执行**ADD USRSECAUTH**命令增加二次授权用户，该用户需已在OM Portal的“安全 > 用户管理”创建。

```jinja2
{%- for item in add_usrsecauth_list -%}
    ADD USRSECAUTH:
    {#- --- 必选参数 --- -#}
    USRNAME="{{item.USRNAME}}",
    ;
{%- endfor -%}
```

### 4 当用户需要增加二次授权命令时执行，执行**ADD SECAUTHMEM**命令。

```jinja2
{%- for item in add_secauthmem_list -%}
    ADD SECAUTHMEM:
    {#- --- 必选参数 --- -#}
    MEID={{item.MEID}},
    COMMAND="{{item.COMMAND}}",
    ;
{%- endfor -%}
```

### 5 在“应用管理 > MML”，执行已添加需二次授权的命令**LST ME**。

### 6 MML操作界面弹出二次授权命令提示，参考图1输入操作步骤3中已配置的二次授权用户名和密码，单击“确定”。

### **图1** 二次授权弹窗

### 7 MML操作界面向操作员返回MML执行结果。

### 8 为保证操作安全，系统提供了二次授权命令的管理功能。凡是在二次授权命令列表中的命令，在执行时均需要经过二次授权确认。同时，系统将一部分高危命令作为默认的二次授权命令，且系统默认的二次授权命令不允许删除。

### 9 **表1** UNC默认的二次授权命令

### 10 | 网元类型 | MML名称 | 说明 |

### | --- | --- | --- |

### | UNC | **MOD VIRTUALIP** | 用于修改登录OM Portal的浮动IP地址。  执行该命令可能会导致通信中断，需要进行二次授权。 |

### | UNC | **SET OMIP** | 用于修改系统OM网络配置参数。  执行该命令可能会导致通信中断，需要进行二次授权。 |

### | UNC | **SET BYPASSSWITCH** | 用于设置存储故障时，节点是否自动进入BYPASS状态。  执行该命令可能会导致系统无法自动进入Bypass，需要进行二次授权。 |

### | UNC | **RST NODEBATCH** | 用于复位指定网元ID下的所有节点。  节点批量复位，模块数据将会丢失，导致业务受到影响，并可能会引起系统中文件损坏。在存储故障期间，执行该命令批量复位节点后，这些节点以及节点中的容器和进程在存储恢复前都无法启动，需要进行二次授权。 |

### | UNC | **MOD NETWORK** | 该命令仅适用于部分场景，具体请参考命令帮助。  用于修改系统OM网络的网卡VLANID。  执行该命令可能会导致通信中断，需要进行二次授权。 |

### | UNC | **MOD OMNWCONF** | 用于配置OM网络故障探测参数。  该命令仅限角色为Administrators的用户执行。  执行该命令可能会导致通信中断，需要进行二次授权。 |

### | UNC | **RMV HPATCH** | 该命令用于删除指定网元微服务进程的热补丁。  执行该命令操作不当会影响系统的正常运行，需要进行二次授权。 |

### | UNC | **RST MESYS** | 该命令用于对网元下的Pod进行重建。  执行该命令会导致Pod复位期间部分服务可能不可用，需要进行二次授权。 |

### | UNC | **SET CNTTMPDIR** | 该命令用于设置容器引擎临时目录。  执行该命令会复位容器引擎，可能导致业务受损，需要进行二次授权。 |

### | UNC | **SET OMSWITCH** | 用于设置OM功能开关的开关状态。  执行该命令可能会导致通信中断，需要进行二次授权。 |

### | UNC | **SET CLTVFYSWITCH** | 用于修改双向认证开关。  执行该命令可能会导致通信中断，需要进行二次授权。 |

### | UNC | **RMV ACLGROUP6IPSEC** | 从20.6.2或20.7.1版本升级到20.8.2及后续版本时，执行这些命令需要进行二次授权。  20.8.2及后续版本新建部署或新建部署后升级到更高版本时，执行这些命令不需要进行二次授权。 |

### |  | **RMV ACLGROUP4IPSEC** |  |

### |  | **RMV ACLRULEADV4IPSEC5G** |  |

### |  | **RMV ACLRULEADV6IPSEC** |  |

### |  | **RMV PROPATTACHIPSECPROPOSAL5G** |  |

### |  | **ADD IKEPROPOSAL5G** |  |

### |  | **MOD IKEPROPOSAL5G** |  |

### |  | **RMV IKEPROPOSAL5G** |  |

### |  | **RMV IPSECINTFCFGIPSEC5G** |  |

### |  | **ADD IPSECPOLICY4** |  |

### |  | **MOD IPSECPOLICY4** |  |

### |  | **RMV IPSECPOLICY4** |  |

### |  | **ADD IPSECPOLICY6** |  |

### |  | **MOD IPSECPOLICY6** |  |

### |  | **RMV IPSECPOLICY6** |  |

### |  | **ADD IPSECPROPOSALIPSEC5G** |  |

### |  | **MOD IPSECPROPOSALIPSEC5G** |  |

### |  | **RMV IPSECPROPOSALIPSEC5G** |  |

### |  | **ADD IPBINDVPNIPSEC5G** |  |

### |  | **MOD IPBINDVPNIPSEC5G** |  |

### |  | **RMV IPBINDVPNIPSEC5G** |  |

### |  | **RMV L3VPNINSTIPSEC5G** |  |

### |  | **RMV VPNINSTAFIPSEC5G** |  |

