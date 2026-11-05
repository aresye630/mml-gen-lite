---
id: ''
name: 卸载IPAPM服务
ne_type: UDG
type: feature
description: 当运营商不需要IPAPM服务或IPAPM服务动态上线失败时，可以单独卸载IPAPM pod，从而下线IPAPM服务。
risk_level: ''
doc_source: ["网络部署","软件安装","基于VNF LCM安装UDG（非SDN）","卸载UDG","卸载IPAPM服务"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST TWAMPSENDER')
- getParameterValue('LST TWAMPCLIENT')
- getParameterValue('LST TWAMPRESPONDER')
- getParameterValue('LST TWAMPLOGICINF')
- getParameterValue('LST TWAMPVPNINST')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商不需要IPAPM服务或IPAPM服务动态上线失败时，可以单独卸载IPAPM pod，从而下线IPAPM服务。

## 必备事项
前提条件

已经完成网络设计，已规划下线IPAPM pod的类型和数量。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    rmv_twampsender_list:
      type: items
      properties:
        CLIENTID:
          name: '客户端ID'
          type: integer
          minimum: 1
          maximum: 12000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_twampclient_list:
      type: items
      properties:
        CLIENTID:
          name: '客户端ID'
          type: integer
          minimum: 1
          maximum: 12000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_twampresponder_list:
      type: items
      properties:
        RESPONDERID:
          name: '响应端索引'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_twamplogicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_twampvpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    opr_featuredisable_list:
      type: items
      properties:
        PODTYPE:
          name: 'Pod类型列表'
          type: string
          minLength: 0
          maxLength: 1024
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        DISABLETYPE:
          name: '下线方式'
          type: string
          enum:
          - Normal
          - Force
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Normal
        FUNCTIONSETNAME:
          name: '网络功能集名称'
          type: string
          minLength: 0
          maxLength: 1024
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    rmv_twampsender_list:
    - CLIENTID: 客户端ID
    rmv_twampclient_list:
    - CLIENTID: 客户端ID
    rmv_twampresponder_list:
    - RESPONDERID: 客户端ID
    rmv_twamplogicinf_list:
    - NAME: '逻辑接口名称'
    rmv_twampvpninst_list:
    - VRFNAME: 'VPN实例名称'
    opr_featuredisable_list:
    - PODTYPE: 'ipapmctrl-pod/ipapmexec-pod'
      DISABLETYPE: Normal
      FUNCTIONSETNAME: 'IPAPM'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录UDG OM Portal。

### 2 执行命令，删除配置数据。

### 在动态下线IPAPM服务前，需要将安装过程中产生的配置数据（实例）进行清除，再执行动态下线命令。清除配置数据需要先查询是否存在实例，如已存在实例，需要进行实例删除。请按如下顺序进行数据清除：

#### 2.1 执行命令，查询发送端实例。

#### 2.2 执行命令，删除发送端实例。

```jinja2
{%- set LST_TWAMPSENDER=getParameterValue('LST TWAMPSENDER') -%}
{%- if LST_TWAMPSENDER -%}
    {%- for item in rmv_twampsender_list -%}
        RMV TWAMPSENDER:
        {#- --- 必选参数 --- -#}
        CLIENTID={{item.CLIENTID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 执行命令，查询客户端实例。

#### 2.4 执行命令，删除客户端实例。

```jinja2
{%- set LST_TWAMPCLIENT=getParameterValue('LST TWAMPCLIENT') -%}
{%- if LST_TWAMPCLIENT -%}
    {%- for item in rmv_twampclient_list -%}
        RMV TWAMPCLIENT:
        {#- --- 必选参数 --- -#}
        CLIENTID={{item.CLIENTID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 执行命令，查询响应端实例。

#### 2.6 执行命令，删除响应端实例。

```jinja2
{%- set LST_TWAMPRESPONDER=getParameterValue('LST TWAMPRESPONDER') -%}
{%- if LST_TWAMPRESPONDER -%}
    {%- for item in rmv_twampresponder_list -%}
        RMV TWAMPRESPONDER:
        {#- --- 必选参数 --- -#}
        RESPONDERID={{item.RESPONDERID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.7 执行命令，查询本端逻辑接口实例。

#### 2.8 执行命令，删除逻辑接口实例。

```jinja2
{%- set LST_TWAMPLOGICINF=getParameterValue('LST TWAMPLOGICINF') -%}
{%- if LST_TWAMPLOGICINF -%}
    {%- for item in rmv_twamplogicinf_list -%}
        RMV TWAMPLOGICINF:
        {#- --- 必选参数 --- -#}
        NAME="{{item.NAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.9 执行命令，查询vpn实例。

#### 2.10 执行命令，删除vpn实例。

```jinja2
{%- set LST_TWAMPVPNINST=getParameterValue('LST TWAMPVPNINST') -%}
{%- if LST_TWAMPVPNINST -%}
    {%- for item in rmv_twampvpninst_list -%}
        RMV TWAMPVPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 执行命令，动态下线IPAPM pod。

```jinja2
{%- for item in opr_featuredisable_list -%}
    OPR FEATUREDISABLE:
    {#- --- 必选参数 --- -#}
    PODTYPE="{{item.PODTYPE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DISABLETYPE is not none -%}
        DISABLETYPE={{item.DISABLETYPE}},
    {%- endif -%}
    {%- if item.FUNCTIONSETNAME is not none -%}
        FUNCTIONSETNAME="{{item.FUNCTIONSETNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 执行命令，确认已经成功下线IPAPM pod。

### 回显为“处理结果=处理成功”。

### 回显“查询Pod不存在”。

### 5 若动态下线IPAPM服务后，不再上线IPAPM服务，则需要缩容IPAPM自身VM（PBU\_P-T），释放VM资源。

### 若后续还需要上线IPAPM服务，则不必缩容IPAPM自身VM。

### **缩容VM**：请参见《UDG中心侧扩缩容指导书(基于LCM)》或《UDG中心侧扩缩容指导书(基于NFVO)》。

