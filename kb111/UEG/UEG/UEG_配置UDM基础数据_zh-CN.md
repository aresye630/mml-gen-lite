---
id: ''
name: 配置UDM基础数据
ne_type: UEG
type: feature
description: 开局时，配置UDM基础数据。  应急UDM从逻辑上划分为FE（Front End）和BE（Back End）两个业务网元：  * FE（Front End）网元也称为UDM网元，实现UDM功能实体的功能，包括协议处理、业务处理以及策略数据管理。 * BE（Back End）网元也称为USCDB网元（Unified Subscriber Center DataBase），实现UDR（Unified Data Repository）功能实体的功能，提供用户数据的增加、删除、更新和查询服务，为FE提供数据存储、数据管理、数据服务等功能支撑。    应急UDM不支持开户，用户数据的增加、删除和更新是通过从中心UDM同步数据文件的方式实现的。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","UEG初始配置（风筝M）","参考：详细配置指导","配置UDM","配置UDM基础数据"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST LOCATION')
- getParameterValue('LST UDMSOFTPARA')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
开局时，配置UDM基础数据。应急UDM从逻辑上划分为FE（Front End）和BE（Back End）两个业务网元：* FE（Front End）网元也称为UDM网元，实现UDM功能实体的功能，包括协议处理、业务处理以及策略数据管理。* BE（Back End）网元也称为USCDB网元（Unified Subscriber Center DataBase），实现UDR（Unified Data Repository）功能实体的功能，提供用户数据的增加、删除、更新和查询服务，为FE提供数据存储、数据管理、数据服务等功能支撑。  应急UDM不支持开户，用户数据的增加、删除和更新是通过从中心UDM同步数据文件的方式实现的。

## 必备事项
前提条件

具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_dbslocation_list:
      type: items
      properties:
        LOCID:
          name: 'Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CNFM:
          name: '是否确认修改'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '取值为YES时，不管当前是否已设置“Location标识”，此次都会强制设置成功。'
          data_source: '本端规划'
          pattern: ''
          default: NO
    add_dbsserviceno_list:
      type: items
      properties:
        SERVICENO:
          name: '服务模块号'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '该服务模块号在系统中唯一。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PODNAME:
          name: 'POD名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '1. 在OM Portal界面选择“应用配置>服务治理”，在“应用名称”选项中选择对应FE网元的名称，搜索“UDRDbbroker”服务。 2. 展开“UDRDbbroker”服务列表，选中“UDRDbbroker”服务实例对应的“属性”列会显示属性信息，属性信息中“podName”对应的值即为POD名称。'
          data_source: '通过OM Portal获取'
          pattern: ''
          default: ''
    add_dbsserviceno_list_2:
      type: items
      properties:
        SERVICENO:
          name: '服务模块号'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '该服务模块号在系统中唯一。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PODNAME:
          name: 'POD名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '1. 在OM Portal界面选择“应用配置>服务治理”，在“应用名称”选项中选择对应FE网元的名称，搜索“UDRDbbroker”服务。 2. 展开“UDRDbbroker”服务列表，选中“UDRDbbroker”服务实例对应的“属性”列会显示属性信息，属性信息中“podName”对应的值即为POD名称。'
          data_source: '通过OM Portal获取'
          pattern: ''
          default: ''
    add_dbsipaddr_list:
      type: items
      properties:
        DBSIPINDEX:
          name: 'Dbbroker IP索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '用于指定业务IP地址对应的索引。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '与USCDB互通的业务IP地址及VPN实例。  VPN名称采用**ADD L3VPNINST**定义的VPN实例名称。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IP1VPNNAME:
          name: 'IP地址1的VPN名称'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: '本地Location IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '本地Location IPV4子网掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        IP2VPNNAME:
          name: 'IP地址2的VPN名称'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4IP2:
          name: '本地Location IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '本地Location IPV4子网掩码2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_vpninfo_list:
      type: items
      properties:
        VPNINFONAME:
          name: 'VPNINFO名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '用于标识对外IP使用的VPN配置的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '用于标识VPNName配置信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNID:
          name: 'VPN ID'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '用于标识VPN ID配置信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ipaddr_list:
      type: items
      properties:
        IPNAME:
          name: 'IP地址名称'
          type: string
          maxLength: 127
          required: true
          description: '存在多条记录时，不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GATEWAYTYPE:
          name: '网关类型'
          type: string
          enum:
          - DSG
          - BSG
          - PAU
          - HSF
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '此处以IPv4地址为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名字'
          type: string
          maxLength: 31
          required: true
          description: '使用表3中的“VPNNAME”。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_httpip_list:
      type: items
      properties:
        IPNAME:
          name: 'IP名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '服务化接口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINFONAME:
          name: 'VPNINFO名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: ''
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_httplserver_list:
      type: items
      properties:
        LSERVERNANE:
          name: '本端服务器名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '用于标识一个本端HTTP服务端的名称。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPNAME:
          name: 'IP名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '用于标识一个微服务对外提供的信令IP地址名称，该参数必须由**ADD HTTPIP**命令配置后才能在此使用。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 1
          maximum: 9999
          required: true
          description: '用于标识一个提供服务的端口。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HTTPSFUNC:
          name: '开启HTTPS'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: '应急AMF、应急SMF与应急UDM均由同一个UEG设备实现，不需要开启HTTPS。'
          data_source: '全网规划'
          pattern: ''
          default: TRUE
    add_httplkspara_list:
      type: items
      properties:
        PARAID:
          name: '链路集参数ID'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '用于标识一个链路集参数的ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LINKNUM:
          name: '链接数目'
          type: integer
          minimum: 0
          maximum: 512
          required: true
          description: '用于标识建立动态链路的最大数目。取值为0（全互联），全互联是指UDM中每个HLB实例都可以处理对端NF发起的HTTP请求链接。'
          data_source: '本端规划'
          pattern: ''
          default: 8
        LNKMOD:
          name: '链路选择模式'
          type: string
          enum:
          - ACTIVEWITHPRI
          - POLLING
          - POLLINGWITHWGT
          required: true
          description: '用于标识待增加的链路集的工作模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_httprsrv_list:
      type: items
      properties:
        RSERVERNAME:
          name: '远端服务器名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '用于标识一个远端HTTP服务端的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LNKTYPE:
          name: '链路类型'
          type: string
          enum:
          - Dynamic
          - Static
          required: true
          description: '用于描述HTTP链路类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LIPNAME:
          name: '本端IP名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '用于标识一个对外提供的信令IP地址名称，该参数必须由**ADD HTTPIP**命令定义后才能在此引用。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PARAID:
          name: '链路集参数ID'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '用于标识一个链路集参数的ID。需要**ADD HTTPLKSPARA**命令定义后才能使用。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    mod_msflowctrl_list:
      type: items
      properties:
        FCTYPE:
          name: '流控类型'
          type: string
          enum:
          - CPUFC
          - ASSUDRFC
          - ASSUDMFC
          - SCHEDULEFC
          required: true
          description: '用于标识流控类型。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        FCMSTYPE:
          name: '微服务类型'
          type: string
          enum:
          - HLB
          - UDM
          - AUSF
          - ENS
          required: true
          description: '用于标识为哪个微服务设置流控参数。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        FCITEM:
          name: '流控资源项'
          type: string
          enum:
          - NODECPU
          - CONTCPU
          - PROCCPU
          - GDRUFCR
          - DRUFCR
          - DSUFCR
          - DSGFCR
          - DBSFCR
          - UDMFCR
          - AUSFFCR
          - LATENCY
          required: true
          description: '用于标识CPU流控资源项。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        FCSTRG:
          name: '起控门限'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: '用于标识虚机CPU的起控阈值，当CPU的使用率超过该阈值时，HLB、UDM或AUSF微服务启动流控功能，控制消息量。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCENDG:
          name: '解控门限'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: '用于标识虚机CPU解控阈值，当CPU的使用率小于该阈值时，HLB、UDM或AUSF微服务解除对应资源项流控。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_dbslocation_list:
    - LOCID: 13
      CNFM: YES
    add_dbsserviceno_list:
    - SERVICENO: 301
      PODNAME: 'dbb-all-pod13-0'
    add_dbsserviceno_list_2:
    - SERVICENO: 301
      PODNAME: 'dbb-all-pod13-0'
    add_dbsipaddr_list:
    - DBSIPINDEX: 1
      IPVER: IPV4
      IP1VPNNAME: 'VRF_DATA'
      IPV4IP1: '10.200.200.22'
      IPV4MASK1: '255.255.255.255'
      IP2VPNNAME: 'VRF_DATA'
      IPV4IP2: '10.200.200.23'
      IPV4MASK2: '255.255.255.255'
    add_vpninfo_list:
    - VPNINFONAME: 'vpn13'
      VPNNAME: 'VRF_SBI'
      VPNID: 1
    add_ipaddr_list:
    - IPNAME: 'HSFIP1'
      GATEWAYTYPE: HSF
      IPTYPE: IPV4
      IPV4IP1: '10.200.200.28'
      VPNNAME: 'VRF_SBI'
    - IPNAME: 'HSFIP1'
      GATEWAYTYPE: HSF
      IPTYPE: IPV4
      IPV4IP1: '10.201.200.28'
      VPNNAME: 'VRF_SBI'
    add_httpip_list:
    - IPNAME: 'HLB13'
      IPVER: IPV4
      IPV4IP1: '10.200.200.27'
      VPNINFONAME: 'vpn13'
    add_httplserver_list:
    - LSERVERNANE: 'HLB'
      IPNAME: 'HLB13'
      PORT: 8080
      HTTPSFUNC: FALSE
    add_httplkspara_list:
    - PARAID: 1
      LINKNUM: 8
      LNKMOD: POLLING
    add_httprsrv_list:
    - RSERVERNAME: 'abc'
      LNKTYPE: Dynamic
      LIPNAME: 'HLB13'
      PARAID: 1
    mod_msflowctrl_list:
    - FCTYPE: CPUFC
      FCMSTYPE: HLB
      FCITEM: NODECPU
      FCSTRG: 85
      FCENDG: 75
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 设置Location信息。

#### 2.1 检查Location标识是否与规划一致。

#### 执行**LST LOCATION**命令，检查“LOCID”参数值是否与规划一致。

#### 主用局UDM/HSS、主用局USCDB、容灾局UDM/HSS、容灾局USCDB的Location标识各不相同。

#### 一致，请执行2.b。

#### 不一致，请联系华为技术支持工程师处理。

#### RETCODE = 0  操作成功

#### 操作结果如下

#### ------------

#### Location标识  =  13

#### 网元类型  =  HSS9860

#### (结果个数 = 1)

#### ---    END

#### 2.2 设置DBS Location标识。

```jinja2
{%- set LST_LOCATION=getParameterValue('LST LOCATION') -%}
{%- if LST_LOCATION=='13' -%}
    {%- for item in set_dbslocation_list -%}
        SET DBSLOCATION:
        {#- --- 必选参数 --- -#}
        LOCID={{item.LOCID}},
        {#- --- 可选参数 --- -#}
        {%- if item.CNFM is not none -%}
            CNFM={{item.CNFM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 设置本端服务ID。

### 参数“PODNAME”，通过以下操作获取：

#### 3.1 在OM Portal界面选择“应用配置>服务治理”，在“应用名称”选项中选择对应FE网元的名称，搜索“UDRDbbroker”服务。

#### 3.2 展开“UDRDbbroker”服务列表，选中“UDRDbbroker”服务实例对应的“属性”列会显示属性信息，属性信息中“podName”对应的值即为POD名称。

#### 3.3 //虚机容器：

```jinja2
{%- if is_scenario_vm_container -%}
    {%- for item in add_dbsserviceno_list -%}
        ADD DBSSERVICENO:
        {#- --- 必选参数 --- -#}
        SERVICENO={{item.SERVICENO}},
        PODNAME="{{item.PODNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 //裸机容器：

```jinja2
{%- if is_scenario_bare_metal_container -%}
    {%- for item in add_dbsserviceno_list_2 -%}
        ADD DBSSERVICENO:
        {#- --- 必选参数 --- -#}
        SERVICENO={{item.SERVICENO}},
        PODNAME="{{item.PODNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 增加业务IP地址，用于和BE进行通信。

```jinja2
{%- for item in add_dbsipaddr_list -%}
    ADD DBSIPADDR:
    {#- --- 必选参数 --- -#}
    DBSIPINDEX={{item.DBSIPINDEX}},
    IPVER={{item.IPVER}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4/IPV6 时必选 --- -#}
    {%- if item.IPVER in ['IPV4', 'IPV6'] -%}
        IP1VPNNAME="{{item.IP1VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4MASK1 is not none -%}
            IPV4MASK1="{{item.IPV4MASK1}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVER=IPV4/IPV6 时可选 --- -#}
    {%- if item.IPVER in ['IPV4', 'IPV6'] -%}
        {%- if item.IP2VPNNAME is not none -%}
            IP2VPNNAME="{{item.IP2VPNNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4IP2 is not none -%}
            IPV4IP2="{{item.IPV4IP2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4MASK2 is not none -%}
            IPV4MASK2="{{item.IPV4MASK2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 增加VPN信息配置。

```jinja2
{%- for item in add_vpninfo_list -%}
    ADD VPNINFO:
    {#- --- 必选参数 --- -#}
    VPNINFONAME="{{item.VPNINFONAME}}",
    VPNNAME="{{item.VPNNAME}}",
    VPNID={{item.VPNID}},
    ;
{%- endfor -%}
```

### 6 增加HSF类型的IP地址。必须执行本步骤，否则**DSP ESN**无法获取到UEG的ESN。

#### 6.1 //DC1：

```jinja2
{%- for item in add_ipaddr_list -%}
    ADD IPADDR:
    {#- --- 必选参数 --- -#}
    IPNAME="{{item.IPNAME}}",
    GATEWAYTYPE={{item.GATEWAYTYPE}},
    IPTYPE={{item.IPTYPE}},
    VPNNAME="{{item.VPNNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- elif item.IPTYPE == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- elif item.IPTYPE == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- elif item.IPTYPE == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 增加HTTP IP地址。

```jinja2
{%- for item in add_httpip_list -%}
    ADD HTTPIP:
    {#- --- 必选参数 --- -#}
    IPNAME="{{item.IPNAME}}",
    IPVER={{item.IPVER}},
    VPNINFONAME="{{item.VPNINFONAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 增加本端服务器配置。

```jinja2
{%- for item in add_httplserver_list -%}
    ADD HTTPLSERVER:
    {#- --- 必选参数 --- -#}
    LSERVERNANE="{{item.LSERVERNANE}}",
    IPNAME="{{item.IPNAME}}",
    PORT={{item.PORT}},
    HTTPSFUNC={{item.HTTPSFUNC}},
    ;
{%- endfor -%}
```

### 9 查询HttpLink的取值。

### 查看HttpLink的取值为1还是0：

### HttpLink取值为0=>结束。

### HttpLink取值为1=>10。

### 10 增加链路集参数配置。

```jinja2
{%- set LST_UDMSOFTPARA=getParameterValue('LST UDMSOFTPARA') -%}
{%- if LST_UDMSOFTPARA=='1' -%}
    {%- for item in add_httplkspara_list -%}
        ADD HTTPLKSPARA:
        {#- --- 必选参数 --- -#}
        PARAID={{item.PARAID}},
        LINKNUM={{item.LINKNUM}},
        LNKMOD={{item.LNKMOD}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 11 增加远端服务器配置。

```jinja2
{%- for item in add_httprsrv_list -%}
    ADD HTTPRSRV:
    {#- --- 必选参数 --- -#}
    RSERVERNAME="{{item.RSERVERNAME}}",
    LNKTYPE={{item.LNKTYPE}},
    LIPNAME="{{item.LIPNAME}}",
    PARAID={{item.PARAID}},
    ;
{%- endfor -%}
```

### 12 修改虚机CPU的流控门限。默认“FCSTRG”值为“80”，“FCENDG”值为“70”，请根据局点规划值修改。

```jinja2
{%- for item in mod_msflowctrl_list -%}
    MOD MSFLOWCTRL:
    {#- --- 必选参数 --- -#}
    FCTYPE={{item.FCTYPE}},
    FCMSTYPE={{item.FCMSTYPE}},
    FCITEM={{item.FCITEM}},
    {#- --- 可选参数 --- -#}
    {%- if item.FCSTRG is not none -%}
        FCSTRG={{item.FCSTRG}},
    {%- endif -%}
    {%- if item.FCENDG is not none -%}
        FCENDG={{item.FCENDG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

