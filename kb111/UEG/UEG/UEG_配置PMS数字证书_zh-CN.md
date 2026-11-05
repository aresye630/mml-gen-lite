---
id: ''
name: 配置PMS数字证书
ne_type: UEG
type: feature
description: PMS作为HTTPS服务端，在完成网元部署和基础数据配置后，必须要配置PMS设备证书，保证UPCF Web UI功能正常使用。此外，当局点涉及使用PMS通过Https的SOAP链路对接POP等第三方服务时，需要进一步配置CA证书。  PMS服务使用到的华为证书详见表1。根据业务需求，若需要配置新的证书，可通过OM Portal页面进行配置和更新。  **表1** PMS数字证书说明  | 数字证书 | 关联场景 | 证书类型 | 私钥文件 | 私钥密码 | 证书应用场景 | | --- | --- | --- | --- | --- | --- | | PMS服务端证书 | PMS WEB服务端证书（UPCF\_PMS\_Lcert） | 设备证书：PMScert.pem | PMScert.key | 联系华为技术支持。 | 用于访问PMS服务，UPCF全新部署完成后，必须加载PMS设备证书。 | |  | PM接口服务端证书（UPCF\_PMS\_certForPM） |  |  |  | 用于Https对接PM接口时，需要关联此场景。 | |  | SCLI接口服务端证书（UPCF\_PMS\_certForSCLI） |  |  |  | 用于Https对接SCLI接口时，需要关联此场景。 | | PMS客户端证书 | POP SOAP接口链路客户端证书（UPCF\_PMS\_certForPOPSOAP） | * 根CA：Huawei\_Equipment\_Root\_CA.der * 二级CA：Huawei Cloud Core Network Product CA.cer | - | - | 用于通过Https的SOAP链路对接POP等第三方服务时，需要关联此场景。 |  * 华为证书获取路径：https://support.huawei.com/ >技术支持>产品软件>云核心网>Mobile Packet Core>5G Packet Core>UEG>UEG。在“产品软件”界面选择对应的UEG版本，“设备证书”、“私钥文件”和提供给对端设备的“CA证书”均存放在UEG-Plus\_XXX\_Tools.zip中的UPCF\_Cert\_Tools.zip里。 * 华为证书仅用于测试环境，不能用于商用环境。商用环境请替换为商用证书，并通过OM Portal的证书管理功能删除华为证书。若客户将华为证书用于商用环境，则需承担相关安全风险和责任。为了提高系统安全性，需定期更新证书和密钥。 * 加载CA证书时，需要加载完整的CA证书链。 * 加载CRL文件时，需要加载完整的CA链签发的CRL文件，即CA证书链中每个CA证书签发的CRL文件都要加载。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置PMS数字证书"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置PMS数字证书"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
PMS作为HTTPS服务端，在完成网元部署和基础数据配置后，必须要配置PMS设备证书，保证UPCF Web UI功能正常使用。此外，当局点涉及使用PMS通过Https的SOAP链路对接POP等第三方服务时，需要进一步配置CA证书。PMS服务使用到的华为证书详见表1。根据业务需求，若需要配置新的证书，可通过OM Portal页面进行配置和更新。**表1** PMS数字证书说明| 数字证书 | 关联场景 | 证书类型 | 私钥文件 | 私钥密码 | 证书应用场景 || --- | --- | --- | --- | --- | --- || PMS服务端证书 | PMS WEB服务端证书（UPCF\_PMS\_Lcert） | 设备证书：PMScert.pem | PMScert.key | 联系华为技术支持。 | 用于访问PMS服务，UPCF全新部署完成后，必须加载PMS设备证书。 ||  | PM接口服务端证书（UPCF\_PMS\_certForPM） |  |  |  | 用于Https对接PM接口时，需要关联此场景。 ||  | SCLI接口服务端证书（UPCF\_PMS\_certForSCLI） |  |  |  | 用于Https对接SCLI接口时，需要关联此场景。 || PMS客户端证书 | POP SOAP接口链路客户端证书（UPCF\_PMS\_certForPOPSOAP） | * 根CA：Huawei\_Equipment\_Root\_CA.der * 二级CA：Huawei Cloud Core Network Product CA.cer | - | - | 用于通过Https的SOAP链路对接POP等第三方服务时，需要关联此场景。 |* 华为证书获取路径：https://support.huawei.com/ >技术支持>产品软件>云核心网>Mobile Packet Core>5G Packet Core>UEG>UEG。在“产品软件”界面选择对应的UEG版本，“设备证书”、“私钥文件”和提供给对端设备的“CA证书”均存放在UEG-Plus\_XXX\_Tools.zip中的UPCF\_Cert\_Tools.zip里。* 华为证书仅用于测试环境，不能用于商用环境。商用环境请替换为商用证书，并通过OM Portal的证书管理功能删除华为证书。若客户将华为证书用于商用环境，则需承担相关安全风险和责任。为了提高系统安全性，需定期更新证书和密钥。* 加载CA证书时，需要加载完整的CA证书链。* 加载CRL文件时，需要加载完整的CA链签发的CRL文件，即CA证书链中每个CA证书签发的CRL文件都要加载。

## 必备事项
前提条件

**前提条件**

* 证书文件已经经过授权和认证。
* 若使用华为证书，证书密码已经通过华为技术工程师获取。
* 若使用运营商自身的证书，证书密码已经从运营商处获取。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_pmsfunc_list:
      type: items
      properties:
        TYPE:
          name: '配置类型'
          type: string
          enum:
          - FtpConfig
          - WebUI
          - MbeanConfig
          - Server
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ITEMN:
          name: '配置项名称'
          type: string
          enum:
          - mode
          - lockTimeout
          - checkVerifyCode
          - sessionTimeout
          - diskLowValue
          - diskHighValue
          - sslEnabledProtocols
          - ciphers
          - cert
          - certForPM
          - certForSCLI
          - logFileFormat
          - xssCheckSwitch
          - cliVerifySwitch
          - sqlCheckSwitch
          - pmsWebSwitch
          - certForRest
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CERTSCENE:
          name: '证书应用场景'
          type: string
          enum:
          - UPCF_PMS_Lcert
          - 'NULL'
          - UPCF_PMS_certForPM
          - UPCF_PMS_certForSCLI
          - UPCF_PMS_certForRest
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_pmsfunc_list_1:
      type: items
      properties:
        TYPE:
          name: '配置类型'
          type: string
          enum:
          - FtpConfig
          - WebUI
          - MbeanConfig
          - Server
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ITEMN:
          name: '配置项名称'
          type: string
          enum:
          - mode
          - lockTimeout
          - checkVerifyCode
          - sessionTimeout
          - diskLowValue
          - diskHighValue
          - sslEnabledProtocols
          - ciphers
          - cert
          - certForPM
          - certForSCLI
          - logFileFormat
          - xssCheckSwitch
          - cliVerifySwitch
          - sqlCheckSwitch
          - pmsWebSwitch
          - certForRest
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CERTSCENE:
          name: '证书应用场景'
          type: string
          enum:
          - UPCF_PMS_Lcert
          - 'NULL'
          - UPCF_PMS_certForPM
          - UPCF_PMS_certForSCLI
          - UPCF_PMS_certForRest
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_pmsfunc_list_2:
      type: items
      properties:
        TYPE:
          name: '配置类型'
          type: string
          enum:
          - FtpConfig
          - WebUI
          - MbeanConfig
          - Server
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ITEMN:
          name: '配置项名称'
          type: string
          enum:
          - mode
          - lockTimeout
          - checkVerifyCode
          - sessionTimeout
          - diskLowValue
          - diskHighValue
          - sslEnabledProtocols
          - ciphers
          - cert
          - certForPM
          - certForSCLI
          - logFileFormat
          - xssCheckSwitch
          - cliVerifySwitch
          - sqlCheckSwitch
          - pmsWebSwitch
          - certForRest
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CERTSCENE:
          name: '证书应用场景'
          type: string
          enum:
          - UPCF_PMS_Lcert
          - 'NULL'
          - UPCF_PMS_certForPM
          - UPCF_PMS_certForSCLI
          - UPCF_PMS_certForRest
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rst_msprocess_list:
      type: items
      properties:
        PROCOBJECT:
          name: '操作对象'
          type: string
          enum:
          - PROCNAME
          - PROCID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROCNAME:
          name: '进程类型'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_pmspeerlinkcfg_list:
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
          - FTPClient
          - POPFTPClient
          - PMS4AClient
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WSDL:
          name: 'WSDL文件'
          type: string
          enum:
          - PPMSOAP
          - POP
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
        LOGONURL:
          name: '认证服务器URL'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CERTSCENE:
          name: '证书应用场景'
          type: string
          enum:
          - UPCF_PMS_certForPOPSOAP
          - 'NULL'
          - UPCF_PMS_certFor4A
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
  examples:
    mod_pmsfunc_list:
    - TYPE: Server
      ITEMN: cert
      CERTSCENE: UPCF_PMS_Lcert
    mod_pmsfunc_list_1:
    - TYPE: Server
      ITEMN: certForPM
      CERTSCENE: UPCF_PMS_certForPM
    mod_pmsfunc_list_2:
    - TYPE: Server
      ITEMN: certForSCLI
      CERTSCENE: UPCF_PMS_certForSCLI
    rst_msprocess_list:
    - PROCOBJECT: PROCNAME
      PROCNAME: 'CELL_PcfPms'
    add_pmstlscfg_list:
    - TLSCFGID: TLS配置ID
      TLSCFGNAME: 'TLS配置名称'
      PROTOCOLVER: 强加密套件
    add_pmspeerlinkcfg_list:
    - LINKID: 链路ID
      PEERID: 对端服务器ID
      LOCALROLE: SOAPClient
      WSDL: POP
      PEERIP: '对端IP地址'
      PEERPORT: 对端端口
      LOGONURL: '认证服务器URL'
      CERTSCENE: UPCF_PMS_certForPOPSOAP
      DESCRIPTION: '描述'
      TLSCFGID: TLS配置ID
      IPVER: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在CSP界面配置新的数字证书后，对于服务端数字证书，需要重启对应的服务；对于客户端数字证书，需要重启对应的链路，新的证书才能生效。

### 重启操作属于产品慎用操作，如果操作不当，会引发业务中断等严重后果。请操作员在华为技术支持指导下谨慎操作。

### **配置PMS服务端数字证书**

### 配置PMS服务端证书需加载设备证书：PMScert.pem，并根据所需的应用场景，将证书关联到对应的关联场景。

#### 1.1 登录CSP Portal界面，选择**安全** > **证书管理** > **证书与证书集管理**，点击上传证书。

#### 1.2 选择“设备证书”，加载PMS设备证书，界面配置参数如表2所示。详细操作请参见证书与证书集管理。

#### **表2** 配置设备证书

#### | 界面参数 | 取值示例 | 取值原则 |

#### | --- | --- | --- |

#### | 证书名称 | PMS\_DeviceCert | 自行命名，保证系统内命名唯一即可。 |

#### | 设备证书 | PMScert.pem | 上传设备证书文件PMScert.pem，解压UPCF\_Cert\_Tools.zip，在PMS文件夹下获取。 |

#### | 私钥文件 | PMScert.key | 上传私钥文件PMScert.key，解压UPCF\_Cert\_Tools.zip，在PMS文件夹下获取。 |

#### | 私钥密码 | *\*\*\*\*\*\** | 联系华为技术支持。 |

#### 1.3 上传证书完成后，选择证书应用场景关联，基于各种应用场景，关联刚加载的PMS设备证书。详细的关联证书操作请参见证书应用场景关联。

##### 1.3.1 **为证书场景“PMS WEB服务端证书”关联刚加载的PMS设备证书。**

##### UPCF网元全新部署完成后，必须加载PMS设备证书，PMS Web UI才可基于Https正常登录。此证书场景必须关联PMS设备证书。

##### 1.3.2 **为证书场景“****PM接口服务端证书****”关联刚加载的PMS设备证书。**

##### 用于Https对接PM接口时，需要关联此场景，否则无需进行关联。

##### 1.3.3 **为证书场景“****SCLI接口服务端证书****”关联刚加载的PMS设备证书。**

##### 用于Https对接SCLI接口时，需要关联此场景，否则无需进行关联。

#### 1.4 执行**MOD PMSFUNC**命令，配置PMS服务端数字证书。

##### 1.4.1 **关联****证书场景“PMS WEB服务端证书”****后，执行以下命令：**

##### `MOD PMSFUNC: TYPE=Server, ITEMN=cert, CERTSCENE=UPCF_PMS_Lcert;`

```jinja2
{%- for item in mod_pmsfunc_list -%}
    MOD PMSFUNC:
    {#- --- 必选参数 --- -#}
    TYPE={{item.TYPE}},
    ITEMN={{item.ITEMN}},
    {#- --- 可选参数 --- -#}
    {%- if item.CERTSCENE is not none -%}
        CERTSCENE={{item.CERTSCENE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.4.2 **关联****证书场景“PM接口服务端证书”****后，执行以下命令，否则跳过此步骤：**

```jinja2
{%- if is_scenario_pm_interface -%}
    {%- for item in mod_pmsfunc_list_1 -%}
        MOD PMSFUNC:
        {#- --- 必选参数 --- -#}
        TYPE={{item.TYPE}},
        ITEMN={{item.ITEMN}},
        {#- --- 可选参数 --- -#}
        {%- if item.CERTSCENE is not none -%}
            CERTSCENE={{item.CERTSCENE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.4.3 **关联****证书场景“****SCLI接口服务端证书****”****后，执行以下命令，****否则跳过此步骤****：**

```jinja2
{%- if is_scenario_scli_interface -%}
    {%- for item in mod_pmsfunc_list_2 -%}
        MOD PMSFUNC:
        {#- --- 必选参数 --- -#}
        TYPE={{item.TYPE}},
        ITEMN={{item.ITEMN}},
        {#- --- 可选参数 --- -#}
        {%- if item.CERTSCENE is not none -%}
            CERTSCENE={{item.CERTSCENE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.5 在CSP Portal界面选择“应用管理 > MML”，进入MML命令界面。选择UEG网元，执行如下命令，进行重启PMS服务。

```jinja2
{%- for item in rst_msprocess_list -%}
    RST MSPROCESS:
    {#- --- 必选参数 --- -#}
    PROCOBJECT={{item.PROCOBJECT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PROCOBJECT=PROCNAME 时必选 --- -#}
    {%- if item.PROCOBJECT == 'PROCNAME' -%}
        PROCNAME="{{item.PROCNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.6 复位服务后，等待4分钟左右，待服务重启生效，操作完成。

### 2 **配置PMS客户端数字证书**

### 当需要通过Https的SOAP链路对接POP等第三方服务时，才需要加载PMS客户端数字证书，否则无需执行本操作。

#### 2.1 登录CSP Portal界面，选择**安全** > **证书管理** > **证书与证书集管理**，点击上传证书。

#### 2.2 选择“CA证书”，加载CA证书，界面配置参数如表3所示。详细操作请参见证书与证书集管理。

#### **表3** 配置CA证书

#### | 界面参数 | 取值示例 | 取值原则 |

#### | --- | --- | --- |

#### | 证书名称 | PMS\_CACert | 自行命名，保证系统内命名唯一即可。 |

#### | CA证书 | Huawei\_Equipment\_Root\_CA.der | 上传CA证书文件Huawei\_Equipment\_Root\_CA.der，解压UPCF\_Cert\_Tools.zip，在PMS文件夹下获取。 |

#### 2.3 上传证书完成后，选择证书应用场景关联，为证书场景“POP SOAP接口链路客户端证书”关联刚加载的PMS CA证书。详细的关联证书操作请参见证书应用场景关联。

#### 2.4 执行**ADD PMSTLSCFG**命令，增加TLS配置信息。

```jinja2
{%- if is_scenario_pop_soap -%}
    {%- for item in add_pmstlscfg_list -%}
        ADD PMSTLSCFG:
        {#- --- 必选参数 --- -#}
        TLSCFGID={{item.TLSCFGID}},
        TLSCFGNAME="{{item.TLSCFGNAME}}",
        PROTOCOLVER={{item.PROTOCOLVER}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 执行**ADD PMSPEERLINKCFG**命令，配置PMS客户端数字证书。

#### 选择“本地角色”为“SOAPClient(SOAP客户端)”，“WSDL文件”为“POP(POP)”进行配置。

```jinja2
{%- if is_scenario_pop_soap -%}
    {%- for item in add_pmspeerlinkcfg_list -%}
        ADD PMSPEERLINKCFG:
        {#- --- 必选参数 --- -#}
        LINKID={{item.LINKID}},
        PEERID={{item.PEERID}},
        LOCALROLE={{item.LOCALROLE}},
        PEERPORT={{item.PEERPORT}},
        IPVER={{item.IPVER}},
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
            PEERIP="{{item.PEERIP}}",
        {%- endif -%}
        {#- --- 条件必选：LOCALROLE=PMS4AClient 时必选 --- -#}
        {%- if item.LOCALROLE == 'PMS4AClient' -%}
            LOGONURL="{{item.LOGONURL}}",
        {#- --- 条件必选：WSDL=POP 时必选 --- -#}
        {%- elif item.WSDL == 'POP' -%}
            LOGONURL="{{item.LOGONURL}}",
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 证书应用场景: 条件必选(本地角色=PMS4AClient) / 条件可选(WSDL文件=POP) --- -#}
        {%- if (item.LOCALROLE == 'PMS4AClient') -%}
            CERTSCENE={{item.CERTSCENE}},
        {%- elif (item.WSDL == 'POP') -%}
            {%- if item.CERTSCENE is not none -%}
                CERTSCENE={{item.CERTSCENE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- TLS配置ID: 条件必选(本地角色=PMS4AClient) / 条件可选(WSDL文件=POP|PPMSOAP) --- -#}
        {%- if (item.LOCALROLE == 'PMS4AClient') -%}
            TLSCFGID={{item.TLSCFGID}},
        {%- elif (item.WSDL in ['POP', 'PPMSOAP']) -%}
            {%- if item.TLSCFGID is not none -%}
                TLSCFGID={{item.TLSCFGID}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

