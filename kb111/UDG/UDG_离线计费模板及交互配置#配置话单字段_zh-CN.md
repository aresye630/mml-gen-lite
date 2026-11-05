---
id: ''
name: 配置话单字段
ne_type: UDG
type: feature
description: 本指导描述话单中某些字段携带规则的配置过程。  对于话单中标识为可选（C）或条件可选（OC）或条件必选（OM）的字段，UNC支持自定义配置是否携带该字段，运营商可根据需要选择配置。  话单可选字段可以基于APN、全局进行配置，它们的优先级顺序是APN > 全局配置 > 默认值。如果高级别的没有配置，则取用低级别的话单字段模板，否则取用默认值。  UNC支持为不同的话单类型绑定不同的CDRFieldTemp话单字段模板，可以分别独立控制SGW-CDR、PGW-CDR、G-CDR话单携带的字段，增强话单字段的灵活度。  * 系统升级时，需注意先升级CG，再升级UNC，以防止UNC先升级后话单中有CG不识别的字段。 * 话单字段修改前需要与对端CG确认是否支持。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案（N40接口+传统Ga/Gy接口）","SMF配置","离线计费配置","离线计费模板及交互配置","配置话单字段"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述话单中某些字段携带规则的配置过程。对于话单中标识为可选（C）或条件可选（OC）或条件必选（OM）的字段，UNC支持自定义配置是否携带该字段，运营商可根据需要选择配置。话单可选字段可以基于APN、全局进行配置，它们的优先级顺序是APN > 全局配置 > 默认值。如果高级别的没有配置，则取用低级别的话单字段模板，否则取用默认值。UNC支持为不同的话单类型绑定不同的CDRFieldTemp话单字段模板，可以分别独立控制SGW-CDR、PGW-CDR、G-CDR话单携带的字段，增强话单字段的灵活度。* 系统升级时，需注意先升级CG，再升级UNC，以防止UNC先升级后话单中有CG不识别的字段。* 话单字段修改前需要与对端CG确认是否支持。

## 必备事项
前提条件

前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。

* 已完成计费属性、APN、User Profile创建。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_cdrfieldtemp_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '话单字段模板名'
          type: string
          required: false
          description: '配置单字段模板，控制话单中是否携带对应字段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PDNCONNECTIONID:
          name: 'pdn-connection-id'
          type: string
          required: false
          description: '配置话单中是否包含pdn-connection-id信息。该字段定义PDN连接的计费标识，用于标识同一PDN连接的不同话单记录。  默认值是“DISABLE”。'
          data_source: ''
          pattern: ''
          default: ''
        PGWADDRESSUSED:
          name: 'pgw-address-used'
          type: string
          required: false
          description: '配置话单中是否携带pgw-address-used字段。该字段标识PGW的控制面地址，如果PGW控制面地址为双栈地址，该字段表示IPv4地址。默认值是“DISABLE”。'
          data_source: ''
          pattern: ''
          default: ''
        PGWPLMNID:
          name: 'pgw-plmn-identifier'
          type: string
          required: false
          description: '配置话单中是否携带pgw-plmn-identifier字段，该字段表示PGW的PLMN标识。  默认值是“DISABLE”。'
          data_source: ''
          pattern: ''
          default: ''
        STARTTIME:
          name: 'start-time'
          type: string
          required: false
          description: '配置话单中是否携带start time字段。该字段记录IP-CAN会话的开始时间，即第一个承载激活时间。  默认值是“DISABLE”。'
          data_source: ''
          pattern: ''
          default: ''
        STOPTIME:
          name: 'stop-time'
          type: string
          required: false
          description: '配置话单中是否携带stop time字段。该字段记录IP-CAN会话的结束时间，即最后一个承载去激活时间。  默认值是“DISABLE”。'
          data_source: ''
          pattern: ''
          default: ''
    set_glbcdrfldtemp_list:
      type: items
      properties:
        PGWCDRTEMPLATE:
          name: 'PGW-CDR话单字段模板名'
          type: string
          required: false
          description: '配置全局绑定话单字段模板'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '为APN实例绑定话单字段模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PGWCDRTEMPLATE:
          name: 'PGW-CDR话单字段模板名'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ofccdrpara_list:
      type: items
      properties:
        GSNNODEIDPREFIX:
          name: 'gsn-node-id字段前缀'
          type: string
          required: false
          description: '配置话单中的gsn-node-id字段的前缀。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        GNIDELIMITER:
          name: 'gsn-node-id字段分隔符'
          type: string
          required: false
          description: '配置话单中的gsn-node-id字段的分隔符。'
          data_source: ''
          pattern: ''
          default: ''
        PGWCDRLOTVSW:
          name: 'PGW-CDR携带List of Traffic Volume'
          type: string
          required: false
          description: '配置PGW-CDR中是否携带listOfTrafficVolume字段。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_cdrfieldtemp_list:
    - TEMPLATENAME: cdrfield-test
      PDNCONNECTIONID: ENABLE
      PGWADDRESSUSED: ENABLE
      PGWPLMNID: ENABLE
      STARTTIME: ENABLE
      STOPTIME: ENABLE
    set_glbcdrfldtemp_list:
    - PGWCDRTEMPLATE: cdrfield-test
    set_apnchargectrl_list:
    - APN: apn-test
      PGWCDRTEMPLATE: cdrfield-test
    set_ofccdrpara_list:
    - GSNNODEIDPREFIX: gsn.huawei
      GNIDELIMITER: '@'
      PGWCDRLOTVSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置话单字段模板。

### UNC默认携带话单可选字段，如果不需要携带某个字段，将对应字段设置为**DISABLE**。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cdrfieldtemp_list的变量区（command: ADD CDRFIELDTEMP） -#}
<!-- MISSING_MACRO: command=ADD CDRFIELDTEMP list_name=add_cdrfieldtemp_list step_id=1 -->
```

### 2 配置全局话单字段模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_glbcdrfldtemp_list的变量区（command: SET GLBCDRFLDTEMP） -#}
<!-- MISSING_MACRO: command=SET GLBCDRFLDTEMP list_name=set_glbcdrfldtemp_list step_id=2 -->
```

### 3 配置APN实例的话单字段模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnchargectrl_list的变量区（command: SET APNCHARGECTRL） -#}
<!-- MISSING_MACRO: command=SET APNCHARGECTRL list_name=set_apnchargectrl_list step_id=3 -->
```

### 4 通过全局参数配置某些话单字段携带规则。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ofccdrpara_list的变量区（command: SET OFCCDRPARA） -#}
<!-- MISSING_MACRO: command=SET OFCCDRPARA list_name=set_ofccdrpara_list step_id=4 -->
```

