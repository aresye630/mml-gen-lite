---
id: ''
name: 修改MTU值
ne_type: UDG
type: feature
description: 修改MTU值为**高危操作**，例如：  * MTU修改可能导致整网分片增多，其他网元的分片重组能力的限制可能导致业务受影响。 * 部分协议对最小报文有限制，如果配置过小会导致协议邻居无法建立。  网元外联口MTU值和直连下一跳网关（DCGW/路由器等）的接口MTU值必须一致，默认值是1500，如果运营商没有特殊要求和组网要求，建议保持默认值。  如下几种场景下，可参考本页面修改MTU值：  * 配合整网规划修改Fabric平面MTU值时。 * 配合整网规划修改Tunnel接口MTU值时。 * 配合整网规划修改外联口MTU值时。 * 配合整网规划修改逻辑接口MTU值时。  * 为保证系统正常通信，**网卡MTU****≥Fabric的MTU>主接口的MTU≥子接口的MTU****≥****逻辑接口MTU值**。 * 建议子接口的MTU和主接口的配置一致。 * 逻辑接口MTU取值须小于等于对应的外联口MTU值。 * 网元实例化完成后，Fabric平面的MTU可以通过命令**SET FABRICMTU**修改。 * 修改硬件网卡的MTU的操作步骤请参考相应的硬件产品手册进行。
risk_level: ''
doc_source: ["网络部署","初始配置","UDG初始配置与调测","修改MTU值"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
修改MTU值为**高危操作**，例如：* MTU修改可能导致整网分片增多，其他网元的分片重组能力的限制可能导致业务受影响。* 部分协议对最小报文有限制，如果配置过小会导致协议邻居无法建立。网元外联口MTU值和直连下一跳网关（DCGW/路由器等）的接口MTU值必须一致，默认值是1500，如果运营商没有特殊要求和组网要求，建议保持默认值。如下几种场景下，可参考本页面修改MTU值：* 配合整网规划修改Fabric平面MTU值时。* 配合整网规划修改Tunnel接口MTU值时。* 配合整网规划修改外联口MTU值时。* 配合整网规划修改逻辑接口MTU值时。* 为保证系统正常通信，**网卡MTU****≥Fabric的MTU>主接口的MTU≥子接口的MTU****≥****逻辑接口MTU值**。* 建议子接口的MTU和主接口的配置一致。* 逻辑接口MTU取值须小于等于对应的外联口MTU值。* 网元实例化完成后，Fabric平面的MTU可以通过命令**SET FABRICMTU**修改。* 修改硬件网卡的MTU的操作步骤请参考相应的硬件产品手册进行。

## 必备事项
前提条件

请阅读并熟悉IPFD-010001 接口管理特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_fabricmtu_list:
      type: items
      properties:
        MTUVALUE:
          name: 'MTU值'
          type: integer
          minimum: 512
          maximum: 9600
          required: true
          description: '设置Fabric平面的MTU值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '设置Tunnel接口MTU值。  IPv6接口MTU值通过**SET IFIPV6ENABLE**命令修改。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ifipv6enable_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_interface_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '设置外联口MTU值，如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。  IPv6接口MTU值通过**SET IFIPV6ENABLE**命令修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ifipv6enable_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_interface_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '设置外联口MTU值，如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。  IPv6接口MTU值通过**SET IFIPV6ENABLE**命令修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ifipv6enable_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_interface_list_3:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '设置外联口MTU值，如果Eth-trunk主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。  IPv6接口MTU值通过**SET IFIPV6ENABLE**命令修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ifipv6enable_list_3:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_interface_list_4:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: '设置外联口MTU值，如果Eth-trunk主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。  IPv6接口MTU值通过**SET IFIPV6ENABLE**命令修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ifipv6enable_list_4:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEFLAG:
          name: 'IPv6使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MTU:
          name: 'IPv6接口最大传输单元（byte）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOLINKLOCAL:
          name: '自动生成链路层地址标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_autoconfig_list:
      type: items
      properties:
        SWITCHFLAG:
          name: '自动配置开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_autoscalingservice_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: '自动化配置模板名称，可通过**LST AUTOSCALINGSERVICE**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MTU:
          name: '最大传输单元'
          type: integer
          minimum:
          - 0
          - 46
          maximum:
          - 0
          - 9600
          required: false
          description: '与**MOD INTERFACE**命令设置的MTU值相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_autoconfig_list_1:
      type: items
      properties:
        SWITCHFLAG:
          name: '自动配置开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '逻辑接口名称及IP版本。  此处以UPF与基站对接的逻辑接口为例，MTU值规划原则及配置指导也适用于其他逻辑接口。  可通过**LST LOGICINF**命令查询待修改MTU值的逻辑接口名称。  IP版本根据局点规划设置为IPV4、IPV6或IPVER\_ALL。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: '设置IPv4逻辑接口MTU值。逻辑接口的IP版本为“IPV4”或“IPVER\_ALL”时，可根据网络规划调整IPV4MTU参数值。  该取值须小于等于对应的外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: '设置IPv6逻辑接口MTU值。逻辑接口的IP版本为“IPV6”或“IPVER\_ALL”时，可根据网络规划调整IPV6MTU参数值。  该取值须小于等于对应的外联口MTU值。   * 当前默认值大于外联口的默认值，建议根据运营商规划进行修改，将逻辑接口的IPV6MTU配置值与外联口的IPv6 MTU配置值保持一致（或小于外联口的配置值）。 * 如果逻辑接口IPV6MTU配置值大于外联口的配置值，则包长在两个MTU配置值之间的报文，从外联口发送时被丢弃并回复Too Big报文，触发逻辑接口学习到外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_logicinf_list_1:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '逻辑接口名称及IP版本。  此处以UPF与基站对接的逻辑接口为例，MTU值规划原则及配置指导也适用于其他逻辑接口。  可通过**LST LOGICINF**命令查询待修改MTU值的逻辑接口名称。  IP版本根据局点规划设置为IPV4、IPV6或IPVER\_ALL。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: '设置IPv6逻辑接口MTU值。逻辑接口的IP版本为“IPV6”或“IPVER\_ALL”时，可根据网络规划调整IPV6MTU参数值。  该取值须小于等于对应的外联口MTU值。   * 当前默认值大于外联口的默认值，建议根据运营商规划进行修改，将逻辑接口的IPV6MTU配置值与外联口的IPv6 MTU配置值保持一致（或小于外联口的配置值）。 * 如果逻辑接口IPV6MTU配置值大于外联口的配置值，则包长在两个MTU配置值之间的报文，从外联口发送时被丢弃并回复Too Big报文，触发逻辑接口学习到外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: '设置IPv4逻辑接口MTU值。逻辑接口的IP版本为“IPV4”或“IPVER\_ALL”时，可根据网络规划调整IPV4MTU参数值。  该取值须小于等于对应的外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_logicinf_list_2:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '逻辑接口名称及IP版本。  此处以UPF与基站对接的逻辑接口为例，MTU值规划原则及配置指导也适用于其他逻辑接口。  可通过**LST LOGICINF**命令查询待修改MTU值的逻辑接口名称。  IP版本根据局点规划设置为IPV4、IPV6或IPVER\_ALL。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: '设置IPv4逻辑接口MTU值。逻辑接口的IP版本为“IPV4”或“IPVER\_ALL”时，可根据网络规划调整IPV4MTU参数值。  该取值须小于等于对应的外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: '设置IPv6逻辑接口MTU值。逻辑接口的IP版本为“IPV6”或“IPVER\_ALL”时，可根据网络规划调整IPV6MTU参数值。  该取值须小于等于对应的外联口MTU值。   * 当前默认值大于外联口的默认值，建议根据运营商规划进行修改，将逻辑接口的IPV6MTU配置值与外联口的IPv6 MTU配置值保持一致（或小于外联口的配置值）。 * 如果逻辑接口IPV6MTU配置值大于外联口的配置值，则包长在两个MTU配置值之间的报文，从外联口发送时被丢弃并回复Too Big报文，触发逻辑接口学习到外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_logicinf_list_3:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '逻辑接口名称及IP版本。  此处以UPF与基站对接的逻辑接口为例，MTU值规划原则及配置指导也适用于其他逻辑接口。  可通过**LST LOGICINF**命令查询待修改MTU值的逻辑接口名称。  IP版本根据局点规划设置为IPV4、IPV6或IPVER\_ALL。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: '设置IPv4逻辑接口MTU值。逻辑接口的IP版本为“IPV4”或“IPVER\_ALL”时，可根据网络规划调整IPV4MTU参数值。  该取值须小于等于对应的外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: '设置IPv6逻辑接口MTU值。逻辑接口的IP版本为“IPV6”或“IPVER\_ALL”时，可根据网络规划调整IPV6MTU参数值。  该取值须小于等于对应的外联口MTU值。   * 当前默认值大于外联口的默认值，建议根据运营商规划进行修改，将逻辑接口的IPV6MTU配置值与外联口的IPv6 MTU配置值保持一致（或小于外联口的配置值）。 * 如果逻辑接口IPV6MTU配置值大于外联口的配置值，则包长在两个MTU配置值之间的报文，从外联口发送时被丢弃并回复Too Big报文，触发逻辑接口学习到外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_logicinf_list_4:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '逻辑接口名称及IP版本。  此处以UPF与基站对接的逻辑接口为例，MTU值规划原则及配置指导也适用于其他逻辑接口。  可通过**LST LOGICINF**命令查询待修改MTU值的逻辑接口名称。  IP版本根据局点规划设置为IPV4、IPV6或IPVER\_ALL。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: '设置IPv6逻辑接口MTU值。逻辑接口的IP版本为“IPV6”或“IPVER\_ALL”时，可根据网络规划调整IPV6MTU参数值。  该取值须小于等于对应的外联口MTU值。   * 当前默认值大于外联口的默认值，建议根据运营商规划进行修改，将逻辑接口的IPV6MTU配置值与外联口的IPv6 MTU配置值保持一致（或小于外联口的配置值）。 * 如果逻辑接口IPV6MTU配置值大于外联口的配置值，则包长在两个MTU配置值之间的报文，从外联口发送时被丢弃并回复Too Big报文，触发逻辑接口学习到外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: '设置IPv4逻辑接口MTU值。逻辑接口的IP版本为“IPV4”或“IPVER\_ALL”时，可根据网络规划调整IPV4MTU参数值。  该取值须小于等于对应的外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_logicinf_list_5:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '逻辑接口名称及IP版本。  此处以UPF与基站对接的逻辑接口为例，MTU值规划原则及配置指导也适用于其他逻辑接口。  可通过**LST LOGICINF**命令查询待修改MTU值的逻辑接口名称。  IP版本根据局点规划设置为IPV4、IPV6或IPVER\_ALL。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: '设置IPv4逻辑接口MTU值。逻辑接口的IP版本为“IPV4”或“IPVER\_ALL”时，可根据网络规划调整IPV4MTU参数值。  该取值须小于等于对应的外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: '设置IPv6逻辑接口MTU值。逻辑接口的IP版本为“IPV6”或“IPVER\_ALL”时，可根据网络规划调整IPV6MTU参数值。  该取值须小于等于对应的外联口MTU值。   * 当前默认值大于外联口的默认值，建议根据运营商规划进行修改，将逻辑接口的IPV6MTU配置值与外联口的IPv6 MTU配置值保持一致（或小于外联口的配置值）。 * 如果逻辑接口IPV6MTU配置值大于外联口的配置值，则包长在两个MTU配置值之间的报文，从外联口发送时被丢弃并回复Too Big报文，触发逻辑接口学习到外联口MTU值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_fabricmtu_list:
    - MTUVALUE: 1800
    mod_interface_list:
    - IFNAME: 'Tunnel6'
      IFMTU: 1500
    set_ifipv6enable_list:
    - IFNAME: 'Tunnel6'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    mod_interface_list_1:
    - IFNAME: 'Ethernet64/0/4'
      IFMTU: 1500
    set_ifipv6enable_list_1:
    - IFNAME: 'Ethernet64/0/4'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    mod_interface_list_2:
    - IFNAME: 'Ethernet64/0/4.1'
      IFMTU: 1500
    set_ifipv6enable_list_2:
    - IFNAME: 'Ethernet64/0/4.1'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    mod_interface_list_3:
    - IFNAME: 'Eth-trunk1'
      IFMTU: 1500
    set_ifipv6enable_list_3:
    - IFNAME: 'Eth-trunk1'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    mod_interface_list_4:
    - IFNAME: 'Eth-trunk1.100'
      IFMTU: 1500
    set_ifipv6enable_list_4:
    - IFNAME: 'Eth-trunk1.100'
      ENABLEFLAG: TRUE
      MTU: 1500
      AUTOLINKLOCAL: ''
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    mod_autoscalingservice_list:
    - SERVICENAME: 'ServName_test1'
      MTU: 1500
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
    mod_logicinf_list:
    - NAME: 'N3if1/1/0'
      IPVERSION: IPV4
      IPV4MTU: 1500
      IPV6MTU: 1500
    mod_logicinf_list_1:
    - NAME: 'N3if1/1/0'
      IPVERSION: IPV6
      IPV6MTU: 1500
      IPV4MTU: 1500
    mod_logicinf_list_2:
    - NAME: 'N3if1/1/0'
      IPVERSION: IPVER_ALL
      IPV4MTU: 1500
      IPV6MTU: 1500
    mod_logicinf_list_3:
    - NAME: 'Saif1/1/0'
      IPVERSION: IPV4
      IPV4MTU: 1500
      IPV6MTU: 1500
    mod_logicinf_list_4:
    - NAME: 'Saif1/1/0'
      IPVERSION: IPV6
      IPV6MTU: 1500
      IPV4MTU: 1500
    mod_logicinf_list_5:
    - NAME: 'Saif1/1/0'
      IPVERSION: IPVER_ALL
      IPV4MTU: 1500
      IPV6MTU: 1500
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 修改Fabric平面的MTU值

### Fabric平面的MTU值不满足要求时，修改Fabric平面的MTU值。

### NP卡加速场景，不支持通过MML修改Fabric MTU。

```jinja2
{%- for item in set_fabricmtu_list -%}
    SET FABRICMTU:
    {#- --- 必选参数 --- -#}
    MTUVALUE={{item.MTUVALUE}},
    ;
{%- endfor -%}
```

### 2 修改Tunnel接口的MTU值

### Tunnel接口的MTU值不满足要求时，修改Tunnel接口的MTU值。

#### 2.1 //IPv4 MTU

```jinja2
{%- if is_scenario_ipv4 -%}
    {%- for item in mod_interface_list -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 //IPv6 MTU

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in set_ifipv6enable_list -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 修改外联口的MTU值

### Ethernet接口组网时，修改外联口（Ethernet接口做外联口）的MTU值。

#### 3.1 修改外联口主接口的MTU值。

##### 3.1.1 //IPv4 MTU

```jinja2
{%- if is_scenario_ethernet and is_scenario_ipv4 -%}
    {%- for item in mod_interface_list_1 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.2 //IPv6 MTU

```jinja2
{%- if is_scenario_ethernet and is_scenario_ipv6 -%}
    {%- for item in set_ifipv6enable_list_1 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 **可选：**如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。

##### 3.2.1 //IPv4 MTU

```jinja2
{%- if is_optional_config_subinterface_mtu and is_scenario_ethernet and is_scenario_ipv4 -%}
    {%- for item in mod_interface_list_2 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.2 //IPv6 MTU

```jinja2
{%- if is_optional_config_subinterface_mtu and is_scenario_ethernet and is_scenario_ipv6 -%}
    {%- for item in set_ifipv6enable_list_2 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 Eth-trunk接口组网时，修改外联口（Eth-trunk接口做外联口）的MTU值。

### Eth-trunk接口组网时，不需要修改成员接口的MTU值。若规划的成员接口在加入Eth-trunk前修改了MTU值，则会导致添加成员接口失败。

#### 4.1 修改外联口主接口的MTU值。

##### 4.1.1 //IPv4 MTU

```jinja2
{%- if is_scenario_eth_trunk and is_scenario_ipv4 -%}
    {%- for item in mod_interface_list_3 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.2 //IPv6 MTU

```jinja2
{%- if is_scenario_eth_trunk and is_scenario_ipv6 -%}
    {%- for item in set_ifipv6enable_list_3 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 **可选：**如果主接口下存在子接口，建议将其子接口的MTU值配置为和主接口MTU值一致。

##### 4.2.1 //IPv4 MTU

```jinja2
{%- if is_optional_config_subinterface_mtu and is_scenario_eth_trunk and is_scenario_ipv4 -%}
    {%- for item in mod_interface_list_4 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.2.2 //IPv6 MTU

```jinja2
{%- if is_optional_config_subinterface_mtu and is_scenario_eth_trunk and is_scenario_ipv6 -%}
    {%- for item in set_ifipv6enable_list_4 -%}
        SET IFIPV6ENABLE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        ENABLEFLAG={{item.ENABLEFLAG}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.MTU is not none -%}
                MTU={{item.MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENABLEFLAG=TRUE 时可选 --- -#}
        {%- if item.ENABLEFLAG == 'TRUE' -%}
            {%- if item.AUTOLINKLOCAL is not none -%}
                AUTOLINKLOCAL={{item.AUTOLINKLOCAL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 自动部署模式时，建议同步修改自动化配置模板中的MTU值。

### 执行本步骤，可避免后续因模板MTU值与接口实际MTU值不一致产生告警ALM-232398849 接口自动化配置失败；后续扩容场景，也可避免新扩容接口仍需参考步骤 3/步骤 4逐个修改MTU值。

#### 5.1 查询自动配置开关。

#### 自动配置开关，与修改前配置保持一致：

##### 5.1.1 “自动配置开关”取值为“是”，请依次执行步骤 5.b～步骤 5.d。

##### 5.1.2 “自动配置开关”取值为“否”，请只执行步骤 5.c，不执行其他步骤。

#### 5.2 关闭自动配置开关。

#### 执行**DSP OPSASSISTSTATE**命令，直到“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”或者查询无该脚本时，才能关闭自动配置开关。否则可能影响业务。

```jinja2
{%- set LST_AUTOCONFIG=getParameterValue('LST AUTOCONFIG') -%}
{%- if is_scenario_auto_deploy and LST_AUTOCONFIG=='是' -%}
    {%- for item in set_autoconfig_list -%}
        SET AUTOCONFIG:
        {#- --- 必选参数 --- -#}
        SWITCHFLAG={{item.SWITCHFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.3 修改自动化配置模板的MTU值。

```jinja2
{%- if is_scenario_auto_deploy and LST_AUTOCONFIG=='是' and LST_AUTOCONFIG=='否' -%}
    {%- for item in mod_autoscalingservice_list -%}
        MOD AUTOSCALINGSERVICE:
        {#- --- 必选参数 --- -#}
        SERVICENAME="{{item.SERVICENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.MTU is not none -%}
            MTU={{item.MTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.4 开启自动配置开关。

```jinja2
{%- if is_scenario_auto_deploy and LST_AUTOCONFIG=='是' -%}
    {%- for item in set_autoconfig_list_1 -%}
        SET AUTOCONFIG:
        {#- --- 必选参数 --- -#}
        SWITCHFLAG={{item.SWITCHFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 修改逻辑接口的MTU值

### 逻辑接口的MTU值不满足要求时，修改逻辑接口的MTU值。采用独立接口时，如下以N3if1/1/0为例；采用抽象接口时，如下以Saif1/1/0为例。

#### 6.1 //修改N3if1/1/0逻辑接口的MTU值。

##### 6.1.1 //IPv4 MTU

```jinja2
{%- if is_scenario_independent_interface and is_scenario_ipv4 -%}
    {%- for item in mod_logicinf_list -%}
        MOD LOGICINF:
        {#- --- 必选参数 --- -#}
        NAME="{{item.NAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPVERSION is not none -%}
            IPVERSION={{item.IPVERSION}},
        {%- endif -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.1.2 //IPv6 MTU

```jinja2
{%- if is_scenario_independent_interface and is_scenario_ipv6 -%}
    {%- for item in mod_logicinf_list_1 -%}
        MOD LOGICINF:
        {#- --- 必选参数 --- -#}
        NAME="{{item.NAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPVERSION is not none -%}
            IPVERSION={{item.IPVERSION}},
        {%- endif -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.1.3 //IPv4 MTU & IPv6 MTU

```jinja2
{%- if is_scenario_independent_interface and is_scenario_ipv4 and is_scenario_ipv6 -%}
    {%- for item in mod_logicinf_list_2 -%}
        MOD LOGICINF:
        {#- --- 必选参数 --- -#}
        NAME="{{item.NAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPVERSION is not none -%}
            IPVERSION={{item.IPVERSION}},
        {%- endif -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 //修改Saif1/1/0逻辑接口的MTU值。

##### 6.2.1 //IPv4 MTU

```jinja2
{%- if is_scenario_abstract_interface and is_scenario_ipv4 -%}
    {%- for item in mod_logicinf_list_3 -%}
        MOD LOGICINF:
        {#- --- 必选参数 --- -#}
        NAME="{{item.NAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPVERSION is not none -%}
            IPVERSION={{item.IPVERSION}},
        {%- endif -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.2.2 //IPv6 MTU

```jinja2
{%- if is_scenario_abstract_interface and is_scenario_ipv6 -%}
    {%- for item in mod_logicinf_list_4 -%}
        MOD LOGICINF:
        {#- --- 必选参数 --- -#}
        NAME="{{item.NAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPVERSION is not none -%}
            IPVERSION={{item.IPVERSION}},
        {%- endif -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.2.3 //IPv4 MTU & IPv6 MTU

```jinja2
{%- if is_scenario_abstract_interface and is_scenario_ipv4 and is_scenario_ipv6 -%}
    {%- for item in mod_logicinf_list_5 -%}
        MOD LOGICINF:
        {#- --- 必选参数 --- -#}
        NAME="{{item.NAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPVERSION is not none -%}
            IPVERSION={{item.IPVERSION}},
        {%- endif -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

