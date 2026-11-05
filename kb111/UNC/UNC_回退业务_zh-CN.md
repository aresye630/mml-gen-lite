---
id: ''
name: 回退业务
ne_type: UNC
type: feature
description: 本节以举例来描述Pool区回退到非Pool区的配置过程。  本场景适用于将Pool区回退成非Pool区。Pool组网回退到非Pool组网，可以分为紧急回退和一般回退。  回退时，在eNodeB上将其他MME链路删除（与eNodeB相连的MME除外），根据回退的目的，决定是否需要修改eNodeB、MME的配置数据。  如果只是临时回退，后续还需要组Pool的情况下，不需要修改eNodeB、MME的配置数据，断开多余的S1链接后进行业务拨测正常即可，否则分别修改eNodeB、MME的配置数据，完成彻底的回退。  紧急回退对用户影响较大，被断开的链接上的正在进行PS业务的用户都会发生业务中断，必须重新接入后才能使用业务。  图1是4G网络演进目标示意图。  回退MME上配置数据的过程如下：  1. eNodeB上将新接入的某个或某几个MME的链路删除（接入Pool之前所连接的MME仍是可用的，保留正常业务接入到原MME）。 2. DNS上删除新增的相关配置。     MMEID的域名解析无需删除，TA对应的SGW域名解析无需删除。 3. eNodeB对应的TA的域名解析需要区分直连和非直连MME，非直连MME的GTPc地址全部删除，直连关系的MME地址要保留。 4. MME上删除新增的数据配置。     删除新增TALIST。 5. 完成从Pool区内分离的MME和eNodeB的基本功能测试。  图1以三个MME分别带3个eNodeB的网路为例，描述如何将Pool区回退为非Pool区组网。  **图1** Pool区回退
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","MME容灾方案","改造部署","4G现网演进成MME Pool","回退业务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本节以举例来描述Pool区回退到非Pool区的配置过程。本场景适用于将Pool区回退成非Pool区。Pool组网回退到非Pool组网，可以分为紧急回退和一般回退。回退时，在eNodeB上将其他MME链路删除（与eNodeB相连的MME除外），根据回退的目的，决定是否需要修改eNodeB、MME的配置数据。如果只是临时回退，后续还需要组Pool的情况下，不需要修改eNodeB、MME的配置数据，断开多余的S1链接后进行业务拨测正常即可，否则分别修改eNodeB、MME的配置数据，完成彻底的回退。紧急回退对用户影响较大，被断开的链接上的正在进行PS业务的用户都会发生业务中断，必须重新接入后才能使用业务。图1是4G网络演进目标示意图。回退MME上配置数据的过程如下：1. eNodeB上将新接入的某个或某几个MME的链路删除（接入Pool之前所连接的MME仍是可用的，保留正常业务接入到原MME）。2. DNS上删除新增的相关配置。   MMEID的域名解析无需删除，TA对应的SGW域名解析无需删除。3. eNodeB对应的TA的域名解析需要区分直连和非直连MME，非直连MME的GTPc地址全部删除，直连关系的MME地址要保留。4. MME上删除新增的数据配置。   删除新增TALIST。5. 完成从Pool区内分离的MME和eNodeB的基本功能测试。图1以三个MME分别带3个eNodeB的网路为例，描述如何将Pool区回退为非Pool区组网。**图1** Pool区回退

```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_sys_list:
      type: items
      properties:
        CAP:
          name: '设备能力'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_talst_list:
      type: items
      properties:
        TALISTID:
          name: 'TA List 标号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAI:
          name: 'TAI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_sys_list:
    - CAP: 50
    rmv_talst_list:
    - TALISTID: 0
      TAI: '123033101'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 Pool参数配置阶段回退。

### 删除MME侧配置的Pool参数。

### 此处只以MME1为例，MME2/MME3相似。

#### 1.1 在MME1上将负载权重修改为原来的值。

```jinja2
{%- for item in set_sys_list -%}
    SET SYS:
    {#- --- 可选参数 --- -#}
    {%- if item.CAP is not none -%}
        CAP={{item.CAP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 重复执行本阶段步骤，删除其他MME配置的Pool参数，本例为MME2，MME3。

#### 1.3 如果修改了MMEID，参见MME ID调整。

#### 修改MMEID会导致用户在一段时间内导致业务失败。

### 2 割接阶段回退。

#### 2.1 删除DNS Server的TA记录中扩展的MME IP地址。

#### 2.2 删除eNodeB侧多余的链路配置。

#### 2.3 删除S1ap层以下的配置。

#### 2.4 删除MME测新增配置。

#### 删除新增TALIST：

```jinja2
{%- for item in rmv_talst_list -%}
    RMV TALST:
    {#- --- 必选参数 --- -#}
    TALISTID={{item.TALISTID}},
    {#- --- 可选参数 --- -#}
    {%- if item.TAI is not none -%}
        TAI="{{item.TAI}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.5 执行Pool参数配置阶段回退。

#### 2.6 执行链路准备阶段回退。

### 3 改造完成阶段回退。

#### 3.1 执行割接阶段回退。

#### 3.2 执行Pool参数配置阶段回退。

#### 3.3 执行链路准备阶段回退。

