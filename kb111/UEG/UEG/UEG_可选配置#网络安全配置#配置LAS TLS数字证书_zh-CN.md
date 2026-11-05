---
id: ''
name: 配置LAS TLS数字证书
ne_type: UEG
type: feature
description: 第三方FE和LAS之间的LDAP接口使用TLS协议进行通信时需要加载证书文件。  长期使用同一数字证书，可能存在安全风险，为了提高系统安全性，强烈建议运营商定期更新证书。证书文件加载成功后，需要手动删除服务器上的证书文件。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","配置LAS TLS数字证书"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
第三方FE和LAS之间的LDAP接口使用TLS协议进行通信时需要加载证书文件。长期使用同一数字证书，可能存在安全风险，为了提高系统安全性，强烈建议运营商定期更新证书。证书文件加载成功后，需要手动删除服务器上的证书文件。

## 必备事项
前提条件

客户已申请证书文件并已获取对应的证书密码。
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
  examples:
    rst_msprocess_list:
    - PROCOBJECT: PROCNAME
      PROCNAME: 'CELL_UdrLas'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录OM Portal界面。

### 2 上传证书。

#### 2.1 选择“安全 > 证书管理”，进入“证书与证书集管理”界面。

#### 2.2 单击“上传证书”，进入证书创建向导界面，选择证书类型为“证书集”。

#### **图1** 选择证书类型

#### 2.3 根据需要选择证书类型后，单击“下一步”。

#### 2.4 填写“证书集名称”、选择“CA证书”、“设备证书”、“私钥文件”、填写“私钥密码”后，单击“确定”，上传证书文件。

#### **图2** 上传证书文件

#### 2.5 返回“证书与证书集管理”界面，查看已上传的证书。

#### **图3** 证书与证书集管理

### 3 登录CSP Portal页面，在对应证书场景关联正确的证书。

#### 3.1 选择“安全 > 证书管理”，进入“证书应用场景关联”界面。

#### **图4** 证书应用场景关联界面

#### 3.2 单击“关联证书”，为“场景名称”为“UDRLas\_LDAP\_Cert”的应用场景关联所需证书。

#### 3.3 选择对应类型的证书后，单击“确定”。

#### **图5** 关联证书

#### 3.4 返回“证书应用场景关联”界面，可查看到应用场景的“关联证书”，则表示证书应用场景关联成功。

### 4 登录“USCDB MML命令”界面，执行如下命令重启所有LAS服务。

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

