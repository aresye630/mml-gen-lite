---
id: ''
name: 配置话单采集监控
ne_type: UNC
type: feature
description: 话单采集提醒功能是可选功能。当NCG采用PULL方式提供给计费中心第二份最终话单时，推荐配置此功能，增加话单监控任务，检查PULL任务开放给计费中心的目录下是否有话单长时间未取走并删除。话单采集监控功能的配置可以分为5G场景下的话单采集监控，4G场景下的话单采集监控以及2/3G场景下的话单采集监控。2/3/4/5G场景下的话单采集监控应分开配置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案二：部署NCG且基于传统Ga/Gy接口计费组网方案","NCG配置","配置话单采集监控"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
话单采集提醒功能是可选功能。当NCG采用PULL方式提供给计费中心第二份最终话单时，推荐配置此功能，增加话单监控任务，检查PULL任务开放给计费中心的目录下是否有话单长时间未取走并删除。话单采集监控功能的配置可以分为5G场景下的话单采集监控，4G场景下的话单采集监控以及2/3G场景下的话单采集监控。2/3/4/5G场景下的话单采集监控应分开配置。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_cdrmonitor_list:
      type: items
      properties:
        MONITORID:
          name: '话单监控标识'
          type: string
          maxLength: 32
          required: true
          description: '该命令用于增加话单监控任务，检查PULL任务开放给计费中心的目录下是否有话单未取走并删除。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: '是否开启Bi口SingleIP功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        CDRDISTRID:
          name: '分发任务标识'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISCUSTOMDIR:
          name: '是否自定义目录'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MONSUBDIR:
          name: '监控子目录'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNAME:
          name: '模块名'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMEOUT:
          name: '长时间未取话单告警的监控时长（分）'
          type: integer
          minimum: 0
          maximum: 259200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 30
        AGID:
          name: '接入网元分组标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHLNAME:
          name: '通道名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'All'
    add_cdrmonitor_list_2:
      type: items
      properties:
        MONITORID:
          name: '话单监控标识'
          type: string
          maxLength: 32
          required: true
          description: '该命令用于增加话单监控任务，检查PULL任务开放给计费中心的目录下是否有话单未取走并删除。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: '是否开启Bi口SingleIP功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        CDRDISTRID:
          name: '分发任务标识'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISCUSTOMDIR:
          name: '是否自定义目录'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MONSUBDIR:
          name: '监控子目录'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNAME:
          name: '模块名'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMEOUT:
          name: '长时间未取话单告警的监控时长（分）'
          type: integer
          minimum: 0
          maximum: 259200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 30
        AGID:
          name: '接入网元分组标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHLNAME:
          name: '通道名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'All'
    add_cdrmonitor_list_3:
      type: items
      properties:
        MONITORID:
          name: '话单监控标识'
          type: string
          maxLength: 32
          required: true
          description: '该命令用于增加话单监控任务，检查PULL任务开放给计费中心的目录下是否有话单未取走并删除。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: '是否开启Bi口SingleIP功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        CDRDISTRID:
          name: '分发任务标识'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISCUSTOMDIR:
          name: '是否自定义目录'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHLNAME:
          name: '通道名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'All'
        MNAME:
          name: '模块名'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMEOUT:
          name: '长时间未取话单告警的监控时长（分）'
          type: integer
          minimum: 0
          maximum: 259200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 30
        MONSUBDIR:
          name: '监控子目录'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cdrmonitor_list_5:
      type: items
      properties:
        MONITORID:
          name: '话单监控标识'
          type: string
          maxLength: 32
          required: true
          description: '该命令用于增加话单监控任务，检查PULL任务开放给计费中心的目录下是否有话单未取走并删除。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: '是否开启Bi口SingleIP功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        CDRDISTRID:
          name: '分发任务标识'
          type: string
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISCUSTOMDIR:
          name: '是否自定义目录'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHLNAME:
          name: '通道名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'All'
        MNAME:
          name: '模块名'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMEOUT:
          name: '长时间未取话单告警的监控时长（分）'
          type: integer
          minimum: 0
          maximum: 259200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 30
        MONSUBDIR:
          name: '监控子目录'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_cdrmonitor_list:
    - MONITORID: 'test_monitor_pgwcdr'
      ISSINGLEBI: NO
      CDRDISTRID: 'test_distr'
      ISCUSTOMDIR: YES
      MONSUBDIR: 'Huawei/PGWCDR'
      MNAME: 'AP64_1'
      TIMEOUT: 30
      AGID: ''
      CHLNAME: 'All'
    add_cdrmonitor_list_2:
    - MONITORID: 'test_monitor_gcdr'
      ISSINGLEBI: NO
      CDRDISTRID: 'test_distr'
      ISCUSTOMDIR: YES
      MONSUBDIR: 'Huawei/GCDR'
      MNAME: 'AP64_1'
      TIMEOUT: 30
      AGID: ''
      CHLNAME: 'All'
    add_cdrmonitor_list_3:
    - MONITORID: 'test_monitor_pgwcdr'
      ISSINGLEBI: NO
      CDRDISTRID: 'test_distr'
      ISCUSTOMDIR: NO
      AGID: 'PS2'
      CHLNAME: 'pgwcdr'
      MNAME: 'AP64_1'
      TIMEOUT: 30
      MONSUBDIR: ''
    add_cdrmonitor_list_5:
    - MONITORID: 'test_monitor_gcdr'
      ISSINGLEBI: NO
      CDRDISTRID: 'test_distr'
      ISCUSTOMDIR: NO
      AGID: 'PS3'
      CHLNAME: 'gcdr'
      MNAME: 'AP64_1'
      TIMEOUT: 30
      MONSUBDIR: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 获取分发任务标识。

### 在“MML命令行 - UNC”窗口执行**LST CDRDISTR**命令，“TRANSMODE”设置为“PULL（PULL方式）”，查看是否返回多于零个结果：

### 是 => 获取其分发任务标识，接着执行步骤 2

### 否 => 其他方式下不需要配置话单采集提醒，操作结束。

### 2 确定是否通过自定义路径进行话单监控。

### 是 => 步骤 3

### 否 => 步骤 4

### 3 通过自定义路径进行话单监控。

### 在“MML命令行 - UNC”窗口执行**DSP FEMPACKET**命令获取话单通道名称。

### 执行**ADD CDRMONITOR**命令，“ISCUSTOMDIR”选择“YES（是）”，填入上一步获取的通道名称。

#### 3.1 4G话单采集监控。

```jinja2
{%- if is_scenario_custom_path and is_scenario_4g -%}
    {%- for item in add_cdrmonitor_list -%}
        ADD CDRMONITOR:
        {#- --- 必选参数 --- -#}
        MONITORID="{{item.MONITORID}}",
        CDRDISTRID="{{item.CDRDISTRID}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ISSINGLEBI is not none -%}
            ISSINGLEBI={{item.ISSINGLEBI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ISSINGLEBI=NO 时必选 --- -#}
        {%- if item.ISSINGLEBI == 'NO' -%}
            ISCUSTOMDIR={{item.ISCUSTOMDIR}},
        {%- endif -%}
        {#- --- 条件必选：ISCUSTOMDIR=YES 时必选 --- -#}
        {%- if item.ISCUSTOMDIR == 'YES' -%}
            MONSUBDIR="{{item.MONSUBDIR}}",
        {%- endif -%}
        {#- --- 条件必选：ISCUSTOMDIR=NO 时必选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            AGID="{{item.AGID}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ISCUSTOMDIR=NO 时可选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            {%- if item.CHLNAME is not none -%}
                CHLNAME="{{item.CHLNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ISCUSTOMDIR=NO 时可选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            {%- if item.MNAME is not none -%}
                MNAME="{{item.MNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ISSINGLEBI=YES/NO 时可选 --- -#}
        {%- if item.ISSINGLEBI in ['YES', 'NO'] -%}
            {%- if item.TIMEOUT is not none -%}
                TIMEOUT={{item.TIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 2/3G话单采集监控。

```jinja2
{%- if is_scenario_custom_path and is_scenario_2_3g -%}
    {%- for item in add_cdrmonitor_list_2 -%}
        ADD CDRMONITOR:
        {#- --- 必选参数 --- -#}
        MONITORID="{{item.MONITORID}}",
        CDRDISTRID="{{item.CDRDISTRID}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ISSINGLEBI is not none -%}
            ISSINGLEBI={{item.ISSINGLEBI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ISSINGLEBI=NO 时必选 --- -#}
        {%- if item.ISSINGLEBI == 'NO' -%}
            ISCUSTOMDIR={{item.ISCUSTOMDIR}},
        {%- endif -%}
        {#- --- 条件必选：ISCUSTOMDIR=YES 时必选 --- -#}
        {%- if item.ISCUSTOMDIR == 'YES' -%}
            MONSUBDIR="{{item.MONSUBDIR}}",
        {%- endif -%}
        {#- --- 条件必选：ISCUSTOMDIR=NO 时必选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            AGID="{{item.AGID}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ISCUSTOMDIR=NO 时可选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            {%- if item.CHLNAME is not none -%}
                CHLNAME="{{item.CHLNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ISCUSTOMDIR=NO 时可选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            {%- if item.MNAME is not none -%}
                MNAME="{{item.MNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ISSINGLEBI=YES/NO 时可选 --- -#}
        {%- if item.ISSINGLEBI in ['YES', 'NO'] -%}
            {%- if item.TIMEOUT is not none -%}
                TIMEOUT={{item.TIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 通过非自定义路径进行话单监控。

### 在“MML命令行 - UNC”窗口执行**LST CDRPROC**命令获取“接入网元分组标识”，执行**DSP FEMPACKET**命令获取话单“通道名称”。

### 执行**ADD CDRMONITOR**命令，“ISCUSTOMDIR”选择“NO（否）”，“AGID”和“CHLNAME”分别填入上一步获取的“接入网元分组标识”和“通道名称”。

#### 4.1 4G话单采集监控。

```jinja2
{%- if is_scenario_non_custom_path and is_scenario_4g -%}
    {%- for item in add_cdrmonitor_list_3 -%}
        ADD CDRMONITOR:
        {#- --- 必选参数 --- -#}
        MONITORID="{{item.MONITORID}}",
        CDRDISTRID="{{item.CDRDISTRID}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ISSINGLEBI is not none -%}
            ISSINGLEBI={{item.ISSINGLEBI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ISSINGLEBI=NO 时必选 --- -#}
        {%- if item.ISSINGLEBI == 'NO' -%}
            ISCUSTOMDIR={{item.ISCUSTOMDIR}},
        {%- endif -%}
        {#- --- 条件必选：ISCUSTOMDIR=NO 时必选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            AGID="{{item.AGID}}",
        {%- endif -%}
        {#- --- 条件必选：ISCUSTOMDIR=YES 时必选 --- -#}
        {%- if item.ISCUSTOMDIR == 'YES' -%}
            MONSUBDIR="{{item.MONSUBDIR}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ISCUSTOMDIR=NO 时可选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            {%- if item.CHLNAME is not none -%}
                CHLNAME="{{item.CHLNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ISCUSTOMDIR=NO 时可选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            {%- if item.MNAME is not none -%}
                MNAME="{{item.MNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ISSINGLEBI=YES/NO 时可选 --- -#}
        {%- if item.ISSINGLEBI in ['YES', 'NO'] -%}
            {%- if item.TIMEOUT is not none -%}
                TIMEOUT={{item.TIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 2/3G话单采集监控。

```jinja2
{%- if is_scenario_non_custom_path and is_scenario_2_3g -%}
    {%- for item in add_cdrmonitor_list_5 -%}
        ADD CDRMONITOR:
        {#- --- 必选参数 --- -#}
        MONITORID="{{item.MONITORID}}",
        CDRDISTRID="{{item.CDRDISTRID}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ISSINGLEBI is not none -%}
            ISSINGLEBI={{item.ISSINGLEBI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ISSINGLEBI=NO 时必选 --- -#}
        {%- if item.ISSINGLEBI == 'NO' -%}
            ISCUSTOMDIR={{item.ISCUSTOMDIR}},
        {%- endif -%}
        {#- --- 条件必选：ISCUSTOMDIR=NO 时必选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            AGID="{{item.AGID}}",
        {%- endif -%}
        {#- --- 条件必选：ISCUSTOMDIR=YES 时必选 --- -#}
        {%- if item.ISCUSTOMDIR == 'YES' -%}
            MONSUBDIR="{{item.MONSUBDIR}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ISCUSTOMDIR=NO 时可选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            {%- if item.CHLNAME is not none -%}
                CHLNAME="{{item.CHLNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ISCUSTOMDIR=NO 时可选 --- -#}
        {%- if item.ISCUSTOMDIR == 'NO' -%}
            {%- if item.MNAME is not none -%}
                MNAME="{{item.MNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ISSINGLEBI=YES/NO 时可选 --- -#}
        {%- if item.ISSINGLEBI in ['YES', 'NO'] -%}
            {%- if item.TIMEOUT is not none -%}
                TIMEOUT={{item.TIMEOUT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

