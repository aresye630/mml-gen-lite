---
id: ''
name: 上传密钥文件到FusionStage
ne_type: UEG
type: feature
description: 部署VNF前，需在FusionStage上传密钥文件，让各容器从该密钥文件读取数字证书，实现数字证书的统一管理。  当VNF LCM为V100R023C10SPC220及以上版本，FusionStage为24.0.0及以上版本时，无需上传密钥文件到FusionStage。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG软件安装（风筝S）","安装UPF（独立部署）","基于中心NFVO (Orchestrator)安装（UPF）","NFVO安装UEG（SDN场景）","安装单个UEG","上传密钥文件到FusionStage"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
部署VNF前，需在FusionStage上传密钥文件，让各容器从该密钥文件读取数字证书，实现数字证书的统一管理。当VNF LCM为V100R023C10SPC220及以上版本，FusionStage为24.0.0及以上版本时，无需上传密钥文件到FusionStage。

## 必备事项
前提条件

已登录FusionStage。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    cd_list:
      type: items
      properties: {}
    openssl_x509_list:
      type: items
      properties: {}
    openssl_rsa_list:
      type: items
      properties: {}
    openssl_crl_list:
      type: items
      properties: {}
    openssl_verify_list:
      type: items
      properties: {}
    openssl_x509_list_2:
      type: items
      properties: {}
    openssl_x509_list_4:
      type: items
      properties: {}
    openssl_crl_list_1:
      type: items
      properties: {}
    openssl_crl_list_2:
      type: items
      properties: {}
    openssl_x509_list_6:
      type: items
      properties: {}
    openssl_rsa_list_1:
      type: items
      properties: {}
    openssl_x509_list_7:
      type: items
      properties: {}
    openssl_crl_list_3:
      type: items
      properties: {}
  examples:
    cd_list:
    - {}
    openssl_x509_list:
    - {}
    openssl_rsa_list:
    - {}
    openssl_crl_list:
    - {}
    openssl_verify_list:
    - {}
    openssl_x509_list_2:
    - {}
    openssl_x509_list_4:
    - {}
    openssl_crl_list_1:
    - {}
    openssl_crl_list_2:
    - {}
    openssl_x509_list_6:
    - {}
    openssl_rsa_list_1:
    - {}
    openssl_x509_list_7:
    - {}
    openssl_crl_list_3:
    - {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 使用客户申请的证书时，需要将非PEM格式的证书转换为PEM格式、校验证书的有效性、并生成inner-comm-cert.yaml文件。

#### 1.1 安装OpenSSL，并将“OpenSSL程序安装路径\bin”添加到PC系统环境变量Path中。以windows操作系统为例，在系统栏搜索“环境变量”，在弹出的“系统属性”对话框中单击“环境变量”，双击“系统变量”中的Path，新增“OpenSSL程序安装路径\bin”，单击“确定”。

#### 1.2 启动命令行程序（本文以windows操作系统的cmd.exe为例），执行如下命令进入证书文件所在路径。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该cd_list的变量区（command: CD） -#}
<!-- MISSING_MACRO: command=CD list_name=cd_list step_id=1.2 -->
```

#### 证书文件所在路径必须为全英文字符。

#### 1.3 当证书文件不是PEM格式时，需要将其转换为PEM格式。此处以DER格式转换为PEM格式为例进行说明，执行如下命令。其它格式的证书转换，请参考OpenSSL帮助文档或联系华为技术服务工程师。

##### 1.3.1 将DER格式的CA证书和公钥证书转换为PEM格式

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_x509_list的变量区（command: openssl x509） -#}
<!-- MISSING_MACRO: command=openssl x509 list_name=openssl_x509_list step_id=1.3.1 -->
```

##### 1.3.2 将DER格式的私钥转换为PEM格式

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_rsa_list的变量区（command: openssl rsa） -#}
<!-- MISSING_MACRO: command=openssl rsa list_name=openssl_rsa_list step_id=1.3.2 -->
```

##### 1.3.3 将DER格式的证书吊销列表（CRL）转换为PEM格式

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_crl_list的变量区（command: openssl crl） -#}
<!-- MISSING_MACRO: command=openssl crl list_name=openssl_crl_list step_id=1.3.3 -->
```

#### 1.4 校验证书的有效性，执行如下命令：

##### 1.4.1 校验CA证书是否可验证公钥证书

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_verify_list的变量区（command: openssl verify） -#}
<!-- MISSING_MACRO: command=openssl verify list_name=openssl_verify_list step_id=1.4.1 -->
```

##### 如果CA证书可以验证公钥证书，执行命令后将返回：*转换后公钥证书文件名称**.pem*: OK。

##### 1.4.2 检查CA证书和公钥证书的有效期

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_x509_list_2的变量区（command: openssl x509） -#}
<!-- MISSING_MACRO: command=openssl x509 list_name=openssl_x509_list_2 step_id=1.4.2 -->
```

##### 执行命令后将返回证书的有效期，示例如下，请根据实际情况判断有效期是否符合要求。

##### notBefore=Dec 19 06:04:00 2019 GMT

##### notAfter=Dec 19 06:04:00 2020 GMT

##### 1.4.3 查看CA证书和公钥证书的指纹信息

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_x509_list_4的变量区（command: openssl x509） -#}
<!-- MISSING_MACRO: command=openssl x509 list_name=openssl_x509_list_4 step_id=1.4.3 -->
```

##### 1.4.4 检查CRL的有效期

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_crl_list_1的变量区（command: openssl crl） -#}
<!-- MISSING_MACRO: command=openssl crl list_name=openssl_crl_list_1 step_id=1.4.4 -->
```

##### 执行命令后将返回CRL的有效期，示例如下，请根据实际情况判断有效期是否符合要求。

##### lastUpdate=Dec 27 13:52:00 2019 GMT

##### nextUpdate=Jan 26 13:52:00 2020 GMT

##### 1.4.5 检查CA证书是否可验证CRL

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_crl_list_2的变量区（command: openssl crl） -#}
<!-- MISSING_MACRO: command=openssl crl list_name=openssl_crl_list_2 step_id=1.4.5 -->
```

##### 如果CA证书可验证CRL，执行命令后将返回：verify OK。

##### 1.4.6 检查公钥证书与私钥是否配对

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_x509_list_6的变量区（command: openssl x509） -#}
<!-- MISSING_MACRO: command=openssl x509 list_name=openssl_x509_list_6 step_id=1.4.6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_rsa_list_1的变量区（command: openssl rsa） -#}
<!-- MISSING_MACRO: command=openssl rsa list_name=openssl_rsa_list_1 step_id=1.4.6 -->
```

##### 如果两条命令执行后返回内容一致，则表示公钥证书与私钥是配对的。

##### 1.4.7 检查证书是否已被吊销。如果证书已被吊销，则需要重新申请证书。

###### 1.4.7.1 //获取公钥证书Serial Number

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_x509_list_7的变量区（command: openssl x509） -#}
<!-- MISSING_MACRO: command=openssl x509 list_name=openssl_x509_list_7 step_id=1.4.7.1 -->
```

###### 1.4.7.2 //检查公钥证书是否已被吊销

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该openssl_crl_list_3的变量区（command: openssl crl） -#}
<!-- MISSING_MACRO: command=openssl crl list_name=openssl_crl_list_3 step_id=1.4.7.2 -->
```

###### 如果在CRL文件中能够找到公钥证书Serial Number，则表示该证书已被吊销，请重新申请。

#### 1.5 制作Secret文件（即inner-comm-cert.yaml文件）。请使用如下模板制作Secret文件，将*红色斜体部分*替换为实际证书信息，并存储为.yaml格式。

#### apiVersion: v1

#### kind: Secret

#### metadata:

#### name: inner-comm-cert

#### comment: 描述内部通信证书信息

#### type: others

#### stringData:

#### #配置是否开启内部安全通信，取值true或false，默认值为true，无需修改。

#### enable: |-

#### true

#### #配置内部证书使用模式，取值shared或special，默认值为shared，无需修改。

#### mode: |-

#### shared

#### #配置私钥口令，默认私钥口令为明文，请根据实际值填写。

#### privKeyPwd: |-

#### YourPrivKeyPwd

#### #配置CA根证书。如果只有一个根CA，则只包含一个CA证书信息；如果存在多个根CA，则包含多个CA证书信息。

#### ca: |-

#### -----BEGIN CERTIFICATE-----

#### xxxx

#### -----END CERTIFICATE-----

#### -----BEGIN CERTIFICATE-----

#### xxxx

#### -----END CERTIFICATE-----

#### #配置TLS公钥证书和中间CA证书。存在多级中间CA时，从低级到高级顺序填写中间CA证书信息，如TLS公钥证书+CA证书+上级CA证书....

#### cert: |-

#### -----BEGIN CERTIFICATE-----

#### xxxx

#### -----END CERTIFICATE-----

#### -----BEGIN CERTIFICATE-----

#### xxxxx

#### -----END CERTIFICATE-----

#### #配置TLS私钥

#### privKey: |-

#### -----BEGIN RSA PRIVATE KEY-----

#### xxxx

#### -----END RSA PRIVATE KEY-----

#### #配置证书吊销列表

#### crl: |-

#### -----BEGIN X509 CRL-----

#### xxxx

#### -----END X509 CRL-----

#### 请勿修改模板格式，否则可能导致证书不可用。

#### 修改*红色斜体部分*内容时，每行前请务必保留4个空格（与当前模板格式一致），且不能存在空白行，否则可能导致证书不可用。

#### 换行符必须转换为unix格式。

### 2 通过FusionStage上传密钥文件（即inner-comm-cert.yaml文件）。

### 如果在FusionStage OM Portal“应用管理 > 应用配置 > Secret”中已存在inner-comm-cert.yaml文件，请单击“删除”后，再上传。

#### 2.1 登录FusionStage OM Portal。

##### 2.1.1 IPv4单栈场景登录地址：https://*IP**地址*:31943，其中IP地址为PaaSOM-1节点的外部网络平面（External\_Plane）的IPv4格式的浮动IP。

##### 2.1.2 混合部署场景仅支持使用IPv6登录，IPv6登录地址：https://*[IP地址]*:31943，其中IP地址为PaaSOM-1节点的外部网络平面（External\_Plane）的IPv6格式的浮动IP。

##### 2.1.3 输入用户名和密码。

##### 系统默认的用户名和密码是“admin/Changeme\_123”，如果已修改客户端用户名和密码，请使用新设置的用户名和密码登录。

#### 2.2 在菜单栏右侧单击，切换为需要上传密钥的项目，该项目承载了UEG。

#### 2.3 在主菜单选择“应用管理 > 应用配置 > Secret”，单击“创建Secret”。

#### **图1** 创建Secret

#### 2.4 单击“上传文件”。

#### 2.5 单击“选择文件”，上传密钥文件。

#### 2.6 单击“创建”。

#### **图2** 上传密钥文件

#### 2.7 返回“Secret”界面，确认已上传密钥文件。

#### **图3** 确认已上传密钥文件

#### 网元安装后若证书更新，需再次执行步骤2并执行MML命令**RST NODEBATCH**重启网元的所有VM以使新的证书生效。重启VM后，请通过VNF LCM的“自愈管理>自愈任务”查看VM是否重启成功。

