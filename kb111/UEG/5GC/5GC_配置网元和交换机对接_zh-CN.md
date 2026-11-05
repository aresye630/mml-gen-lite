---
id: ''
name: 配置网元和交换机对接
ne_type: UEG
type: feature
description: CSP对接交换机，运营商可以通过CSP纳管指定的华为交换机并支持告警上报功能。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","软件安装与初始配置","部署UEG","电力专网采用风筝S部署模式","UEG初始配置","裸机容器模式UPF初始配置","参考：详细配置指导","基础数据配置","配置网元和交换机对接"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-S","子园区UEG-S初始配置","裸机容器模式UPF初始配置","参考：详细配置指导","基础数据配置","配置网元和交换机对接"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
CSP对接交换机，运营商可以通过CSP纳管指定的华为交换机并支持告警上报功能。

## 必备事项
前提条件

* 已登录网元OM Portal。
* 交换机运行正常。
* 交换机和CSP之间网络正常。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_lsw_list:
      type: items
      properties:
        LSNAME:
          name: '以太网交换机名称'
          type: string
          maxLength: 64
          required: true
          description: '用于网元配置对接交换机设备。  说明：  * 仅支持通过SNMPv3协议与交换机对接。 * 多个交换机如果配置同样的SNMP用户名，其他密码和协议信息也必须一致。 * “SNMP用户名”、“认证密码”和“加密密码”需要从交换机对端获取，CSP仅作为客户端存储使用。'
          data_source: '全网规划。'
          pattern: ''
          default: ''
        IPTYPE:
          name: '以太网交换机IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        LSIP:
          name: '以太网交换机IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USER:
          name: 'SNMP用户名'
          type: string
          minLength: 6
          maxLength: 20
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '以太网交换机端口'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTVER:
          name: '协议版本'
          type: string
          enum:
          - SNMPv3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: SNMPv3
        AUTHPROT:
          name: '认证协议'
          type: string
          enum:
          - SHA256
          - SHA384
          - SHA512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: SHA512
        AUTHKEY:
          name: '认证密码'
          type: string
          minLength: 10
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRVPROT:
          name: '加密协议'
          type: string
          enum:
          - AES256
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: AES256
        PRVKEY:
          name: '加密密码'
          type: string
          minLength: 10
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_lsw_list:
    - LSNAME: 'LSW1'
      IPTYPE: IPV4
      LSIP: '10.0.0.0'
      USER: 'AdminUser'
      PORT: 161
      PROTVER: SNMPv3
      AUTHPROT: SHA512
      AUTHKEY: '*****'
      PRVPROT: AES256
      PRVKEY: '*****'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录网元OM Portal，选择“应用管理 > MML”。

### 2 请参见交换机产品文档，配置CSP和交换机对接。

### 在华为技术支持网站，下载交换机产品文档。支持的产品型号及版本号请参见表1。

### **表1** 网元支持纳管的产品

### | 产品名称 | 版本号 |

### | --- | --- |

### | CE6865E | V2R22C00及以上版本。 |

### | NetEngine 8000 F1A | V800R021C00及以上版本。 |

### | FM6865-SI | V2R22C00&最新补丁版本。 |

### | CE6885-48YS8CQ | V2R22C00及以上版本。 |

### | CE8865-4C | V2R22C00及以上版本。 |

### | CE6863H | V2R22C00及以上版本。 |

### 3 执行**ADD LSW**添加交换机，命令执行示例如下。

```jinja2
{%- for item in add_lsw_list -%}
    ADD LSW:
    {#- --- 必选参数 --- -#}
    LSNAME="{{item.LSNAME}}",
    IPTYPE={{item.IPTYPE}},
    USER="{{item.USER}}",
    PORT={{item.PORT}},
    PROTVER={{item.PROTVER}},
    AUTHPROT={{item.AUTHPROT}},
    AUTHKEY="{{item.AUTHKEY}}",
    PRVPROT={{item.PRVPROT}},
    PRVKEY="{{item.PRVKEY}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        LSIP="{{item.LSIP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### RETCODE = 0  操作成功

### ---    END

