---
id: ''
name: 配置DRS数字证书
ne_type: UEG
type: feature
description: DRS作为HTTPS服务端，在完成网元部署和基础数据配置后，必须要配置DRS设备证书。此外，当局点涉及使用DRS通过Https的SOAP链路对接POP等第三方服务时，需要进一步配置CA证书。  无论商用还是测试场景下，DRS服务使用到的华为证书需要联系华为技术进行申请获取。当申请获取证书的场景及样例参考表1。  **表1** DRS数字证书示例  | 数字证书 | 关联场景 | 证书类型 | 私钥文件 | 私钥密码 | 证书应用场景 | | --- | --- | --- | --- | --- | --- | | DRS服务端证书 | DRS SOAP服务端证书（UPCF\_DRS\_certForPM） | 设备证书：DRScert.pem | DRScert.pem | 联系华为技术支持。 | 用于通过Https的SOAP链路对接POP-D等第三方服务，供对端进行UPCF日志信息查询时，需要关联此场景。 | |  | DRS SOAP服务端CA证书  （UPCF\_DRS\_certForPM\_CA） | * 根CA：Huawei\_Equipment\_Root\_CA.der * 二级CA：Huawei Cloud Core Network Product CA.cer | - | - | 用于UPCF\_DRS\_certForPM设备证书场景支持证书链功能时，需要关联此场景。 | | DRS客户端证书 | DRS SOAP客户端证书  （UPCF\_DRS\_certForSOAP） | * 根CA：Huawei\_Equipment\_Root\_CA.der * 二级CA：Huawei Cloud Core Network Product CA.cer | - | - | 用于通过Https的SOAP链路对接POP-D等第三方服务，向对端发送报表上传失败通知时，需要关联此场景。 | |  | DRS FIM客户端证书  （UPCF\_DRS\_certForFIM） |  |  |  | 用于通过Https向FIM发起rest请求查询告警时，需要关联此场景。 |  * 华为证书仅用于测试环境，不能用于商用环境。商用环境请替换为商用证书，并通过OM Portal的证书管理功能删除华为证书。若客户将华为证书用于商用环境，则需承担相关安全风险和责任。为了提高系统安全性，需定期更新证书和密钥。 * 加载CA证书时，需要加载完整的CA证书链。 * 加载CRL文件时，需要加载完整的CA链签发的CRL文件，即CA证书链中每个CA证书签发的CRL文件都要加载。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置DRS数字证书"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置DRS数字证书"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置DRS数字证书"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置DRS数字证书"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
DRS作为HTTPS服务端，在完成网元部署和基础数据配置后，必须要配置DRS设备证书。此外，当局点涉及使用DRS通过Https的SOAP链路对接POP等第三方服务时，需要进一步配置CA证书。无论商用还是测试场景下，DRS服务使用到的华为证书需要联系华为技术进行申请获取。当申请获取证书的场景及样例参考表1。**表1** DRS数字证书示例| 数字证书 | 关联场景 | 证书类型 | 私钥文件 | 私钥密码 | 证书应用场景 || --- | --- | --- | --- | --- | --- || DRS服务端证书 | DRS SOAP服务端证书（UPCF\_DRS\_certForPM） | 设备证书：DRScert.pem | DRScert.pem | 联系华为技术支持。 | 用于通过Https的SOAP链路对接POP-D等第三方服务，供对端进行UPCF日志信息查询时，需要关联此场景。 ||  | DRS SOAP服务端CA证书  （UPCF\_DRS\_certForPM\_CA） | * 根CA：Huawei\_Equipment\_Root\_CA.der * 二级CA：Huawei Cloud Core Network Product CA.cer | - | - | 用于UPCF\_DRS\_certForPM设备证书场景支持证书链功能时，需要关联此场景。 || DRS客户端证书 | DRS SOAP客户端证书  （UPCF\_DRS\_certForSOAP） | * 根CA：Huawei\_Equipment\_Root\_CA.der * 二级CA：Huawei Cloud Core Network Product CA.cer | - | - | 用于通过Https的SOAP链路对接POP-D等第三方服务，向对端发送报表上传失败通知时，需要关联此场景。 ||  | DRS FIM客户端证书  （UPCF\_DRS\_certForFIM） |  |  |  | 用于通过Https向FIM发起rest请求查询告警时，需要关联此场景。 |* 华为证书仅用于测试环境，不能用于商用环境。商用环境请替换为商用证书，并通过OM Portal的证书管理功能删除华为证书。若客户将华为证书用于商用环境，则需承担相关安全风险和责任。为了提高系统安全性，需定期更新证书和密钥。* 加载CA证书时，需要加载完整的CA证书链。* 加载CRL文件时，需要加载完整的CA链签发的CRL文件，即CA证书链中每个CA证书签发的CRL文件都要加载。

## 必备事项
前提条件

* 若使用华为证书，证书密码已经通过华为技术工程师获取。
* 若使用运营商自身的证书，证书密码已经从运营商处获取。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
    mod_drspeerlinkcfg_list:
      type: items
      properties:
        LINKID:
          name: 'LINKID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALROLE:
          name: 'LOCALROLE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVER:
          name: 'IPVER'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CERTSCENE:
          name: 'CERTSCENE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    rst_msprocess_list:
    - PROCOBJECT: PROCNAME
      PROCNAME: 'CELL_PcfDrs'
    mod_drspeerlinkcfg_list:
    - LINKID: 链路ID
      LOCALROLE: SOAPClient
      IPVER: 对端IP版本
      CERTSCENE: UPCF_DRS_certForSOAP
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在CSP界面配置新的数字证书后，对于服务端数字证书，需要重启对应的服务；对于客户端数字证书，需要重启对应的链路，新的证书才能生效。

### 2 重启操作属于产品慎用操作，如果操作不当，会引发业务中断等严重后果。请操作员在华为技术支持指导下谨慎操作。

### 3 **配置DRS服务端数字证书**

### 当DRS通过Https的SOAP链路对接POP-D等第三方服务，供对端进行UPCF日志信息查询时，需要加载服务端数字证书，否则无需加载。

### 配置DRS服务端证书需加载设备证书，以DRScert.pem为例，将证书关联到“DRS SOAP服务端证书”场景下。

#### 3.1 登录CSP Portal界面，选择**安全** > **证书管理** > **证书与证书集管理**，单击上传证书。

#### 3.2 选择“设备证书”，加载DRS设备证书，界面配置参数如表2所示。详细操作请参见证书与证书集管理。

#### **表2** 配置设备证书

#### | 界面参数 | 取值示例 | 取值原则 |

#### | --- | --- | --- |

#### | 证书名称 | DRS\_DeviceCert | 自行命名，保证系统内命名唯一即可。 |

#### | 设备证书 | DRScert.pem | 上传设备证书文件DRScert.pem，以实际申请到的证书为准。 |

#### | 私钥文件 | DRScert.key | 上传私钥文件DRScert.key，以实际申请到的证书为准。 |

#### | 私钥密码 | *\*\*\*\*\*\** | 联系华为技术支持。 |

#### 3.3 上传证书完成后，选择证书应用场景关联，关联刚加载的设备证书到“DRS SOAP服务端证书”。详细的关联证书操作请参见证书应用场景关联。

#### 3.4 在OM Portal界面选择“应用管理 > MML”，进入MML命令界面。选择UPCF网元，执行如下命令，进行重启DRS服务。

```jinja2
{%- if is_scenario_server_cert -%}
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
{%- endif -%}
```

#### 3.5 复位服务后，等待4分钟左右，待服务重启生效，操作完成。

### 4 **配置DRS客户端数字证书**

### 当DRS通过Https的SOAP链路对接POP-D等第三方服务，向对端发送报表上传失败通知时，需要加载DRS客户端数字证书，否则无需加载。

#### 4.1 登录CSP Portal界面，选择**安全** > **证书管理** > **证书与证书集管理**，点击上传证书。

#### 4.2 选择“CA证书”，加载CA证书，界面配置参数如表3所示。详细操作请参见证书与证书集管理。

#### **表3** 配置CA证书

#### | 界面参数 | 取值示例 | 取值原则 |

#### | --- | --- | --- |

#### | 证书名称 | DRS\_CACert | 自行命名，保证系统内命名唯一即可。 |

#### | CA证书 | Huawei\_Equipment\_Root\_CA.der | 上传CA证书文件Huawei\_Equipment\_Root\_CA.der，以实际申请到的证书为准。 |

#### 4.3 上传证书完成后，选择证书应用场景关联，为证书场景“DRS SOAP客户端证书”关联刚加载的CA证书。详细的关联证书操作请参见证书应用场景关联。

#### 4.4 执行**MOD DRSPEERLINKCFG**命令，配置DRS客户端数字证书。

#### 选择“本地角色”为“SOAPClient(SOAP客户端)”，“CERTSCENE”为UPCF\_DRS\_certForSOAP进行配置。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_drspeerlinkcfg_list的变量区（command: MOD DRSPEERLINKCFG） -#}
<!-- MISSING_MACRO: command=MOD DRSPEERLINKCFG list_name=mod_drspeerlinkcfg_list step_id=4.4 -->
```

#### 若DRS与POP-D的链路未配置，则直接通过ADD DRSPEERLINKCFG配置链路，同时配置CERTSCENE=**UPCF\_DRS\_certForSOAP**。

