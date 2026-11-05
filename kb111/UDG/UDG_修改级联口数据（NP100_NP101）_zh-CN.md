---
id: ''
name: 修改级联口数据（NP100/NP101）
ne_type: UDG
type: feature
description: 带NP卡的专有硬件之间级联组网时，若VNF实例化后级联口数据与规划不一致，可参考本页面进行修改级联口数据。
risk_level: ''
doc_source: ["网络部署","初始配置","UDG初始配置与调测","组网路由配置","配置VNF侧IP路由数据（NP卡直连PE）","修改级联口数据（NP100/NP101）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
带NP卡的专有硬件之间级联组网时，若VNF实例化后级联口数据与规划不一致，可参考本页面进行修改级联口数据。

## 必备事项
前提条件

* 已经确认现网规划的级联口与VNF实例化后的级联口不同。
* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_npdirectconnectport_list:
      type: items
      properties:
        SUBRACK:
          name: '框号'
          type: string
          enum:
          - Subrack_0
          - Subrack_1
          - Subrack_2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLOTID:
          name: '槽位号'
          type: string
          enum:
          - Slot_1
          - Slot_2
          - Slot_3
          - Slot_4
          - Slot_5
          - Slot_6
          - Slot_7
          - Slot_8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTID:
          name: '端口号'
          type: string
          enum:
          - P1
          - P2
          - P3
          - P4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_npdirectconnectport_list_6:
      type: items
      properties:
        SUBRACK:
          name: '框号'
          type: string
          enum:
          - Subrack_0
          - Subrack_1
          - Subrack_2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLOTID:
          name: '槽位号'
          type: string
          enum:
          - Slot_1
          - Slot_2
          - Slot_3
          - Slot_4
          - Slot_5
          - Slot_6
          - Slot_7
          - Slot_8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTID:
          name: '端口号'
          type: string
          enum:
          - P1
          - P2
          - P3
          - P4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_npdirectconnectport_list:
    - SUBRACK: Subrack_0
      SLOTID: Slot_1
      PORTID: P3
    add_npdirectconnectport_list_6:
    - SUBRACK: Subrack_1
      SLOTID: Slot_1
      PORTID: P3
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 执行**ADD NPDIRECTCONNECTPORT**命令，使能级联口。

### 框0的Slot1～Slot6上的P3口作为级联口时，需要执行如下配置：

```jinja2
{%- for item in add_npdirectconnectport_list -%}
    ADD NPDIRECTCONNECTPORT:
    {#- --- 必选参数 --- -#}
    SUBRACK={{item.SUBRACK}},
    SLOTID={{item.SLOTID}},
    PORTID={{item.PORTID}},
    ;
{%- endfor -%}
```

### 框1的Slot1～Slot6上的P3口作为级联口时，需要执行如下配置：

```jinja2
{%- for item in add_npdirectconnectport_list_6 -%}
    ADD NPDIRECTCONNECTPORT:
    {#- --- 必选参数 --- -#}
    SUBRACK={{item.SUBRACK}},
    SLOTID={{item.SLOTID}},
    PORTID={{item.PORTID}},
    ;
{%- endfor -%}
```

### VNF实例化后执行步骤 1，则以步骤 1配置的级联口为准。

### 先连线再使能级联口场景，使能后会产生外联口DOWN告警，该告警不影响业务。确认由此原因产生的ALM-89005 NP端口状态为Down告警，可手动清除。

