---
id: ''
name: 配置容灾模式
ne_type: UEG
type: feature
description: 为避免单点故障，园区需部署两套UEG实现容灾。  两套UEG采用负荷分担容灾时，需要参考本页面进行配置。  本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG初始配置（风筝M）","配置实例（虚机容器）","配置容灾模式"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG初始配置（风筝M）","配置实例（裸机容器）","配置容灾模式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为避免单点故障，园区需部署两套UEG实现容灾。两套UEG采用负荷分担容灾时，需要参考本页面进行配置。本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。

## 必备事项
前提条件

已完成各NF选择本UEG内NF的数据配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_drcouplingreset_list:
      type: items
      properties:
        COUPLINGRESET:
          name: '是否使能负荷分担容灾功能'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '两套UEG采用负荷分担容灾时设置为“YES”，其他情况下设置为“NO”。'
          data_source: '本端规划'
          pattern: ''
          default: NO
    set_drkeynf_list:
      type: items
      properties:
        MME:
          name: '是否监控MME服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: NO
        AMF:
          name: '是否监控AMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        HSS:
          name: '是否监控HSS服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        UDM:
          name: '是否监控UDM服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        SMF:
          name: '是否监控SMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        GWC:
          name: '是否监控GW-C服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        PCF:
          name: '是否监控PCF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        PCRF:
          name: '是否监控PCRF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        UPF:
          name: '是否监控UPF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        UDR:
          name: '是否监控UDR服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
  examples:
    set_drcouplingreset_list:
    - COUPLINGRESET: YES
    set_drkeynf_list:
    - MME: NO
      AMF: NO
      HSS: NO
      UDM: NO
      SMF: NO
      GWC: NO
      PCF: NO
      PCRF: NO
      UPF: YES
      UDR: NO
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 使能负荷分担容灾功能。

```jinja2
{%- for item in set_drcouplingreset_list -%}
    SET DRCOUPLINGRESET:
    {#- --- 可选参数 --- -#}
    {%- if item.COUPLINGRESET is not none -%}
        COUPLINGRESET={{item.COUPLINGRESET}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置监控的关键部件信息。

#### 3.1 UEG作为风筝M时，仅监控UPF。

#### 3.2 开启容灾功能的UEG出现设备异常，需要通过重新实例化操作进行恢复的场景：若MML文件中**SET DRKEYNF**命令的HSS、UDM、PCRF、PCF、UDR参数值存在“YES”，则在导入MML文件进行配置恢复前，需要先修改MML文件，将**SET DRKEYNF**命令的HSS、UDM、PCRF、PCF、UDR参数值“YES”修改为“NO”；待HSS、UDM、PCRF、PCF、UDR服务的配置恢复完成后，再按照修改前的**SET DRKEYNF**配置重新开启对这些服务的监控。

```jinja2
{%- for item in set_drkeynf_list -%}
    SET DRKEYNF:
    {#- --- 可选参数 --- -#}
    {%- if item.MME is not none -%}
        MME={{item.MME}},
    {%- endif -%}
    {%- if item.AMF is not none -%}
        AMF={{item.AMF}},
    {%- endif -%}
    {%- if item.HSS is not none -%}
        HSS={{item.HSS}},
    {%- endif -%}
    {%- if item.UDM is not none -%}
        UDM={{item.UDM}},
    {%- endif -%}
    {%- if item.SMF is not none -%}
        SMF={{item.SMF}},
    {%- endif -%}
    {%- if item.GWC is not none -%}
        GWC={{item.GWC}},
    {%- endif -%}
    {%- if item.PCF is not none -%}
        PCF={{item.PCF}},
    {%- endif -%}
    {%- if item.PCRF is not none -%}
        PCRF={{item.PCRF}},
    {%- endif -%}
    {%- if item.UPF is not none -%}
        UPF={{item.UPF}},
    {%- endif -%}
    {%- if item.UDR is not none -%}
        UDR={{item.UDR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

