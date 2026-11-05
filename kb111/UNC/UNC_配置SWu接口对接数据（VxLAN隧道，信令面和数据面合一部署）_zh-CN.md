---
id: ''
name: 配置SWu接口对接数据（VxLAN隧道，信令面和数据面合一部署）
ne_type: UNC
type: feature
description: 专网UPF对接家庭网关、信令面和数据面合一部署场景下，信令面和数据面均采用swuif逻辑接口。该任务旨在指导操作人员完成UPF的SWu接口对接。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置一跳入家专网UPF","配置SWu接口对接数据（VxLAN隧道，信令面和数据面合一部署）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
专网UPF对接家庭网关、信令面和数据面合一部署场景下，信令面和数据面均采用swuif逻辑接口。该任务旨在指导操作人员完成UPF的SWu接口对接。

## 必备事项
前提条件

* UPF软件安装已完成。
* UPF初始配置已完成。
* 已完成一跳入家依赖功能的License加载。
* 运营商固网BRAS设备已经完成和专网UPF之间的VPN和路由配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '* SWu接口需重新规划VPN。 * 此VPN规划时不能与Home DNN的VPN重复'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_l3vpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '* SWu接口需重新规划VPN。 * 此VPN规划时不能与Home DNN的VPN重复'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_vpninstaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS2:
          name: '逻辑接口的IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '逻辑接口的IPv4掩码2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: '逻辑接口的IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ikeglobalconfig_list:
      type: items
      properties:
        DPDTYPE:
          name: 'DPD类型'
          type: string
          enum:
          - None
          - Periodic
          - Ondemand
          required: false
          description: '如需开启DPD功能，可配置该参数。'
          data_source: '固定值'
          pattern: ''
          default: ''
        DPDINTERVAL:
          name: 'DPD检查间隔（s）'
          type: integer
          minimum: 10
          maximum: 3600
          required: false
          description: '如需开启DPD功能，可配置该参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DPDRETRYINTRVL:
          name: 'DPD重试间隔（s）'
          type: integer
          minimum: 2
          maximum: 60
          required: false
          description: '如需开启DPD功能，可配置该参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_l3vpninstipsec_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vpninstafipsec_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - Ipv4uni
          - Ipv6uni
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_interfaceipsec_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFADMINSTATUS:
          name: '管理状态'
          type: string
          enum:
          - Down
          - Up
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipbindvpnipsec_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPTYPECHECK:
          name: '校验为V4还是V6'
          type: string
          enum:
          - Ipv4
          - Ipv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Ipv4
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBNETMASKIPV6:
          name: 'IPv6地址掩码'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ifipv4addressipsec_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IPv4地址类型'
          type: string
          enum:
          - Main
          - Sub
          - Brwd
          - Brw
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Main
    add_ikeproposal_list:
      type: items
      properties:
        PROPOSALNUMBER:
          name: '安全提议号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTHMETHOD:
          name: '认证方法'
          type: string
          enum:
          - Pre_share
          - Rsa_signature
          - Cert_signature
          - Digital_envelope
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Pre_share
        AUTHALGORITHM:
          name: '认证算法'
          type: string
          enum:
          - Md5
          - Sha1
          - Sha2_256
          - Sha2_384
          - Sha2_512
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Sha2_256
        ENCRALGORITHM:
          name: '加密算法'
          type: string
          enum:
          - Des_cbc
          - Aes_cbc_128
          - Aes_cbc_192
          - Aes_cbc_256
          - Alg_3Des_cbc
          - Aes_gcm_128
          - Aes_gcm_256
          - Sm4
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Aes_gcm_128
        INTEGALGORITHM:
          name: '完整性算法'
          type: string
          enum:
          - Hmac_md5_96
          - Hmac_sha1_96
          - Hmac_sha2_256
          - Hmac_sha2_384
          - Aes_xcbc_96
          - Sm3
          - Hmac_sha2_512
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Hmac_sha2_256
        DHGROUP:
          name: 'DH组'
          type: string
          enum:
          - None
          - Dh_group1
          - Dh_group2
          - Dh_group5
          - Dh_group14
          - Dh_group19
          - Dh_group20
          - Dh_group31
          required: false
          description: '推荐配置为Dh\_group1，性能最优。'
          data_source: '对端协商'
          pattern: ''
          default: Dh_group19
        ASYMENCRALG:
          name: '非对称加密算法'
          type: string
          enum:
          - 'NULL'
          - Sm2
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Sm2
        SIGHASHALGNEGSW:
          name: '签名哈希算法协商开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Enable
    add_ikepeer_list:
      type: items
      properties:
        PEERNAME:
          name: '对等体名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRESHAREDKEY:
          name: '预共享密钥'
          type: string
          minLength: 1
          maxLength: 127
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: ''
        EXCHANGEMODE:
          name: '交换模式'
          type: string
          enum:
          - Main
          - Aggressive
          required: false
          description: '-'
          data_source: '固定值'
          pattern: ''
          default: Main
        PROPOSAL:
          name: '安全提议'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALIDTYPE:
          name: '本地ID类型'
          type: string
          enum:
          - Ip
          - Fqdn
          - User_fqdn
          - Dn
          - Ip_disable
          required: false
          description: '-'
          data_source: '固定值'
          pattern: ''
          default: Ip
        VERSION1:
          name: '版本1'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '-'
          data_source: '固定值'
          pattern: ''
          default: TRUE
        VERSION2:
          name: '版本2'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '-'
          data_source: '固定值'
          pattern: ''
          default: TRUE
        DPDHASHSEQ:
          name: 'DPD载荷顺序'
          type: string
          enum:
          - Hash_notify
          - Notify_hash
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Hash_notify
        IKEMSGSYNC:
          name: '使能IKE消息序列号同步'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        IPSECMSGSYNC:
          name: '使能IPSEC消息序列号同步'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
    add_ipsecproposalipsec_list:
      type: items
      properties:
        PROPOSALNAME:
          name: 'Proposal名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPSECPROTOCOL:
          name: 'IPsec安全协议'
          type: string
          enum:
          - Ah
          - Esp
          - Ah_esp
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Esp
        ESPAUTHALGO:
          name: 'ESP认证算法'
          type: string
          enum:
          - Md5
          - Sha1
          - Sha2_256
          - Sha2_384
          - Sha2_512
          - 'Null'
          - Unconfigure
          - Sm3
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: 'Null'
        ESPENCRYPTALGO:
          name: 'ESP加密算法'
          type: string
          enum:
          - Des
          - A3des
          - Aes_128
          - Aes_192
          - Aes_256
          - Unconfigure
          - Sm4
          - Aes_gcm_128
          - Aes_gcm_256
          - Aes_gmac_128
          - 'Null'
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Aes_gcm_128
        ENCAPMODE:
          name: '封装模式'
          type: string
          enum:
          - Transport
          - Tunnel
          required: false
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: Tunnel
        AHAUTHALGO:
          name: 'AH认证算法'
          type: string
          enum:
          - Md5
          - Sha1
          - Sha2_256
          - Sha2_384
          - Sha2_512
          - Unconfigure
          - Sm3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Sha2_256
    add_ipsecpolicytm_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略模板名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEQUENCENUMBER:
          name: '策略模板序列号'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERNAME:
          name: '对等体名称'
          type: string
          minLength: 0
          maxLength: 15
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPSECPROPNAME:
          name: 'IPsec安全提议名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TRAFFSADISFLG:
          name: '去使能SA按流量计长'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLTYPE:
          name: 'ACL类型'
          type: string
          enum:
          - AclIPv4
          - AclIPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TFCENABLE:
          name: '数据流可信使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SALIFETIMEKB:
          name: 'SA按流量计长 (mbyte)'
          type: integer
          minimum: 8000
          maximum: 200000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipsecpolicy_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEQUENCENUMBER:
          name: '序列号'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: ''
        POLICYMODE:
          name: '策略模式'
          type: string
          enum:
          - Isakmp
          required: true
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: ''
        TEMPLATEMODE:
          name: '模板模式'
          type: string
          enum:
          - None
          - PolicyTemplate
          required: true
          description: '-'
          data_source: '对端协商'
          pattern: ''
          default: ''
        TEMPLATENAME:
          name: '策略模板名称'
          type: string
          minLength: 0
          maxLength: 15
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLNAME:
          name: 'ACL名称'
          type: string
          minLength: 1
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLNUMBER:
          name: 'ACL编号'
          type: integer
          minimum:
          - 3000
          - 0
          maximum:
          - 3999
          - 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLTYPE:
          name: 'ACL类型'
          type: string
          enum:
          - AclIPv4
          - AclIPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AclIPv4
        ANTIREPLAYENUM:
          name: '抗重放'
          type: string
          enum:
          - NotConfigured
          - Enable
          - Disable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NotConfigured
        DFBITCLEAR:
          name: '清除分片标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        DSCPINSELECT:
          name: '选择DSCP入方向值'
          type: string
          enum:
          - Af11
          - Af12
          - Af13
          - Af21
          - Af22
          - Af23
          - Af31
          - Af32
          - Af33
          - Af41
          - Af42
          - Af43
          - Cs1
          - Cs2
          - Cs3
          - Cs4
          - Cs5
          - Cs6
          - Cs7
          - Default
          - Ef
          - None
          - EnterDSCPCode
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSCPOUTSELECT:
          name: '选择DSCP出方向值'
          type: string
          enum:
          - Af11
          - Af12
          - Af13
          - Af21
          - Af22
          - Af23
          - Af31
          - Af32
          - Af33
          - Af41
          - Af42
          - Af43
          - Cs1
          - Cs2
          - Cs3
          - Cs4
          - Cs5
          - Cs6
          - Cs7
          - Default
          - Ef
          - None
          - EnterDSCPCode
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ESN:
          name: '扩展序列号'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        FRAGBEFOREENCR:
          name: '加密前分片报文'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        INSPEEDLIMIT:
          name: '入方向限速 (kbyte/s)'
          type: integer
          minimum:
          - 8
          - 0
          maximum:
          - 4194303
          - 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOGENABLE:
          name: '日志使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OUTSPEEDLIMIT:
          name: '出方向限速 (kbyte/s)'
          type: integer
          minimum:
          - 8
          - 0
          maximum:
          - 4194303
          - 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PFS:
          name: 'PFS'
          type: string
          enum:
          - None
          - Dh_group1
          - Dh_group2
          - Dh_group5
          - Dh_group14
          - Dh_group19
          - Dh_group20
          - Dh_group31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SALIFETIMESEC:
          name: 'SA按时计长 (s)'
          type: integer
          minimum:
          - 0
          - 480
          maximum:
          - 0
          - 604800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TFCENABLE:
          name: '数据流可信使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TRAFFSADISFLG:
          name: '去使能SA按流量计长'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        WORKMODE:
          name: '工作模式'
          type: string
          enum:
          - Round_robin
          - Master_standby
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Round_robin
    add_ipsecintfcfgipsec_list:
      type: items
      properties:
        INTERFACENAME:
          name: '接口名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNLTYPE:
          name: 'Tunnel口协议类型'
          type: string
          enum:
          - IPSEC
          - IPSEC6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 1
          maxLength: 15
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_tohvxlanpara_list:
      type: items
      properties:
        VXLANTNLSW:
          name: 'VXLAN隧道开关'
          type: string
          required: false
          description: '-'
          data_source: '固定值'
          pattern: ''
          default: ''
        SRCMAC:
          name: 'VXLAN隧道源端MAC地址'
          type: string
          required: false
          description: '* 推荐使用单播地址，不允许使用组播地址。 * 为了避免和其他网元MAC地址冲突，推荐使用本端网元外联口的MAC地址。可通过LST INTERFACE命令查询，取任意一个外联口的MAC地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VGWIPV4ADDR:
          name: '虚拟网关IPv4地址'
          type: string
          required: false
          description: '向家庭网关发送免费ARP时作为虚拟网关地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_upnon3gpppara_list:
      type: items
      properties:
        SWUWAL:
          name: 'SWU接口UE接入速率'
          type: string
          required: false
          description: '控制IKE协商速率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AGINGTIME:
          name: '老化时长'
          type: string
          required: false
          description: '* 用于配置ToH SESSION的老化时长。配置为0时，表示不开启老化。 * 主UPF不配置老化时长，备UPF配置老化时长为1440分钟。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_upnon3gpppara_list_1:
      type: items
      properties:
        SWUWAL:
          name: 'SWU接口UE接入速率'
          type: string
          required: false
          description: '控制IKE协商速率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AGINGTIME:
          name: '老化时长'
          type: string
          required: false
          description: '* 用于配置ToH SESSION的老化时长。配置为0时，表示不开启老化。 * 主UPF不配置老化时长，备UPF配置老化时长为1440分钟。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_SWu'
    add_l3vpninst_list:
    - VRFNAME: 'VPN_SWu'
    add_vpninstaf_list:
    - VRFNAME: 'VPN_SWu'
      AFTYPE: ipv4uni
    add_logicinf_list:
    - NAME: 'swuif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '192.168.1.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_SWu'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    set_ikeglobalconfig_list:
    - DPDTYPE: Periodic
      DPDINTERVAL: 60
      DPDRETRYINTRVL: 3
    add_l3vpninstipsec_list:
    - VRFNAME: 'VPN_SWu'
    add_vpninstafipsec_list:
    - VRFNAME: 'VPN_SWu'
      AFTYPE: ipv4uni
    add_interfaceipsec_list:
    - IFNAME: 'Tunnel10'
      IFADMINSTATUS: Up
    add_ipbindvpnipsec_list:
    - IFNAME: 'Tunnel10'
      VRFNAME: 'VPN_SWu'
      IPTYPECHECK: Ipv4
      IFIPADDR: ''
      IPV6ADDR: ''
      SUBNETMASK: ''
      SUBNETMASKIPV6: ''
    add_ifipv4addressipsec_list:
    - IFNAME: 'Tunnel10'
      IFIPADDR: '192.168.1.1'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: Main
    add_ikeproposal_list:
    - PROPOSALNUMBER: 1
      AUTHMETHOD: Pre_share
      AUTHALGORITHM: Sha2_256
      ENCRALGORITHM: Aes_cbc_128
      INTEGALGORITHM: Hmac_sha2_256
      DHGROUP: Dh_group1
      ASYMENCRALG: Sm2
      SIGHASHALGNEGSW: Enable
    add_ikepeer_list:
    - PEERNAME: 'peer1'
      PRESHAREDKEY: 'abcde'
      EXCHANGEMODE: Main
      PROPOSAL: 1
      LOCALIDTYPE: Fqdn
      VERSION1: FALSE
      VERSION2: TRUE
      DPDHASHSEQ: Hash_notify
      IKEMSGSYNC: Disable
      IPSECMSGSYNC: Disable
    add_ipsecproposalipsec_list:
    - PROPOSALNAME: 'asdf2'
      IPSECPROTOCOL: Esp
      ESPAUTHALGO: Sha2_256
      ESPENCRYPTALGO: Aes_256
      ENCAPMODE: Tunnel
      AHAUTHALGO: Sha2_256
    add_ipsecpolicytm_list:
    - POLICYNAME: 'ipsecply2tm'
      SEQUENCENUMBER: 10
      PEERNAME: 'peer1'
      IPSECPROPNAME: 'asdf2'
      TRAFFSADISFLG: FALSE
      ACLTYPE: AclIPv4
      TFCENABLE: TRUE
      SALIFETIMEKB: ''
    add_ipsecpolicy_list:
    - POLICYNAME: 'ipsecply2'
      SEQUENCENUMBER: 10
      POLICYMODE: Isakmp
      TEMPLATEMODE: PolicyTemplate
      TEMPLATENAME: 'ipsecply2tm'
      ACLNAME: ''
      ACLNUMBER: ''
      ACLTYPE: AclIPv4
      ANTIREPLAYENUM: NotConfigured
      DFBITCLEAR: FALSE
      DSCPINSELECT: ''
      DSCPOUTSELECT: ''
      ESN: Disable
      FRAGBEFOREENCR: FALSE
      INSPEEDLIMIT: ''
      LOGENABLE: FALSE
      OUTSPEEDLIMIT: ''
      PFS: ''
      SALIFETIMESEC: ''
      TFCENABLE: FALSE
      TRAFFSADISFLG: FALSE
      WORKMODE: Round_robin
    add_ipsecintfcfgipsec_list:
    - INTERFACENAME: 'Tunnel10'
      TNLTYPE: IPSEC
      POLICYNAME: 'ipsecply2'
    set_tohvxlanpara_list:
    - VXLANTNLSW: ENABLE
      SRCMAC: FA-16-3E-CB-D1-FA
      VGWIPV4ADDR: 192.168.12.33
    set_upnon3gpppara_list:
    - SWUWAL: '1000'
      AGINGTIME: '0'
    set_upnon3gpppara_list_1:
    - SWUWAL: '1000'
      AGINGTIME: '1440'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 创建VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 2 创建L3VPN实例。

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

### 3 配置swuif逻辑接口，VPN实例名称为VPN\_SWu。

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4ADDRESS2 is not none -%}
            IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MASK2 is not none -%}
            IPV4MASK2="{{item.IPV4MASK2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置IKE。

#### 4.1 配置DPD功能。

```jinja2
{%- for item in set_ikeglobalconfig_list -%}
    SET IKEGLOBALCONFIG:
    {#- --- 可选参数 --- -#}
    {%- if item.DPDTYPE is not none -%}
        DPDTYPE={{item.DPDTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DPDTYPE=Periodic/Ondemand 时必选 --- -#}
    {%- if item.DPDTYPE in ['Periodic', 'Ondemand'] -%}
        DPDINTERVAL={{item.DPDINTERVAL}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DPDTYPE=Periodic/Ondemand 时可选 --- -#}
    {%- if item.DPDTYPE in ['Periodic', 'Ondemand'] -%}
        {%- if item.DPDRETRYINTRVL is not none -%}
            DPDRETRYINTRVL={{item.DPDRETRYINTRVL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 创建IPsec隧道接口，绑定VPN并配置IP地址。IKE认证需要该配置。

```jinja2
{%- for item in add_l3vpninstipsec_list -%}
    ADD L3VPNINSTIPSEC:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstafipsec_list -%}
    ADD VPNINSTAFIPSEC:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_interfaceipsec_list -%}
    ADD INTERFACEIPSEC:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IFADMINSTATUS is not none -%}
        IFADMINSTATUS={{item.IFADMINSTATUS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ipbindvpnipsec_list -%}
    ADD IPBINDVPNIPSEC:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPTYPECHECK is not none -%}
        IPTYPECHECK={{item.IPTYPECHECK}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPTYPECHECK=Ipv4 时可选 --- -#}
    {%- if item.IPTYPECHECK == 'Ipv4' -%}
        {%- if item.IFIPADDR is not none -%}
            IFIPADDR="{{item.IFIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPECHECK=Ipv6 时可选 --- -#}
    {%- if item.IPTYPECHECK == 'Ipv6' -%}
        {%- if item.IPV6ADDR is not none -%}
            IPV6ADDR="{{item.IPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPECHECK=Ipv4 时可选 --- -#}
    {%- if item.IPTYPECHECK == 'Ipv4' -%}
        {%- if item.SUBNETMASK is not none -%}
            SUBNETMASK="{{item.SUBNETMASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPTYPECHECK=Ipv6 时可选 --- -#}
    {%- if item.IPTYPECHECK == 'Ipv6' -%}
        {%- if item.SUBNETMASKIPV6 is not none -%}
            SUBNETMASKIPV6="{{item.SUBNETMASKIPV6}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4addressipsec_list -%}
    ADD IFIPV4ADDRESSIPSEC:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 增加IKE安全提议号为1的IKE安全提议。

```jinja2
{%- for item in add_ikeproposal_list -%}
    ADD IKEPROPOSAL:
    {#- --- 必选参数 --- -#}
    PROPOSALNUMBER={{item.PROPOSALNUMBER}},
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHMETHOD is not none -%}
        AUTHMETHOD={{item.AUTHMETHOD}},
    {%- endif -%}
    {%- if item.AUTHALGORITHM is not none -%}
        AUTHALGORITHM={{item.AUTHALGORITHM}},
    {%- endif -%}
    {%- if item.ENCRALGORITHM is not none -%}
        ENCRALGORITHM={{item.ENCRALGORITHM}},
    {%- endif -%}
    {%- if item.INTEGALGORITHM is not none -%}
        INTEGALGORITHM={{item.INTEGALGORITHM}},
    {%- endif -%}
    {%- if item.DHGROUP is not none -%}
        DHGROUP={{item.DHGROUP}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTHMETHOD=Digital_envelope 时必选 --- -#}
    {%- if item.AUTHMETHOD == 'Digital_envelope' -%}
        ASYMENCRALG={{item.ASYMENCRALG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AUTHMETHOD=Cert_signature 时可选 --- -#}
    {%- if item.AUTHMETHOD == 'Cert_signature' -%}
        {%- if item.SIGHASHALGNEGSW is not none -%}
            SIGHASHALGNEGSW={{item.SIGHASHALGNEGSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.4 增加名称为“peer1”的IKE对等体，同时指定交换模式为main模式，IKE版本1为FALSE，IKE版本2为TRUE，LOCALIDTYPE为FQDN。

```jinja2
{%- for item in add_ikepeer_list -%}
    ADD IKEPEER:
    {#- --- 必选参数 --- -#}
    PEERNAME="{{item.PEERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRESHAREDKEY is not none -%}
        PRESHAREDKEY="{{item.PRESHAREDKEY}}",
    {%- endif -%}
    {%- if item.EXCHANGEMODE is not none -%}
        EXCHANGEMODE={{item.EXCHANGEMODE}},
    {%- endif -%}
    {%- if item.PROPOSAL is not none -%}
        PROPOSAL={{item.PROPOSAL}},
    {%- endif -%}
    {%- if item.LOCALIDTYPE is not none -%}
        LOCALIDTYPE={{item.LOCALIDTYPE}},
    {%- endif -%}
    {%- if item.VERSION1 is not none -%}
        VERSION1={{item.VERSION1}},
    {%- endif -%}
    {%- if item.VERSION2 is not none -%}
        VERSION2={{item.VERSION2}},
    {%- endif -%}
    {%- if item.DPDHASHSEQ is not none -%}
        DPDHASHSEQ={{item.DPDHASHSEQ}},
    {%- endif -%}
    {%- if item.IKEMSGSYNC is not none -%}
        IKEMSGSYNC={{item.IKEMSGSYNC}},
    {%- endif -%}
    {%- if item.IPSECMSGSYNC is not none -%}
        IPSECMSGSYNC={{item.IPSECMSGSYNC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.5 增加名称为“asdf2”的IPsec安全提议。

```jinja2
{%- for item in add_ipsecproposalipsec_list -%}
    ADD IPSECPROPOSALIPSEC:
    {#- --- 必选参数 --- -#}
    PROPOSALNAME="{{item.PROPOSALNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPSECPROTOCOL is not none -%}
        IPSECPROTOCOL={{item.IPSECPROTOCOL}},
    {%- endif -%}
    {%- if item.ENCAPMODE is not none -%}
        ENCAPMODE={{item.ENCAPMODE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPSECPROTOCOL=Esp/Ah_esp 时可选 --- -#}
    {%- if item.IPSECPROTOCOL in ['Esp', 'Ah_esp'] -%}
        {%- if item.ESPAUTHALGO is not none -%}
            ESPAUTHALGO={{item.ESPAUTHALGO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPSECPROTOCOL=Esp/Ah_esp 时可选 --- -#}
    {%- if item.IPSECPROTOCOL in ['Esp', 'Ah_esp'] -%}
        {%- if item.ESPENCRYPTALGO is not none -%}
            ESPENCRYPTALGO={{item.ESPENCRYPTALGO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPSECPROTOCOL=Ah/Ah_esp 时可选 --- -#}
    {%- if item.IPSECPROTOCOL in ['Ah', 'Ah_esp'] -%}
        {%- if item.AHAUTHALGO is not none -%}
            AHAUTHALGO={{item.AHAUTHALGO}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.6 增加IPSec策略模板。

```jinja2
{%- for item in add_ipsecpolicytm_list -%}
    ADD IPSECPOLICYTM:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    SEQUENCENUMBER={{item.SEQUENCENUMBER}},
    PEERNAME="{{item.PEERNAME}}",
    IPSECPROPNAME="{{item.IPSECPROPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TRAFFSADISFLG is not none -%}
        TRAFFSADISFLG={{item.TRAFFSADISFLG}},
    {%- endif -%}
    {%- if item.ACLTYPE is not none -%}
        ACLTYPE={{item.ACLTYPE}},
    {%- endif -%}
    {%- if item.TFCENABLE is not none -%}
        TFCENABLE={{item.TFCENABLE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TRAFFSADISFLG=FALSE 时可选 --- -#}
    {%- if item.TRAFFSADISFLG == 'FALSE' -%}
        {%- if item.SALIFETIMEKB is not none -%}
            SALIFETIMEKB={{item.SALIFETIMEKB}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.7 增加IPSec安全策略POLICY。

```jinja2
{%- for item in add_ipsecpolicy_list -%}
    ADD IPSECPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    SEQUENCENUMBER={{item.SEQUENCENUMBER}},
    POLICYMODE={{item.POLICYMODE}},
    TEMPLATEMODE={{item.TEMPLATEMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TEMPLATEMODE=PolicyTemplate 时必选 --- -#}
    {%- if item.TEMPLATEMODE == 'PolicyTemplate' -%}
        TEMPLATENAME="{{item.TEMPLATENAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.ACLNAME is not none -%}
            ACLNAME="{{item.ACLNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.ACLNUMBER is not none -%}
            ACLNUMBER={{item.ACLNUMBER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.ACLTYPE is not none -%}
            ACLTYPE={{item.ACLTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.ANTIREPLAYENUM is not none -%}
            ANTIREPLAYENUM={{item.ANTIREPLAYENUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.DFBITCLEAR is not none -%}
            DFBITCLEAR={{item.DFBITCLEAR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.DSCPINSELECT is not none -%}
            DSCPINSELECT={{item.DSCPINSELECT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.DSCPOUTSELECT is not none -%}
            DSCPOUTSELECT={{item.DSCPOUTSELECT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.ESN is not none -%}
            ESN={{item.ESN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.FRAGBEFOREENCR is not none -%}
            FRAGBEFOREENCR={{item.FRAGBEFOREENCR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.INSPEEDLIMIT is not none -%}
            INSPEEDLIMIT={{item.INSPEEDLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.LOGENABLE is not none -%}
            LOGENABLE={{item.LOGENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.OUTSPEEDLIMIT is not none -%}
            OUTSPEEDLIMIT={{item.OUTSPEEDLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.PFS is not none -%}
            PFS={{item.PFS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.SALIFETIMESEC is not none -%}
            SALIFETIMESEC={{item.SALIFETIMESEC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.TFCENABLE is not none -%}
            TFCENABLE={{item.TFCENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.TRAFFSADISFLG is not none -%}
            TRAFFSADISFLG={{item.TRAFFSADISFLG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TEMPLATEMODE=None 时可选 --- -#}
    {%- if item.TEMPLATEMODE == 'None' -%}
        {%- if item.WORKMODE is not none -%}
            WORKMODE={{item.WORKMODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.8 tunnel口绑定POLICY。

```jinja2
{%- for item in add_ipsecintfcfgipsec_list -%}
    ADD IPSECINTFCFGIPSEC:
    {#- --- 必选参数 --- -#}
    INTERFACENAME="{{item.INTERFACENAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.POLICYNAME is not none -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置家庭网关业务使用VxLAN隧道传输业务参数。注意MAC地址不可和其他网元冲突。SRCINTF默认值为swuif1/0/0。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_tohvxlanpara_list的变量区（command: SET TOHVXLANPARA） -#}
<!-- MISSING_MACRO: command=SET TOHVXLANPARA list_name=set_tohvxlanpara_list step_id=5 -->
```

### 6 设置SWu接口UE接入速率和UPF老化时长。

#### 6.1 主UPF配置，设置SWu接口UE接入速率为1000个/s，老化时长为0：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_upnon3gpppara_list的变量区（command: SET UPNON3GPPPARA） -#}
<!-- MISSING_MACRO: command=SET UPNON3GPPPARA list_name=set_upnon3gpppara_list step_id=6.1 -->
```

#### 6.2 备UPF配置，设置SWu接口UE接入速率为1000个/s，老化时长为1440：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_upnon3gpppara_list_1的变量区（command: SET UPNON3GPPPARA） -#}
<!-- MISSING_MACRO: command=SET UPNON3GPPPARA list_name=set_upnon3gpppara_list_1 step_id=6.2 -->
```

