---
id: ''
name: 激活溯源日志携带用户标志
ne_type: UDG
type: feature
description: 若运营商需要查看更详细的日志信息，精准定位不同用户的地址转换过程，则需要开启溯源日志携带用户标志特性。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG NAT功能专题","数据配置与调测","数据配置","配置NAT溯源日志","激活溯源日志携带用户标志"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
若运营商需要查看更详细的日志信息，精准定位不同用户的地址转换过程，则需要开启溯源日志携带用户标志特性。

## 必备事项
前提条件

* 已完成激活溯源日志上报。
* 已完成UDG与日志服务器之间IPSEC安全传输通道的建立，详情可参考“IPFD-016000 IPSec功能”特性。
* 已登录OM Portal。
* 已完成配置NAT基本功能License开关。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '打开溯源日志携带用户标志License开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    system-view_list:
      type: items
      properties: {}
    nap-view_list:
      type: items
      properties: {}
    natlog-view_list:
      type: items
      properties: {}
    natlog-syslog_template_list:
      type: items
      properties:
        TEMPLATE:
          name: 'templatename'
          type: string
          required: false
          description: '配置日志内容模板名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FORMAT:
          name: 'format'
          type: string
          required: false
          description: '配置用户自定义日志内容格式，当发送会话日志或者端口预分配日志会根据自定义格式将日志内容发送到日志服务器。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV4NATUSR01'
      SWITCH: ENABLE
    system-view_list:
    - {}
    nap-view_list:
    - {}
    natlog-view_list:
    - {}
    natlog-syslog_template_list:
    - TEMPLATE: syslog
      FORMAT: $date_utc $time_utc $rcd_type source=$src_ip source_nat=$src_nat_ip:$src_nat_port dest=$dest_ip:$dest_port vpn=$vpn_id imsi=$imsi msisdn=$msisdn
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 选择“应用管理 > NAT”，进入NAT的CLI执行界面。

### 3 进入NAT系统视图。

### **sy****stem-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该system-view_list的变量区（command: system-view） -#}
<!-- MISSING_MACRO: command=system-view list_name=system-view_list step_id=3 -->
```

### 4 进入natlog-view视图。

### **nap-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该nap-view_list的变量区（command: nap-view） -#}
<!-- MISSING_MACRO: command=nap-view list_name=nap-view_list step_id=4 -->
```

### **natlog-view**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-view_list的变量区（command: natlog-view） -#}
<!-- MISSING_MACRO: command=natlog-view list_name=natlog-view_list step_id=4 -->
```

### 5 自定义syslog日志的内容格式。

### **natlog-syslog template**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该natlog-syslog_template_list的变量区（command: natlog-syslog template） -#}
<!-- MISSING_MACRO: command=natlog-syslog template list_name=natlog-syslog_template_list step_id=5 -->
```

