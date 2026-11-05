---
id: ''
name: 配置NTS数字证书
ne_type: UEG
type: feature
description: NTS服务作为HTTPS客户端，当需要通过Https与SOAP/SMPP/CMPP/SMTP通知服务器对接时，需要加载CA证书。NTS服务使用到的证书详见表1。  **表1** NTS数字证书说明  | 数字证书 | 关联场景 | 证书类型 | 私钥文件 | 私钥密码 | 证书应用场景 | | --- | --- | --- | --- | --- | --- | | NTS客户端证书 | 通用SOAP通知链路客户端证书（UPCF\_NTS\_certForComSOAP） | CA证书：由对端SOAP服务器提供 | - | - | 用于通过Https与SOAP通知服务器对接需要加载。 | |  | NTS SMPP通知链路客户端证书（UPCF\_NTS\_certForSMPP） | CA证书：由对端SMPP服务器提供 | - | - | 用于通过Https与SMPP通知服务器对接需要加载。 | |  | NTS CMPP通知链路客户端证书（UPCF\_NTS\_certForCMPP） | CA证书：由对端CMPP服务器提供 | - | - | 用于通过Https与CMPP通知服务器对接需要加载。 | |  | NTS SMTP通知链路客户端证书（UPCF\_NTS\_certForSMTP） | CA证书：由对端SMTP服务器提供 | - | - | 用于通过Https与SMTP通知服务器对接需要加载。 |  * 华为证书获取路径：https://support.huawei.com/ >技术支持>产品支持>云核心网>Mobile Packet Core>5G Convergent Data>UPCF>UPCF。在“产品软件”界面选择对应的UPCF版本，“设备证书”、“私钥文件”和提供给对端设备的“CA证书”均存放在UPCF\_Cert\_Tools.zip里，UPCF\_Cert\_Tools.zip包含在UPCF\_2\*.\*\*\*.\*\*\*.\*\*\*\_Tools.zip当中。 * 华为证书仅用于测试环境，不能用于商用环境。商用环境请替换为商用证书，并通过OM Portal的证书管理功能删除华为证书。若客户将华为证书用于商用环境，则需承担相关安全风险和责任。为了提高系统安全性，需定期更新证书和密钥。 * 加载CA证书时，需要加载完整的CA证书链。 * 加载CRL文件时，需要加载完整的CA链签发的CRL文件，即CA证书链中每个CA证书签发的CRL文件都要加载。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置NTS数字证书"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置NTS数字证书"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置NTS数字证书"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置NTS数字证书"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
NTS服务作为HTTPS客户端，当需要通过Https与SOAP/SMPP/CMPP/SMTP通知服务器对接时，需要加载CA证书。NTS服务使用到的证书详见表1。**表1** NTS数字证书说明| 数字证书 | 关联场景 | 证书类型 | 私钥文件 | 私钥密码 | 证书应用场景 || --- | --- | --- | --- | --- | --- || NTS客户端证书 | 通用SOAP通知链路客户端证书（UPCF\_NTS\_certForComSOAP） | CA证书：由对端SOAP服务器提供 | - | - | 用于通过Https与SOAP通知服务器对接需要加载。 ||  | NTS SMPP通知链路客户端证书（UPCF\_NTS\_certForSMPP） | CA证书：由对端SMPP服务器提供 | - | - | 用于通过Https与SMPP通知服务器对接需要加载。 ||  | NTS CMPP通知链路客户端证书（UPCF\_NTS\_certForCMPP） | CA证书：由对端CMPP服务器提供 | - | - | 用于通过Https与CMPP通知服务器对接需要加载。 ||  | NTS SMTP通知链路客户端证书（UPCF\_NTS\_certForSMTP） | CA证书：由对端SMTP服务器提供 | - | - | 用于通过Https与SMTP通知服务器对接需要加载。 |* 华为证书获取路径：https://support.huawei.com/ >技术支持>产品支持>云核心网>Mobile Packet Core>5G Convergent Data>UPCF>UPCF。在“产品软件”界面选择对应的UPCF版本，“设备证书”、“私钥文件”和提供给对端设备的“CA证书”均存放在UPCF\_Cert\_Tools.zip里，UPCF\_Cert\_Tools.zip包含在UPCF\_2\*.\*\*\*.\*\*\*.\*\*\*\_Tools.zip当中。* 华为证书仅用于测试环境，不能用于商用环境。商用环境请替换为商用证书，并通过OM Portal的证书管理功能删除华为证书。若客户将华为证书用于商用环境，则需承担相关安全风险和责任。为了提高系统安全性，需定期更新证书和密钥。* 加载CA证书时，需要加载完整的CA证书链。* 加载CRL文件时，需要加载完整的CA链签发的CRL文件，即CA证书链中每个CA证书签发的CRL文件都要加载。

## 必备事项
前提条件

**前提条件**

* 证书文件已经经过授权和认证。
* 已经从运营商获取对端SOAP/SMPP/CMPP/SMTP服务器CA证书。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_pmstlscfg_list:
      type: items
      properties:
        TLSCFGID:
          name: 'TLS配置ID'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSCFGNAME:
          name: 'TLS配置名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTOCOLVER:
          name: '协议版本'
          type: string
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ntspeerlinkcfg_list:
      type: items
      properties:
        LINKID:
          name: '链路ID'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERID:
          name: '对端服务器ID'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALROLE:
          name: '本地角色'
          type: string
          enum:
          - SOAPClient
          - SMTPClient
          - JMSClient
          - CMPPClient
          - SMPPClient
          - SGIPClient
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WSDL:
          name: 'WSDL文件'
          type: string
          enum:
          - NwT
          - NlK
          - IrZ
          - Common
          - FrB
          - IdnX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIP:
          name: '本端IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIP:
          name: '对端IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SOAPURL:
          name: 'SOAP服务器URL'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFLINK:
          name: '默认链路'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CERTSCENE:
          name: '证书应用场景'
          type: string
          enum:
          - 'NULL'
          - UPCF_NTS_certForComSOAP
          - UPCF_NTS_certForSMPP
          - UPCF_NTS_certForCMPP
          - UPCF_NTS_certForSMTP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSCFGID:
          name: 'TLS配置ID'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ntspeerlinkcfg_list_1:
      type: items
      properties:
        LINKID:
          name: '链路ID'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERID:
          name: '对端服务器ID'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALROLE:
          name: '本地角色'
          type: string
          enum:
          - SOAPClient
          - SMTPClient
          - JMSClient
          - CMPPClient
          - SMPPClient
          - SGIPClient
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIP:
          name: '本端IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIP:
          name: '对端IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRNAME:
          name: '用户名'
          type: string
          minLength: 0
          maxLength: 96
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PASSWD:
          name: '密码'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISENCRYPTED:
          name: '是否支持加密'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CERTSCENE:
          name: '证书应用场景'
          type: string
          enum:
          - 'NULL'
          - UPCF_NTS_certForComSOAP
          - UPCF_NTS_certForSMPP
          - UPCF_NTS_certForCMPP
          - UPCF_NTS_certForSMTP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSCFGID:
          name: 'TLS配置ID'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WSDL:
          name: 'WSDL文件'
          type: string
          enum:
          - NwT
          - NlK
          - IrZ
          - Common
          - FrB
          - IdnX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ntspeerlinkcfg_list_2:
      type: items
      properties:
        LINKID:
          name: '链路ID'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERID:
          name: '对端服务器ID'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALROLE:
          name: '本地角色'
          type: string
          enum:
          - SOAPClient
          - SMTPClient
          - JMSClient
          - CMPPClient
          - SMPPClient
          - SGIPClient
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIP:
          name: '本端IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIP:
          name: '对端IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SENDER:
          name: '发送人'
          type: string
          minLength: 0
          maxLength: 96
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRNAME:
          name: '用户名'
          type: string
          minLength: 0
          maxLength: 96
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PASSWD:
          name: '密码'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISENCRYPTED:
          name: '是否支持加密'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CERTSCENE:
          name: '证书应用场景'
          type: string
          enum:
          - 'NULL'
          - UPCF_NTS_certForComSOAP
          - UPCF_NTS_certForSMPP
          - UPCF_NTS_certForCMPP
          - UPCF_NTS_certForSMTP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSCFGID:
          name: 'TLS配置ID'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WSDL:
          name: 'WSDL文件'
          type: string
          enum:
          - NwT
          - NlK
          - IrZ
          - Common
          - FrB
          - IdnX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ntspeerlinkcfg_list_3:
      type: items
      properties:
        LINKID:
          name: '链路ID'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERID:
          name: '对端服务器ID'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALROLE:
          name: '本地角色'
          type: string
          enum:
          - SOAPClient
          - SMTPClient
          - JMSClient
          - CMPPClient
          - SMPPClient
          - SGIPClient
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIP:
          name: '本端IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIP:
          name: '对端IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SENDER:
          name: '发送人'
          type: string
          minLength: 0
          maxLength: 96
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRNAME:
          name: '用户名'
          type: string
          minLength: 0
          maxLength: 96
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PASSWD:
          name: '密码'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISENCRYPTED:
          name: '是否支持加密'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CERTSCENE:
          name: '证书应用场景'
          type: string
          enum:
          - 'NULL'
          - UPCF_NTS_certForComSOAP
          - UPCF_NTS_certForSMPP
          - UPCF_NTS_certForCMPP
          - UPCF_NTS_certForSMTP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSCFGID:
          name: 'TLS配置ID'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WSDL:
          name: 'WSDL文件'
          type: string
          enum:
          - NwT
          - NlK
          - IrZ
          - Common
          - FrB
          - IdnX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_pmstlscfg_list:
    - TLSCFGID: TLS配置ID
      TLSCFGNAME: 'TLS配置名称'
      PROTOCOLVER: 强加密套件
    add_ntspeerlinkcfg_list:
    - LINKID: 链路ID
      PEERID: 对端服务器ID
      LOCALROLE: SOAPClient
      WSDL: Common
      IPVER: IPV4
      LOCALIP: '本端IP地址'
      PEERIP: '对端IP地址'
      PEERPORT: 对端端口
      SOAPURL: 'SOAP服务器URL'
      DEFLINK: YES
      CERTSCENE: UPCF_NTS_certForComSOAP
      DESCRIPTION: '描述'
      TLSCFGID: TLS配置ID
    add_ntspeerlinkcfg_list_1:
    - LINKID: 链路ID
      PEERID: 对端服务器ID
      LOCALROLE: CMPPClient
      IPVER: IPV4
      LOCALIP: '本端IP地址'
      PEERIP: '对端IP地址'
      PEERPORT: 对端端口
      USRNAME: '用户名'
      PASSWD: '密码'
      CFM: '确认密码'
      ISENCRYPTED: YES
      CERTSCENE: UPCF_NTS_certForCMPP
      DESCRIPTION: '描述'
      TLSCFGID: TLS配置ID
      WSDL: ''
    add_ntspeerlinkcfg_list_2:
    - LINKID: 链路ID
      PEERID: 对端服务器ID
      LOCALROLE: SMPPClient
      IPVER: IPV4
      LOCALIP: '本端IP地址'
      PEERIP: '对端IP地址'
      PEERPORT: 对端端口
      SENDER: '发送人'
      USRNAME: '用户名'
      PASSWD: '密码'
      CFM: '确认密码'
      ISENCRYPTED: YES
      CERTSCENE: UPCF_NTS_certForSMPP
      DESCRIPTION: '描述'
      TLSCFGID: TLS配置ID
      WSDL: ''
    add_ntspeerlinkcfg_list_3:
    - LINKID: 链路ID
      PEERID: 对端服务器ID
      LOCALROLE: SMTPClient
      IPVER: IPV4
      LOCALIP: '本端IP地址'
      PEERIP: '对端IP地址'
      PEERPORT: 对端端口
      SENDER: '发送人'
      USRNAME: '用户名'
      PASSWD: '密码'
      CFM: '确认密码'
      ISENCRYPTED: YES
      CERTSCENE: UPCF_NTS_certForSMTP
      DESCRIPTION: '描述'
      TLSCFGID: TLS配置ID
      WSDL: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在CSP界面配置新的数字证书后，对于服务端数字证书，需要重启对应的服务；对于客户端数字证书，需要重启对应的链路，新的证书才能生效。

### 重启操作属于产品慎用操作，如果操作不当，会引发业务中断等严重后果。请操作员在华为技术支持指导下谨慎操作。

### 配置NTS数字证书需加载CA证书，并将证书关联到证书应用场景下。

### 登录OM Portal，选择**安全** > **证书管理** > **证书与证书集管理**，单击“上传证书”。

### 2 选择“CA证书”，加载NTS数字证书，界面配置参数如表2所示。详细操作请参见证书与证书集管理。

### **表2** 配置CA证书

### | 界面参数 | 取值示例 | 取值原则 |

### | --- | --- | --- |

### | 证书名称 | NTS\_CACert | 自行命名，保证系统内命名唯一即可。 |

### | CA证书 | \*\*\*.der | 上传的CA证书文由待对接的SOAP/CMPP/SMPP/SMTP通知服务器提供。 |

### 3 上传证书完成后，选择“证书应用场景关联”，为证书场景关联加载的CA证书。详细的关联证书操作请参见证书应用场景关联。

#### 3.1 “通用SOAP通知链路客户端证书”需关联2中加载的SOAP通知服务器提供的CA证书。

#### 3.2 “NTS SMPP通知链路客户端证书”需关联2中加载的SMPP通知服务器提供的CA证书。

#### 3.3 “NTS CMPP通知链路客户端证书”需关联2中加载的CMPP通知服务器提供的CA证书。

#### 3.4 “NTS SMTP通知链路客户端证书”需关联2中加载的SMTP通知服务器提供的CA证书。

### 4 执行**ADD PMSTLSCFG**命令，增加TLS配置信息。

```jinja2
{%- for item in add_pmstlscfg_list -%}
    ADD PMSTLSCFG:
    {#- --- 必选参数 --- -#}
    TLSCFGID={{item.TLSCFGID}},
    TLSCFGNAME="{{item.TLSCFGNAME}}",
    PROTOCOLVER={{item.PROTOCOLVER}},
    ;
{%- endfor -%}
```

### 5 执行**ADD NTSPEERLINKCFG**命令，配置NTS客户端数字证书。

#### 5.1 选择“本地角色”为“SOAPClient(SOAP客户端)”，“WSDL文件”为“Common(Common)”进行配置。

```jinja2
{%- if is_scenario_soap_client -%}
    {%- for item in add_ntspeerlinkcfg_list -%}
        ADD NTSPEERLINKCFG:
        {#- --- 必选参数 --- -#}
        LINKID={{item.LINKID}},
        PEERID={{item.PEERID}},
        LOCALROLE={{item.LOCALROLE}},
        IPVER={{item.IPVER}},
        PEERPORT={{item.PEERPORT}},
        {#- --- 可选参数 --- -#}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：LOCALROLE=SOAPClient 时必选 --- -#}
        {%- if item.LOCALROLE == 'SOAPClient' -%}
            WSDL={{item.WSDL}},
        {%- endif -%}
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            LOCALIP="{{item.LOCALIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            PEERIP="{{item.PEERIP}}",
        {%- endif -%}
        {#- --- 条件必选：LOCALROLE=SOAPClient 时必选 --- -#}
        {%- if item.LOCALROLE == 'SOAPClient' -%}
            SOAPURL="{{item.SOAPURL}}",
        {%- endif -%}
        {#- --- 条件必选：WSDL=Common/IdnX 时必选 --- -#}
        {%- if item.WSDL in ['Common', 'IdnX'] -%}
            DEFLINK={{item.DEFLINK}},
        {%- endif -%}
        {#- --- 条件必选：LOCALROLE=CMPPClient/SMPPClient/SMTPClient 时必选 --- -#}
        {%- if item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SMTPClient'] -%}
            CERTSCENE={{item.CERTSCENE}},
        {#- --- 条件必选：WSDL=Common/IdnX 时必选 --- -#}
        {%- elif item.WSDL in ['Common', 'IdnX'] -%}
            CERTSCENE={{item.CERTSCENE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：LOCALROLE=CMPPClient/SMPPClient/SOAPClient/SMTPClient 时可选 --- -#}
        {%- if item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SOAPClient', 'SMTPClient'] -%}
            {%- if item.TLSCFGID is not none -%}
                TLSCFGID={{item.TLSCFGID}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 选择“本地角色”为“CMPPClient(CMPP客户端)”，“是否支持加密”配置为“YES(YES)”进行配置。

```jinja2
{%- if is_scenario_cmpp_client -%}
    {%- for item in add_ntspeerlinkcfg_list_1 -%}
        ADD NTSPEERLINKCFG:
        {#- --- 必选参数 --- -#}
        LINKID={{item.LINKID}},
        PEERID={{item.PEERID}},
        LOCALROLE={{item.LOCALROLE}},
        IPVER={{item.IPVER}},
        PEERPORT={{item.PEERPORT}},
        {#- --- 可选参数 --- -#}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            LOCALIP="{{item.LOCALIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            PEERIP="{{item.PEERIP}}",
        {%- endif -%}
        {#- --- 条件必选：LOCALROLE=CMPPClient/SMPPClient/SMTPClient 时必选 --- -#}
        {%- if item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SMTPClient'] -%}
            ISENCRYPTED={{item.ISENCRYPTED}},
        {%- endif -%}
        {#- --- 条件必选：LOCALROLE=CMPPClient/SMPPClient/SMTPClient 时必选 --- -#}
        {%- if item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SMTPClient'] -%}
            CERTSCENE={{item.CERTSCENE}},
        {#- --- 条件必选：WSDL=Common/IdnX 时必选 --- -#}
        {%- elif item.WSDL in ['Common', 'IdnX'] -%}
            CERTSCENE={{item.CERTSCENE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：LOCALROLE=CMPPClient/SMPPClient/SOAPClient/SMTPClient 时可选 --- -#}
        {%- if item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SOAPClient', 'SMTPClient'] -%}
            {%- if item.TLSCFGID is not none -%}
                TLSCFGID={{item.TLSCFGID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 用户名: 条件必选(本地角色=CMPPClient|SMPPClient|SGIPClient) / 条件可选(本地角色=SMTPClient) --- -#}
        {%- if (item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SGIPClient']) -%}
            USRNAME="{{item.USRNAME}}",
        {%- elif (item.LOCALROLE == 'SMTPClient') -%}
            {%- if item.USRNAME is not none -%}
                USRNAME="{{item.USRNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 密码: 条件必选(本地角色=CMPPClient|SMPPClient|SGIPClient) / 条件可选(本地角色=SMTPClient) --- -#}
        {%- if (item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SGIPClient']) -%}
            PASSWD="{{item.PASSWD}}",
        {%- elif (item.LOCALROLE == 'SMTPClient') -%}
            {%- if item.PASSWD is not none -%}
                PASSWD="{{item.PASSWD}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 确认密码: 条件必选(本地角色=CMPPClient|SMPPClient|SGIPClient) / 条件可选(本地角色=SMTPClient) --- -#}
        {%- if (item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SGIPClient']) -%}
            CFM="{{item.CFM}}",
        {%- elif (item.LOCALROLE == 'SMTPClient') -%}
            {%- if item.CFM is not none -%}
                CFM="{{item.CFM}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.3 选择“本地角色”为“SMPPClient(SMPP客户端)”，“是否支持加密”配置为“YES(YES)”进行配置。

```jinja2
{%- if is_scenario_smpp_client -%}
    {%- for item in add_ntspeerlinkcfg_list_2 -%}
        ADD NTSPEERLINKCFG:
        {#- --- 必选参数 --- -#}
        LINKID={{item.LINKID}},
        PEERID={{item.PEERID}},
        LOCALROLE={{item.LOCALROLE}},
        IPVER={{item.IPVER}},
        PEERPORT={{item.PEERPORT}},
        {#- --- 可选参数 --- -#}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            LOCALIP="{{item.LOCALIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            PEERIP="{{item.PEERIP}}",
        {%- endif -%}
        {#- --- 条件必选：LOCALROLE=SMPPClient/SMTPClient 时必选 --- -#}
        {%- if item.LOCALROLE in ['SMPPClient', 'SMTPClient'] -%}
            SENDER="{{item.SENDER}}",
        {%- endif -%}
        {#- --- 条件必选：LOCALROLE=CMPPClient/SMPPClient/SMTPClient 时必选 --- -#}
        {%- if item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SMTPClient'] -%}
            ISENCRYPTED={{item.ISENCRYPTED}},
        {%- endif -%}
        {#- --- 条件必选：LOCALROLE=CMPPClient/SMPPClient/SMTPClient 时必选 --- -#}
        {%- if item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SMTPClient'] -%}
            CERTSCENE={{item.CERTSCENE}},
        {#- --- 条件必选：WSDL=Common/IdnX 时必选 --- -#}
        {%- elif item.WSDL in ['Common', 'IdnX'] -%}
            CERTSCENE={{item.CERTSCENE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：LOCALROLE=CMPPClient/SMPPClient/SOAPClient/SMTPClient 时可选 --- -#}
        {%- if item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SOAPClient', 'SMTPClient'] -%}
            {%- if item.TLSCFGID is not none -%}
                TLSCFGID={{item.TLSCFGID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 用户名: 条件必选(本地角色=CMPPClient|SMPPClient|SGIPClient) / 条件可选(本地角色=SMTPClient) --- -#}
        {%- if (item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SGIPClient']) -%}
            USRNAME="{{item.USRNAME}}",
        {%- elif (item.LOCALROLE == 'SMTPClient') -%}
            {%- if item.USRNAME is not none -%}
                USRNAME="{{item.USRNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 密码: 条件必选(本地角色=CMPPClient|SMPPClient|SGIPClient) / 条件可选(本地角色=SMTPClient) --- -#}
        {%- if (item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SGIPClient']) -%}
            PASSWD="{{item.PASSWD}}",
        {%- elif (item.LOCALROLE == 'SMTPClient') -%}
            {%- if item.PASSWD is not none -%}
                PASSWD="{{item.PASSWD}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 确认密码: 条件必选(本地角色=CMPPClient|SMPPClient|SGIPClient) / 条件可选(本地角色=SMTPClient) --- -#}
        {%- if (item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SGIPClient']) -%}
            CFM="{{item.CFM}}",
        {%- elif (item.LOCALROLE == 'SMTPClient') -%}
            {%- if item.CFM is not none -%}
                CFM="{{item.CFM}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.4 选择“本地角色”为“SMTPClient(SMTP客户端)”，“是否支持加密”配置为“YES(YES)”进行配置。

```jinja2
{%- if is_scenario_smtp_client -%}
    {%- for item in add_ntspeerlinkcfg_list_3 -%}
        ADD NTSPEERLINKCFG:
        {#- --- 必选参数 --- -#}
        LINKID={{item.LINKID}},
        PEERID={{item.PEERID}},
        LOCALROLE={{item.LOCALROLE}},
        IPVER={{item.IPVER}},
        PEERPORT={{item.PEERPORT}},
        {#- --- 可选参数 --- -#}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            LOCALIP="{{item.LOCALIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            PEERIP="{{item.PEERIP}}",
        {%- endif -%}
        {#- --- 条件必选：LOCALROLE=SMPPClient/SMTPClient 时必选 --- -#}
        {%- if item.LOCALROLE in ['SMPPClient', 'SMTPClient'] -%}
            SENDER="{{item.SENDER}}",
        {%- endif -%}
        {#- --- 条件必选：LOCALROLE=CMPPClient/SMPPClient/SMTPClient 时必选 --- -#}
        {%- if item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SMTPClient'] -%}
            ISENCRYPTED={{item.ISENCRYPTED}},
        {%- endif -%}
        {#- --- 条件必选：LOCALROLE=CMPPClient/SMPPClient/SMTPClient 时必选 --- -#}
        {%- if item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SMTPClient'] -%}
            CERTSCENE={{item.CERTSCENE}},
        {#- --- 条件必选：WSDL=Common/IdnX 时必选 --- -#}
        {%- elif item.WSDL in ['Common', 'IdnX'] -%}
            CERTSCENE={{item.CERTSCENE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：LOCALROLE=CMPPClient/SMPPClient/SOAPClient/SMTPClient 时可选 --- -#}
        {%- if item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SOAPClient', 'SMTPClient'] -%}
            {%- if item.TLSCFGID is not none -%}
                TLSCFGID={{item.TLSCFGID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 用户名: 条件必选(本地角色=CMPPClient|SMPPClient|SGIPClient) / 条件可选(本地角色=SMTPClient) --- -#}
        {%- if (item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SGIPClient']) -%}
            USRNAME="{{item.USRNAME}}",
        {%- elif (item.LOCALROLE == 'SMTPClient') -%}
            {%- if item.USRNAME is not none -%}
                USRNAME="{{item.USRNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 密码: 条件必选(本地角色=CMPPClient|SMPPClient|SGIPClient) / 条件可选(本地角色=SMTPClient) --- -#}
        {%- if (item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SGIPClient']) -%}
            PASSWD="{{item.PASSWD}}",
        {%- elif (item.LOCALROLE == 'SMTPClient') -%}
            {%- if item.PASSWD is not none -%}
                PASSWD="{{item.PASSWD}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 确认密码: 条件必选(本地角色=CMPPClient|SMPPClient|SGIPClient) / 条件可选(本地角色=SMTPClient) --- -#}
        {%- if (item.LOCALROLE in ['CMPPClient', 'SMPPClient', 'SGIPClient']) -%}
            CFM="{{item.CFM}}",
        {%- elif (item.LOCALROLE == 'SMTPClient') -%}
            {%- if item.CFM is not none -%}
                CFM="{{item.CFM}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

