---
id: ''
name: 配置PGW HTTPS数字证书
ne_type: UEG
type: feature
description: 用户使用浏览器首次使用HTTPS认证方式登录PGW Web LMT或DMS WebUI之前需要加载HTTPS证书文件。业务发放系统和PGW服务端之间使用HTTPS协议进行通信时使用SOAP、MML或REST类型的HTTPS证书文件；客户端（PGW Web LMT或DMS WebUI）和PGW服务端之间使用HTTPS协议进行通信时使用WEBLMT类型的HTTPS证书文件。  * 安装USCDB网元时已不再默认加载华为证书文件，客户需要自行申请并部署商用证书文件。当仅用于系统调测时，如果客户无法申请到证书文件，请联系华为技术工程师获取。 * 长期使用同一数字证书，可能存在安全风险，为了提高系统安全性，强烈建议运营商定期更新证书。证书文件加载成功后，需要手动删除服务器上的证书文件。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","必选配置","网络安全配置","配置PGW HTTPS数字证书"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","必选配置","网络安全配置","配置PGW HTTPS数字证书"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","必选配置","网络安全配置","配置PGW HTTPS数字证书"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
用户使用浏览器首次使用HTTPS认证方式登录PGW Web LMT或DMS WebUI之前需要加载HTTPS证书文件。业务发放系统和PGW服务端之间使用HTTPS协议进行通信时使用SOAP、MML或REST类型的HTTPS证书文件；客户端（PGW Web LMT或DMS WebUI）和PGW服务端之间使用HTTPS协议进行通信时使用WEBLMT类型的HTTPS证书文件。* 安装USCDB网元时已不再默认加载华为证书文件，客户需要自行申请并部署商用证书文件。当仅用于系统调测时，如果客户无法申请到证书文件，请联系华为技术工程师获取。* 长期使用同一数字证书，可能存在安全风险，为了提高系统安全性，强烈建议运营商定期更新证书。证书文件加载成功后，需要手动删除服务器上的证书文件。

## 必备事项
前提条件

客户已申请证书文件并已获取对应的证书密码。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties: {}
  examples: {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录OM Portal界面。

### 2 进入“系统 > 文件传输”页面。

### 3 在左侧“文件传输”菜单中选择“CGPLite文件 > 网元文件”。

### 4 单击“添加文件”，选择需要上传的证书文件并上传。

### **图1** 上传证书文件

### 5 登录“USCDB MML命令”界面。

### 6 执行**ADD PORT**命令设置SUP-FE网元的“端口子类型”为SOAP、MML或REST端口。

### 加载SOAP、MML或REST类型的证书时需要执行该操作。

### 如果是加载USCDB的默认端口的证书，则可跳过此步骤。端口相关信息可参考PGW端口配置管理中的“表1 端口类型和协议关系表”。

### “SUP-FE”仅为示例，此处请以实际的FE类型为准。

### 7 执行**LOD VERIF**命令分别加载CA证书、设备证书和密钥文件。

### 8 根据加载证书的端口类型不同，需要做如下操作：

#### 8.1 加载SOAP类型的证书，需要执行**MOD INSP**命令设置如下软件参数。

##### 8.1.1 “PROVRIGHTSWITCH（营帐权限开关）”设置为“1”。

##### 8.1.2 “TLSMODE（TLS工作模式）”设置为“3”。

##### 8.1.3 “HTTPSAUTHSWITCH（HTTPS鉴权开关）”为“0”

#### 8.2 加载MML类型的证书，需要执行**ADD PORT**/**MOD PORT**命令设置参数“端口子类型”为“PORT\_FOR\_MML” 且“是否使用HTTPS”为“YES”，执行**MOD INSP**命令设置“MMLTLSAUTHSWITCH（MML TLS鉴权开关）”为“0”。

#### 8.3 加载WEBLMT类型的证书，需要执行**MOD INSP**命令设置软件参数“WEBLMTHTTPSSWITCH（weblmt https控制开关）”为“1”。

### 9 执行**RST MODULE**命令重启PGW进程使配置生效。

### 如果加载的是WEBLMT类型的证书，需要重启所有PGW模块、所有DMA模块、网关类型为PGW的DPU模块和DMA类型的DPU模块。

