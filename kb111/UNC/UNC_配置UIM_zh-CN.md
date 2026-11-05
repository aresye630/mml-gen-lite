---
id: ''
name: 配置UIM
ne_type: UNC
type: feature
description: 该任务旨在指导操作人员在UIM上完成家庭CPE的后路由网段配置以及UE的配置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置UIM"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员在UIM上完成家庭CPE的后路由网段配置以及UE的配置。

## 必备事项
前提条件

* 已完成UIM的本局数据。
* 已完成UIM和SMF之间的对接配置。
* 已完成**三层VPN**的License加载。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_urealm_list:
      type: items
      properties:
        REALM:
          name: '域名'
          type: string
          required: false
          description: '添加REALM模板'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHMODE:
          name: '认证方式'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '配置APN信息'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSGTYPE:
          name: '消息类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHMODE:
          name: '认证方式'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TYPE:
          name: 'APN类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uuser_list:
      type: items
      properties:
        ACCESSNETWORK:
          name: '接入网络'
          type: string
          required: false
          description: '添加UE和CPE用户信息'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERNAME:
          name: '用户名'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALM:
          name: '域名'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PASSWORD:
          name: '用户密码'
          type: string
          required: false
          description: '要与SMF上的**SET APNAUTHATTR**命令的**鉴权密码**保持一致'
          data_source: '全局规划'
          pattern: ''
          default: ''
        APN:
          name: '接入点名称'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uiproute_list:
      type: items
      properties:
        ACCESSNETWORK:
          name: '接入网络'
          type: string
          required: false
          description: '配置家庭CPE的后路由网段'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USERNAME:
          name: '用户名'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALM:
          name: '域名'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APN:
          name: '企业网接入点名称'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPROUTE:
          name: '路由IP地址/掩码'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_urealm_list:
    - REALM: huawei.com
      AUTHMODE: USERNAME_PASSWORD
    add_uapn_list:
    - APN: home.dnn
      MSGTYPE: BOTH
      AUTHMODE: USERNAME
      TYPE: Static
    add_uuser_list:
    - ACCESSNETWORK: WCDMA
      USERNAME: '8613900000001'
      REALM: huawei.com
      PASSWORD: '*****'
      APN: home.dnn
    add_uiproute_list:
    - ACCESSNETWORK: WCDMA
      USERNAME: '8613900000001'
      REALM: huawei.com
      APN: home.dnn
      IPROUTE: 10.1.1.1/24
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //添加REALM模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_urealm_list的变量区（command: ADD UREALM） -#}
<!-- MISSING_MACRO: command=ADD UREALM list_name=add_urealm_list step_id=1 -->
```

### 2 //配置APN信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_uapn_list的变量区（command: ADD UAPN） -#}
<!-- MISSING_MACRO: command=ADD UAPN list_name=add_uapn_list step_id=2 -->
```

### 3 //登录到UIM MML命令界面，配置CPE和UE配置用户信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_uuser_list的变量区（command: ADD UUSER） -#}
<!-- MISSING_MACRO: command=ADD UUSER list_name=add_uuser_list step_id=3 -->
```

### 4 //配置家庭CPE后路由网段。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_uiproute_list的变量区（command: ADD UIPROUTE） -#}
<!-- MISSING_MACRO: command=ADD UIPROUTE list_name=add_uiproute_list step_id=4 -->
```

