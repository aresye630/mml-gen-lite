---
id: ''
name: 接入网侧组Pool过程
ne_type: UNC
type: feature
description: 本配置指导描述新建SGSN Pool时接入网侧组Pool的配置过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","SGSN容灾方案","新建部署","激活业务","典型场景：SGSN Pool新建","全网新建","接入网侧组Pool过程"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本配置指导描述新建SGSN Pool时接入网侧组Pool的配置过程。

## 必备事项
前提条件

* 数据规划已完成。
* 网元基础数据配置完成。
* Pool功能预设置完成。
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
    add_resrec_list_2:
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
    add_resrec_list_3:
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
    mod_rnc_list:
    - RNCX: RNC索引
      IU\_FLEX: RNC是否支持IU-FLEX
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
    mod_nse_list:
    - NSEI: '0'
      GB\_FLEX: YES
    mod_gbnsecfgpara_list:
    - PARAINDEX: '1'
      GB\_FLEX: YES
    add_resrec_list_2:
    - TYPE: A
      NAME: MNC000.MCC123.gprs
      DOMAIN: RAC0001.LAC0011
      IP: 10.168.155.2
    add_resrec_list_3:
    - TYPE: A
      NAME: MNC000.MCC123.gprs
      DOMAIN: RAC0001.LAC0011
      IP: 10.168.153.1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 接入网侧为RNC（3G）。

#### 1.1 配置SGSN1数据（3G）。

##### 1.1.1 将一个RNC1加入到SGSN1。

##### 具体操作过程参考《UNC初始配置与调测》中“到RNC的数据配置”。

##### 1.1.2 修改RNC1的Iu-flex属性。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_rnc_list的变量区（command: MOD RNC） -#}
<!-- MISSING_MACRO: command=MOD RNC list_name=mod_rnc_list step_id=1.1.2 -->
```

##### 参数“IUFLEX（RNC是否支持IU-FLEX）”选择“YES”。

##### 1.1.3 将其他RNC加入到SGSN1。

#### 1.2 配置其他SGSN的数据。

#### 配置其他SGSN数据的步骤请参见本节“配置SGSN1数据（3G）”。

#### 1.3 DNS Server上Default SGSN配置。

#### Default SGSN需要基于路由区进行规划，且保证分摊均匀。其中的路由区包括待割接RNC下所有POOL内的RAI。

#### 考虑容灾备份，最好对同一个路由区至少有两个SGSN互为备份。本例中，对于域名“RAC0001.LAC0011.MNC000.MCC123.GPRS.”，将SGSN1和SGSN2配置为Default SGSN，即在DNS上将BSC1的路由区域名解析成为SGSN1和SGSN2的GTPC地址。并通知与该BSC1覆盖范围相邻的非本SGSN Pool的其他SGSN做相应的数据修改。

#### 通常地，本网内有一个本地DNS Server，上一级DNS Server不在本地。这种情况下，当核心网内多个SGSN改造成POOL后，该DNS Server可以视作POOL外的DNS Server，也可以视作POOL内的DNS Server，它除了保留原有的域名解析数据、解析功能外，还需要为SGSN POOL增加Default SGSN的数据配置。 以华为DNS Server为例：

##### 1.3.1 在华为DNS Server的LMT上配置，主备均需要：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_resrec_list的变量区（command: ADD RESREC） -#}
<!-- MISSING_MACRO: command=ADD RESREC list_name=add_resrec_list step_id=1.3.1 -->
```

##### 1.3.2 在不带LMT的DNS Server上，在named.ra文件中增加A记录（详细参见《DNS产品文档》）：

##### RAC0001.LAC0011                       IN       A        10.166.155.2

#### 以下为DNS Server上原有配置，不需新增：

##### 1.3.3 在华为DNS Server上：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_resrec_list_1的变量区（command: ADD RESREC） -#}
<!-- MISSING_MACRO: command=ADD RESREC list_name=add_resrec_list_1 step_id=1.3.3 -->
```

##### 1.3.4 在不带LMT的DNS Server上：

##### RAC0001.LAC0011                       IN       A        10.166.153.1

##### 1.3.5 如果本网的运营商除了本地DNS Server外，还有上一级的DNS Server也在本地，在改造成SGSN POOL后，POOL内有一个DNS Server A，POOL外还有一个上级的DNS Server B，则，Default SGSN的数据配置就需要在DNS Server B上完成。这种情况比较少见。

##### 1.3.6 如果POOL内某个SGSN下扩容BSC/RNC网元，在POOL内的DNS Server上，需要在扩容操作阶段，新增加该BSC/RNC的全部RAI的相关A记录（对应哪几个SGSN作为DefaultSGSN，需在扩容前完成规划），并且增加RNCID的相关A记录。

##### 1.3.7 如果修改了DNS Server的数据，需要清除各SGSN的cash数据。

#### 1.4 在RNC上需要配置的数据。

#### RNC上的具体数据配置，根据网络中实际应用的不同设备厂商的RNC，使用相应设备厂商RNC的配置命令，请参考相应RNC的数据配置手册。

#### 此处配置过程仅供参考。配置华为RNC的步骤如下：

##### 1.4.1 启动Iu-flex开关，配置NRI长度、Null-NRI。

##### 1.4.2 增加相关CN节点，包括CN运营商索引、CN-ID、CN节点域ID、Off-load状态、CN节点容量等。

##### 1.4.3 增加相关CN节点与NRI之间的映射关系。

##### 1.4.4 配置RNC到SGSN的相关信令和链路数据。

### 2 接入网侧为BSC（2G）。

#### 2.1 配置SGSN1数据（2G）。

##### 2.1.1 将一个BSC1加入到SGSN1。

##### 具体操作过程参考《UNC初始配置与调测》中“到PCU的数据配置”。

##### 2.1.2 修改BSC1的Gb-flex属性。

###### 2.1.2.1 Gb接口静态配置：**MOD NSE**: NSEI=0, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_nse_list的变量区（command: MOD NSE） -#}
<!-- MISSING_MACRO: command=MOD NSE list_name=mod_nse_list step_id=2.1.2.1 -->
```

###### 2.1.2.2 Gb接口动态自动配置：**MOD GBNSECFGPARA**: PARAINDEX=1, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_gbnsecfgpara_list的变量区（command: MOD GBNSECFGPARA） -#}
<!-- MISSING_MACRO: command=MOD GBNSECFGPARA list_name=mod_gbnsecfgpara_list step_id=2.1.2.2 -->
```

##### 2.1.3 将其他BSC加入到SGSN1。

#### 2.2 配置其他SGSN的数据。

#### 配置其他SGSN数据的步骤请参见本节“配置SGSN1数据（2G）”的描述。

#### 2.3 DNS Server上Default SGSN配置。

#### Default SGSN需要基于路由区进行规划，且保证分摊均匀。其中的路由区包括待割接RNC下所有POOL内的RAI。

#### 考虑容灾备份，最好对同一个路由区至少有两个SGSN互为备份。本例中，对于域名“RAC0001.LAC0011.MNC000.MCC123.GPRS.”，将SGSN1和SGSN2配置为Default SGSN，即在DNS上将BSC1的路由区域名解析成为SGSN1和SGSN2的GTPC地址。并通知与该BSC1覆盖范围相邻的非本SGSN Pool的其他SGSN做相应的数据修改。

#### 通常地，本网内有一个本地DNS Server，上一级DNS Server不在本地。这种情况下，当核心网内多个SGSN改造成POOL后，该DNS Server可以视作POOL外的DNS Server，也可以视作POOL内的DNS Server，它除了保留原有的域名解析数据、解析功能外，还需要为SGSN POOL增加Default SGSN的数据配置。 以华为DNS Server为例：

##### 2.3.1 方式一：在华为DNS Server的LMT上配置，主备均需要：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_resrec_list_2的变量区（command: ADD RESREC） -#}
<!-- MISSING_MACRO: command=ADD RESREC list_name=add_resrec_list_2 step_id=2.3.1 -->
```

##### 2.3.2 方式二：在不带LMT的DNS Server上，在named.ra文件中增加A记录（详细参见《DNS产品文档》）：

##### RAC0001.LAC0011                       IN       A        10.168.155.2

#### 以下为DNS Server上原有配置，不需新增：

##### 2.3.3 方式一：在华为DNS Server上：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_resrec_list_3的变量区（command: ADD RESREC） -#}
<!-- MISSING_MACRO: command=ADD RESREC list_name=add_resrec_list_3 step_id=2.3.3 -->
```

##### 2.3.4 方式二：在不带LMT的DNS Server上：

##### RAC0001.LAC0011                       IN       A        10.168.153.1

##### 2.3.5 如果本网的运营商除了本地DNS Server外，还有上一级的DNS Server也在本地，在改造成SGSN POOL后，POOL内有一个DNS Server A，POOL外还有一个上级的DNS Server B，则，Default SGSN的数据配置就需要在DNS Server B上完成。这种情况比较少见。

##### 2.3.6 如果POOL内某个SGSN下割接BSC/RNC网元，在POOL内的DNS Server上，需要在扩容操作阶段，新增加该BSC/RNC的全部RAI的相关A记录（对应哪几个SGSN作为DefaultSGSN，需在扩容前完成规划），并且增加RNCID的相关A记录。

##### 2.3.7 如果修改了DNS Server的数据，需要清除各SGSN的cash数据。

#### 2.4 在BSC上需要配置的数据。

#### BSC上的具体数据配置，根据网络中实际应用的不同设备厂商的BSC，使用相应设备厂商BSC的配置命令，请参考相应BSC的数据配置手册。此处配置过程仅供参考。

#### 配置华为BSC的步骤如下：

##### 2.4.1 启动SGSN Pool功能，配置NRI长度。

##### 2.4.2 增加Null-NRI和NSE映射关系。

##### 2.4.3 增加NRI和NSE映射关系。

##### 2.4.4 配置NSE的管理状态。

#### 2.5 检查数据一致性

#### 执行**LST GBPAGING**检查2G路由区是否正确。

#### SGSN覆盖的2G路由区是否包含了Pool区内所有接入的BSC所覆盖的路由区。

#### 只有确保BSC侧与SGSN之间链路连通后才执行该脚本。如果SGSN包含的2G路由区少于Pool区内所有接入的BSC覆盖的路由区则需要检查SGSN与对应BSC直接链路是否正常。

