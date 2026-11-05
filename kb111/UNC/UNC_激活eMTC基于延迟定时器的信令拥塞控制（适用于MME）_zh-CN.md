---
id: ''
name: 激活eMTC基于延迟定时器的信令拥塞控制（适用于MME）
ne_type: UNC
type: feature
description: 随着物联网的广泛应用，NB-IoT终端被广泛应用在多种行业中，例如水、电表的上报、物流、智能停车等。目前运营商对于NB-IoT终端业务的接入控制较为薄弱，当大量的NB-IoT终端在很短的时间内同时发起业务（例如指定日期的水表上报），可能会造成系统过载并影响普通终端用户的业务接入。MME通过APN识别NB-IoT终端，并发送Back-off time信元来减缓NB-IoT终端业务的接入速度，确保普通终端业务的正常进行，预防系统进入拥塞状态。  适用于MME。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","eMTC业务功能","WSFD-216101 eMTC基于延迟定时器的信令拥塞控制","WSFD-216101 eMTC基于延迟定时器的信令拥塞控制（适用于MME）","激活eMTC基于延迟定时器的信令拥塞控制（适用于MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
随着物联网的广泛应用，NB-IoT终端被广泛应用在多种行业中，例如水、电表的上报、物流、智能停车等。目前运营商对于NB-IoT终端业务的接入控制较为薄弱，当大量的NB-IoT终端在很短的时间内同时发起业务（例如指定日期的水表上报），可能会造成系统过载并影响普通终端用户的业务接入。MME通过APN识别NB-IoT终端，并发送Back-off time信元来减缓NB-IoT终端业务的接入速度，确保普通终端业务的正常进行，预防系统进入拥塞状态。适用于MME。

## 必备事项
前提条件

* 请仔细阅读WSFD-216101 eMTC基于延迟定时器的信令拥塞控制特性概述（适用于MME）。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnnigroup_list:
      type: items
      properties:
        GRPID:
          name: 'APNNI组号'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '低优先级APN流控参数'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 256
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_apnni_list:
      type: items
      properties:
        GRPID:
          name: 'APNNI组号'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 256
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    set_lowpriapnfc_list:
      type: items
      properties:
        FCSWITCH:
          name: '低优先级APN流控功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GRPID:
          name: 'APNNI组号'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINTHD:
          name: '流控速率最小值（个/秒）'
          type: integer
          minimum: 0
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXTHD:
          name: '流控速率最大值（个/秒）'
          type: integer
          minimum: 0
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINBOT:
          name: 'Back off timer最小值（秒）'
          type: integer
          minimum: 1
          maximum: 11160
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXBOT:
          name: 'Back off timer最大值（秒）'
          type: integer
          minimum: 1
          maximum: 11160
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: '测试IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_backofftime_list:
      type: items
      properties:
        APNNAME:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OVERLOADSW:
          name: '系统过载场景下Back-off Time开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BACKOFFTIMER:
          name: 'Back-off时长(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INHERIT:
          name: '是否继承全局Back-off时长'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pgwgroup_list:
      type: items
      properties:
        GRPID:
          name: 'P-GW组号'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '基于P-GW Back-off timer的APN流控参数'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 256
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_pgwnode_list:
      type: items
      properties:
        GRPID:
          name: 'P-GW组号'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUFFIX:
          name: 'P-GW Nodename后缀'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 256
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    set_pgwbackoff_list:
      type: items
      properties:
        FCSWITCH:
          name: '流控开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNNIGRPID:
          name: 'APNNI组号'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PGWGRPID:
          name: 'PGWGRPID'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2LTCC02'
      SWITCH: ENABLE
    add_apnnigroup_list:
    - GRPID: 2
      DESC: 'M2M APNNI Group'
    add_apnni_list:
    - GRPID: 2
      APNNI: 'HUAWEI.COM'
      DESC: 'noname'
    set_lowpriapnfc_list:
    - FCSWITCH: ON
      GRPID: 2
      MINTHD: 10
      MAXTHD: 300
      MINBOT: 900
      MAXBOT: 1800
      IMSI: ''
    set_backofftime_list:
    - APNNAME: 'apn-op'
      OVERLOADSW: ENABLE
      BACKOFFTIMER: 600
      INHERIT: ''
    add_pgwgroup_list:
    - GRPID: 2
      DESC: 'M2M P-GW Group'
    add_pgwnode_list:
    - GRPID: 2
      SUFFIX: 'MNC000.MCC123.3GPPNETWORK.ORG'
      DESC: 'noname'
    set_pgwbackoff_list:
    - FCSWITCH: ON
      APNNIGRPID: 2
      PGWGRPID: 2
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 设置低优先级APN流控。

#### 3.1 增加APNNI组。

```jinja2
{%- for item in add_apnnigroup_list -%}
    ADD APNNIGROUP:
    {#- --- 必选参数 --- -#}
    GRPID={{item.GRPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 增加APNNI。

```jinja2
{%- for item in add_apnni_list -%}
    ADD APNNI:
    {#- --- 必选参数 --- -#}
    GRPID={{item.GRPID}},
    APNNI="{{item.APNNI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 设置低优先级APN流控参数。

```jinja2
{%- for item in set_lowpriapnfc_list -%}
    SET LOWPRIAPNFC:
    {#- --- 可选参数 --- -#}
    {%- if item.FCSWITCH is not none -%}
        FCSWITCH={{item.FCSWITCH}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FCSWITCH=ON 时必选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        GRPID={{item.GRPID}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.MINTHD is not none -%}
            MINTHD={{item.MINTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.MAXTHD is not none -%}
            MAXTHD={{item.MAXTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.IMSI is not none -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.MAXBOT is not none -%}
            MAXBOT={{item.MAXBOT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.MINBOT is not none -%}
            MINBOT={{item.MINBOT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置MME支持基于PGW-C Back-off timer的APN级流控。

#### 4.1 增加PGW-C组。

```jinja2
{%- for item in set_backofftime_list -%}
    SET BACKOFFTIME:
    {#- --- 必选参数 --- -#}
    APNNAME="{{item.APNNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.OVERLOADSW is not none -%}
        OVERLOADSW={{item.OVERLOADSW}},
    {%- endif -%}
    {%- if item.INHERIT is not none -%}
        INHERIT={{item.INHERIT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.BACKOFFTIMER is not none -%}
            BACKOFFTIMER={{item.BACKOFFTIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pgwgroup_list -%}
    ADD PGWGROUP:
    {#- --- 必选参数 --- -#}
    GRPID={{item.GRPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 增加PGW-C局向。

```jinja2
{%- for item in add_pgwnode_list -%}
    ADD PGWNODE:
    {#- --- 必选参数 --- -#}
    GRPID={{item.GRPID}},
    SUFFIX="{{item.SUFFIX}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 设置PGW-C Back-off流控参数。

```jinja2
{%- for item in set_pgwbackoff_list -%}
    SET PGWBACKOFF:
    {#- --- 可选参数 --- -#}
    {%- if item.FCSWITCH is not none -%}
        FCSWITCH={{item.FCSWITCH}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FCSWITCH=ON 时必选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        APNNIGRPID={{item.APNNIGRPID}},
    {%- endif -%}
    {#- --- 条件必选：FCSWITCH=ON 时必选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        PGWGRPID={{item.PGWGRPID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### MME支持基于PGW-C Back-off timer的APN级流控不受**SET LOWPRIAPNFC**控制。即，**SET LOWPRIAPNFC**可设置为“OFF”。

