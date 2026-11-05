---
id: ''
name: 配置到CHF(OCS)的Local NRF
ne_type: UDG
type: feature
description: 该任务用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案（N40接口+传统Ga/Gy接口）","NCG配置","配置到CHF(OCS)的Local NRF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          required: false
          description: '该命令用于增加本地配置的对端NF实例的概述信息'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。  全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NF类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFSTATUS:
          name: 'NF状态'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: 'IPV6地址1'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfservice_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          required: false
          description: '该命令用于增加本地配置对端NF实例支持的服务实例信息'
          data_source: ''
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFSERVICESTATUS:
          name: '服务实例状态'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfgpsi_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: string
          required: false
          description: '该命令用于增加本地配置的对端NF实例支持的GPSI信息'
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUERYTYPE:
          name: '查询方式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: CHF_Instance_0
      NFTYPE: NfCUSTOM_OCS
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV6
      IPV6ADDRESS1: fd11:f111:2222:3333:4444:5555:2111:151
      PORT: '8080'
      CAPACITY: '100'
      PRIORITY: '10'
    add_pnfservice_list:
    - NFINSTANCEID: CHF_Instance_0
      SRVINSTANCEID: Service_Instance_1
      SERVICENAME: NocsConvCharg
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
      PRIORITY: '10'
      CAPACITY: '100'
    add_pnfgpsi_list:
    - INDEX: '1'
      NFINSTANCEID: CHF_Instance_0
      QUERYTYPE: START_END
      RANGESTART: '123001200100001'
      RANGEEND: '123001200109999'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置主备CHF(OCS)的NF Profile。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pnfprofile_list的变量区（command: ADD PNFPROFILE） -#}
<!-- MISSING_MACRO: command=ADD PNFPROFILE list_name=add_pnfprofile_list step_id=1 -->
```

### NFINSTANCEID参数需要填写对端NF的UUID，如果无法获得，也可以使用长度小于18的字符串，该字符串不能是IPv4或IPv6地址格式的字符串。

### 2 配置主备CHF(OCS)的服务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pnfservice_list的变量区（command: ADD PNFSERVICE） -#}
<!-- MISSING_MACRO: command=ADD PNFSERVICE list_name=add_pnfservice_list step_id=2 -->
```

### 3 配置对端CHF(OCS)的支持的GPSI号段范围。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pnfgpsi_list的变量区（command: ADD PNFGPSI） -#}
<!-- MISSING_MACRO: command=ADD PNFGPSI list_name=add_pnfgpsi_list step_id=3 -->
```

