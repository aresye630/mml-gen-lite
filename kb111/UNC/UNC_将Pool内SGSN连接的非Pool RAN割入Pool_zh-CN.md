---
id: ''
name: 将Pool内SGSN连接的非Pool RAN割入Pool
ne_type: UNC
type: feature
description: 本场景适用于将现网Pool内的SGSN连接的非Pool的RAN割接到Pool中，以扩大Pool区的覆盖范围。  此过程与“2G现网演进成SGSN Pool”、“3G现网演进成SGSN Pool”过程类似，不同的是没有核心网的Pool License加载阶段和Pool参数准备阶段的核心网参数配置。  如图1所示为将Pool内SGSN连接的非Pool RAN割入Pool的组网实例。  **图1** 将Pool内SGSN连接的非Pool RAN割入Pool组网实例
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","SGSN容灾方案","扩容部署","激活业务","RAN侧扩容","将Pool内SGSN连接的非Pool RAN割入Pool"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本场景适用于将现网Pool内的SGSN连接的非Pool的RAN割接到Pool中，以扩大Pool区的覆盖范围。此过程与“2G现网演进成SGSN Pool”、“3G现网演进成SGSN Pool”过程类似，不同的是没有核心网的Pool License加载阶段和Pool参数准备阶段的核心网参数配置。如图1所示为将Pool内SGSN连接的非Pool RAN割入Pool的组网实例。**图1** 将Pool内SGSN连接的非Pool RAN割入Pool组网实例

```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_rnc_list:
      type: items
      properties:
        RNCX:
          name: 'RNCX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IU\_FLEX:
          name: 'IU\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_nse_list:
      type: items
      properties:
        NSEI:
          name: 'NSEI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GB\_FLEX:
          name: 'GB\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_gbnsecfgpara_list:
      type: items
      properties:
        PARAINDEX:
          name: 'PARAINDEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GB\_FLEX:
          name: 'GB\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolla_list:
      type: items
      properties:
        BGNTAI:
          name: '起始TAI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDTAI:
          name: '终止TAI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LAC:
          name: '位置区域码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_iupaging_list:
      type: items
      properties:
        LAI:
          name: '位置区标识'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: '路由区编码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCINDEX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_rnc_list:
    - RNCX: '1'
      IU\_FLEX: YES
    mod_nse_list:
    - NSEI: '1'
      GB\_FLEX: YES
    mod_gbnsecfgpara_list:
    - PARAINDEX: '1'
      GB\_FLEX: YES
    add_poolla_list:
    - BGNTAI: '123035601'
      ENDTAI: '123035605'
      LAC: '6001'
    add_iupaging_list:
    - LAI: '123000011'
      RAC: '01'
      RNCINDEX: 1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 路由准备和配置同步阶段。

#### 1.1 链路准备阶段。

#### 配置Iu接口和Gb接口的路由信息。

#### 1.2 各SGSN配置参数同步。

### 2 Pool参数配置阶段。

### 配置RAN当前连接的SGSN的Pool参数。

### 在SGSN上打开需要加入Pool的RNC或BSC的Flex开关。

### Iu-Flex：**MOD RNC**: RNCX=1, IU\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_rnc_list的变量区（command: MOD RNC） -#}
<!-- MISSING_MACRO: command=MOD RNC list_name=mod_rnc_list step_id=2 -->
```

### Gb-Flex：

### Gb接口静态配置：**MOD NSE**: NSEI=1, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_nse_list的变量区（command: MOD NSE） -#}
<!-- MISSING_MACRO: command=MOD NSE list_name=mod_nse_list step_id=2 -->
```

### Gb接口动态自动配置：**MOD GBNSECFGPARA**: PARAINDEX=1, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_gbnsecfgpara_list的变量区（command: MOD GBNSECFGPARA） -#}
<!-- MISSING_MACRO: command=MOD GBNSECFGPARA list_name=mod_gbnsecfgpara_list step_id=2 -->
```

### 如果SGSN是使用USN作为融合节点支持MME POOL，在SGSN上配置Mapping的GUMMEI。

```jinja2
{%- if is_scenario_usn_mme_pool -%}
    {%- for item in add_poolla_list -%}
        ADD POOLLA:
        {#- --- 必选参数 --- -#}
        LAC="{{item.LAC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.BGNTAI is not none -%}
            BGNTAI="{{item.BGNTAI}}",
        {%- endif -%}
        {%- if item.ENDTAI is not none -%}
            ENDTAI="{{item.ENDTAI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 用户P-TMSI重分配阶段。

### 运行至少两个周期路由更新时长。

### 4 割接阶段。

### 割接阶段就是将BSC/RNC逐个接入Pool的过程。

#### 4.1 在待割接的BSC/RNC上配置链路层参数。将Gb接口NS层调通，Iu接口SCCP层配通。Gb接口保证不向新的SGSN上报小区信息。

#### 4.2 在各SGSN上配置待割接的BSC/RNC的链路层参数，Gb接口将NSVC调通，Iu接口SCCP层配通。

#### 待割接的BSC/RNC当前所连接的SGSN上已经有此BSC/RNC相关的配置数据，不用新增，只需在其他SGSN上配置BSC/RNC的相关数据。

#### 本步骤具体配置请参考《UNC初始配置与调测》。

#### 4.3 在所有非当前连接的SGSN上面配置待割接的BSC/RNC的相关信息，包括IuPaging表，并进行核查。按照规划修改割接RAI对应的DNS记录，RNC对应的SGSN IP地址。

#### 每个SGSN上添加BSC/RNC下的路由区数据到Pool区：

```jinja2
{%- for item in add_iupaging_list -%}
    ADD IUPAGING:
    {#- --- 必选参数 --- -#}
    LAI="{{item.LAI}}",
    RAC="{{item.RAC}}",
    RNCINDEX={{item.RNCINDEX}},
    ;
{%- endfor -%}
```

#### 4.4 在待割接的BSC/RNC上配置Pool参数。

##### 4.4.1 在割接的BSC/RNC上将所有SGSN状态设置为正常状态。

##### 4.4.2 在BSC/RNC上配置NRI长度。

##### 4.4.3 在BSC/RNC上设置CN ID、NRI。

##### 4.4.4 在BSC/RNC上设置各SGSN负荷分担权重，即SGSN的容量比。

##### 4.4.5 在BSC/RNC上打开Flex功能开关。

#### 4.5 进行业务拨测。

#### 详细请参见配置举例中业务拨测步骤。

### 5 **可选：**负荷均衡阶段。

### 执行用户迁移保证负荷均衡。具体请参见《U2020 MBB网络管理系统 虚拟化产品文档》 / 《iMaster MAE产品文档》的手工迁移用户部分。

