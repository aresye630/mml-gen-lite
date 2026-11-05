---
id: ''
name: 配置到AMF的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MME时，在配置完成MME到AMF的路由数据后，可通过配置N26接口数据建立MME到AMF的逻辑连接。  由于MME上N26接口与S10接口共用同一个接口实现，所以如果已经配置S10接口，不需要再配置N26接口的业务IP、GTP数据以及解析数据。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到AMF的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，在配置完成MME到AMF的路由数据后，可通过配置N26接口数据建立MME到AMF的逻辑连接。由于MME上N26接口与S10接口共用同一个接口实现，所以如果已经配置S10接口，不需要再配置N26接口的业务IP、GTP数据以及解析数据。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_serviceip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置业务IP参数'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcle_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置GTP-C本地实体。'
          data_source: ''
          pattern: ''
          default: 0
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ugtp_list:
      type: items
      properties:
        ICI:
          name: '空闲计数器扫描间隔（秒）'
          type: integer
          minimum: 60
          maximum: 1800
          required: false
          description: '配置GTP路径管理参数'
          data_source: ''
          pattern: ''
          default: ''
        SSI:
          name: 'SM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSI:
          name: 'MM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHVERCHKINT:
          name: '路径版本探测扫描周期（分钟）'
          type: integer
          minimum: 1
          maximum: 2400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcle_list_1:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置GTP-C本地实体。'
          data_source: ''
          pattern: ''
          default: 0
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ugtp_list_1:
      type: items
      properties:
        ICI:
          name: '空闲计数器扫描间隔（秒）'
          type: integer
          minimum: 60
          maximum: 1800
          required: false
          description: '配置GTP路径管理参数'
          data_source: ''
          pattern: ''
          default: ''
        SSI:
          name: 'SM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSI:
          name: 'MM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHVERCHKINT:
          name: '路径版本探测扫描周期（分钟）'
          type: integer
          minimum: 1
          maximum: 2400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcintfattr_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_NOID
          required: true
          description: '配置N26接口分离。'
          data_source: ''
          pattern: ''
          default: ''
        INTFTP:
          name: '接口类型'
          type: string
          enum:
          - ALL_INTERFACE
          - GN-GGSN/GP
          - GN-SGSN/S16
          - S10
          - S11
          - S3
          - S4
          - SV
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRPID:
          name: '组号'
          type: integer
          minimum: 1
          maximum: 32
          required: true
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
        INTFTP2:
          name: '接口类型2'
          type: string
          enum:
          - ALL_INTERFACE
          - GN-GGSN/GP
          - S11
          - S4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置AMF的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。HOSTNAME及FQDN格式定义详见配置Hostfile数据。如果对端AMF开启了MME-S10和AMF-N26接口地址合一功能，则注意此处的AMF IP地址与MME S10地址相同，需要修改MME上查询AMF的IPV4DNSH的地址为MME的GTPCLE地址。当配置对端AMF解析时，可以通过S10或N26选择AMF，S10和N26方式二选一。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR2:
          name: 'IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
    set_dns_list:
      type: items
      properties:
        N26DNSTYPE:
          name: 'N26DNSTYPE'
          type: string
          enum:
          - N26
          - S10
          required: false
          description: '配置LTE和5G网络互操作DNS查询方式，S10与N26方式二选一。如果运营商希望DNS查询AMF时采用N26标准方式，则配置为N26。如果运营商希望DNS查询AMF时采用S10标准方式，则配置为S10。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_dns_list_1:
      type: items
      properties:
        N26DNSTYPE:
          name: 'N26DNSTYPE'
          type: string
          enum:
          - N26
          - S10
          required: false
          description: '配置LTE和5G网络互操作DNS查询方式，S10与N26方式二选一。如果运营商希望DNS查询AMF时采用N26标准方式，则配置为N26。如果运营商希望DNS查询AMF时采用S10标准方式，则配置为S10。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ipv4dnsh_list_1:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置AMF的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。HOSTNAME及FQDN格式定义详见配置Hostfile数据。如果对端AMF开启了MME-S10和AMF-N26接口地址合一功能，则注意此处的AMF IP地址与MME S10地址相同，需要修改MME上查询AMF的IPV4DNSH的地址为MME的GTPCLE地址。当配置对端AMF解析时，可以通过S10或N26选择AMF，S10和N26方式二选一。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR2:
          name: 'IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipv4dnsh_list_2:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置AMF的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。HOSTNAME及FQDN格式定义详见配置Hostfile数据。如果对端AMF开启了MME-S10和AMF-N26接口地址合一功能，则注意此处的AMF IP地址与MME S10地址相同，需要修改MME上查询AMF的IPV4DNSH的地址为MME的GTPCLE地址。当配置对端AMF解析时，可以通过S10或N26选择AMF，S10和N26方式二选一。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list_2:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
    add_dnsn_list_4:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
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
    set_softparaofbit_list:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_n26iwkplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: '配置LTE和5G网络互操作策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IS5GCALLOW:
          name: '是否支持接入5GC'
          type: string
          enum:
          - NO
          - YES
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISNRALLOW:
          name: '是否允许接入5GS的NR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: YES
        SMFSELPLCY:
          name: '融合SMF+PGW-C选择策略'
          type: string
          enum:
          - CNR
          - N1CAP
          - N1CAP_CNR
          - RESV_PLCY1
          - RESV_PLCY2
          - RESV_PLCY3
          - RESV_PLCY4
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: N1CAP_CNR
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dns_list_2:
      type: items
      properties:
        NON5GSEL:
          name: '非5G用户是否选择到融合的SMF+PGW-C'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '限制非5G用户接入融合网关SMF+PGW-C。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_s1cmpt_list:
      type: items
      properties:
        NRRIN5GS:
          name: '是否携带NR Restriction in 5GS信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '配置S1接口兼容性参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CNR:
          name: '是否携带Core Network Type Restrictions信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_mmecharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_MME
          - COMB_AMF
          - SPECIAL_MME
          required: true
          description: '增加对端MME属性信息，配置S10接口兼容性参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UENRSECCAP:
          name: '是否携带UE NR安全能力'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_s1cmpt_list_1:
      type: items
      properties:
        GUAMIGUMMEI:
          name: '是否携带GUAMI映射的GUMMEI'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '可选，仅当在LTE和5G网络间重选的过程中需要优选AMF与MME融合部署的AMF时执行。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.17'
      VPNINSTNAME: 'VPN_CN'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_gtpcle_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.17'
      VPNNAME: 'VPN_CN'
      LEIPV6: ''
    set_ugtp_list:
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    add_gtpcle_list_1:
    - GROUPID: 3
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.17'
      VPNNAME: 'VPN_CN'
      LEIPV6: ''
    set_ugtp_list_1:
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    add_gtpcintfattr_list:
    - SUBRANGE: ALL_USER
      INTFTP: S10
      GRPID: 3
      IMSIPRE: ''
      INTFTP2: ''
      NOID: ''
    add_ipv4dnsh_list:
    - HSINDEX: 4
      HOSTNAME: 'topon.eth6.mmec14.mmegi8001.mme'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.10.1.1'
      IPV4ADDR2: '10.10.1.2'
    add_dnsn_list:
    - FQDN: 'MMEC14.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 4
      ENTITY: MME
      INTYPE: S10
      PRIORITY: 18
      WEIGHT: 112
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
    set_dns_list:
    - N26DNSTYPE: S10
    set_dns_list_1:
    - N26DNSTYPE: N26
    add_ipv4dnsh_list_1:
    - HSINDEX: 6
      HOSTNAME: 'topon.eth4.mmec12.mmegi8001.mme'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.11.1.3'
      IPV4ADDR2: '10.11.1.4'
    add_ipv4dnsh_list_2:
    - HSINDEX: 6
      HOSTNAME: 'topon.eth4.mmec12.mmegi8001.mme'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '192.168.140.17'
    add_dnsn_list_2:
    - FQDN: 'MMEC12.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 6
      ENTITY: MME
      INTYPE: S10
      PRIORITY: 20
      WEIGHT: 114
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
    add_dnsn_list_4:
    - FQDN: 'PT12.SET260.REGION31.AMFI.5GC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 6
      ENTITY: AMF
      INTYPE: N26
      PRIORITY: 20
      WEIGHT: 114
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
    set_licenseswitch_list:
    - LICITEM: 'LKV2NRBL5'
      SWITCH: ENABLE
    set_softparaofbit_list:
    - DT: BYTE_EX_B
      PARANUM: 5
      VALUE: VALUE_1
      POSITION: 8
    add_n26iwkplcy_list:
    - SUBRANGE: ALL_USER
      IS5GCALLOW: YES
      ISNRALLOW: YES
      SMFSELPLCY: N1CAP_CNR
      IMSIPRE: ''
      NOID: ''
    set_dns_list_2:
    - NON5GSEL: NO
    set_s1cmpt_list:
    - NRRIN5GS: YES
      CNR: YES
    add_mmecharact_list:
    - RANGE: ALL_MME
      UENRSECCAP: YES
      IPTYPE: ''
    set_s1cmpt_list_1:
    - GUAMIGUMMEI: YES
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置N26接口业务IP。

```jinja2
{%- for item in add_serviceip_list -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置GTP数据。

#### 3.1 配置N26接口与其他接口共部署时，GTPC本端实体对应的组号配置为0。

##### 3.1.1 配置MME在N26接口的GTPC IP。

```jinja2
{%- if is_scenario_n26_co_deploy -%}
    {%- for item in add_gtpcle_list -%}
        ADD GTPCLE:
        {#- --- 必选参数 --- -#}
        IPTYPE={{item.IPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GROUPID is not none -%}
            GROUPID={{item.GROUPID}},
        {%- endif -%}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            LEIPV4="{{item.LEIPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
            LEIPV6="{{item.LEIPV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.2 配置GTP路径管理参数。

```jinja2
{%- if is_scenario_n26_co_deploy -%}
    {%- for item in set_ugtp_list -%}
        SET UGTP:
        {#- --- 可选参数 --- -#}
        {%- if item.ICI is not none -%}
            ICI={{item.ICI}},
        {%- endif -%}
        {%- if item.SSI is not none -%}
            SSI={{item.SSI}},
        {%- endif -%}
        {%- if item.MSI is not none -%}
            MSI={{item.MSI}},
        {%- endif -%}
        {%- if item.PATHVERCHKINT is not none -%}
            PATHVERCHKINT={{item.PATHVERCHKINT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 当需要将N26接口与其他接口分离部署时，配置N26接口分离。此时将GTPC本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。

##### 3.2.1 配置MME在N26接口的GTPC IP。

```jinja2
{%- if is_scenario_n26_separate_deploy -%}
    {%- for item in add_gtpcle_list_1 -%}
        ADD GTPCLE:
        {#- --- 必选参数 --- -#}
        IPTYPE={{item.IPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GROUPID is not none -%}
            GROUPID={{item.GROUPID}},
        {%- endif -%}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            LEIPV4="{{item.LEIPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
            LEIPV6="{{item.LEIPV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.2 配置GTP路径管理参数。

```jinja2
{%- if is_scenario_n26_separate_deploy -%}
    {%- for item in set_ugtp_list_1 -%}
        SET UGTP:
        {#- --- 可选参数 --- -#}
        {%- if item.ICI is not none -%}
            ICI={{item.ICI}},
        {%- endif -%}
        {%- if item.SSI is not none -%}
            SSI={{item.SSI}},
        {%- endif -%}
        {%- if item.MSI is not none -%}
            MSI={{item.MSI}},
        {%- endif -%}
        {%- if item.PATHVERCHKINT is not none -%}
            PATHVERCHKINT={{item.PATHVERCHKINT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.3 配置GTPC接口属性。

```jinja2
{%- if is_scenario_n26_separate_deploy -%}
    {%- for item in add_gtpcintfattr_list -%}
        ADD GTPCINTFATTR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        GRPID={{item.GRPID}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=ALL_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'ALL_USER' -%}
            INTFTP={{item.INTFTP}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE/SPECIAL_NOID 时必选 --- -#}
        {%- if item.SUBRANGE in ['SPECIAL_IMSIPRE', 'SPECIAL_NOID'] -%}
            INTFTP2={{item.INTFTP2}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_NOID 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_NOID' -%}
            NOID={{item.NOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置本端MME的域名解析数据，包含在Inter Attach/TAU流程中根据GUTI值选择MME使用的DNS记录及在Inter Handover流程中根据TAI值选择MME使用的DNS记录。

```jinja2
{%- if is_optional_local_mme_dns_data -%}
    {%- for item in add_ipv4dnsh_list -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        {%- if item.IPV4ADDR2 is not none -%}
            IPV4ADDR2="{{item.IPV4ADDR2}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_local_mme_dns_data -%}
    {%- for item in add_dnsn_list -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置LTE和5G互操作DNS查询方式。

#### 5.1 //配置基于S10选择AMF（S10与N26方式二选一）：

```jinja2
{%- if is_scenario_s10 -%}
    {%- for item in set_dns_list -%}
        SET DNS:
        {#- --- 可选参数 --- -#}
        {%- if item.N26DNSTYPE is not none -%}
            N26DNSTYPE={{item.N26DNSTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 //配置基于N26选择AMF（S10与N26方式二选一）：

```jinja2
{%- if is_scenario_n26 -%}
    {%- for item in set_dns_list_1 -%}
        SET DNS:
        {#- --- 可选参数 --- -#}
        {%- if item.N26DNSTYPE is not none -%}
            N26DNSTYPE={{item.N26DNSTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 （可选）配置对端AMF的域名解析数据，包含在Inter Attach/TAU流程中根据GUTI值选择AMF使用的DNS记录及在Inter Handover流程中根据TAI值选择AMF使用的DNS记录。

#### 6.1 //当未对接DNS服务器，需要配置本地解析时，执行本操作。

```jinja2
{%- if is_optional_peer_amf_dns_data -%}
    {%- for item in add_ipv4dnsh_list_1 -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        {%- if item.IPV4ADDR2 is not none -%}
            IPV4ADDR2="{{item.IPV4ADDR2}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 //当未对接DNS服务器，需要配置本地解析，S10和N26地址合一时，执行本操作。

```jinja2
{%- if is_optional_peer_amf_dns_data and is_scenario_n26_s10_addr_unified -%}
    {%- for item in add_ipv4dnsh_list_2 -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.3 //配置基于S10选择AMF（S10与N26方式二选一）：

```jinja2
{%- if is_optional_peer_amf_dns_data and is_scenario_s10 -%}
    {%- for item in add_dnsn_list_2 -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.4 //配置基于N26选择AMF（S10与N26方式二选一）：

```jinja2
{%- if is_optional_peer_amf_dns_data and is_scenario_n26 -%}
    {%- for item in add_dnsn_list_4 -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 配置支持UE在LTE与5G SA网络间互操作。

#### 7.1 打开LTE与5G SA网络互操作特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 7.2 设置本特性必选软件参数。

```jinja2
{%- for item in set_softparaofbit_list -%}
    SET SOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    PARANUM={{item.PARANUM}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    ;
{%- endfor -%}
```

#### 7.3 配置LTE和5G网络互操作策略。

##### 7.3.1 增加互操作本地策略。

```jinja2
{%- for item in add_n26iwkplcy_list -%}
    ADD N26IWKPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    IS5GCALLOW={{item.IS5GCALLOW}},
    {#- --- 可选参数 --- -#}
    {%- if item.SMFSELPLCY is not none -%}
        SMFSELPLCY={{item.SMFSELPLCY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
    {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
        NOID={{item.NOID}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IS5GCALLOW=YES 时可选 --- -#}
    {%- if item.IS5GCALLOW == 'YES' -%}
        {%- if item.ISNRALLOW is not none -%}
            ISNRALLOW={{item.ISNRALLOW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 7.3.2 **可选：**如果需要限制非5G用户接入融合网关SMF+PGW-C，执行本步骤。

```jinja2
{%- if is_optional_restrict_non5g_users -%}
    {%- for item in set_dns_list_2 -%}
        SET DNS:
        {#- --- 可选参数 --- -#}
        {%- if item.NON5GSEL is not none -%}
            NON5GSEL={{item.NON5GSEL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.4 **可选：**配置S1接口兼容性参数。

```jinja2
{%- if is_optional_s1_compatibility_params -%}
    {%- for item in set_s1cmpt_list -%}
        SET S1CMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.NRRIN5GS is not none -%}
            NRRIN5GS={{item.NRRIN5GS}},
        {%- endif -%}
        {%- if item.CNR is not none -%}
            CNR={{item.CNR}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.5 **可选：**增加对端MME属性信息，配置S10接口兼容性参数。

```jinja2
{%- if is_optional_add_peer_mme_attributes -%}
    {%- for item in add_mmecharact_list -%}
        ADD MMECHARACT:
        {#- --- 必选参数 --- -#}
        RANGE={{item.RANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.UENRSECCAP is not none -%}
            UENRSECCAP={{item.UENRSECCAP}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RANGE=SPECIAL_MME 时必选 --- -#}
        {%- if item.RANGE == 'SPECIAL_MME' -%}
            IPTYPE={{item.IPTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.6 **可选：**（可选）配置在LTE和5G网络间重选的过程中优选AMF与MME融合部署的UAM。

```jinja2
{%- if is_optional_prefer_converged_amf_mme -%}
    {%- for item in set_s1cmpt_list_1 -%}
        SET S1CMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.GUAMIGUMMEI is not none -%}
            GUAMIGUMMEI={{item.GUAMIGUMMEI}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

