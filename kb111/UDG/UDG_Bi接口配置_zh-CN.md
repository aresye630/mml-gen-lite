---
id: ''
name: Bi接口配置
ne_type: UDG
type: feature
description: 该任务用于指导操作人员完成Bi口的IP资源数据的配置。配置Bi口后可以通过PULL或者PUSH模式向计费中心分发话单。  PULL模式下计费中心主动到NCG取话单。此时NCG作为FTP/SFTP的服务器端，计费中心作为FTP/SFTP的客户端；PUSH模式下NCG采用FTP/SFTP协议分发第二份最终话单到计费中心。此时NCG作为FTP/SFTP的客户端，计费中心作为FTP/SFTP的服务器端。大多数情况下，NCG采用PULL方式分发话单。  PULL方式下，NCG默认开放“/opt/CG\_VNFC/run/vrpv8/product/backsave/”目录下的话单给计费中心，下级相对目录因运营商不同而不同。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案二：部署NCG且基于传统Ga/Gy接口计费组网方案","NCG配置","Bi接口配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务用于指导操作人员完成Bi口的IP资源数据的配置。配置Bi口后可以通过PULL或者PUSH模式向计费中心分发话单。PULL模式下计费中心主动到NCG取话单。此时NCG作为FTP/SFTP的服务器端，计费中心作为FTP/SFTP的客户端；PUSH模式下NCG采用FTP/SFTP协议分发第二份最终话单到计费中心。此时NCG作为FTP/SFTP的客户端，计费中心作为FTP/SFTP的服务器端。大多数情况下，NCG采用PULL方式分发话单。PULL方式下，NCG默认开放“/opt/CG\_VNFC/run/vrpv8/product/backsave/”目录下的话单给计费中心，下级相对目录因运营商不同而不同。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ipresource_list:
      type: items
      properties:
        IPRID:
          name: 'IP资源标识'
          type: string
          required: false
          description: '该命令用于增加NCG话单接收、分发和备份时所使用的IP地址等信息。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        IPRPURPOSE:
          name: 'IP资源用途'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RUID:
          name: 'RU的ID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: '虚拟网络名称'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rst_vnfc_list:
      type: items
      properties:
        SERVICEINSTANCE:
          name: '服务实例'
          type: string
          maxLength: 255
          required: true
          description: '该命令用于重启系统。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISFORCEOPER:
          name: '强制操作标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_cdrdistr_list:
      type: items
      properties:
        CDRDISTRID:
          name: '分发任务标识'
          type: string
          required: false
          description: '+ 该命令用于配置第二份最终话单的分发任务，包括话单分发的方式、采用的协议、计费中心（本文档中又称BS（Billing System））IP地址等信息。 + 该命令使用PULL模式时，BS取走话单后应立即删除取走的话单，防止保存的话单数量过多导致磁盘空间不足。'
          data_source: ''
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: '是否开启Bi口SingleIP功能'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRANSMODE:
          name: '分发方式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OTPTYPE:
          name: '非SinglePULL传输协议类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OUSERNAME:
          name: '开放给BS侧的用户名'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPASSWORD:
          name: '开放给BS侧的密码'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPASSWD:
          name: '确认密码'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ipresource_list:
    - IPRID: biV4
      IPRPURPOSE: Bi
      RUID: '64'
      IPTYPE: IPV4
      IPV4: 172.16.1.10
      VPNNAME: Bi-test
      IPV6: fc01:f111:2222:3333:4444:5555:2111:161
    rst_vnfc_list:
    - SERVICEINSTANCE: 'CG_VNFC_999'
      ISFORCEOPER: TRUE
    add_cdrdistr_list:
    - CDRDISTRID: test_distr
      ISSINGLEBI: NO
      TRANSMODE: PULL
      OTPTYPE: FTP
      OUSERNAME: ftpuser
      OPASSWORD: '*****'
      CPASSWD: '*****'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置本端服务端IP信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ipresource_list的变量区（command: ADD IPRESOURCE） -#}
<!-- MISSING_MACRO: command=ADD IPRESOURCE list_name=add_ipresource_list step_id=1 -->
```

### CG\_VNFC的每个RU都需要配置BI IP。

### 2 重启CG服务。

```jinja2
{%- for item in rst_vnfc_list -%}
    RST VNFC:
    {#- --- 必选参数 --- -#}
    SERVICEINSTANCE="{{item.SERVICEINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ISFORCEOPER is not none -%}
        ISFORCEOPER={{item.ISFORCEOPER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置话单分发任务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cdrdistr_list的变量区（command: ADD CDRDISTR） -#}
<!-- MISSING_MACRO: command=ADD CDRDISTR list_name=add_cdrdistr_list step_id=3 -->
```

### PULL模式下，登录用户名和密码可以自行规划。

### 使用FTP传输协议方式时，传输数据时不加密，安全性低。使用SFTP传输协议方式时，会对传输数据进行加密，安全性较高。建议和计费中心协商选择SFTP协议。

