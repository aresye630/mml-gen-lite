---
id: ''
name: 核心网侧组Pool过程
ne_type: UNC
type: feature
description: 本操作指导描述核心网组Pool配置过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","MME容灾方案","新建部署","全网新建Pool","激活业务","核心网侧组Pool过程"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导描述核心网组Pool配置过程。

```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
  examples:
    add_poolla_list:
    - LAC: '1011'
    add_poolla_list_3:
    - BGNTAI: '123033101'
      ENDTAI: '123033105'
      LAC: '1011'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置MME的域名解析。

### 为了保证其他MME能通过GUTI找到对应的MME，需要增加该MME的域名解析。

### 配置MME的域名解析有两种方式：

### 方式一：DNS配置方式。

### 方式二：Hostfile配置方式。

### 本例中，对于域名“MMEC8.MMEGI8001.MME.EPC.MNC003.MCC123.3GPPNETWORK.ORG”，将在DNS上配置成为MME1的GTPC地址。

### 2 **可选：**在使用UNC作为融合节点同时支持SGSN Pool功能和MME Pool功能的场景下，如果MME需要通过S1接口下发LTE GUMMEI和Mapped GUMMEI，需要进行如下操作。

#### 2.1 没有规划TA和LA对应关系。

```jinja2
{%- if is_optional_lte_gummei_and_mapped_gummei and is_scenario_no_ta_la_mapping -%}
    {%- for item in add_poolla_list -%}
        ADD POOLLA:
        {#- --- 必选参数 --- -#}
        LAC="{{item.LAC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 规划了TA和LA的对应关系。

```jinja2
{%- if is_optional_lte_gummei_and_mapped_gummei and is_scenario_ta_la_mapping -%}
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

### 3 重复步骤 1和步骤 2，配置其他MME的Pool参数，本例中需要配置MME2、MME3的数据。

### **表1** Pool参数配置阶段Checklist

### | 数据配置的一致性检查 | 要求结果 |

### | --- | --- |

### | MMEID | 一致 |

### | License开关 | 打开 |

### | 权重信息 | 一致 |

### | DNS Service MMEID域名解析 | 和规划一致 |

### | POOLLA | 和规划一致 |

### | 建立待割接的第一个eNodeB的所有TAI的性能测量任务（包括Attach，TAU，Service Request，Paging，Relocation基本流程） | 已经建立 |

