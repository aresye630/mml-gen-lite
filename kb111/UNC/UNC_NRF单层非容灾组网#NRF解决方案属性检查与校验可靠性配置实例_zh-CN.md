---
id: ''
name: NRF解决方案属性检查与校验可靠性配置实例
ne_type: UNC
type: feature
description: 为了避免NF的异常操作影响到NRF设备安全及5G Core业务，NRF支持对NF进行白名单和校验控制：符合NRF白名单的NF才允许注册/更新；NF进行上述服务化流程时，对应参数校验通过的NF才能完成对应的服务化流程。  为了避免号段类NF的号段配置错误影响到5G Core业务，NRF支持对NF Profile的属性冲突核验，对于存在号段冲突的情况可以查询或提示告警。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NRF解决方案","NRF功能部署","4/5G融合部署","NRF单层非容灾组网","NRF解决方案属性检查与校验可靠性配置实例"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为了避免NF的异常操作影响到NRF设备安全及5G Core业务，NRF支持对NF进行白名单和校验控制：符合NRF白名单的NF才允许注册/更新；NF进行上述服务化流程时，对应参数校验通过的NF才能完成对应的服务化流程。为了避免号段类NF的号段配置错误影响到5G Core业务，NRF支持对NF Profile的属性冲突核验，对于存在号段冲突的情况可以查询或提示告警。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。
* 完成加载License。

* NRF解决方案基本功能在NF侧和NRF侧均已配置完成，详细参考NRF解决方案基本功能配置实例（NF注册/更新/去注册、NF订阅/通知）。
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
    set_nrfwhitelistsw_list:
      type: items
      properties:
        NFWHITELISTSW:
          name: 'NF白名单开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: '启用NF白名单接入控制功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_nrfwhitelist_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 40
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nfnrfmgmtpara_list:
      type: items
      properties:
        NFPROFILECHKSW:
          name: 'NF参数检查开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nrftakepararule_list:
      type: items
      properties:
        NFTYPE:
          name: '网元类型'
          type: string
          enum:
          - UDM
          - AMF
          - SMF
          - AUSF
          - PCF
          - UDR
          - BSF
          - CHF
          - CUSTOM_OCS
          - SMSF
          - NWDAF
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NOTAISW:
          name: 'NF无TAI处理开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NOIPRANGESW:
          name: 'NF无IP处理开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOSEGGUARDSW:
          name: 'NF号段防呆开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REGUPDSW:
          name: '注册更新处理开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nrfpatupdidxsw_list:
      type: items
      properties:
        PATUPDWITHIDXSW:
          name: '禁止PATCH更新携带下标开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: 'NRF处理携带array下标的部分更新流程为更新失败，避免NF和NRF间对array下标处理不一致而影响业务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nrfdiscpararule_list:
      type: items
      properties:
        NFTYPE:
          name: '网元类型'
          type: string
          enum:
          - DEFAULT
          - NRF
          - UDM
          - AMF
          - SMF
          - AUSF
          - NEF
          - PCF
          - SMSF
          - NSSF
          - UDR
          - LMF
          - GMLC
          - EIR_5G
          - SEPP
          - UPF
          - N3IWF
          - AF
          - UDSF
          - BSF
          - CHF
          - NWDAF
          - CUSTOM_OCS
          - SCP
          required: true
          description: '目标为AMF的服务发现，发现参数除基本发现参数及NF Type外，必须携带其他发现参数，否则服务发现失败。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DISCPARA:
          name: '发现参数防呆规则'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    opr_nrfnfattrvry_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: 'NRF上打开AMF的NF Profile的属性冲突人工核验。  对本NRF管理的AMF间TAI属性进行核验，选择NF实例标识中大区省份信息起始位置为4信息长度为3的部分，可以通过**DSP NRFNFATTRVRY**查看核验结果。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nrfverifypara_list:
      type: items
      properties:
        START:
          name: '起始位置'
          type: integer
          minimum: 0
          maximum: 35
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LENGTH:
          name: '长度'
          type: integer
          minimum: 0
          maximum: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VRYLOCALATTR:
          name: 'NF间冲突核验属性'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nrfdiscverify_list:
      type: items
      properties:
        DISCVRYFSW:
          name: '服务发现NF属性冲突核验开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: 'AMF和NRF上分别打开NF Profile的属性冲突自动核验，如果存在属性冲突，会上报对应的告警。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        START:
          name: '起始位置'
          type: integer
          minimum: 0
          maximum: 35
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LENGTH:
          name: '长度'
          type: integer
          minimum: 0
          maximum: 36
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DISCLOCALATTR:
          name: 'NF间冲突核验属性'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DISCINTERATTR:
          name: 'NF和跨NRF路由数据冲突核验属性'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        AGINGDURATION:
          name: '告警最长老化时长(分钟)'
          type: integer
          minimum: 1
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISCPRELOCALSW:
          name: '服务发现NF属性冲突优选开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXRATE:
          name: '单进程最大核验速率(次/秒)'
          type: integer
          minimum: 0
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nfdiscplcy_list:
      type: items
      properties:
        NFIDCHECK:
          name: 'NF实例标识冲突核查开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nrfbigpkgpara_list:
      type: items
      properties:
        MAXREGSEGNUM:
          name: '单NF的最大号段数量'
          type: integer
          minimum: 1
          maximum: 80000
          required: false
          description: 'AMF和NRF上分别设置最大包处理能力，保证网络稳定性，避免超大包影响网络带宽。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXDISCSEGNUM:
          name: '服务发现返回的最大号段数'
          type: integer
          minimum: 1
          maximum: 160000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXPKGSIZE:
          name: '最大报文长度(KByte)'
          type: integer
          minimum: 0
          maximum: 16000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nfdiscplcy_list_1:
      type: items
      properties:
        MAXPLDSIZE:
          name: '最大有效负载(千字节)'
          type: integer
          minimum: 0
          maximum: 16000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFACV01'
      SWITCH: ENABLE
    set_nrfwhitelistsw_list:
    - NFWHITELISTSW: FUNC_ON
    add_nrfwhitelist_list:
    - NFINSTANCEID: '88888888-4444-1234-5678-123456789ABC'
    set_nfnrfmgmtpara_list:
    - NFPROFILECHKSW: AMF_TAI-1
    set_nrftakepararule_list:
    - NFTYPE: AMF
      NOTAISW: FUNC_ON
      NOIPRANGESW: ''
      NOSEGGUARDSW: ''
      REGUPDSW: ''
    set_nrfpatupdidxsw_list:
    - PATUPDWITHIDXSW: FUNC_ON
    set_nrfdiscpararule_list:
    - NFTYPE: AMF
      DISCPARA: TARGETNFTYPE-1
    opr_nrfnfattrvry_list:
    - NFINSTANCEID: '88888888-4444-1234-5678-123456789ABC'
    set_nrfverifypara_list:
    - START: 4
      LENGTH: 3
      VRYLOCALATTR: TAI-1
    set_nrfdiscverify_list:
    - DISCVRYFSW: FUNC_ON
      START: 4
      LENGTH: 3
      DISCLOCALATTR: TAI-1
      DISCINTERATTR: TAI-1
      AGINGDURATION: ''
      DISCPRELOCALSW: ''
      MAXRATE: ''
    set_nfdiscplcy_list:
    - NFIDCHECK: ON
    set_nrfbigpkgpara_list:
    - MAXREGSEGNUM: 20000
      MAXDISCSEGNUM: 40000
      MAXPKGSIZE: 200
    set_nfdiscplcy_list_1:
    - MAXPLDSIZE: 160
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 任务场景1：属性冲突检查等可靠性功能。为了确保NF Profile正确性，避免NF由于属性配置错误导致NF间存在属性冲突，AMF和NRF侧进行如下可靠性配置：

#### 1.1 //打开属性冲突检查相关License。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.3 //NRF侧打开NF白名单接入控制功能。NRF将处理白名单内NF的注册、更新及心跳，未在白名单内的NF将无法正常注册、更新以及维持到NRF的心跳。

```jinja2
{%- for item in set_nrfwhitelistsw_list -%}
    SET NRFWHITELISTSW:
    {#- --- 可选参数 --- -#}
    {%- if item.NFWHITELISTSW is not none -%}
        NFWHITELISTSW={{item.NFWHITELISTSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 //AMF侧人工检验NF Profile符合规范后，NRF侧将此AMF的InstanceID：88888888-4444-1234-5678-123456789ABC加入到白名单内，确保可以到NRF上注册/更新。

```jinja2
{%- for item in add_nrfwhitelist_list -%}
    ADD NRFWHITELIST:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    ;
{%- endfor -%}
```

#### 1.6 //AMF侧检查此规则。

```jinja2
{%- for item in set_nfnrfmgmtpara_list -%}
    SET NFNRFMGMTPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.NFPROFILECHKSW is not none -%}
        NFPROFILECHKSW={{item.NFPROFILECHKSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 //NRF侧检查此规则。

```jinja2
{%- for item in set_nrftakepararule_list -%}
    SET NRFTAKEPARARULE:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=AMF/SMF/NWDAF 时可选 --- -#}
    {%- if item.NFTYPE in ['AMF', 'SMF', 'NWDAF'] -%}
        {%- if item.NOTAISW is not none -%}
            NOTAISW={{item.NOTAISW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=BSF 时可选 --- -#}
    {%- if item.NFTYPE == 'BSF' -%}
        {%- if item.NOIPRANGESW is not none -%}
            NOIPRANGESW={{item.NOIPRANGESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=UDM/UDR/AUSF/CUSTOM_OCS/CHF/PCF/SMSF 时可选 --- -#}
    {%- if item.NFTYPE in ['UDM', 'UDR', 'AUSF', 'CUSTOM_OCS', 'CHF', 'PCF', 'SMSF'] -%}
        {%- if item.NOSEGGUARDSW is not none -%}
            NOSEGGUARDSW={{item.NOSEGGUARDSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NOSEGGUARDSW=FUNC_ON 时可选 --- -#}
    {%- if item.NOSEGGUARDSW == 'FUNC_ON' -%}
        {%- if item.REGUPDSW is not none -%}
            REGUPDSW={{item.REGUPDSW}},
        {%- endif -%}
    {#- --- 条件可选：NOTAISW=FUNC_ON 时可选 --- -#}
    {%- elif item.NOTAISW == 'FUNC_ON' -%}
        {%- if item.REGUPDSW is not none -%}
            REGUPDSW={{item.REGUPDSW}},
        {%- endif -%}
    {#- --- 条件可选：NOIPRANGESW=FUNC_ON 时可选 --- -#}
    {%- elif item.NOIPRANGESW == 'FUNC_ON' -%}
        {%- if item.REGUPDSW is not none -%}
            REGUPDSW={{item.REGUPDSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.8 //NRF侧处理携带array下标的部分更新流程为更新失败，避免NF和NRF间对array下标处理不一致而影响业务。

```jinja2
{%- for item in set_nrfpatupdidxsw_list -%}
    SET NRFPATUPDIDXSW:
    {#- --- 可选参数 --- -#}
    {%- if item.PATUPDWITHIDXSW is not none -%}
        PATUPDWITHIDXSW={{item.PATUPDWITHIDXSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.9 //NRF侧配置，目标为AMF的服务发现，发现参数除基本发现参数及NF Type外，必须携带其他发现参数，否则服务发现失败。

```jinja2
{%- for item in set_nrfdiscpararule_list -%}
    SET NRFDISCPARARULE:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DISCPARA is not none -%}
        DISCPARA={{item.DISCPARA}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.11 //NRF侧对本NRF管理的AMF间TAI属性进行核验，选择NF实例标识中大区省份信息起始位置为4信息长度为3的部分。

```jinja2
{%- for item in opr_nrfnfattrvry_list -%}
    OPR NRFNFATTRVRY:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_nrfverifypara_list -%}
    SET NRFVERIFYPARA:
    {#- --- 必选参数 --- -#}
    START={{item.START}},
    LENGTH={{item.LENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRYLOCALATTR is not none -%}
        VRYLOCALATTR={{item.VRYLOCALATTR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.12 //可以通过DSP NRFNFATTRVRY查看核验结果。

#### 1.14 //NRF侧对本NRF管理服务发现结果的NF进行核验，选择NF实例标识中大区省份信息起始位置为4信息长度为3的部分，如果存在NF与当前NF的实现大区省份信息不一致会核验上报告警。对于跨NRF路由属性冲突也进行核验，如果本NRF服务发现结果有匹配的AMF，跨NRF寻址路由也有符合的NF，则会核验上报告警。

```jinja2
{%- for item in set_nrfdiscverify_list -%}
    SET NRFDISCVERIFY:
    {#- --- 可选参数 --- -#}
    {%- if item.DISCVRYFSW is not none -%}
        DISCVRYFSW={{item.DISCVRYFSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DISCVRYFSW=FUNC_ON 时必选 --- -#}
    {%- if item.DISCVRYFSW == 'FUNC_ON' -%}
        START={{item.START}},
    {%- endif -%}
    {#- --- 条件必选：DISCVRYFSW=FUNC_ON 时必选 --- -#}
    {%- if item.DISCVRYFSW == 'FUNC_ON' -%}
        LENGTH={{item.LENGTH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DISCVRYFSW=FUNC_ON 时可选 --- -#}
    {%- if item.DISCVRYFSW == 'FUNC_ON' -%}
        {%- if item.DISCLOCALATTR is not none -%}
            DISCLOCALATTR={{item.DISCLOCALATTR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DISCVRYFSW=FUNC_ON 时可选 --- -#}
    {%- if item.DISCVRYFSW == 'FUNC_ON' -%}
        {%- if item.DISCINTERATTR is not none -%}
            DISCINTERATTR={{item.DISCINTERATTR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DISCVRYFSW=FUNC_ON 时可选 --- -#}
    {%- if item.DISCVRYFSW == 'FUNC_ON' -%}
        {%- if item.AGINGDURATION is not none -%}
            AGINGDURATION={{item.AGINGDURATION}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DISCVRYFSW=FUNC_ON 时可选 --- -#}
    {%- if item.DISCVRYFSW == 'FUNC_ON' -%}
        {%- if item.DISCPRELOCALSW is not none -%}
            DISCPRELOCALSW={{item.DISCPRELOCALSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DISCVRYFSW=FUNC_ON 时可选 --- -#}
    {%- if item.DISCVRYFSW == 'FUNC_ON' -%}
        {%- if item.MAXRATE is not none -%}
            MAXRATE={{item.MAXRATE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.15 //AMF侧打开NF实例标识冲突核查开关。AMF在本地缓存中匹配成功的NF存在大区/省份标识不同，则上报告警。

```jinja2
{%- for item in set_nfdiscplcy_list -%}
    SET NFDISCPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.NFIDCHECK is not none -%}
        NFIDCHECK={{item.NFIDCHECK}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 任务场景2：为了避免NF和NRF间传递大包影响网络带宽，NF和NRF侧设置各自的最大包处理能力。

#### 2.2 //NRF侧配置支持单NF的最大号段数量20000，服务发现返回的最大号段数40000，最大报文长度200千字节。

```jinja2
{%- for item in set_nrfbigpkgpara_list -%}
    SET NRFBIGPKGPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.MAXREGSEGNUM is not none -%}
        MAXREGSEGNUM={{item.MAXREGSEGNUM}},
    {%- endif -%}
    {%- if item.MAXDISCSEGNUM is not none -%}
        MAXDISCSEGNUM={{item.MAXDISCSEGNUM}},
    {%- endif -%}
    {%- if item.MAXPKGSIZE is not none -%}
        MAXPKGSIZE={{item.MAXPKGSIZE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 //AMF侧设置最大有效负载，在服务发现过程中带给NRF，告知返回NF profile的最大字节数为160千字节。

```jinja2
{%- for item in set_nfdiscplcy_list_1 -%}
    SET NFDISCPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.MAXPLDSIZE is not none -%}
        MAXPLDSIZE={{item.MAXPLDSIZE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

