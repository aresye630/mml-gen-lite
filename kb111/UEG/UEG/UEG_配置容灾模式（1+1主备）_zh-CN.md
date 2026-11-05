---
id: ''
name: 配置容灾模式（1+1主备）
ne_type: UEG
type: feature
description: 为避免单点故障，园区需部署两套UEG实现容灾。  两套UEG采用1+1主备容灾时，需要参考本页面进行配置。  本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","配置实例（虚机容器）","配置容灾模式","配置容灾模式（1+1主备）"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","配置实例（裸机容器）","配置容灾模式","配置容灾模式（1+1主备）"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST DRCOUPLINGRESET')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为避免单点故障，园区需部署两套UEG实现容灾。两套UEG采用1+1主备容灾时，需要参考本页面进行配置。本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。

## 必备事项
前提条件

前提条件

* 已完成各NF选择本UEG内NF的数据配置。
* 已完成UEG间容灾消息传输使用的外联口IP及路由数据。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_drcouplingreset_list:
      type: items
      properties:
        COUPLINGRESET:
          name: '是否使能负荷分担容灾功能'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_drgroupinfo_list:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '两套UEG采用主备容灾时，容灾组标识+容灾组名称取值必须一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DRGROUPNAME:
          name: '容灾组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LDRINSTID:
          name: '本端容灾实例标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '两套UEG上该参数必须不同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFTMODE:
          name: '本端默认运行模式'
          type: string
          enum:
          - ACTIVE
          - STANDBY
          required: true
          description: '主用UEG上设置为ACTIVE，备用UEG上设置为STANDBY。  AMF/MME的capacity设置为255为主用UEG，AMF/MME的capacity设置为0为备用UEG。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDRINSTID:
          name: '对端容灾实例标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '对端UEG上的容灾实例标识。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
    add_drdci_list:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '引用**ADD DRGROUPINFO**定义的容灾组标识。可通过**LST DRGROUPINFO**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本号'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '两套UEG上，该参数取值必须一致。  DC间通信通道采用IPv4时需要规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LDCIP:
          name: '本端DC通信IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDCIP:
          name: '对端DC通信IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '引用**ADD VPNINST**定义的VPN实例名称。可通过**LST VPNINST**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DATABKMODE:
          name: '数据备份模式'
          type: string
          enum:
          - Active-Standby
          - Active-Standby_Hot_Backup
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: Active-Standby
        LDCIPV6:
          name: '本端DC通信IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDCIPV6:
          name: '对端DC通信IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_drhbnegotimer_list:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '引用**ADD DRGROUPINFO**定义的容灾组标识。可通过**LST DRGROUPINFO**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HELLOINTERVAL:
          name: '心跳消息传递间隔(100毫秒)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '心跳消息达到“重传次数（TIMES）”参数值后，仍未收到响应消息时，则认为DCI通道故障。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEGOINTERVAL:
          name: '协商消息传递间隔(100毫秒)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '协商消息达到“重传次数（TIMES）”参数值后，仍未收到响应消息时，则认为容灾组协商失败。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        TIMES:
          name: '重传次数'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: 'UEG间发送心跳和协商消息的最大重传次数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_drkeynf_list:
      type: items
      properties:
        MME:
          name: '是否监控MME服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '需要根据规划，监控UEG上部署的服务。  此处以UEG监控MME、AMF、HSS、UDM、SMF、GWC、UPF、UDR，未监控PCF/PCRF为例。'
          data_source: '本端规划'
          pattern: ''
          default: NO
        AMF:
          name: '是否监控AMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        HSS:
          name: '是否监控HSS服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        UDM:
          name: '是否监控UDM服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        SMF:
          name: '是否监控SMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        GWC:
          name: '是否监控GW-C服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        PCF:
          name: '是否监控PCF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        PCRF:
          name: '是否监控PCRF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        UPF:
          name: '是否监控UPF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        UDR:
          name: '是否监控UDR服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
    set_amfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '使能AMF服务主备容灾功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWORD索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_softparaofbit_list:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: '使能MME服务主备容灾功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '软参值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_upsoftpara_list:
      type: items
      properties:
        DT:
          name: '软参记录数据类型'
          type: string
          enum:
          - BIT
          - BYTE
          - DWORD
          - STRING
          required: true
          description: '使能UPF服务主备容灾功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_drcouplingreset_list:
    - COUPLINGRESET: NO
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_DCI'
    add_drgroupinfo_list:
    - DRGROUPID: 1
      DRGROUPNAME: 'DRGROUP01'
      LDRINSTID: 0
      DFTMODE: ACTIVE
      PDRINSTID: 1
    - DRGROUPID: 1
      DRGROUPNAME: 'DRGROUP01'
      LDRINSTID: 1
      DFTMODE: STANDBY
      PDRINSTID: 0
    add_drdci_list:
    - DRGROUPID: 1
      IPVERSION: IPV4
      LDCIP: '10.10.198.8'
      PDCIP: '10.10.199.8'
      VPNINSTANCE: 'VPN_DCI'
      DATABKMODE: Active-Standby
      LDCIPV6: 'FC00::10:10:198:8'
      PDCIPV6: 'FC00::10:10:199:8'
    - DRGROUPID: 1
      IPVERSION: IPV4
      LDCIP: '10.10.199.8'
      PDCIP: '10.10.198.8'
      VPNINSTANCE: 'VPN_DCI'
      DATABKMODE: Active-Standby
      LDCIPV6: 'FC00::10:10:199:8'
      PDCIPV6: 'FC00::10:10:198:8'
    set_drhbnegotimer_list:
    - DRGROUPID: 1
      HELLOINTERVAL: 10
      NEGOINTERVAL: 10
      TIMES: 30
    - DRGROUPID: 1
      HELLOINTERVAL: 10
      NEGOINTERVAL: 10
      TIMES: 30
    set_drkeynf_list:
    - MME: YES
      AMF: YES
      HSS: YES
      UDM: YES
      SMF: YES
      GWC: YES
      PCF: NO
      PCRF: NO
      UPF: YES
      UDR: YES
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 400
      VALUE: VALUE_1
      POSITION: 1
    set_softparaofbit_list:
    - DT: DWORD_EX_B
      PARANUM: 61
      VALUE: VALUE_1
      POSITION: 1
    set_upsoftpara_list:
    - DT: BIT
      BITNUM: 3001
      BITVALUE: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 检查负荷分担容灾功能的使能开关是否为“NO”。

### “COUPLINGRESET”值为“YES”时，请执行3。

### “COUPLINGRESET”值为“NO”时，执行4。

### 3 关闭负荷分担容灾功能开关。

```jinja2
{%- set LST_DRCOUPLINGRESET=getParameterValue('LST DRCOUPLINGRESET') -%}
{%- if LST_DRCOUPLINGRESET=='YES' -%}
    {%- for item in set_drcouplingreset_list -%}
        SET DRCOUPLINGRESET:
        {#- --- 可选参数 --- -#}
        {%- if item.COUPLINGRESET is not none -%}
            COUPLINGRESET={{item.COUPLINGRESET}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 增加VPN实例。

```jinja2
{%- if LST_DRCOUPLINGRESET=='NO' -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 增加容灾组信息。

#### 5.1 //DC1：

```jinja2
{%- for item in add_drgroupinfo_list -%}
    ADD DRGROUPINFO:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    DRGROUPNAME="{{item.DRGROUPNAME}}",
    LDRINSTID={{item.LDRINSTID}},
    DFTMODE={{item.DFTMODE}},
    PDRINSTID={{item.PDRINSTID}},
    ;
{%- endfor -%}
```

### 6 增加DC间通信通道信息。

#### 6.1 //DC1：

```jinja2
{%- for item in add_drdci_list -%}
    ADD DRDCI:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    IPVERSION={{item.IPVERSION}},
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DATABKMODE is not none -%}
        DATABKMODE={{item.DATABKMODE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        LDCIP="{{item.LDCIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        PDCIP="{{item.PDCIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        PDCIPV6="{{item.PDCIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        LDCIPV6="{{item.LDCIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 设置容灾定时器。

#### 7.1 //DC1：

```jinja2
{%- for item in set_drhbnegotimer_list -%}
    SET DRHBNEGOTIMER:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.HELLOINTERVAL is not none -%}
        HELLOINTERVAL={{item.HELLOINTERVAL}},
    {%- endif -%}
    {%- if item.NEGOINTERVAL is not none -%}
        NEGOINTERVAL={{item.NEGOINTERVAL}},
    {%- endif -%}
    {%- if item.TIMES is not none -%}
        TIMES={{item.TIMES}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 设置监控的关键部件信息。

### 此处以UEG监控MME、AMF、HSS、UDM、SMF、GWC、UPF、UDR，未监控PCF/PCRF为例。实际请以网设规划为准。

### 开启容灾功能的UEG出现设备异常，需要通过重新实例化操作进行恢复的场景：若MML文件中**SET DRKEYNF**命令的HSS、UDM、PCRF、PCF、UDR参数值存在“YES”，则在导入MML文件进行配置恢复前，需要先修改MML文件，将**SET DRKEYNF**命令的HSS、UDM、PCRF、PCF、UDR参数值“YES”修改为“NO”；待HSS、UDM、PCRF、PCF、UDR服务的配置恢复完成后，再按照修改前的**SET DRKEYNF**配置重新开启对这些服务的监控。

```jinja2
{%- for item in set_drkeynf_list -%}
    SET DRKEYNF:
    {#- --- 可选参数 --- -#}
    {%- if item.MME is not none -%}
        MME={{item.MME}},
    {%- endif -%}
    {%- if item.AMF is not none -%}
        AMF={{item.AMF}},
    {%- endif -%}
    {%- if item.HSS is not none -%}
        HSS={{item.HSS}},
    {%- endif -%}
    {%- if item.UDM is not none -%}
        UDM={{item.UDM}},
    {%- endif -%}
    {%- if item.SMF is not none -%}
        SMF={{item.SMF}},
    {%- endif -%}
    {%- if item.GWC is not none -%}
        GWC={{item.GWC}},
    {%- endif -%}
    {%- if item.PCF is not none -%}
        PCF={{item.PCF}},
    {%- endif -%}
    {%- if item.PCRF is not none -%}
        PCRF={{item.PCRF}},
    {%- endif -%}
    {%- if item.UPF is not none -%}
        UPF={{item.UPF}},
    {%- endif -%}
    {%- if item.UDR is not none -%}
        UDR={{item.UDR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 设置软参。

```jinja2
{%- for item in set_amfsoftparaofbit_list -%}
    SET AMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_softparaofbit_list -%}
    SET SOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    PARANUM={{item.PARANUM}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_upsoftpara_list -%}
    SET UPSOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

