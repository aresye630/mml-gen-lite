---
id: ''
name: 激活支持Direct Tunnel功能
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活支持Direct Tunnel功能的操作过程。  Direct Tunnel是在3G网络中，为减小SGSN的负荷和传输时延、提升网络的可扩容性而引入的。  适用于SGSN、GGSN。  * **接入网与核心网的承载网合一，****Gn/Iu端口合用物理端口。**    本方案中，SGSN和GGSN的Gn/Iu接口组网方式为：    + RNC采用双主端口。   + SGSN Gn/Iu合用端口，采用双主端口+OSPF。   + GGSN Gn/Iu合用端口，采用双主端口+OSPF。    组网方案如图1所示：    + RNC的数据经由三层设备PE接入SGSN。   + SGSN到核心网的数据，通过二层设备CE汇聚，经由PE接入GGSN。   + GGSN提供两个10GE以太网接口与PE相连。   + PE1和PE2间启用OSPF。   + PE和SGSN间启用OSPF。   + PE和GGSN间启用OSPF。    **图1** 组网方案           |  |  |   | --- | --- |   | 黑色连接线代表GE线缆 | 蓝色连接线代表10GE线缆 |   | 实线连接线代表接口状态为主 | - |    PE端口不足或使用10GE端口时，需使用CE汇聚接入网和承载网流量。反之，SGSN与PE直连即可。    如果CE为三层设备，则RNC的流量可以接入CE。    吞吐量小于10G的组网，可以相应减少Eth-Trunk中绑定的端口数。推荐配置Eth-Trunk内冗余，捆绑端口数N+1（N与网络吞吐量相关，是实际规划的端口数）。 * **接入网与核心网的承载网分离****，Gn/Iu端口使用不同物理端口。对组网无特殊要求。**    本方案中，SGSN和GGSN的Gn/Iu接口组网方式为：    + RNC采用主备端口。   + SGSN Gn/Iu分离使用端口，Iu采用主备端口+VRRP+静态路由，Gn采用双主端口+OSPF。   + GGSN Gn/Iu分离使用端口，均采用双主端口+OSPF。    组网方案如图2所示：    + RNC的数据经由三层设备PE接入SGSN。   + SGSN到核心网的数据，通过二层设备CE汇聚，经由PE接入GGSN。   + GGSN提供两个10GE以太网接口与PE相连。   + SGSN与PE间的Gn接口，启用OSPF。   + GGSN和PE间启用OSPF。   + PE1和PE2间启用VRRP+OSPF。    **图2** 组网方案           |  |  |   | --- | --- |   | 黑色连接线代表GE线缆 | 蓝色连接线代表10GE线缆 |   | 实线连接线代表接口状态为主 | 虚线连接线代表接口状态为备 |    PE端口不足或使用10GE端口时，需使用CE汇聚接入网和承载网流量。反之，SGSN与PE直连即可。    如果CE为三层设备，则RNC的流量可以接入CE。    吞吐量小于10G的组网，可以相应减少Eth-Trunk中绑定的端口数。推荐配置Eth-Trunk内冗余，捆绑端口数N+1（N与网络吞吐量相关，是实际规划的端口数）。 * **接入网与核心网的承载网分离****，不互通。要求SGSN双主组网。**    本方案中，SGSN和GGSN的Gn/Iu接口组网方式为：    + RNC采用双主端口。   + SGSN Gn/Iu使用分离端口，Iu采用双主端口+BFD+静态路由，Gn采用双主端口+OSPF。   + GGSN Gn/Iu使用分离端口，Iu/Gn均采用双主端口+OSPF。    组网方案如图3所示：    + RNC的数据经由三层设备PE接入SGSN。   + SGSN到核心网的数据，通过二层设备CE汇聚，经由PE接入GGSN。   + GGSN提供两个10GE以太网接口与PE相连。   + GGSN和PE间启用OSPF。   + PE1和PE2间启用OSPF。    **图3** 组网方案      |  |  |   | --- | --- |   | 黑色连接线代表GE线缆 | 蓝色连接线代表10GE线缆 |   | 实线连接线代表接口状态为主 | - |    PE端口不足或使用10GE端口时，需使用CE汇聚接入网和承载网流量。反之，SGSN与PE直连即可。    如果CE为三层设备，则RNC的流量可以接入CE。    吞吐量小于10G的组网，可以相应减少Eth-Trunk中绑定的端口数。推荐配置Eth-Trunk内冗余，捆绑端口数N+1（N与网络吞吐量相关，是实际规划的端口数）。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","组网功能","WSFD-104506 支持Direct Tunnel功能","激活支持Direct Tunnel功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持Direct Tunnel功能的操作过程。Direct Tunnel是在3G网络中，为减小SGSN的负荷和传输时延、提升网络的可扩容性而引入的。适用于SGSN、GGSN。* **接入网与核心网的承载网合一，****Gn/Iu端口合用物理端口。**  本方案中，SGSN和GGSN的Gn/Iu接口组网方式为：  + RNC采用双主端口。  + SGSN Gn/Iu合用端口，采用双主端口+OSPF。  + GGSN Gn/Iu合用端口，采用双主端口+OSPF。  组网方案如图1所示：  + RNC的数据经由三层设备PE接入SGSN。  + SGSN到核心网的数据，通过二层设备CE汇聚，经由PE接入GGSN。  + GGSN提供两个10GE以太网接口与PE相连。  + PE1和PE2间启用OSPF。  + PE和SGSN间启用OSPF。  + PE和GGSN间启用OSPF。  **图1** 组网方案        |  |  |  | --- | --- |  | 黑色连接线代表GE线缆 | 蓝色连接线代表10GE线缆 |  | 实线连接线代表接口状态为主 | - |  PE端口不足或使用10GE端口时，需使用CE汇聚接入网和承载网流量。反之，SGSN与PE直连即可。  如果CE为三层设备，则RNC的流量可以接入CE。  吞吐量小于10G的组网，可以相应减少Eth-Trunk中绑定的端口数。推荐配置Eth-Trunk内冗余，捆绑端口数N+1（N与网络吞吐量相关，是实际规划的端口数）。* **接入网与核心网的承载网分离****，Gn/Iu端口使用不同物理端口。对组网无特殊要求。**  本方案中，SGSN和GGSN的Gn/Iu接口组网方式为：  + RNC采用主备端口。  + SGSN Gn/Iu分离使用端口，Iu采用主备端口+VRRP+静态路由，Gn采用双主端口+OSPF。  + GGSN Gn/Iu分离使用端口，均采用双主端口+OSPF。  组网方案如图2所示：  + RNC的数据经由三层设备PE接入SGSN。  + SGSN到核心网的数据，通过二层设备CE汇聚，经由PE接入GGSN。  + GGSN提供两个10GE以太网接口与PE相连。  + SGSN与PE间的Gn接口，启用OSPF。  + GGSN和PE间启用OSPF。  + PE1和PE2间启用VRRP+OSPF。  **图2** 组网方案        |  |  |  | --- | --- |  | 黑色连接线代表GE线缆 | 蓝色连接线代表10GE线缆 |  | 实线连接线代表接口状态为主 | 虚线连接线代表接口状态为备 |  PE端口不足或使用10GE端口时，需使用CE汇聚接入网和承载网流量。反之，SGSN与PE直连即可。  如果CE为三层设备，则RNC的流量可以接入CE。  吞吐量小于10G的组网，可以相应减少Eth-Trunk中绑定的端口数。推荐配置Eth-Trunk内冗余，捆绑端口数N+1（N与网络吞吐量相关，是实际规划的端口数）。* **接入网与核心网的承载网分离****，不互通。要求SGSN双主组网。**  本方案中，SGSN和GGSN的Gn/Iu接口组网方式为：  + RNC采用双主端口。  + SGSN Gn/Iu使用分离端口，Iu采用双主端口+BFD+静态路由，Gn采用双主端口+OSPF。  + GGSN Gn/Iu使用分离端口，Iu/Gn均采用双主端口+OSPF。  组网方案如图3所示：  + RNC的数据经由三层设备PE接入SGSN。  + SGSN到核心网的数据，通过二层设备CE汇聚，经由PE接入GGSN。  + GGSN提供两个10GE以太网接口与PE相连。  + GGSN和PE间启用OSPF。  + PE1和PE2间启用OSPF。  **图3** 组网方案    |  |  |  | --- | --- |  | 黑色连接线代表GE线缆 | 蓝色连接线代表10GE线缆 |  | 实线连接线代表接口状态为主 | - |  PE端口不足或使用10GE端口时，需使用CE汇聚接入网和承载网流量。反之，SGSN与PE直连即可。  如果CE为三层设备，则RNC的流量可以接入CE。  吞吐量小于10G的组网，可以相应减少Eth-Trunk中绑定的端口数。推荐配置Eth-Trunk内冗余，捆绑端口数N+1（N与网络吞吐量相关，是实际规划的端口数）。

## 必备事项
前提条件

* 请仔细阅读WSFD-104506 支持Direct Tunnel 功能特性概述。
* 完成加载License。
* RNC侧的Direct Tunnel配置已完成。
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
    add_rnc_list:
      type: items
      properties:
        RNCX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCMCC:
          name: '移动国家代码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCMNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCID:
          name: 'RNC标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPC:
          name: '信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OTS:
          name: 'RNC是否支持OneTunnel'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_ggsncharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_GGSN
          - Gn_GGSN
          - Gp_GGSN
          - SPECIAL_GGSN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        GGSNIPV4:
          name: 'GGSN的信令面IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: '掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OTS:
          name: 'GGSN是否支持DirectTunnel'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        GGSNIPV6:
          name: 'GGSN的信令面IP地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV6:
          name: '子网前缀长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsidt_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsidt_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsidt_list_2:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsidt_list_3:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsidt_list_4:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsidt_list_5:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnnidt_list:
      type: items
      properties:
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnnidt_list_1:
      type: items
      properties:
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnnidt_list_2:
      type: items
      properties:
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srroute_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTVRFNAME:
          name: '下一跳VPN名字'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTHOP:
          name: '路由下一跳'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2DIRTUN02'
      SWITCH: ENABLE
    add_rnc_list:
    - RNCX: 1
      RNCMCC: '123'
      RNCMNC: '45'
      RNCID: 1
      NI: NAT
      SPC: '1111'
      OTS: YES
    add_ggsncharact_list:
    - RANGE: SPECIAL_GGSN
      IPT: IPV4
      GGSNIPV4: '10.3.1.1'
      MASKV4: '255.255.255.0'
      OTS: YES
      GGSNIPV6: ''
      MASKV6: ''
    add_imsidt_list:
    - SUBRANGE: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
    add_imsidt_list_1:
    - SUBRANGE: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
    add_imsidt_list_2:
    - SUBRANGE: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
    add_imsidt_list_3:
    - SUBRANGE: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
    add_imsidt_list_4:
    - SUBRANGE: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
    add_imsidt_list_5:
    - SUBRANGE: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
    add_apnnidt_list:
    - APNNI: ''
    add_apnnidt_list_1:
    - APNNI: ''
    add_apnnidt_list_2:
    - APNNI: ''
    add_srroute_list:
    - VRFNAME: '_public_'
      AFTYPE: ipv4unicast
      PREFIX: '10.3.1.1'
      MASKLENGTH: 32
      DESTVRFNAME: '_public_'
      NEXTHOP: '10.4.1.1'
      IFNAME: 'NULL0'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开Direct Tunnel特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置SGSN。

### SGSN的Direct Tunnel配置，除个别参数外，与Indirect Tunnel配置无异。相关配置请参考“UNC产品文档 > 安装与调测 > 初始配置与调测”。

#### 3.1 添加支持Direct Tunnel的RNC。

```jinja2
{%- for item in add_rnc_list -%}
    ADD RNC:
    {#- --- 必选参数 --- -#}
    RNCX={{item.RNCX}},
    RNCMCC="{{item.RNCMCC}}",
    RNCMNC="{{item.RNCMNC}}",
    RNCID={{item.RNCID}},
    NI={{item.NI}},
    SPC="{{item.SPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.OTS is not none -%}
        OTS={{item.OTS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 参数“OTS”（RNC是否支持OneTunnel）选择“YES（支持）”。

#### 3.2 添加支持Direct Tunnel的GGSN。

```jinja2
{%- for item in add_ggsncharact_list -%}
    ADD GGSNCHARACT:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.OTS is not none -%}
        OTS={{item.OTS}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIAL_GGSN 时必选 --- -#}
    {%- if item.RANGE == 'SPECIAL_GGSN' -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        GGSNIPV4="{{item.GGSNIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        MASKV4="{{item.MASKV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        GGSNIPV6="{{item.GGSNIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        MASKV6={{item.MASKV6}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 参数“RANGE”（对端设备范围）选择“SPECIAL\_GGSN”。

#### 参数“IPT”（IP地址类型）选择“IPV4”。

#### 参数“OTS”（GGSN是否支持DirectTunnel）选择“YES（支持）”。

#### DT与UDG **GWFD-012100 Single IP**特性交互时，需要通过**ADD GGSNCHARACT**命令配置GGSN的Gn接口的SPU Group IP和SPU Instance IP。

#### 3.3 **可选：**增加IMSI DT属性配置信息。

#### 允许所有IMSI用户使用DT功能时，不需要配置该步骤。

#### 当需要指定IMSI用户开启或者关闭Direct Tunnel功能时，按照下面步骤配置。

##### 3.3.1 指定IMSI前缀的用户开启Direct Tunnel功能。

###### 3.3.1.1 关闭所有IMSI用户的Direct Tunnel功能。

```jinja2
{%- if is_optional_imsi_dt_attribute and is_scenario_imsi_prefix_enable -%}
    {%- for item in add_imsidt_list -%}
        ADD IMSIDT:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.3.1.2 打开指定IMSI前缀用户的Direct Tunnel功能。

```jinja2
{%- if is_optional_imsi_dt_attribute and is_scenario_imsi_prefix_enable -%}
    {%- for item in add_imsidt_list_1 -%}
        ADD IMSIDT:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.3.2 指定IMSI范围的用户开启Direct Tunnel功能。

###### 3.3.2.1 关闭所有IMSI用户的Direct Tunnel功能。

```jinja2
{%- if is_optional_imsi_dt_attribute and is_scenario_imsi_range_enable -%}
    {%- for item in add_imsidt_list_2 -%}
        ADD IMSIDT:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.3.2.2 打开指定IMSI范围用户的Direct Tunnel功能。

```jinja2
{%- if is_optional_imsi_dt_attribute and is_scenario_imsi_range_enable -%}
    {%- for item in add_imsidt_list_3 -%}
        ADD IMSIDT:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.3.3 指定IMSI前缀的用户关闭Direct Tunnel功能。

```jinja2
{%- if is_optional_imsi_dt_attribute and is_scenario_imsi_prefix_disable -%}
    {%- for item in add_imsidt_list_4 -%}
        ADD IMSIDT:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.3.4 指定IMSI范围的用户关闭Direct Tunnel功能。

```jinja2
{%- if is_optional_imsi_dt_attribute and is_scenario_imsi_range_disable -%}
    {%- for item in add_imsidt_list_5 -%}
        ADD IMSIDT:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 **可选：**增加APNNI DT属性配置信息。

#### 允许所有APN用户使用DT功能时，不需要配置该步骤。

#### 当需要指定APN用户开启或者关闭Direct Tunnel功能时，按照下面步骤配置。

##### 3.4.1 当需要指定APN用户开启Direct Tunnel功能时，先关闭所有APN用户的Direct Tunnel功能，再打开指定APN用户的Direct Tunnel功能。

##### 重复执行可以指定多个APN用户开启Direct Tunnel功能。

###### 3.4.1.1 关闭所有APN的Direct Tunnel功能。

```jinja2
{%- if is_optional_apnni_dt_attribute and is_scenario_apn_enable -%}
    {%- for item in add_apnnidt_list -%}
        ADD APNNIDT:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.4.1.2 打开指定APN的Direct Tunnel功能。

```jinja2
{%- if is_optional_apnni_dt_attribute and is_scenario_apn_enable -%}
    {%- for item in add_apnnidt_list_1 -%}
        ADD APNNIDT:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.4.2 指定APN用户关闭Direct Tunnel功能。

##### 重复执行可以指定多个APN用户关闭Direct Tunnel功能。

```jinja2
{%- if is_optional_apnni_dt_attribute and is_scenario_apn_disable -%}
    {%- for item in add_apnnidt_list_2 -%}
        ADD APNNIDT:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.5 两次执行**ADD SRROUTE**，分别配置到GGSN和到RNC的控制面路由。

```jinja2
{%- for item in add_srroute_list -%}
    ADD SRROUTE:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    PREFIX="{{item.PREFIX}}",
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.DESTVRFNAME is not none -%}
        DESTVRFNAME="{{item.DESTVRFNAME}}",
    {%- endif -%}
    {%- if item.NEXTHOP is not none -%}
        NEXTHOP="{{item.NEXTHOP}}",
    {%- endif -%}
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

