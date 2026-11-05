---
id: ''
name: 配置举例
ne_type: UNC
type: feature
description: 本操作指导Pool区通过新建SGSN来扩容SGSN侧的配置过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","SGSN容灾方案","扩容部署","激活业务","SGSN侧扩容","新建SGSN割入Pool","配置举例"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导Pool区通过新建SGSN来扩容SGSN侧的配置过程。

## 必备事项
前提条件

前提条件

网元基础数据配置完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pool_list:
      type: items
      properties:
        POOLID:
          name: 'POOL标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRILENGTH:
          name: 'NRI长度'
          type: integer
          minimum: 1
          maximum: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_localnri_list:
      type: items
      properties:
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRIVBGN:
          name: 'NRI起始值'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRINUM:
          name: 'NRI个数'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sys_list:
      type: items
      properties:
        CNID:
          name: '核心网标识'
          type: integer
          minimum:
          - 0
          - 65535
          maximum:
          - 4095
          - 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolnri_list:
      type: items
      properties:
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRIV:
          name: 'NRI值'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV4V6
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'SGSN信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNN:
          name: 'SGSN名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        ALTERNATIVE:
          name: 'SGSN信令面地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'SGSN信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nonrai_list:
      type: items
      properties:
        NONRAI:
          name: '路由区标识'
          type: string
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV4V6
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'SGSN IPv4信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNN:
          name: 'SGSN名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        ALTERNATIVE:
          name: 'SGSN IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'SGSN IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    set_licenseswitch_list_1:
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
    set_offloadinf_list:
      type: items
      properties:
        OFFLOADTMR:
          name: '迁移模式周期路由更新定时器（s）'
          type: integer
          minimum: 2
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FIRSTTM:
          name: '第一阶段迁移时间（min）'
          type: integer
          minimum: 0
          maximum: 432
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NONRAI:
          name: '非广播 RAI'
          type: string
          maxLength: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NULLNRIV:
          name: 'NULL NRI值'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolla_list:
      type: items
      properties:
        LAC:
          name: '位置区域码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolla_list_3:
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
    add_poolnri_list_2:
      type: items
      properties:
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRIV:
          name: 'NRI值'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV4V6
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'SGSN信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNN:
          name: 'SGSN名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        ALTERNATIVE:
          name: 'SGSN信令面地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'SGSN信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_pool_list:
    - POOLID: 0
      NRILENGTH: 5
    add_localnri_list:
    - POOLID: 0
      NRIVBGN: 3
      NRINUM: 1
    set_sys_list:
    - CNID: 1
    add_poolnri_list:
    - POOLID: 0
      NRIV: 1
      IPTYPE: IPV4
      IPV4: '192.168.153.1'
      SGSNN: 'SGSN 1'
      ALTERNATIVE: ''
      IPV6: ''
    - POOLID: 0
      NRIV: 2
      IPTYPE: IPV4
      IPV4: '192.168.155.2'
      SGSNN: 'SGSN 2'
      ALTERNATIVE: ''
      IPV6: ''
    add_nonrai_list:
    - NONRAI: '12300611111'
      IPTYPE: IPV4
      IPV4: '192.168.153.1'
      SGSNN: 'SGSN 1'
      ALTERNATIVE: ''
      IPV6: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2IUFLEX02'
      SWITCH: ENABLE
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2GBFLEX02'
      SWITCH: ENABLE
    set_offloadinf_list:
    - OFFLOADTMR: 4
      FIRSTTM: 54
      NONRAI: '12300613333'
      POOLID: 0
      NULLNRIV: 0
    add_poolla_list:
    - LAC: '0001'
    add_poolla_list_3:
    - BGNTAI: '123033101'
      ENDTAI: '123033105'
      LAC: '0001'
    add_poolnri_list_2:
    - POOLID: 0
      NRIV: 3
      IPTYPE: IPV4
      IPV4: '192.168.151.3'
      SGSNN: 'SGSN 3'
      ALTERNATIVE: ''
      IPV6: ''
    mod_rnc_list:
    - RNCX: '1'
      IU\_FLEX: YES
    mod_nse_list:
    - NSEI: '1'
      GB\_FLEX: YES
    mod_gbnsecfgpara_list:
    - PARAINDEX: '1'
      GB\_FLEX: YES
    add_iupaging_list:
    - LAI: '123000011'
      RAC: '01'
      RNCINDEX: 1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 路由准备和配置同步阶段。

#### 1.1 申请并加载具有SGSN Iu-flex（LKV2IUFLEX02）和SGSN Pool用户迁移（LKV2SGSNMG02）功能的License。

#### 1.2 链路准备阶段。

#### 准备Iu接口和Gb接口的路由配置脚本。

#### 1.3 各SGSN配置参数同步。

### 2 Pool参数配置阶段。

### 配置新建SGSN3的Pool参数

#### 2.1 设置SGSN3的Pool ID和NRI长度。

```jinja2
{%- for item in add_pool_list -%}
    ADD POOL:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRILENGTH={{item.NRILENGTH}},
    ;
{%- endfor -%}
```

#### 目前NRI长度等于7bit仅允许在中国部署。在其他国家部署时，NRI长度不能超过5bit。

#### 2.2 配置本局NRI信息，SGSN3在P-TMSI分配时将填写此处设定的NRI值。

```jinja2
{%- for item in add_localnri_list -%}
    ADD LOCALNRI:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRIVBGN={{item.NRIVBGN}},
    NRINUM={{item.NRINUM}},
    ;
{%- endfor -%}
```

#### 2.3 设置SGSN3侧CN ID。

```jinja2
{%- for item in set_sys_list -%}
    SET SYS:
    {#- --- 可选参数 --- -#}
    {%- if item.CNID is not none -%}
        CNID={{item.CNID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 在SGSN3配置原Pool区内的SGSN与NRI的对应关系。一般情况下，建议在DNS Server中配置，如果运营商采用POOLNRI配置，则命令如下：

##### 2.4.1 //设置SGSN1的NRI信息

```jinja2
{%- for item in add_poolnri_list -%}
    ADD POOLNRI:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRIV={{item.NRIV}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SGSNN is not none -%}
        SGSNN="{{item.SGSNN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4/IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE in ['IPV4', 'IPV4V6'] -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4V6' -%}
        ALTERNATIVE="{{item.ALTERNATIVE}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.5 在SGSN3上配置Pool区内其他SGSN的NONRAI信息。一般情况下，建议在DNS Server中配置，如果运营商采用NONRAI配置，则命令如下：

```jinja2
{%- for item in add_nonrai_list -%}
    ADD NONRAI:
    {#- --- 必选参数 --- -#}
    NONRAI="{{item.NONRAI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPTYPE is not none -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {%- if item.SGSNN is not none -%}
        SGSNN="{{item.SGSNN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4/IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE in ['IPV4', 'IPV4V6'] -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4V6' -%}
        ALTERNATIVE="{{item.ALTERNATIVE}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.6 打开SGSN3兼容性配置中的Flex开关。

#### Iu：

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### Gb：

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 2.7 在SGSN3配置迁移相关参数。

```jinja2
{%- for item in set_offloadinf_list -%}
    SET OFFLOADINF:
    {#- --- 可选参数 --- -#}
    {%- if item.OFFLOADTMR is not none -%}
        OFFLOADTMR={{item.OFFLOADTMR}},
    {%- endif -%}
    {%- if item.FIRSTTM is not none -%}
        FIRSTTM={{item.FIRSTTM}},
    {%- endif -%}
    {%- if item.NONRAI is not none -%}
        NONRAI="{{item.NONRAI}}",
    {%- endif -%}
    {%- if item.POOLID is not none -%}
        POOLID={{item.POOLID}},
    {%- endif -%}
    {%- if item.NULLNRIV is not none -%}
        NULLNRIV={{item.NULLNRIV}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.8 可选：如果没有规划POOLLA，跳过此步。如果规划了POOLLA，即MME是使用UNC作为融合节点同时支持SGSN POOL功能和MME POOL功能，进行如下操作。

##### 2.8.1 没有规划TA和LA对应关系

```jinja2
{%- if is_optional_poolla_config and is_scenario_no_ta_la_mapping -%}
    {%- for item in add_poolla_list -%}
        ADD POOLLA:
        {#- --- 必选参数 --- -#}
        LAC="{{item.LAC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.8.2 规划了TA和LA的对应关系

```jinja2
{%- if is_optional_poolla_config and is_scenario_ta_la_mapping -%}
    {%- for item in add_poolla_list_3 -%}
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

#### 2.9 在Pool中原有SGSN上配置新建SGSN3相关PoolNRI记录和NonRAI记录。一般情况下，建议在DNS Server中配置，如果运营商采用POOLNRI配置，则命令如下：

```jinja2
{%- for item in add_poolnri_list_2 -%}
    ADD POOLNRI:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRIV={{item.NRIV}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SGSNN is not none -%}
        SGSNN="{{item.SGSNN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4/IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE in ['IPV4', 'IPV4V6'] -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4V6' -%}
        ALTERNATIVE="{{item.ALTERNATIVE}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.10 Pool参数配置完成后，需要进行数据配置一致性检查。

#### **表1** 预配置数据阶段Checklist

#### | 数据配置的一致性检查 | 要求结果 |

#### | --- | --- |

#### | Pool ID | 一致 |

#### | NRI长度 | 一致 |

#### | Local NRI | 不重复，与规划数据一致 |

#### | CN ID | 不重复，与规划数据一致 |

#### | Pool NRI | SGSN3配置了Pool内其他SGSN的NRI和IP地址的对应关系，且IP地址配置一致。 |

#### | POOLLA | 一致 |

#### | 建立待割接的第一个RNC的所有RAI的性能测量任务 | 已经建立 |

### 3 链路配置阶段。

### 进行链路配置，对于Gb接口保证NS层配通；对于Iu接口保证SCCP配通；但是RAN侧不向新建SGSN分发用户。

### 4 割接阶段。

### 割接阶段就是将RAN逐个连接到新建的SGSN。

#### 4.1 根据之前准备的脚本进行链路配置，将Gb接口和Iu接口配通。

#### 4.2 在待割接的RAN上配置RAN侧Pool参数。

#### 在待割接的RAN上配置新建SGSN的CN ID、NRI值和负荷权重。

#### 4.3 在新建SGSN上配置待割接的RAN的相关参数。

##### 4.3.1 在新建SGSN3配置待割接的RAN的NSE或RNC记录，打开Flex开关。

##### Iu-Flex：**MOD RNC**: RNCX=1, IU\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_rnc_list的变量区（command: MOD RNC） -#}
<!-- MISSING_MACRO: command=MOD RNC list_name=mod_rnc_list step_id=4.3.1 -->
```

##### Gb-Flex：

###### 4.3.1.1 Gb接口静态配置：**MOD NSE**: NSEI=1, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_nse_list的变量区（command: MOD NSE） -#}
<!-- MISSING_MACRO: command=MOD NSE list_name=mod_nse_list step_id=4.3.1.1 -->
```

###### 4.3.1.2 Gb接口动态自动配置：**MOD GBNSECFGPARA**: PARAINDEX=1, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_gbnsecfgpara_list的变量区（command: MOD GBNSECFGPARA） -#}
<!-- MISSING_MACRO: command=MOD GBNSECFGPARA list_name=mod_gbnsecfgpara_list step_id=4.3.1.2 -->
```

##### 4.3.2 在新建SGSN3配置IuPaging表，以及基于规划扩展DNS中的RAI记录。

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

#### 4.4 进行业务拨测。

#### 详细请参见SGSN Pool改造配置举例中“业务拨测”步骤。

#### 4.5 重复上述步骤，以相同的方式割接剩余的RAN。

