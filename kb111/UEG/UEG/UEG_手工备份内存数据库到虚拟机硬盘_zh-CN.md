---
id: ''
name: 手工备份内存数据库到虚拟机硬盘
ne_type: UEG
type: feature
description: 重大操作前（主要包括扩容虚拟机、业务改造等）为了系统的安全性需要手工对内存数据库进行备份，以保证在操作过程中出现异常时可以快速使系统恢复到操作前的运行状态。此时可以手工备份内存数据库到DRU/DSU节点所在Pod对应的虚拟机硬盘中。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG USCDB数据备份与恢复（风筝L）","备份与恢复用户手册","备份与恢复原理及基本操作","内存数据库备份与恢复","基本操作","手工备份和手动恢复","手工备份内存数据库到虚拟机硬盘"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
重大操作前（主要包括扩容虚拟机、业务改造等）为了系统的安全性需要手工对内存数据库进行备份，以保证在操作过程中出现异常时可以快速使系统恢复到操作前的运行状态。此时可以手工备份内存数据库到DRU/DSU节点所在Pod对应的虚拟机硬盘中。

## 必备事项
前提条件

* 已经通过“CSP MML命令”界面执行**DSP POD**命令查询USRSU虚拟机的“Pod状态”为“Running”。
* 已经通过“USCDB MML命令”界面执行**DSP NODE**命令查询DRU/DSU节点的“节点状态”为“Master”或“Slave”，“备份状态”为“未备份”。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    bkp_node_list:
      type: items
      properties:
        CID:
          name: 'Cluster标识'
          type: integer
          minimum: 0
          maximum: 4096
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NID:
          name: '节点标识'
          type: integer
          minimum: 0
          maximum: 32768
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BKPTYPE:
          name: '备份类型'
          type: string
          enum:
          - NORMAL
          - FORCED
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    bkp_node_list:
    - CID: Cluster标识
      NID: 节点标识
      BKPTYPE: FORCED
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

### 2 执行**LST NODE**命令，查询需要备份数据的节点的“Cluster标识”和“节点标识”。

### 3 根据2中查询出来的“Cluster标识”和“节点标识”，执行**BKP NODE**命令备份每个DRU/DSU节点的数据。

### 参数“备份类型”选择“NORMAL”时只能备份Slave节点；选择“FORCED”时可以备份Master节点或Slave节点。重大操作前需要对全部节点进行备份时该参数选择“FORCED”。

```jinja2
{%- for item in bkp_node_list -%}
    BKP NODE:
    {#- --- 必选参数 --- -#}
    CID={{item.CID}},
    NID={{item.NID}},
    BKPTYPE={{item.BKPTYPE}},
    ;
{%- endfor -%}
```

### 重大操作前要对全部DRU/DSU节点的数据进行备份，针对每个节点都需要执行一次备份命令。

### 每个节点备份的平均时间大约为1分钟～2分钟。使用命令脚本文件批量执行每个节点的备份命令时，根据一对配置相同Cluster USRSU Pod中的Cluster数量进行计算总备份时长，以最多Cluster数量的Pod为准。例如系统中有两对USRSU，一对的Cluster数为6个，另外一对的Cluster数为8个，则备份总时长大约为8\*1分钟～8\*2分钟。

### 4 待接近备份完成的时间时，执行**DSP NODE**命令查看节点的备份状态。

### 查看各节点的“备份状态”信息：

### 如果为“备份中”表示节点还没有备份完。

### 如果为“未备份”表示节点都已经备份完。

