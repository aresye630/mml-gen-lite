---
id: ''
name: 配置计费方式
ne_type: UDG
type: feature
description: 本指导用于描述UNC支持融合的离线计费的操作过程。  **GGSN-C/PGW-C/SMF**  对于SMF，计费方式的选择有PCF下发和本地配置，PCF下发的优先级高于本地配置。对于GGSN-C/PGW-C，计费方式的选择有PCRF下发、RADIUS Server下发和本地配置，优先级从高到低依次为：PCRF下发>RADIUS Server下发>本地配置。  GGSN-C/PGW-C/SMF本地配置计费方式开关有三种粒度：User Profile、DNN和计费属性，优先级依次降低。  根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET CHARGECTRL**是控制GGSN-C/PGW-C/SMF本地配置的计费开关是否有效的总开关，当总开关使能了某种计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线/融合计费。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案三：部署NCG且基于服务化接口的纯离线计费组网方案（N40接口）","SMF配置","配置计费方式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导用于描述UNC支持融合的离线计费的操作过程。**GGSN-C/PGW-C/SMF**对于SMF，计费方式的选择有PCF下发和本地配置，PCF下发的优先级高于本地配置。对于GGSN-C/PGW-C，计费方式的选择有PCRF下发、RADIUS Server下发和本地配置，优先级从高到低依次为：PCRF下发>RADIUS Server下发>本地配置。GGSN-C/PGW-C/SMF本地配置计费方式开关有三种粒度：User Profile、DNN和计费属性，优先级依次降低。根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET CHARGECTRL**是控制GGSN-C/PGW-C/SMF本地配置的计费开关是否有效的总开关，当总开关使能了某种计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线/融合计费。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_chargectrl_list:
      type: items
      properties:
        HOMECONVERGED:
          name: '归属地融合用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOMEONLINE:
          name: '归属地在线用户计费控制'
          type: string
          required: false
          description: '开启GGSN-C/PGW-C/SMF计费总开关，配置漫游用户、拜访用户、本地用户均只开启融合计费，不开启离线计费和在线计费。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOMEOFFLINE:
          name: '归属地离线用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITONLINE:
          name: '拜访地在线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访地离线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITCONVERGED:
          name: '拜访地融合计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMONLINE:
          name: '漫游在线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游离线计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMCONVERGED:
          name: '漫游融合计费用户计费控制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '（可选）基于用户模板配置GGSN-C/PGW-C/SMF的计费方式。在全局配置不能满足业务要求时，可执行本命令基于用户模板配置计费方式。  说明：  * 当“RGAPPLIED”配置为“DEFAULT”时，不能同时配置RG相同的离线和在线URR。 * 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，建议同时配置离线和在线URR。  * 本示例配置User Profile为up-test的用户融合计费开关使能，融合计费仅允许离线计费RG可以向CHF进行业务申请和上报，在线计费开关和离线计费开关不使能。请根据业务实际需要进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ONLINESW:
          name: '在线计费开关'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFFLINESW:
          name: '离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVERGEDSW:
          name: '融合计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '（可选）基于DNN配置GGSN-C/PGW-C/SMF的计费方式。在全局配置不能满足业务要求时，可执行本命令基于DNN配置计费方式。  说明：  * 当“RGAPPLIED”配置为“DEFAULT”时，不能同时配置RG相同的离线和在线URR。 * 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，建议同时配置离线和在线URR。  * 本示例配置APN为apn-test的用户融合计费开关使能，融合计费仅允许离线计费RG可以向CHF进行业务申请和上报，在线计费开关和离线计费开关不使能。请根据业务实际需要进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ONLINESW:
          name: '在线计费开关'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFFLINESW:
          name: '离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVERGEDSW:
          name: '融合计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chargemethod_list:
      type: items
      properties:
        CHARGECHARACT:
          name: '计费属性'
          type: string
          required: false
          description: '（可选）基于用户计费属性配置GGSN-C/PGW-C/SMF的计费方式。在全局配置不能满足业务要求时，可执行本命令基于计费属性配置计费方式。  说明：  * 当“RGAPPLIED”配置为“DEFAULT”时，不能同时配置RG相同的离线和在线URR。 * 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，建议同时配置离线和在线URR。 * 本示例配置计费属性为0x0400的用户融合计费开关使能，融合计费仅允许离线计费RG可以向CHF进行业务申请和上报，在线计费开关和离线计费开关不使能。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASK:
          name: '计费属性掩码'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '计费属性优先级'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINE:
          name: '在线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFLINE:
          name: '离线计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVERGED:
          name: '融合计费开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_chargectrl_list:
    - HOMECONVERGED: ENABLE
      HOMEONLINE: DISABLE
      HOMEOFFLINE: DISABLE
      VISITONLINE: DISABLE
      VISITOFFLINE: DISABLE
      VISITCONVERGED: ENABLE
      ROAMONLINE: DISABLE
      ROAMOFFLINE: DISABLE
      ROAMCONVERGED: ENABLE
    set_usrprofcharge_list:
    - USRPROFNAME: up-test
      ONLINESW: DISABLE
      OFFLINESW: DISABLE
      CONVERGEDSW: ''
      RGAPPLIED: OFFLINERGONLY
    set_apnchargectrl_list:
    - APN: apn-test
      ONLINESW: DISABLE
      OFFLINESW: DISABLE
      CONVERGEDSW: ENABLE
      RGAPPLIED: OFFLINERGONLY
    add_chargemethod_list:
    - CHARGECHARACT: SPECIFIC_VALUE
      CCVALUE: '0x0400'
      MASK: '0xFFFF'
      PRIORITY: '1'
      ONLINE: DISABLE
      OFFLINE: DISABLE
      CONVERGED: ENABLE
      RGAPPLIED: OFFLINERGONLY
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 基于用户归属属性配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_chargectrl_list的变量区（command: SET CHARGECTRL） -#}
<!-- MISSING_MACRO: command=SET CHARGECTRL list_name=set_chargectrl_list step_id=1 -->
```

### **SET CHARGECTRL**根据用户漫游属性设置计费方式，**ADD CHARGEMETHOD**根据计费属性设置计费方式，针对同一个用户，两者规划的计费方式要一致，否则用户计费会出错。例如，针对计费属性是normal的本地用户，如果设置本地用户进行在线计费，又设置normal用户进行离线计费，那用户最终计费结果将出错。

### 2 **可选：**基于User Profile配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_usrprofcharge_list的变量区（command: SET USRPROFCHARGE） -#}
<!-- MISSING_MACRO: command=SET USRPROFCHARGE list_name=set_usrprofcharge_list step_id=2 -->
```

### 3 **可选：**基于DNN配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnchargectrl_list的变量区（command: SET APNCHARGECTRL） -#}
<!-- MISSING_MACRO: command=SET APNCHARGECTRL list_name=set_apnchargectrl_list step_id=3 -->
```

### 4 **可选：**基于用户计费属性配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_chargemethod_list的变量区（command: ADD CHARGEMETHOD） -#}
<!-- MISSING_MACRO: command=ADD CHARGEMETHOD list_name=add_chargemethod_list step_id=4 -->
```

