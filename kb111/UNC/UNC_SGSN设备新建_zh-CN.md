---
id: ''
name: SGSN设备新建
ne_type: UNC
type: feature
description: 本操作指导适用于所有SGSN为新建设备，RAN侧为现网设备的搬迁场景。  如图1所示为新建SGSN设备的组Pool实例。  **图1** SGSN新建组网
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","SGSN容灾方案","新建部署","激活业务","典型场景：SGSN Pool新建","SGSN设备新建"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导适用于所有SGSN为新建设备，RAN侧为现网设备的搬迁场景。如图1所示为新建SGSN设备的组Pool实例。**图1** SGSN新建组网

## 必备事项
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
    add_resrec_list:
      type: items
      properties:
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NAME:
          name: 'NAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOMAIN:
          name: 'DOMAIN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IP:
          name: 'IP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_resrec_list_1:
      type: items
      properties:
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NAME:
          name: 'NAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOMAIN:
          name: 'DOMAIN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IP:
          name: 'IP'
          type: string
          required: false
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
      NRIVBGN: 1
      NRINUM: 1
    set_sys_list:
    - CNID: 1
    add_poolnri_list:
    - POOLID: 0
      NRIV: 2
      IPTYPE: IPV4
      IPV4: '10.168.155.2'
      SGSNN: 'SGSN2'
      ALTERNATIVE: ''
      IPV6: ''
    add_nonrai_list:
    - NONRAI: '12300615555'
      IPTYPE: IPV4
      IPV4: '10.168.155.2'
      SGSNN: 'SGSN2'
      ALTERNATIVE: ''
      IPV6: ''
    - NONRAI: '12300616666'
      IPTYPE: IPV4
      IPV4: '10.168.151.3'
      SGSNN: 'SGSN3'
      ALTERNATIVE: ''
      IPV6: ''
    mod_rnc_list:
    - RNCX: '0'
      IU\_FLEX: YES
    mod_nse_list:
    - NSEI: '0'
      GB\_FLEX: YES
    mod_gbnsecfgpara_list:
    - PARAINDEX: '1'
      GB\_FLEX: YES
    set_licenseswitch_list:
    - LICITEM: 'LKV2IUFLEX02'
      SWITCH: ENABLE
    set_offloadinf_list:
    - OFFLOADTMR: 4
      FIRSTTM: 54
      NONRAI: '12300611111'
      POOLID: 0
      NULLNRIV: 0
    add_poolla_list:
    - LAC: '1011'
    add_poolla_list_3:
    - BGNTAI: '123033101'
      ENDTAI: '123033105'
      LAC: '1011'
    add_iupaging_list:
    - LAI: '123000011'
      RAC: '01'
      RNCINDEX: 1
    add_resrec_list:
    - TYPE: A
      NAME: MNC000.MCC123.gprs
      DOMAIN: RAC0001.LAC0011
      IP: 10.166.155.2
    add_resrec_list_1:
    - TYPE: A
      NAME: MNC000.MCC123.gprs
      DOMAIN: RAC0001.LAC0011
      IP: 10.166.153.1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 链路准备阶段。

#### 1.1 为各SGSN上申请并加载具有Iu-flex（LKV2IUFLEX02）、Gb-flex（LKV2GBFLEX02）和SGSN Pool用户迁移（LKV2SGSNMG02）功能的License控制项。

#### 1.2 准备各SGSN上Iu接口和Gb接口的路由配置信息。

### 2 设置SGSN1的Pool ID和NRI长度。

```jinja2
{%- for item in add_pool_list -%}
    ADD POOL:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRILENGTH={{item.NRILENGTH}},
    ;
{%- endfor -%}
```

### 目前NRI长度等于7bit仅在中国部署。在海外部署时，NRI长度采用5bit。

### 3 配置SGSN1的本局NRI，SGSN1在P-TMSI分配时将使用此处设定的NRI值。

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

### 4 设置SGSN1的CN ID。

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

### 5 配置SGSN1的Pool参数。

#### 5.1 在SGSN1上配置Pool区内其他SGSN的NRI信息。一般情况下，建议在DNS Server中配置，如果运营商采用POOLNRI配置，则命令如下：

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

#### 5.2 设置Pool区内其它SGSN的非广播路由区信息。一般情况下，建议在DNS Server中配置，如果运营商采用NONRAI配置，则命令如下：

##### 5.2.1 //设置SGSN2的非广播路由区信息

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

##### 5.2.2 Pool区内其它SGSN的非广播路由区信息，主要是在迁移模式下的Attach和Inter Rau流程时，根据非广播路由区与IP地址的对应关系获取对端SGSN的地址信息。

##### 如果SGSN存在多个GTPC地址时，选择其中一个来配置到其他的SGSN上。如果为了负载均衡，可以考虑在不同的SGSN配置本SGSN GTPC地址不同。

#### 5.3 在SGSN1上打开需要加入Pool的RNC/BSC的Flex开关。

#### Iu-Flex：**MOD RNC**: RNCX=0, IU\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_rnc_list的变量区（command: MOD RNC） -#}
<!-- MISSING_MACRO: command=MOD RNC list_name=mod_rnc_list step_id=5.3 -->
```

#### Gb-Flex：

##### 5.3.1 Gb接口静态配置：**MOD NSE**: NSEI=0, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_nse_list的变量区（command: MOD NSE） -#}
<!-- MISSING_MACRO: command=MOD NSE list_name=mod_nse_list step_id=5.3.1 -->
```

##### 5.3.2 Gb接口动态自动配置：**MOD GBNSECFGPARA**: PARAINDEX=1, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_gbnsecfgpara_list的变量区（command: MOD GBNSECFGPARA） -#}
<!-- MISSING_MACRO: command=MOD GBNSECFGPARA list_name=mod_gbnsecfgpara_list step_id=5.3.2 -->
```

#### 5.4 打开SGSN1 License配置中的Flex开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 5.5 配置迁移相关参数。

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

#### 5.6 可选：如果没有规划POOLLA，跳过此步。

#### 如果规划了POOLLA，即MME是使用UNC作为融合节点同时支持SGSN POOL功能和MME POOL功能，进行如下操作。

##### 5.6.1 没有规划TA和LA对应关系

```jinja2
{%- if is_optional_pool_la and is_scenario_no_ta_la_mapping -%}
    {%- for item in add_poolla_list -%}
        ADD POOLLA:
        {#- --- 必选参数 --- -#}
        LAC="{{item.LAC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 5.6.2 规划了TA和LA的对应关系

```jinja2
{%- if is_optional_pool_la and is_scenario_ta_la_mapping -%}
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

### 6 重复上述步骤2~6，配置其他新建SGSN的Pool参数。

### 7 各SGSN配置完成后，进行数据配置一致性检查。

### **表1** 数据配置一致性检查

### | 数据配置的一致性检查 | 要求结果 |

### | --- | --- |

### | Pool ID | 一致 |

### | NRI长度 | 一致 |

### | Local NRI | 不重复，与规划数据一致 |

### | CN ID | 不重复，与规划数据一致 |

### | Pool NRI | 所有SGSN均配置了Pool内其他SGSN的NRI和IP地址的对应关系，且IP地址配置一致。 |

### | Flex开关（LICENSESWITCH） | Iu-flex开启 |

### | 鉴权开关 | 与规划一致 |

### | 建立待割接的第一个RNC的所有RAI的性能测量任务 | 已经建立 |

### 8 链路配置阶段。

### 9 割接阶段。

### 将RAN从旧SGSN上割接到新的SGSN上。

#### 9.1 根据之前准备的脚本进行链路配置，将Gb接口和Iu接口配通。

#### 9.2 配置割接新侧SGSN。

##### 9.2.1 配置新割接的RAN的NSE或RNC记录。

##### 本步骤具体配置请参考《UNC初始配置与调测》。

##### 9.2.2 在新建SGSN上配置IuPaging表，以及基于规划扩展DNS中的RAI记录。

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

#### 9.3 配置RAN侧Pool参数。

##### 9.3.1 **可选：**如果新建RAN侧为BSC，则需要配置NSE记录。

##### 9.3.2 在RAN上配置SGSN的CN ID、NRI值、负荷权重。

##### 9.3.3 在RAN上打开Flex功能开关。

#### 9.4 DNS Server上Default SGSN配置。

#### Default SGSN需要基于路由区进行规划，且保证分摊均匀。其中的路由区包括待割接RNC下所有POOL内的RAI。

#### 考虑容灾备份，最好对同一个路由区至少有两个SGSN互为备份。本例中，对于域名“RAC0001.LAC0011.MNC000.MCC123.GPRS.”，将SGSN1和SGSN2配置为Default SGSN，即在DNS上将BSC1的路由区域名解析成为SGSN1和SGSN2的GTPC地址。并通知与该BSC1覆盖范围相邻的非本SGSN Pool的其他SGSN做相应的数据修改。

#### 通常地，本网内有一个本地DNS Server，上一级DNS Server不在本地。这种情况下，当核心网内多个SGSN改造成POOL后，该DNS Server可以视作POOL外的DNS Server，也可以视作POOL内的DNS Server，它除了保留原有的域名解析数据、解析功能外，还需要为SGSN POOL增加Default SGSN的数据配置。 以华为DNS Server为例：

##### 9.4.1 方式一：在华为DNS Server的LMT上配置，主备均需要：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_resrec_list的变量区（command: ADD RESREC） -#}
<!-- MISSING_MACRO: command=ADD RESREC list_name=add_resrec_list step_id=9.4.1 -->
```

##### 9.4.2 方式二：在不带LMT的DNS Server上，在named.ra文件中增加A记录（详细参见《DNS产品文档》）：

##### RAC0001.LAC0011                       IN       A        10.166.155.2

#### 以下为DNS Server上原有配置，不需新增：

##### 9.4.3 方式一：在华为DNS Server上：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_resrec_list_1的变量区（command: ADD RESREC） -#}
<!-- MISSING_MACRO: command=ADD RESREC list_name=add_resrec_list_1 step_id=9.4.3 -->
```

##### 9.4.4 方式二：在不带LMT的DNS Server上：

##### RAC0001.LAC0011                       IN       A        10.166.153.1

##### 9.4.5 如果本网的运营商除了本地DNS Server外，还有上一级的DNS Server也在本地，在改造成SGSN POOL后，POOL内有一个DNS Server A，POOL外还有一个上级的DNS Server B，则，Default SGSN的数据配置就需要在DNS Server B上完成。这种情况比较少见。

##### 9.4.6 如果POOL内某个SGSN下扩容BSC/RNC网元，在POOL内的DNS Server上，需要在扩容操作阶段，新增加该BSC/RNC的全部RAI的相关A记录（对应哪几个SGSN作为DefaultSGSN，需在扩容前完成规划），并且增加RNCID的相关A记录。

##### 9.4.7 如果修改了DNS Server的数据，需要清除各SGSN的cash记录。

#### 9.5 配置旧侧SGSN。

#### 断开旧SGSN上与待割接RAN的连接，进行业务拨测。

#### 删除旧侧SGSN的配置：

##### 9.5.1 删除NSE记录或RNC相关链路配置。

##### 9.5.2 删除IuPaging中对应的RAI记录，删除DNS中RAI对应的旧侧SGSN IP记录。

#### 9.6 重复步骤3，步骤4，以相同的方式割接剩余的RAN。

### 10 **可选：**执行用户迁移保证负荷均衡。

### 当出现负荷不均衡告警时可执行本步骤，具体请参见《U2020 MBB网络管理系统 虚拟化产品文档》中的“操作与维护 > 核心网管理 > MME Pool管理 > MME Pool日常维护 > 均衡MME Pool负荷 > 手工迁移MME Pool用户”章节。

