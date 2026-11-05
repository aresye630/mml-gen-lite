---
id: ''
name: 配置UDM-UIM与专网UPF的对接数据（DRA转接）
ne_type: UDG
type: feature
description: 本页面用于指导操作员配置UDM-UIM通过Diameter信令与专网UPF的对接数据，UDM-UIM与专网UPF以DRA转接方式对接。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置UDM-UIM（Non-SIM AAA）","配置UDM-UIM与专网UPF的对接数据（DRA转接）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本页面用于指导操作员配置UDM-UIM通过Diameter信令与专网UPF的对接数据，UDM-UIM与专网UPF以DRA转接方式对接。

## 必备事项
前提条件

* 操作人员具有管理员权限。
* CSP与服务器端通信正常。
* UDM-UIM与DRA侧均完成了软件安装和基础数据的配置。
* UDM-UIM与DRA的对接信令数据已经协商。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_dmle_list:
      type: items
      properties:
        EN:
          name: '实体名称'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        LOCTYPE:
          name: '本端设备类型'
          type: string
          required: false
          description: '当与UPF对接时，该参数配置为AAA。'
          data_source: ''
          pattern: ''
          default: ''
        DN:
          name: '域名'
          type: string
          required: false
          description: '与对端网元协商确定。'
          data_source: ''
          pattern: ''
          default: ''
        HN:
          name: '主机名'
          type: string
          required: false
          description: '与对端网元协商确定。'
          data_source: ''
          pattern: ''
          default: ''
    add_dmpe_list:
      type: items
      properties:
        EN:
          name: '实体名称'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        PEERTYPE:
          name: 'Diameter对端实体类型'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        HN:
          name: '主机名'
          type: string
          required: false
          description: '与对端网元协商确定。'
          data_source: ''
          pattern: ''
          default: ''
        PEPRI:
          name: 'Diameter对端实体优先级'
          type: string
          required: false
          description: '工程设计输出。  用于在配置数据库中定义一个对端设备的实体优先级。'
          data_source: ''
          pattern: ''
          default: ''
    add_dmrts_list:
      type: items
      properties:
        RTSNAME:
          name: '路由组名称'
          type: string
          required: false
          description: '工程设计输出，全局唯一。'
          data_source: ''
          pattern: ''
          default: ''
        RN:
          name: '目标域名'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        APPID:
          name: '应用类型'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        SMODE:
          name: '路由选择模式'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
    add_dmrt_list:
      type: items
      properties:
        RTNAME:
          name: '路由组名称'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        PEERNAME:
          name: '对端标识名称'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
    add_dmlks_list:
      type: items
      properties:
        LINKSNAM:
          name: '链路集名称'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        LOCALNAM:
          name: 'Diameter本端实体名称'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        PEERNAM:
          name: 'Diameter对端实体名称'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        LNKMOD:
          name: '链路选择模式'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
    add_dmlnk_list:
      type: items
      properties:
        LNKNAME:
          name: '链路名称'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        LINKSNAM:
          name: 'Diameter链路集名称'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        HSFMID:
          name: 'HSF模块号'
          type: string
          required: false
          description: 'FE的HSF模块号，通过**ADD MODULE**命令定义后，在此引用。可使用**LST MODULE**命令查询获取HSF模块号。'
          data_source: ''
          pattern: ''
          default: ''
        PTYPE:
          name: '传输协议类型'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        WMODE:
          name: '工作模式'
          type: string
          required: false
          description: '与对端网元协商确定。'
          data_source: ''
          pattern: ''
          default: ''
        IPNAM1:
          name: 'IP地址名称1'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        PIPVER:
          name: '对端IP地址版本'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        PIPV4:
          name: '对端IPV4地址'
          type: string
          required: false
          description: '与对端网元协商确定。'
          data_source: ''
          pattern: ''
          default: ''
        IPNAM2:
          name: 'IP地址名称2'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        SPIPVER:
          name: '对端备用IP地址版本'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        SPIPV4:
          name: '对端备用IPV4地址'
          type: string
          required: false
          description: '与对端网元协商确定。'
          data_source: ''
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: string
          required: false
          description: '与对端网元协商确定。'
          data_source: ''
          pattern: ''
          default: ''
        LINKPRI:
          name: 'Diameter对端链路优先级'
          type: string
          required: false
          description: '工程设计输出。  用于在配置Diameter对端使用的链路优先级。取值越小优先级越高。'
          data_source: ''
          pattern: ''
          default: ''
        CROSSPATHFLAG:
          name: '交叉路径是否可用'
          type: string
          required: false
          description: '工程设计输出。  用于在标识SCTP双归属链路中交叉链路是否可用。  参数为条件可选，只有参数“PTYPE”取值为“SCTP”时才配置。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_dmle_list:
    - EN: AAA
      LOCTYPE: AAA
      DN: huawei.com
      HN: UDM.huawei.com
    add_dmpe_list:
    - EN: DRA01
      PEERTYPE: OTHER
      HN: dra01.huawei.com
      PEPRI: '15'
    add_dmrts_list:
    - RTSNAME: DRA_RT01
      RN: huawei.com
      APPID: SWm
      SMODE: POLLING
    add_dmrt_list:
    - RTNAME: DRA_RT01
      PEERNAME: DRA01
    add_dmlks_list:
    - LINKSNAM: Diameter_aaa01
      LOCALNAM: AAA
      PEERNAM: DRA01
      LNKMOD: ACTIVE
    add_dmlnk_list:
    - LNKNAME: LINKDRA01_AAA001
      LINKSNAM: Diameter_aaa01
      HSFMID: '67'
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: HSFIP1
      PIPVER: IPV4
      PIPV4: 192.168.251.66
      IPNAM2: HSFIP2
      SPIPVER: IPV4
      SPIPV4: 192.168.252.66
      PPT: '5062'
      LINKPRI: '15'
      CROSSPATHFLAG: NO
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录“UDM MML命令”界面。

### 2 使用**ADD DMLE**命令增加Diameter本端实体。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dmle_list的变量区（command: ADD DMLE） -#}
<!-- MISSING_MACRO: command=ADD DMLE list_name=add_dmle_list step_id=2 -->
```

### 3 使用**ADD DMPE**命令增加Diameter对端实体DRA。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dmpe_list的变量区（command: ADD DMPE） -#}
<!-- MISSING_MACRO: command=ADD DMPE list_name=add_dmpe_list step_id=3 -->
```

### 4 使用**ADD DMRTS**命令增加Diameter路由组数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dmrts_list的变量区（command: ADD DMRTS） -#}
<!-- MISSING_MACRO: command=ADD DMRTS list_name=add_dmrts_list step_id=4 -->
```

### 5 使用**ADD DMRT**命令增加Diameter路由数据到DRA对端。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dmrt_list的变量区（command: ADD DMRT） -#}
<!-- MISSING_MACRO: command=ADD DMRT list_name=add_dmrt_list step_id=5 -->
```

### 6 使用**ADD DMLKS** 命令增加Diameter链路集。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dmlks_list的变量区（command: ADD DMLKS） -#}
<!-- MISSING_MACRO: command=ADD DMLKS list_name=add_dmlks_list step_id=6 -->
```

### 7 使用**ADD DMLNK**命令增加Diameter链路。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dmlnk_list的变量区（command: ADD DMLNK） -#}
<!-- MISSING_MACRO: command=ADD DMLNK list_name=add_dmlnk_list step_id=7 -->
```

### 配置UDM-UIM的DRA链路时，一般都配置2条链路，两条链路的HSF模块使用不同虚拟机上面的HSF模块。

### 在对端网元支持的情况下，UDM-UIM一般配置为双归属组网。此时配置两条链路的“对端IP地址”为对方的“对端备用IP地址”。

### 链路增加后会自动激活，但是如果对链路进行了修改，则需要使用**DEA DMLNK**命令去激活链路，再使用**ACT DMLNK**命令激活链路。

### 如果同一设备类型配置了多个本地主机名，则DRA需要和该类型的所有本地主机名配置链路。

### 为保证各IPU（Interface Processing Unit）之间实现负载均衡，需要在HSF模块上配置多个IP。同时，在配置链路时需要将链路均分到多个IP上。

### 当本命令中的“工作模式”参数设为“SERVERMULTPORT(服务端多端口)”时，由于本端端口与HSF模块一一对应，为保证各HSF模块之间实现负载均衡，在配置链路时需要在多个HSF模块上配置不同的本端端口。同时，将对端的链路配置均分到多个本端端口上。

