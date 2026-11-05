---
id: ''
name: 配置用户数据文件同步
ne_type: UEG
type: feature
description: 5G 2B解决方案中，用户数据不出园区。需要园区UDM处理用户业务。但为了简化运维，支持园区用户在中心UDM开户，园区UDM从中心UDM同步数据。该场景下，需要配置本页面。  配置后，园区UDM支持定时自动从SFTP服务器同步用户数据文件。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置UDM/HSS","配置用户数据同步","配置用户数据文件同步"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置UDM/HSS","配置用户数据同步","配置用户数据文件同步"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置UDM/HSS","配置用户数据同步","配置用户数据文件同步"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools:
- getParameterValue('ADD RDATASYNSERVER')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
5G 2B解决方案中，用户数据不出园区。需要园区UDM处理用户业务。但为了简化运维，支持园区用户在中心UDM开户，园区UDM从中心UDM同步数据。该场景下，需要配置本页面。配置后，园区UDM支持定时自动从SFTP服务器同步用户数据文件。

## 必备事项
前提条件

具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_vpninfo_list:
      type: items
      properties:
        VPNINFONAME:
          name: 'VPNINFO名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '用于标识对外IP使用的VPN配置的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '与外联口的VRF名称相同。  该参数必须先由**ADD L3VPNINST**命令定义后才能在此处引用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNID:
          name: 'VPN ID'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '用于标识VPN ID配置信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_edgeudmip_list:
      type: items
      properties:
        IPNAME:
          name: 'IP地址名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '存在多条记录时，“IPNAME+IPTYPE”不能重复。  配置的IP用于用户数据文件同步。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址的类型'
          type: string
          enum:
          - DSM
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: '本端IP，用户访问SFTP服务器。  远端采用IPv6地址与本端互通时，请规划IPv6地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 1500
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '采用**ADD VPNINFO**命令定义的“VPNNAME”参数值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rdatasynserver_list:
      type: items
      properties:
        SERVERNAME:
          name: '服务器名称'
          type: string
          minLength: 0
          maxLength: 16
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GROUPID:
          name: '服务器组ID'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: 'SFTP服务器所属的服务器组ID。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PRIORITY:
          name: '服务器优先级'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '优先级值越小，优先级越高。同一服务器组内服务器间的优先级必须不同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROTOCOL:
          name: '传输协议类型'
          type: string
          enum:
          - SFTP
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: SFTP
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '远端SFTP服务器的IP地址和端口号。此处以IPv4为例。  远端采用IPv6地址与本端互通时，请规划IPv6地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVERIPV4:
          name: '服务端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SERVERPORT:
          name: '服务器端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 22
        USERNAME:
          name: '用户名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '访问SFTP服务器某一路径的用户名。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        AUTHTYPE:
          name: '认证模式'
          type: string
          enum:
          - PASSWORD
          - PUBLICKEY
          required: true
          description: '“认证模式”包括“PASSWORD”和“PUBLICKEY”。  当希望获取更好的安全性时请选择公钥认证，公钥认证时须通过**LOD RDATASYNUSERKEY**加载密钥。'
          data_source: '与对端协商'
          pattern: ''
          default: PASSWORD
        PWD:
          name: '密码'
          type: string
          minLength: 0
          maxLength: 433
          required: false
          description: '“认证模式”设置为“PASSWORD”时规划。  “认证模式”设置为“PUBLICKEY”时不需要规划。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PWDCFM:
          name: '确认密码'
          type: string
          minLength: 0
          maxLength: 433
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        RWORKDIR:
          name: '远端工作目录'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: 'SFTP服务器存放用户数据文件的路径。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DETECTSWITCH:
          name: '探测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '园区UDM定时探测该SFTP服务器是否故障时，设置为“ENABLE”；否则设置为“DISABLE”。  此处以园区UDM定时探测该SFTP服务器是否故障为例。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
    add_rdatasynserver_list_1:
      type: items
      properties:
        SERVERNAME:
          name: '服务器名称'
          type: string
          minLength: 0
          maxLength: 16
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GROUPID:
          name: '服务器组ID'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: 'SFTP服务器所属的服务器组ID。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PRIORITY:
          name: '服务器优先级'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '优先级值越小，优先级越高。同一服务器组内服务器间的优先级必须不同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROTOCOL:
          name: '传输协议类型'
          type: string
          enum:
          - SFTP
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: SFTP
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '远端SFTP服务器的IP地址和端口号。此处以IPv4为例。  远端采用IPv6地址与本端互通时，请规划IPv6地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVERIPV4:
          name: '服务端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SERVERPORT:
          name: '服务器端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 22
        USERNAME:
          name: '用户名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '访问SFTP服务器某一路径的用户名。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        AUTHTYPE:
          name: '认证模式'
          type: string
          enum:
          - PASSWORD
          - PUBLICKEY
          required: true
          description: '“认证模式”包括“PASSWORD”和“PUBLICKEY”。  当希望获取更好的安全性时请选择公钥认证，公钥认证时须通过**LOD RDATASYNUSERKEY**加载密钥。'
          data_source: '与对端协商'
          pattern: ''
          default: PASSWORD
        RWORKDIR:
          name: '远端工作目录'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: 'SFTP服务器存放用户数据文件的路径。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DETECTSWITCH:
          name: '探测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '园区UDM定时探测该SFTP服务器是否故障时，设置为“ENABLE”；否则设置为“DISABLE”。  此处以园区UDM定时探测该SFTP服务器是否故障为例。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        PWD:
          name: '密码'
          type: string
          minLength: 0
          maxLength: 433
          required: false
          description: '“认证模式”设置为“PASSWORD”时规划。  “认证模式”设置为“PUBLICKEY”时不需要规划。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PWDCFM:
          name: '确认密码'
          type: string
          minLength: 0
          maxLength: 433
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    lod_rdatasynuserkey_list:
      type: items
      properties:
        SERVERNAME:
          name: '服务器名称'
          type: string
          minLength: 0
          maxLength: 16
          required: true
          description: '采用**ADD RDATASYNSERVER**命令定义的服务器名称参数值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        USERNAME:
          name: '用户名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '采用**ADD RDATASYNSERVER**命令定义的用户名称参数值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        KEYNAME:
          name: '密钥名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '存在多条记录时，SERVERNAME + USERNAME + KEYNAME不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PUBKEYFILE:
          name: '公钥文件名'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '与待加载的公钥文件名一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIVATEKEYFILE:
          name: '私钥文件名'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '与待加载的私钥文件名一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIVATEKEYPWD:
          name: '私钥文件解密密码'
          type: string
          minLength: 0
          maxLength: 433
          required: true
          description: '私钥文件的解密密码。解密密码正确时，加载后密钥状态才会是“正常”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_rsftpfirsttime_list:
      type: items
      properties:
        FIRSTTIMEENABLE:
          name: '首次认证使能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '园区UDM认证SFTP服务器的公钥时，设置为“DISABLE”；否则，设置为“ENABLE”。  设置为“ENABLE”时，不需要规划SFTP服务器的公钥（**ADD RSFTPPUBLICKEY**）。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rsftppublickey_list:
      type: items
      properties:
        KEYNAME:
          name: '密钥名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PUBKEYTYPE:
          name: '密钥类型'
          type: string
          enum:
          - ECDSA
          - RSA
          required: true
          description: '与SFTP服务器的公钥信息一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        KEYCODE:
          name: '密钥'
          type: string
          minLength: 0
          maxLength: 1024
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ENCODETYPE:
          name: '编码类型'
          type: string
          enum:
          - OPENSSH
          - PEM
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: PEM
    add_rsftpbindpublickey_list:
      type: items
      properties:
        SERVERNAME:
          name: '服务器名称'
          type: string
          minLength: 0
          maxLength: 16
          required: true
          description: '采用**ADD RDATASYNSERVER**命令定义的服务器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        KEYNAME:
          name: '密钥名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '采用**ADD RSFTPPUBLICKEY**命令定义的密钥名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_rsftpfirsttime_list_1:
      type: items
      properties:
        FIRSTTIMEENABLE:
          name: '首次认证使能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_edgedspolicy_list:
      type: items
      properties:
        CYCLE:
          name: '获取周期'
          type: string
          minLength: 0
          maxLength: 15
          required: false
          description: '同步用户数据的周期。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        STARTTIME:
          name: '开始时间'
          type: string
          minLength: 0
          maxLength: 5
          required: false
          description: '数据同步起始时间要避开业务高峰期。  多个园区UDM从同一SFTP服务器（中心UDM或外置SFTP服务器）同步用户数据时，建议合理规划开始时间，避免对SFTP服务器造成冲击。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDTIME:
          name: '结束时间'
          type: string
          minLength: 0
          maxLength: 5
          required: false
          description: '允许和开始时间跨天。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RETRYINTVL:
          name: '重试间隔'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '尝试重新建立SFTP连接的时间间隔。在当前周期结束时间到达之前，如SFTP连接未建立成功，SFTP Client会持续按照RETRYINTVL时间间隔尝试重新建立SFTP连接。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ALMTHESTIMES:
          name: '连续链接失败告警阈值'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: '连续尝试连接SFTP服务器3次不成功，上报SFTP失败告警。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FILTERPREFIX:
          name: '文件名前缀匹配条件'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '用于定义用户数据文件名格式，当SFTP服务器上的用户数据文件名与此处配置的文件名规则匹配时，UDM才能成功从SFTP服务器同步用户数据文件。   * “PREFIXFORMAT”设置为“Common”时，SFTP服务器上的用户数据文件名格式为“园区描述”+分隔符+“自定义描述”+分隔符+“日期时间（格式YYYYMMDDHHMMSS）”+分隔符+“文件序号”。 * “PREFIXFORMAT”设置为“Custom1”时，SFTP服务器上的用户数据文件名格式为”园区描述”+分隔符+“序号”+分隔符+“导出时间戳（格式YYYYMMDDHHMMSS）”+分隔符+ “备注”。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        FILTERSUFFIX:
          name: '文件名后缀匹配条件'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '固定配置'
          pattern: ''
          default: ''
        PREFIXSEPARATOR:
          name: '文件名前缀分隔符'
          type: string
          minLength: 0
          maxLength: 1
          required: false
          description: ''
          data_source: '固定配置'
          pattern: ''
          default: ''
        PREFIXFORMAT:
          name: '文件名前缀的格式'
          type: string
          enum:
          - Common
          - Custom1
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        FILEEXPIRE:
          name: '文件老化时间'
          type: integer
          minimum: 2
          maximum: 7
          required: false
          description: '因文件备份空间有限，老化时间需要谨慎配置，建议配置为3天。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '同步用户数据文件的开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_edgedecrypt_list:
      type: items
      properties:
        DECRYALGO:
          name: '解密算法'
          type: string
          enum:
          - AES256CBC
          required: false
          description: '与中心UDM一致，否则用户数据文件无法解密。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PASSWORD:
          name: '密码'
          type: string
          minLength: 0
          maxLength: 433
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PWDCFM:
          name: '密码确认'
          type: string
          minLength: 0
          maxLength: 433
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        OPTIONALPARA:
          name: '可选参数'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: '解密用户数据文件时，涉及“KEYGENALGO”、“ITERATION”、“MD”和“ENCODEMODE”时，设置为ENABLE。否则设置为DISABLE。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        KEYGENALGO:
          name: '密钥生成算法'
          type: string
          enum:
          - Default
          - PBKDF2
          required: false
          description: '与中心UDM一致，否则用户数据文件无法解密。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ITERATION:
          name: '迭代次数'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        MD:
          name: '消息摘要算法'
          type: string
          enum:
          - md5
          - sha256
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ENCODEMODE:
          name: '密文编码格式'
          type: string
          enum:
          - Base64
          - None
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    set_edgedecrypt_list_1:
      type: items
      properties:
        DECRYALGO:
          name: '解密算法'
          type: string
          enum:
          - AES256CBC
          required: false
          description: '与中心UDM一致，否则用户数据文件无法解密。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PASSWORD:
          name: '密码'
          type: string
          minLength: 0
          maxLength: 433
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PWDCFM:
          name: '密码确认'
          type: string
          minLength: 0
          maxLength: 433
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        OPTIONALPARA:
          name: '可选参数'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: '解密用户数据文件时，涉及“KEYGENALGO”、“ITERATION”、“MD”和“ENCODEMODE”时，设置为ENABLE。否则设置为DISABLE。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        KEYGENALGO:
          name: '密钥生成算法'
          type: string
          enum:
          - Default
          - PBKDF2
          required: false
          description: '与中心UDM一致，否则用户数据文件无法解密。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ITERATION:
          name: '迭代次数'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        MD:
          name: '消息摘要算法'
          type: string
          enum:
          - md5
          - sha256
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ENCODEMODE:
          name: '密文编码格式'
          type: string
          enum:
          - Base64
          - None
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
  examples:
    add_vpninfo_list:
    - VPNINFONAME: 'vpndsm'
      VPNNAME: 'VRF_DSM'
      VPNID: 2
    add_edgeudmip_list:
    - IPNAME: 'edgeudmip01'
      IPTYPE: DSM
      IPVERSION: IPV4
      IPV4ADDRESS: '10.100.20.20'
      IPV4MTU: 1500
      VPNINSTANCE: 'VRF_DSM'
    add_rdatasynserver_list:
    - SERVERNAME: 'Rserver_01'
      GROUPID: 1
      PRIORITY: 1
      PROTOCOL: SFTP
      IPVERSION: IPV4
      SERVERIPV4: '10.110.20.20'
      SERVERPORT: 22
      USERNAME: 'localudm'
      AUTHTYPE: PASSWORD
      PWD: 'sftp123#'
      PWDCFM: 'sftp123#'
      RWORKDIR: 'D:\sftpserver'
      DETECTSWITCH: ENABLE
    add_rdatasynserver_list_1:
    - SERVERNAME: 'Rserver_01'
      GROUPID: 1
      PRIORITY: 1
      PROTOCOL: SFTP
      IPVERSION: IPV4
      SERVERIPV4: '10.110.20.20'
      SERVERPORT: 22
      USERNAME: 'localudm'
      AUTHTYPE: PUBLICKEY
      RWORKDIR: 'D:\sftpserver'
      DETECTSWITCH: ENABLE
      PWD: 'sftp123#'
      PWDCFM: 'sftp123#'
    lod_rdatasynuserkey_list:
    - SERVERNAME: 'Rserver_01'
      USERNAME: 'localudm'
      KEYNAME: 'key1'
      PUBKEYFILE: 'rsa_key.pub'
      PRIVATEKEYFILE: 'rsa_key'
      PRIVATEKEYPWD: '*****'
    set_rsftpfirsttime_list:
    - FIRSTTIMEENABLE: DISABLE
    add_rsftppublickey_list:
    - KEYNAME: 'rsa1'
      PUBKEYTYPE: RSA
      KEYCODE: 'MIICIqhkiG9wEAAQ=='
      ENCODETYPE: PEM
    add_rsftpbindpublickey_list:
    - SERVERNAME: 'Rserver_01'
      KEYNAME: 'rsa1'
    set_rsftpfirsttime_list_1:
    - FIRSTTIMEENABLE: ENABLE
    set_edgedspolicy_list:
    - CYCLE: '1D'
      STARTTIME: '00:00'
      ENDTIME: '01:00'
      RETRYINTVL: 5
      ALMTHESTIMES: 3
      FILTERPREFIX: 'Campus1'
      FILTERSUFFIX: 'tar.gz'
      PREFIXSEPARATOR: '_'
      PREFIXFORMAT: Common
      FILEEXPIRE: 3
      SWITCH: ENABLE
    set_edgedecrypt_list:
    - DECRYALGO: AES256CBC
      PASSWORD: 'edgedecrypt123#'
      PWDCFM: 'edgedecrypt123#'
      OPTIONALPARA: ENABLE
      KEYGENALGO: Default
      ITERATION: 0
      MD: sha256
      ENCODEMODE: Base64
    set_edgedecrypt_list_1:
    - DECRYALGO: AES256CBC
      PASSWORD: 'edgedecrypt123#'
      PWDCFM: 'edgedecrypt123#'
      OPTIONALPARA: DISABLE
      KEYGENALGO: Default
      ITERATION: 0
      MD: sha256
      ENCODEMODE: Base64
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 增加VPN信息配置。

```jinja2
{%- for item in add_vpninfo_list -%}
    ADD VPNINFO:
    {#- --- 必选参数 --- -#}
    VPNINFONAME="{{item.VPNINFONAME}}",
    VPNNAME="{{item.VPNNAME}}",
    VPNID={{item.VPNID}},
    ;
{%- endfor -%}
```

### 3 配置用于访问SFTP服务器的本端IP。

```jinja2
{%- for item in add_edgeudmip_list -%}
    ADD EDGEUDMIP:
    {#- --- 必选参数 --- -#}
    IPNAME="{{item.IPNAME}}",
    IPTYPE={{item.IPTYPE}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加远端用户数据同步服务器。

### 此处配置的是SFTP服务器认证SFTP客户端（园区UDM）使用的认证方式。

#### 4.1 密码认证

```jinja2
{%- if is_scenario_password_auth -%}
    {%- for item in add_rdatasynserver_list -%}
        ADD RDATASYNSERVER:
        {#- --- 必选参数 --- -#}
        SERVERNAME="{{item.SERVERNAME}}",
        GROUPID={{item.GROUPID}},
        PRIORITY={{item.PRIORITY}},
        IPVERSION={{item.IPVERSION}},
        USERNAME="{{item.USERNAME}}",
        AUTHTYPE={{item.AUTHTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PROTOCOL is not none -%}
            PROTOCOL={{item.PROTOCOL}},
        {%- endif -%}
        {%- if item.SERVERPORT is not none -%}
            SERVERPORT={{item.SERVERPORT}},
        {%- endif -%}
        {%- if item.RWORKDIR is not none -%}
            RWORKDIR="{{item.RWORKDIR}}",
        {%- endif -%}
        {%- if item.DETECTSWITCH is not none -%}
            DETECTSWITCH={{item.DETECTSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            SERVERIPV4="{{item.SERVERIPV4}}",
        {%- endif -%}
        {#- --- 条件必选：AUTHTYPE=PASSWORD 时必选 --- -#}
        {%- if item.AUTHTYPE == 'PASSWORD' -%}
            PWD="{{item.PWD}}",
        {%- endif -%}
        {#- --- 条件必选：AUTHTYPE=PASSWORD 时必选 --- -#}
        {%- if item.AUTHTYPE == 'PASSWORD' -%}
            PWDCFM="{{item.PWDCFM}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 公钥认证（推荐）

```jinja2
{%- if is_scenario_publickey_auth -%}
    {%- for item in add_rdatasynserver_list_1 -%}
        ADD RDATASYNSERVER:
        {#- --- 必选参数 --- -#}
        SERVERNAME="{{item.SERVERNAME}}",
        GROUPID={{item.GROUPID}},
        PRIORITY={{item.PRIORITY}},
        IPVERSION={{item.IPVERSION}},
        USERNAME="{{item.USERNAME}}",
        AUTHTYPE={{item.AUTHTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PROTOCOL is not none -%}
            PROTOCOL={{item.PROTOCOL}},
        {%- endif -%}
        {%- if item.SERVERPORT is not none -%}
            SERVERPORT={{item.SERVERPORT}},
        {%- endif -%}
        {%- if item.RWORKDIR is not none -%}
            RWORKDIR="{{item.RWORKDIR}}",
        {%- endif -%}
        {%- if item.DETECTSWITCH is not none -%}
            DETECTSWITCH={{item.DETECTSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            SERVERIPV4="{{item.SERVERIPV4}}",
        {%- endif -%}
        {#- --- 条件必选：AUTHTYPE=PASSWORD 时必选 --- -#}
        {%- if item.AUTHTYPE == 'PASSWORD' -%}
            PWDCFM="{{item.PWDCFM}}",
        {%- endif -%}
        {#- --- 条件必选：AUTHTYPE=PASSWORD 时必选 --- -#}
        {%- if item.AUTHTYPE == 'PASSWORD' -%}
            PWD="{{item.PWD}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 4中“AUTHTYPE”设置为“PUBLICKEY”时，加载远端用户数据同步用户认证的密钥文件。“AUTHTYPE”设置为“PASSWORD”时，请跳过本步骤。

#### 5.1 获取并上传用户公私钥文件。

#### 密钥文件为OPENSSH格式或PEM格式。私钥文件须使用加密格式。

#### 需要将公私钥文件上传到“数据同步客户端用户密钥”文件夹中。上传的详细操作请参见文件传输。

#### 5.2 加载远端用户数据同步用户认证的密钥文件。

```jinja2
{%- set ADD_RDATASYNSERVER=getParameterValue('ADD RDATASYNSERVER') -%}
{%- if ADD_RDATASYNSERVER -%}
    {%- for item in lod_rdatasynuserkey_list -%}
        LOD RDATASYNUSERKEY:
        {#- --- 必选参数 --- -#}
        SERVERNAME="{{item.SERVERNAME}}",
        USERNAME="{{item.USERNAME}}",
        KEYNAME="{{item.KEYNAME}}",
        PUBKEYFILE="{{item.PUBKEYFILE}}",
        PRIVATEKEYFILE="{{item.PRIVATEKEYFILE}}",
        PRIVATEKEYPWD="{{item.PRIVATEKEYPWD}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.3 检查密钥加载状态。

#### RETCODE = 0  操作成功

#### 结果如下

#### -------------------------

#### 服务器名称 = Rserver_01

#### 用户名称 = localudm

#### 密钥名称 = key1

#### 公钥文件名 = rsa_key.pub

#### 私钥文件名 = rsa_key

#### 密钥状态 = 正常

#### (结果个数 = 1)

#### ---   END

#### “密钥状态”为“正常”时，说明密钥文件加载成功。否则，请联系华为技术支持工程师处理。

#### 园区UDM认证SFTP服务器时，推荐配置为认证SFTP服务器的公钥。

#### 认证SFTP服务器的公钥时，执行6。

#### 不认证SFTP服务器的公钥时，执行7。

### 6 配置认证SFTP服务器的公钥。

#### 6.1 使能认证SFTP服务器的公钥。

```jinja2
{%- if is_scenario_auth_sftp_publickey -%}
    {%- for item in set_rsftpfirsttime_list -%}
        SET RSFTPFIRSTTIME:
        {#- --- 必选参数 --- -#}
        FIRSTTIMEENABLE={{item.FIRSTTIMEENABLE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 增加SFTP服务器的公钥。

```jinja2
{%- if is_scenario_auth_sftp_publickey -%}
    {%- for item in add_rsftppublickey_list -%}
        ADD RSFTPPUBLICKEY:
        {#- --- 必选参数 --- -#}
        KEYNAME="{{item.KEYNAME}}",
        PUBKEYTYPE={{item.PUBKEYTYPE}},
        KEYCODE="{{item.KEYCODE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ENCODETYPE is not none -%}
            ENCODETYPE={{item.ENCODETYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.3 配置SFTP服务器公钥与SFTP服务器的绑定关系。

```jinja2
{%- if is_scenario_auth_sftp_publickey -%}
    {%- for item in add_rsftpbindpublickey_list -%}
        ADD RSFTPBINDPUBLICKEY:
        {#- --- 必选参数 --- -#}
        SERVERNAME="{{item.SERVERNAME}}",
        KEYNAME="{{item.KEYNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 配置不认证SFTP服务器的公钥。

```jinja2
{%- if is_scenario_no_auth_sftp_publickey -%}
    {%- for item in set_rsftpfirsttime_list_1 -%}
        SET RSFTPFIRSTTIME:
        {#- --- 必选参数 --- -#}
        FIRSTTIMEENABLE={{item.FIRSTTIMEENABLE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 设置用户数据文件同步策略。

```jinja2
{%- for item in set_edgedspolicy_list -%}
    SET EDGEDSPOLICY:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    {#- --- 可选参数 --- -#}
    {%- if item.CYCLE is not none -%}
        CYCLE="{{item.CYCLE}}",
    {%- endif -%}
    {%- if item.STARTTIME is not none -%}
        STARTTIME="{{item.STARTTIME}}",
    {%- endif -%}
    {%- if item.ENDTIME is not none -%}
        ENDTIME="{{item.ENDTIME}}",
    {%- endif -%}
    {%- if item.RETRYINTVL is not none -%}
        RETRYINTVL={{item.RETRYINTVL}},
    {%- endif -%}
    {%- if item.ALMTHESTIMES is not none -%}
        ALMTHESTIMES={{item.ALMTHESTIMES}},
    {%- endif -%}
    {%- if item.FILTERPREFIX is not none -%}
        FILTERPREFIX="{{item.FILTERPREFIX}}",
    {%- endif -%}
    {%- if item.FILTERSUFFIX is not none -%}
        FILTERSUFFIX="{{item.FILTERSUFFIX}}",
    {%- endif -%}
    {%- if item.PREFIXSEPARATOR is not none -%}
        PREFIXSEPARATOR="{{item.PREFIXSEPARATOR}}",
    {%- endif -%}
    {%- if item.PREFIXFORMAT is not none -%}
        PREFIXFORMAT={{item.PREFIXFORMAT}},
    {%- endif -%}
    {%- if item.FILEEXPIRE is not none -%}
        FILEEXPIRE={{item.FILEEXPIRE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 设置解密用户数据文件所需的数据。

### 用户数据文件包含用户签约信息，中心UDM对园区用户数据文件先加密再压缩，因此，园区UDM需要支持解密用户数据文件。

#### 9.1 //中心UDM加密用户数据文件时，涉及“KEYGENALGO”、“ITERATION”、“MD”或“ENCODEMODE”参数。

```jinja2
{%- if is_scenario_optional_para_enable -%}
    {%- for item in set_edgedecrypt_list -%}
        SET EDGEDECRYPT:
        {#- --- 可选参数 --- -#}
        {%- if item.DECRYALGO is not none -%}
            DECRYALGO={{item.DECRYALGO}},
        {%- endif -%}
        {%- if item.PASSWORD is not none -%}
            PASSWORD="{{item.PASSWORD}}",
        {%- endif -%}
        {%- if item.PWDCFM is not none -%}
            PWDCFM="{{item.PWDCFM}}",
        {%- endif -%}
        {%- if item.OPTIONALPARA is not none -%}
            OPTIONALPARA={{item.OPTIONALPARA}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：OPTIONALPARA=Enable 时可选 --- -#}
        {%- if item.OPTIONALPARA == 'Enable' -%}
            {%- if item.KEYGENALGO is not none -%}
                KEYGENALGO={{item.KEYGENALGO}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OPTIONALPARA=Enable 时可选 --- -#}
        {%- if item.OPTIONALPARA == 'Enable' -%}
            {%- if item.ITERATION is not none -%}
                ITERATION={{item.ITERATION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OPTIONALPARA=Enable 时可选 --- -#}
        {%- if item.OPTIONALPARA == 'Enable' -%}
            {%- if item.MD is not none -%}
                MD={{item.MD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OPTIONALPARA=Enable 时可选 --- -#}
        {%- if item.OPTIONALPARA == 'Enable' -%}
            {%- if item.ENCODEMODE is not none -%}
                ENCODEMODE={{item.ENCODEMODE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 9.2 //中心UDM加密用户数据文件时，不涉及“KEYGENALGO”、“ITERATION”、“MD”和“ENCODEMODE”参数。

```jinja2
{%- if is_scenario_optional_para_disable -%}
    {%- for item in set_edgedecrypt_list_1 -%}
        SET EDGEDECRYPT:
        {#- --- 可选参数 --- -#}
        {%- if item.DECRYALGO is not none -%}
            DECRYALGO={{item.DECRYALGO}},
        {%- endif -%}
        {%- if item.PASSWORD is not none -%}
            PASSWORD="{{item.PASSWORD}}",
        {%- endif -%}
        {%- if item.PWDCFM is not none -%}
            PWDCFM="{{item.PWDCFM}}",
        {%- endif -%}
        {%- if item.OPTIONALPARA is not none -%}
            OPTIONALPARA={{item.OPTIONALPARA}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：OPTIONALPARA=Enable 时可选 --- -#}
        {%- if item.OPTIONALPARA == 'Enable' -%}
            {%- if item.ITERATION is not none -%}
                ITERATION={{item.ITERATION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OPTIONALPARA=Enable 时可选 --- -#}
        {%- if item.OPTIONALPARA == 'Enable' -%}
            {%- if item.ENCODEMODE is not none -%}
                ENCODEMODE={{item.ENCODEMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OPTIONALPARA=Enable 时可选 --- -#}
        {%- if item.OPTIONALPARA == 'Enable' -%}
            {%- if item.MD is not none -%}
                MD={{item.MD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：OPTIONALPARA=Enable 时可选 --- -#}
        {%- if item.OPTIONALPARA == 'Enable' -%}
            {%- if item.KEYGENALGO is not none -%}
                KEYGENALGO={{item.KEYGENALGO}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

