---
id: ''
name: 配置LDAP数字证书
ne_type: UEG
type: feature
description: LDAP服务作为客户端，当需要通过TLS与LDAP服务器对接时，需要加载CA证书。LDAP服务使用到的证书详见表1。  **表1** LDAP数字证书说明  | 数字证书 | 关联场景 | 证书类型 | 私钥文件 | 私钥密码 | 证书应用场景 | | --- | --- | --- | --- | --- | --- | | LDAP客户端证书 | LDAP接口链路客户端证书  （UPCF\_LDAP\_certForLDAPLNK） | CA证书：由对端LDAP服务器提供 | - | - | 用于通过TLS与LDAP服务器对接需要加载。 |  * 华为证书仅用于测试环境，不能用于商用环境。商用环境请替换为商用证书，并通过OM Portal的证书管理功能删除华为证书。若客户将华为证书用于商用环境，则需承担相关安全风险和责任。为了提高系统安全性，需定期更新证书和密钥。 * 加载CA证书时，需要加载完整的CA证书链。 * 加载CRL文件时，需要加载完整的CA链签发的CRL文件，即CA证书链中每个CA证书签发的CRL文件都要加载。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置LDAP数字证书"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置LDAP数字证书"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置LDAP数字证书"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","网络安全配置","配置UPCF HTTPS数字证书","配置LDAP数字证书"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
LDAP服务作为客户端，当需要通过TLS与LDAP服务器对接时，需要加载CA证书。LDAP服务使用到的证书详见表1。**表1** LDAP数字证书说明| 数字证书 | 关联场景 | 证书类型 | 私钥文件 | 私钥密码 | 证书应用场景 || --- | --- | --- | --- | --- | --- || LDAP客户端证书 | LDAP接口链路客户端证书  （UPCF\_LDAP\_certForLDAPLNK） | CA证书：由对端LDAP服务器提供 | - | - | 用于通过TLS与LDAP服务器对接需要加载。 |* 华为证书仅用于测试环境，不能用于商用环境。商用环境请替换为商用证书，并通过OM Portal的证书管理功能删除华为证书。若客户将华为证书用于商用环境，则需承担相关安全风险和责任。为了提高系统安全性，需定期更新证书和密钥。* 加载CA证书时，需要加载完整的CA证书链。* 加载CRL文件时，需要加载完整的CA链签发的CRL文件，即CA证书链中每个CA证书签发的CRL文件都要加载。

## 必备事项
前提条件

* 证书文件已经经过授权和认证。
* 已经从运营商获取对端LDAP服务CA证书。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ldaplnk_list:
      type: items
      properties:
        LINKID:
          name: '链路ID'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LNKNAME:
          name: '链路名称'
          type: string
          minLength: 0
          maxLength: 32
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
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIP:
          name: '对端IPV4地址'
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
        USERNAME:
          name: '用户名'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PWD:
          name: '密码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSPRI:
          name: '数据源优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFUNC:
          name: 'TLS功能'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ON
        CERTSCENE:
          name: '证书应用场景'
          type: string
          enum:
          - UPCF_LDAP_certForLDAPLNK
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CRLPOLICY:
          name: 'CRL策略'
          type: string
          enum:
          - Check
          - NoCheck
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Check
  examples:
    add_ldaplnk_list:
    - LINKID: 链路ID
      LNKNAME: '链路名称'
      IPVER: IPV4
      LOCALPORT: 本端端口
      PEERIP: '对端IPV4地址'
      PEERPORT: 对端端口
      USERNAME: '用户名'
      PWD: '密码'
      CFM: '确认密码'
      DSPRI: 数据源优先级
      TLSFUNC: ON
      CERTSCENE: UPCF_LDAP_certForLDAPLNK
      CRLPOLICY: CRL策略
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在CSP界面配置新的数字证书后，原有的已经建链的LDAP链路会自动断链，系统会使用新的证书再重新建链。

### 更新证书会导致链路重启，重启操作属于产品慎用操作，如果操作不当，会引发业务中断等严重后果。请操作员在华为技术支持指导下谨慎操作。

### 配置LDAP数字证书需加载CA证书，并将证书关联到证书应用场景下。

### 登录OM Portal，选择**安全** > **证书管理** > **证书与证书集管理**，单击“上传证书”。

### 2 选择“CA证书”，加载LDAP数字证书，界面配置参数如表2所示。详细操作请参见证书与证书集管理。

### **表2** 配置CA证书

### | 界面参数 | 取值示例 | 取值原则 |

### | --- | --- | --- |

### | 证书名称 | LDAP\_CACert | 自行命名，保证系统内命名唯一即可。 |

### | CA证书 | \*\*\*.der | 上传的CA证书文由待对接的LDAP服务器提供。 |

### 3 上传证书完成后，选择“证书应用场景关联”，为证书场景关联加载的CA证书。详细的关联证书操作请参见证书应用场景关联。

### “LDAP接口链路客户端证书”需关联2中加载的LDAP服务器提供的CA证书。

### 4 执行**ADD LDAPLNK**命令，配置LDAP客户端数字证书。

### 选择“TLS功能”为“ON(打开)”，“证书应用场景”为“UPCF\_LDAP\_certForLDAPLNK(LDAP接口链路客户端证书)”进行配置。

```jinja2
{%- for item in add_ldaplnk_list -%}
    ADD LDAPLNK:
    {#- --- 必选参数 --- -#}
    LINKID={{item.LINKID}},
    IPVER={{item.IPVER}},
    LOCALPORT={{item.LOCALPORT}},
    PEERPORT={{item.PEERPORT}},
    USERNAME="{{item.USERNAME}}",
    PWD="{{item.PWD}}",
    CFM="{{item.CFM}}",
    DSPRI={{item.DSPRI}},
    {#- --- 可选参数 --- -#}
    {%- if item.LNKNAME is not none -%}
        LNKNAME="{{item.LNKNAME}}",
    {%- endif -%}
    {%- if item.TLSFUNC is not none -%}
        TLSFUNC={{item.TLSFUNC}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        PEERIP="{{item.PEERIP}}",
    {%- endif -%}
    {#- --- 条件必选：TLSFUNC=ON 时必选 --- -#}
    {%- if item.TLSFUNC == 'ON' -%}
        CERTSCENE={{item.CERTSCENE}},
    {%- endif -%}
    {#- --- 条件必选：TLSFUNC=ON 时必选 --- -#}
    {%- if item.TLSFUNC == 'ON' -%}
        CRLPOLICY={{item.CRLPOLICY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

