---
id: ''
name: 异常处理：双活NRF回退到单机NRF
ne_type: UNC
type: feature
description: 单机改造双活后，双活NRF不能正常处理业务，也无法规避故障问题，希望通过回退到原单机的场景来保证NRF可以继续提供正常业务。  本操作指导介绍在运行网络中将现网原有单机改造后的双活NRF，回退为单机NRF的操作过程。  适用于NRF。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NRF解决方案","NRF功能部署","4/5G融合部署","NRF单层容灾组网","NRF解决方案基本功能配置实例（NRF双活容灾+ NF注册/更新/去注册、NF订阅/通知+NF发现）","新建场景/2个单机改造双活场景","异常处理：双活NRF回退到单机NRF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
单机改造双活后，双活NRF不能正常处理业务，也无法规避故障问题，希望通过回退到原单机的场景来保证NRF可以继续提供正常业务。本操作指导介绍在运行网络中将现网原有单机改造后的双活NRF，回退为单机NRF的操作过程。适用于NRF。

## 必备事项
前提条件

* 已完成新建场景/2个单机改造双活场景。
* 已按照自身组网完成两个NRF之间的路由配置，对于IPv4组网，各配置场景请参考“初始配置与调测”中自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 已按照自身组网完成两个NRF之间的路由配置，对于IPv6组网，各配置场景请参考“初始配置与调测”中自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
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
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
    rmv_drcomm_list:
      type: items
      properties:
        DRINSTID:
          name: '容灾实例ID'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'ip版本号'
          type: string
          enum:
          - COMM_IPV4
          - COMM_IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        COMMIPV4:
          name: 'ipv4通信地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        COMMIPV6:
          name: 'ipv6通信地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_drinst_list:
      type: items
      properties:
        DRINSTID:
          name: '容灾实例ID'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2DLNRR01'
      SWITCH: DISABLE
    rmv_drcomm_list:
    - DRINSTID: 1
      IPVERSION: COMM_IPV4
      COMMIPV4: '10.5.5.2'
      COMMIPV6: ''
    rmv_drinst_list:
    - DRINSTID: 0
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 NRF1和NRF2上分别执行解除NRF的双活容灾配置。

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 关闭双活NRF容灾特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.3 删除双活NRF容灾实例通信地址信息。

```jinja2
{%- for item in rmv_drcomm_list -%}
    RMV DRCOMM:
    {#- --- 必选参数 --- -#}
    DRINSTID={{item.DRINSTID}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=COMM_IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'COMM_IPV4' -%}
        COMMIPV4="{{item.COMMIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=COMM_IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'COMM_IPV6' -%}
        COMMIPV6="{{item.COMMIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 删除双活容灾实例。

```jinja2
{%- for item in rmv_drinst_list -%}
    RMV DRINST:
    {#- --- 必选参数 --- -#}
    DRINSTID={{item.DRINSTID}},
    ;
{%- endfor -%}
```

#### 1.5 查询容灾配置信息，确保容灾配置信息已删除。

#### 查询结果中，如果“数据备份状态” 为 “容灾配置表已删除”，表示容灾配置信息已删除；如果“数据备份状态” 为 “ 容灾配置表仍然存在”，表示容灾配置信息正在删除，请1分钟后再次执行此命令，如果连续5次查询都是配置信息正在删除，说明系统异常，请联系华为技术支持。

