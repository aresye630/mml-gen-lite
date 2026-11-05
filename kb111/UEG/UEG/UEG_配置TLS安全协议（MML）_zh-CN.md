---
id: ''
name: 配置TLS安全协议（MML）
ne_type: UEG
type: feature
description: 当USCDB使用MML接口与业务发放系统对接时，MML接口支持TCP和TCP+TLS两种传输方式。  在传输数据时，TLS会建立一个信息安全通道，该通道用于提供加密通讯及对网络服务器身份的鉴定，因此出于安全的考虑，推荐在MML接口上配置TLS安全协议。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","配置TLS安全协议（MML）"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","可选配置","网络安全配置","配置TLS安全协议（MML）"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","配置TLS安全协议（MML）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当USCDB使用MML接口与业务发放系统对接时，MML接口支持TCP和TCP+TLS两种传输方式。在传输数据时，TLS会建立一个信息安全通道，该通道用于提供加密通讯及对网络服务器身份的鉴定，因此出于安全的考虑，推荐在MML接口上配置TLS安全协议。

## 必备事项
前提条件

* 向系统管理员获取OM Portal的帐号的密码。
* 确认已加载“连接类型”为“MML”的“CAVERIF(CA证书)”或“ROOTVERIF(根证书)”、“DEVVERIF(设备证书)”和“KEYFILE(密钥文件)”的证书文件。可通过在“USCDB MML命令”界面执行**LST VERIF**命令查询。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rst_module_list:
      type: items
      properties:
        MID:
          name: '模块号'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT:
          name: '模块类型'
          type: string
          enum:
          - DPU
          - NDF
          - DBG
          - DSG
          - DRU
          - DSU
          - PGW
          - DMA
          - CAG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    rst_module_list:
    - MID: 模块号
      MT: PGW
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

### 2 执行**LST FEPLUG**命令查询网元类型。

### 3 执行**ADD PORT**/**MOD PORT**命令，设置参数“端口子类型”为“PORT\_FOR\_MML”和“PORT\_FOR\_LMT\_MML ”且“是否使用HTTPS”为“YES”。

### 4 执行**LST MODULE**命令，查询所有PGW模块的模块号。

### 5 执行**RST MODULE**命令，重启所有的PGW模块。

### 重启PGW进程会导致短暂的业务发放指令执行失败，因此推荐此操作在话务低峰期执行，并提前通知客户做好准备。

```jinja2
{%- for item in rst_module_list -%}
    RST MODULE:
    {#- --- 必选参数 --- -#}
    MID={{item.MID}},
    MT={{item.MT}},
    ;
{%- endfor -%}
```

