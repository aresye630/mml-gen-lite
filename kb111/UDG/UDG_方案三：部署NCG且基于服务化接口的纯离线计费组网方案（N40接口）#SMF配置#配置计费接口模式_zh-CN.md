---
id: ''
name: 配置计费接口模式
ne_type: UDG
type: feature
description: 本指导描述终端在接入网络时计费接口使用Nchf接口的配置过程。  UNC支持配置在不同类型终端接入不同网络时选择计费接口，计费接口选择有三种方式，优先级从高到低为：基于用户漫游属性选择计费接口 （对应命令为**ADD ROAMCHGMODE**）> 基于APN/DNN选择计费接口 （对应命令为**ADD APNCHGMODE**）> 全局配置计费接口（对应命令为**SET CHGMODE**）。  图1绘制了不同类型终端接入不同网络时计费接口选择。  **图1** 不同类型终端接入不同网络时计费接口选择逻辑图  SGW-C独立部署的场景下，需要SGW-C发起计费会话。在这种场景下，通过设置SGW-C上**ADD ROAMCHGMODE**/**ADD APNCHGMODE**/**SET CHGMODE**命令中**FORSGWONLY**的值可以手动指定计费接口。  UNC支持配置在不同类型终端接入不同网络时选择策略接口，策略接口选择有两种方式，优先级从高到低为：基于APN/DNN选择策略接口 > 全局配置策略接口。  图2绘制了不同类型终端接入不同网络时策略接口选择。  **图2** 不同类型终端接入不同网络时策略接口选择逻辑图  当UNC通过上述方式配置了计费接口和策略接口后，可通过**ADD PCCCHGMODEBYPCFID**命令基于PCF instance ID配置用户最终使用的策略接口类型和计费接口类型。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案三：部署NCG且基于服务化接口的纯离线计费组网方案（N40接口）","SMF配置","配置计费接口模式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述终端在接入网络时计费接口使用Nchf接口的配置过程。UNC支持配置在不同类型终端接入不同网络时选择计费接口，计费接口选择有三种方式，优先级从高到低为：基于用户漫游属性选择计费接口 （对应命令为**ADD ROAMCHGMODE**）> 基于APN/DNN选择计费接口 （对应命令为**ADD APNCHGMODE**）> 全局配置计费接口（对应命令为**SET CHGMODE**）。图1绘制了不同类型终端接入不同网络时计费接口选择。**图1** 不同类型终端接入不同网络时计费接口选择逻辑图SGW-C独立部署的场景下，需要SGW-C发起计费会话。在这种场景下，通过设置SGW-C上**ADD ROAMCHGMODE**/**ADD APNCHGMODE**/**SET CHGMODE**命令中**FORSGWONLY**的值可以手动指定计费接口。UNC支持配置在不同类型终端接入不同网络时选择策略接口，策略接口选择有两种方式，优先级从高到低为：基于APN/DNN选择策略接口 > 全局配置策略接口。图2绘制了不同类型终端接入不同网络时策略接口选择。**图2** 不同类型终端接入不同网络时策略接口选择逻辑图当UNC通过上述方式配置了计费接口和策略接口后，可通过**ADD PCCCHGMODEBYPCFID**命令基于PCF instance ID配置用户最终使用的策略接口类型和计费接口类型。

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
    set_chgmode_list:
      type: items
      properties:
        TMACCTYPE:
          name: '指定终端和接入类型'
          type: string
          required: false
          description: '配置5G终端接入4G网络时使用的计费接口模式。  说明：  本示例配置5G终端接入4G网络时，使用Nchf接口模式。请根据实际情况使用该命令进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BY5GSIWKI:
          name: '按5GS互操作指示选择计费接口'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FORCED:
          name: '指定的计费接口'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FORVSMFONLY:
          name: '作为V-SMF计费模式'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISMFCHGSW:
          name: 'ISMF是否支持计费'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BYIWKUEN5GR4G:
          name: '非5G终端4G接入时按5GS互操作指示选择计费接口'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_apnchgmode_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '（可选）基于APN/DNN配置计费接口模式。当全局配置不能满足诉求，需要基于APN/DNN对某些用户群做特殊计费接口配置时，可以执行此操作。  说明：  本示例配置对于APN为ap-test的5G终端接入4G网络时，使用Nchf接口。请根据实际情况使用该命令进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TMACCTYPE:
          name: '指定终端和接入类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BY5GSIWKI:
          name: '按5GS互操作指示选择计费接口'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FORCED:
          name: '指定的计费接口'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_roamchgmode_list:
      type: items
      properties:
        TMACCTYPE:
          name: '指定终端和接入类型'
          type: string
          required: false
          description: '（可选）基于终端漫游属性计费接口模式。当全局配置不能满足诉求，需要基于漫游属性对某些用户群做特殊计费接口配置时，可以执行此操作。  说明：  本示例配置对于全局的漫游用户，在使用5G终端接入4G网络时，使用Nchf计费接口；UNC作为V-SMF时，计费接口使用Nchf接口模式。请根据实际情况使用该命令进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '控制类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROAMINGTYPE:
          name: '漫游属性'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BY5GSIWKI:
          name: '按5GS互操作指示选择计费接口'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FORCED:
          name: '指定的计费接口'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FORVSMFONLY:
          name: '作为V-SMF计费模式'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pccchgmodebypcfid_list:
      type: items
      properties:
        PCFINSID:
          name: 'PCF实例标识'
          type: string
          required: false
          description: '（可选）一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以通过该命令进行配置。  用户的计费接口类型以**ADD APNCHGMODE**或**SET CHGMODE**为初选结果，在此基础上，可以通过本命令决策是否由N40回落GaGy，或者是否由GaGy升级为N40。  说明：  本示例以pcf1，策略接口类型为N7，计费接口类型继承**ADD APNCHGMODE**或**SET CHGMODE**命令配置举例。请根据实际情况使用该命令进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        POLICYINTF:
          name: '策略接口类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHGINTF:
          name: '计费接口类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_chgmode_list:
    - TMACCTYPE: UE5G_RAT4G
      BY5GSIWKI: False
      FORCED: NchfMode
      FORVSMFONLY: NchfMode
      ISMFCHGSW: DISABLE
      BYIWKUEN5GR4G: False
    add_apnchgmode_list:
    - APN: apn-test
      TMACCTYPE: UE5G_RAT4G
      BY5GSIWKI: False
      FORCED: NchfMode
    add_roamchgmode_list:
    - TMACCTYPE: UE5G_RAT4G
      CTRLTYPE: GLOBAL_LEVEL
      ROAMINGTYPE: ROAMING
      BY5GSIWKI: False
      FORCED: NchfMode
      FORVSMFONLY: NchfMode
    add_pccchgmodebypcfid_list:
    - PCFINSID: pcf1
      POLICYINTF: N7
      CHGINTF: INHERIT
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置在不同类型终端接入不同网络时所选择的计费接口。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_chgmode_list的变量区（command: SET CHGMODE） -#}
<!-- MISSING_MACRO: command=SET CHGMODE list_name=set_chgmode_list step_id=1 -->
```

### 2 **可选：**配置不同的APN/DNN在不同类型终端接入不同网络时所选择的计费接口。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apnchgmode_list的变量区（command: ADD APNCHGMODE） -#}
<!-- MISSING_MACRO: command=ADD APNCHGMODE list_name=add_apnchgmode_list step_id=2 -->
```

### 3 **可选：**配置不同漫游类型在不同类型终端接入不同网络时所选择的计费接口。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_roamchgmode_list的变量区（command: ADD ROAMCHGMODE） -#}
<!-- MISSING_MACRO: command=ADD ROAMCHGMODE list_name=add_roamchgmode_list step_id=3 -->
```

### 4 **可选：**配置基于PCF的计费接口和策略接口类型。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pccchgmodebypcfid_list的变量区（command: ADD PCCCHGMODEBYPCFID） -#}
<!-- MISSING_MACRO: command=ADD PCCCHGMODEBYPCFID list_name=add_pccchgmodebypcfid_list step_id=4 -->
```

### 一般情况下不需要配置该命令，当需要基于PCF实例标识调整用户最终使用的策略接口类型 (N7/Gx) 或计费接口类型 (N40/GaGy) 时，可以通过该命令进行配置。

