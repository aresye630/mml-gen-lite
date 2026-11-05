---
id: ''
name: 上传国密IPsec证书
ne_type: UNC
type: feature
description: 在IPsec VPN中，对等体间可以通过证书进行身份认证。对等体事先向证书颁发机构申请证书，在建立VPN连接之前，先验证对方证书是否合法。认证通过后，才能与对方建立连接，从而有效防止中间人攻击。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","可选配置","网络安全配置","配置IPSec功能","上传国密IPsec证书"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在IPsec VPN中，对等体间可以通过证书进行身份认证。对等体事先向证书颁发机构申请证书，在建立VPN连接之前，先验证对方证书是否合法。认证通过后，才能与对方建立连接，从而有效防止中间人攻击。

## 必备事项
前提条件

* 操作人员已经登录OM Portal。
* 已申请并获取IPsec证书，包括CA证书、签名设备证书、签名设备证书私钥文件、加密设备证书和加密设备证书私钥文件。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_pkicrlcheck_list:
      type: items
      properties:
        ISCRLENABLE:
          name: 'CRL检查'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '可选操作，存在IPsec CA证书对应的证书吊销列表（CRL文件）时，使能CRL检查功能。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
    add_certscene_list:
      type: items
      properties:
        SCENENAME:
          name: '场景名称'
          type: string
          minLength: 0
          maxLength: 192
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCENETYPE:
          name: '场景类型'
          type: string
          enum:
          - CA
          - LOCAL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDESCRIPTION:
          name: '场景英文描述'
          type: string
          minLength: 0
          maxLength: 192
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNDESCRIPTION:
          name: '场景中文描述'
          type: string
          minLength: 0
          maxLength: 192
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CERTTYPE:
          name: '证书类型'
          type: string
          enum:
          - 'NULL'
          - Cert_sig
          - Cert_enc
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Cert_sig
  examples:
    set_pkicrlcheck_list:
    - ISCRLENABLE: TRUE
    add_certscene_list:
    - SCENENAME: 'DeviceA_CA'
      SCENETYPE: CA
      ENDESCRIPTION: 'DeviceA_CA'
      CNDESCRIPTION: 'DeviceA_CA'
      CERTTYPE: Cert_sig
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 如果存在IPsec CA证书对应的证书吊销列表（CRL文件），则使能CRL检查功能。

```jinja2
{%- if is_optional_crl_check -%}
    {%- for item in set_pkicrlcheck_list -%}
        SET PKICRLCHECK:
        {#- --- 可选参数 --- -#}
        {%- if item.ISCRLENABLE is not none -%}
            ISCRLENABLE={{item.ISCRLENABLE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 上传IPsec证书文件。

### 选择“安全 > 证书管理>证书与证书集管理”，单击“上传证书”，分别上传IPsec CA证书和IPsec设备证书（包含设备证书私钥文件）。

### 3 如果步骤 1中使能了CRL检查功能，则必须上传IPsec CRL文件。

### 选择“安全 > 证书管理>上传证书吊销列表”，单击“上传证书吊销列表”，上传IPsec CRL文件。

### 4 分别创建IPsec CA证书场景和IPsec设备证书场景。

```jinja2
{%- for item in add_certscene_list -%}
    ADD CERTSCENE:
    {#- --- 必选参数 --- -#}
    SCENENAME="{{item.SCENENAME}}",
    SCENETYPE={{item.SCENETYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ENDESCRIPTION is not none -%}
        ENDESCRIPTION="{{item.ENDESCRIPTION}}",
    {%- endif -%}
    {%- if item.CNDESCRIPTION is not none -%}
        CNDESCRIPTION="{{item.CNDESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SCENETYPE=LOCAL 时可选 --- -#}
    {%- if item.SCENETYPE == 'LOCAL' -%}
        {%- if item.CERTTYPE is not none -%}
            CERTTYPE={{item.CERTTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 关联IPsec证书和证书场景。

#### 5.1 选择“安全 > 证书管理 > 证书应用场景关联”，在证书场景列表中选择步骤 4中增加的IPsec证书场景，单击“关联证书”。

#### 5.2 选择需要与该场景关联的IPsec证书，比如IPsec设备证书场景则选择对应的IPsec设备证书进行关联，IPsec CA证书场景则选择对应的IPsec CA证书和CRL文件进行关联。

#### CA证书与CRL文件一一对应。当一个证书场景关联了多个CA证书时，如果需要启用CRL功能，那么还需要一一关联这些CA证书所对应的CRL文件。当使用v1国密数字信封时，如果签名证书和加密证书配反了，需要正确配置两次以上才可恢复到正常的配置，其他情况下的证书认证，只需要正确配置一次即可。

### 6 查询IPsec微服务证书列表，检查步骤 2中的证书是否已通过场景关联同步到IPsec微服务。

