---
id: ''
name: 配置HLB数字证书
ne_type: UEG
type: feature
description: HLB服务作为HTTPS服务端或客户端，当需要通过Https与SMF、AMF、NRF等NF对接时，需要加载HLB证书集。HLB服务使用到的华为证书详见表1。  **表1** HLB数字证书说明  | 数字证书 | 关联场景 | 证书类型 | 私钥文件 | 私钥密码 | 证书应用场景 | | --- | --- | --- | --- | --- | --- | | HLB服务端证书 | HLB 服务证书集  （UPCF\_HLB\_Lcert） | * 设备证书：HLBcert.pem * 根CA：Huawei\_Equipment\_Root\_CA.der * 二级CA：Huawei Cloud Core Network Product CA.cer | HLBcert.key | 联系华为技术支持。 | 用于通过Https访问HLB服务时需要一起加载。 | | HLB客户端证书 |  |  |  |  |  |  * 华为证书获取路径：https://support.huawei.com/ >技术支持>产品支持>云核心网>Mobile Packet Core>5G Convergent Data>UPCF>UPCF。在“产品软件”界面选择对应的UPCF版本，“设备证书”、“私钥文件”和提供给对端设备的“CA证书”均存放在UPCF\_Cert\_Tools.zip里，UPCF\_Cert\_Tools.zip包含在UPCF\_2\*.\*\*\*.\*\*\*.\*\*\*\_Tools.zip当中。 * 华为证书仅用于测试环境，不能用于商用环境。商用环境请替换为商用证书，并通过OM Portal的证书管理功能删除华为证书。若客户将华为证书用于商用环境，则需承担相关安全风险和责任。为了提高系统安全性，需定期更新证书和密钥。 * 加载CA证书时，需要加载完整的CA证书链。 * 加载CRL文件时，需要加载完整的CA链签发的CRL文件，即CA证书链中每个CA证书签发的CRL文件都要加载。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置HLB数字证书"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置HLB数字证书"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
HLB服务作为HTTPS服务端或客户端，当需要通过Https与SMF、AMF、NRF等NF对接时，需要加载HLB证书集。HLB服务使用到的华为证书详见表1。**表1** HLB数字证书说明| 数字证书 | 关联场景 | 证书类型 | 私钥文件 | 私钥密码 | 证书应用场景 || --- | --- | --- | --- | --- | --- || HLB服务端证书 | HLB 服务证书集  （UPCF\_HLB\_Lcert） | * 设备证书：HLBcert.pem * 根CA：Huawei\_Equipment\_Root\_CA.der * 二级CA：Huawei Cloud Core Network Product CA.cer | HLBcert.key | 联系华为技术支持。 | 用于通过Https访问HLB服务时需要一起加载。 || HLB客户端证书 |  |  |  |  |  |* 华为证书获取路径：https://support.huawei.com/ >技术支持>产品支持>云核心网>Mobile Packet Core>5G Convergent Data>UPCF>UPCF。在“产品软件”界面选择对应的UPCF版本，“设备证书”、“私钥文件”和提供给对端设备的“CA证书”均存放在UPCF\_Cert\_Tools.zip里，UPCF\_Cert\_Tools.zip包含在UPCF\_2\*.\*\*\*.\*\*\*.\*\*\*\_Tools.zip当中。* 华为证书仅用于测试环境，不能用于商用环境。商用环境请替换为商用证书，并通过OM Portal的证书管理功能删除华为证书。若客户将华为证书用于商用环境，则需承担相关安全风险和责任。为了提高系统安全性，需定期更新证书和密钥。* 加载CA证书时，需要加载完整的CA证书链。* 加载CRL文件时，需要加载完整的CA链签发的CRL文件，即CA证书链中每个CA证书签发的CRL文件都要加载。

## 必备事项
前提条件

* 证书文件已经经过授权和认证。
* 若使用华为证书，证书密码已经通过华为技术工程师获取。
* 若使用运营商自身的证书，证书密码已经从运营商处获取。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_hlbtlscfg_list:
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
          enum:
          - TLS1_2
          - TLS1_3
          - TLS1_2+TLS1_3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_hlbdevaddr_list:
      type: items
      properties:
        DEVAID:
          name: '设备地址标识'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPSFUNC:
          name: 'HTTPS功能'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CERTSCENE:
          name: '证书应用场景'
          type: string
          enum:
          - UPCF_HLB_Lcert
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
    add_hlbpeer_list:
      type: items
      properties:
        ID:
          name: 'ID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NAME:
          name: 'NAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPSFUNC:
          name: 'HTTPSFUNC'
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
        TLSCFGID:
          name: 'TLSCFGID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_hlbtlscfg_list:
    - TLSCFGID: TLS配置ID
      TLSCFGNAME: 'TLS配置名称'
      PROTOCOLVER: TLS1_2
    mod_hlbdevaddr_list:
    - DEVAID: 设备地址标识
      HTTPSFUNC: ON
      CERTSCENE: UPCF_HLB_Lcert
      TLSCFGID: TLS配置ID
    add_hlbpeer_list:
    - ID: 索引
      NAME: 名称
      TYPE: SMF
      HTTPSFUNC: ON
      CERTSCENE: UPCF_HLB_Lcert
      TLSCFGID: TLS配置ID
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在CSP界面配置新的数字证书后，对于服务端数字证书，需要重启对应的服务；对于客户端数字证书，需要重启对应的链路，新的证书才能生效。

### 重启操作属于产品慎用操作，如果操作不当，会引发业务中断等严重后果。请操作员在华为技术支持指导下谨慎操作。

### 配置HLB数字证书需加载证书集（包括设备证书和CA证书），将证书集关联到“HLB 服务证书集（UPCF\_HLB\_Lcert）”场景下。

### 登录CSP Portal界面，选择**安全** > **证书管理** > **证书与证书集管理**，点击上传证书。

### 2 选择“证书集”，加载HLB数字证书集，界面配置参数如表2所示。详细操作请参见证书与证书集管理。

### **表2** 配置证书集

### | 界面参数 | 取值示例 | 取值原则 |

### | --- | --- | --- |

### | 证书集 | HLB\_CertSet | 自行命名，保证系统内命名唯一即可。 |

### | 设备证书 | HLBcert.pem | 上传设备证书文件HLBcert.pem，解压UPCF\_Cert\_Tools.zip，在HLB文件夹下获取。 |

### | 私钥文件 | HLBcert.key | 上传私钥文件HLBcert，解压UPCF\_Cert\_Tools.zip，在HLB文件夹下获取。 |

### | 私钥密码 | *\*\*\*\*\*\** | 联系华为技术支持。 |

### | CA证书 | Huawei\_Equipment\_Root\_CA.der | 上传CA证书Huawei\_Equipment\_Root\_CA.der，解压UPCF\_Cert\_Tools.zip，在HLB文件夹下获取。 |

### 3 上传证书完成后，选择证书应用场景关联，为证书场景“HLB 服务证书集（UPCF\_HLB\_Lcert）”关联刚加载的HLB证书集。详细的关联证书操作请参见证书应用场景关联。

### 4 执行**ADD HLBTLSCFG**命令，增加TLS配置信息。

```jinja2
{%- for item in add_hlbtlscfg_list -%}
    ADD HLBTLSCFG:
    {#- --- 必选参数 --- -#}
    TLSCFGID={{item.TLSCFGID}},
    TLSCFGNAME="{{item.TLSCFGNAME}}",
    PROTOCOLVER={{item.PROTOCOLVER}},
    ;
{%- endfor -%}
```

### 5 执行**MOD HLBDEVADDR**命令，配置HLB数字证书。

```jinja2
{%- for item in mod_hlbdevaddr_list -%}
    MOD HLBDEVADDR:
    {#- --- 必选参数 --- -#}
    DEVAID={{item.DEVAID}},
    {#- --- 可选参数 --- -#}
    {%- if item.HTTPSFUNC is not none -%}
        HTTPSFUNC={{item.HTTPSFUNC}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：HTTPSFUNC=ON 时可选 --- -#}
    {%- if item.HTTPSFUNC == 'ON' -%}
        {%- if item.CERTSCENE is not none -%}
            CERTSCENE={{item.CERTSCENE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：HTTPSFUNC=ON 时可选 --- -#}
    {%- if item.HTTPSFUNC == 'ON' -%}
        {%- if item.TLSCFGID is not none -%}
            TLSCFGID={{item.TLSCFGID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 仅当现网存在静态链路时，才需要执行本步骤，否则跳过本步骤。

### 执行**ADD HLBPEER**命令，配置HLB数字证书。以“类型”为“SMF”举例：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_hlbpeer_list的变量区（command: ADD HLBPEER） -#}
<!-- MISSING_MACRO: command=ADD HLBPEER list_name=add_hlbpeer_list step_id=6 -->
```

