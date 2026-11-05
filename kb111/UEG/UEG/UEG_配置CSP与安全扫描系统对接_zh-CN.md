---
id: ''
name: 配置CSP与安全扫描系统对接
ne_type: UEG
type: feature
description: 网元提供OMU OS管理维护接口用于与外部系统对接，当网元需要对接外部系统进行安全扫描时，可以参考本章节操作。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","可选配置","运维安全配置","配置CSP与安全扫描系统对接"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
网元提供OMU OS管理维护接口用于与外部系统对接，当网元需要对接外部系统进行安全扫描时，可以参考本章节操作。

## 必备事项
前提条件

已登录网元OM Portal。
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

### 1 （可选）如果是CSP 21.3.3之前版本实例化的VNF，升级至CSP 21.3.3版本后需要扩容VNF管理节点vNIC。请联系华为工程师获取网元扩缩容指导书，执行对应操作。如果是CSP 21.3.3及之后版本实例化的VNF，则不需要执行本步骤。

### 2 操作系统默认帐号“mtuser”一般用于操作人员登录系统进行日常维护操作，建议创建专用的OS帐号用于安全扫描时的机机对接。

### 仅可以在两个管理节点创建OS帐号。操作员可登录OM Portal执行**DSP NODE**命令查看OMU管理节点所在的IP地址，其中虚拟机类型为A和B的节点支持创建OS用户。

#### 2.1 使用mtuser用户通过“putty.exe”（0.63版本及以上）登录系统管理节点，执行**su - root**切换至root用户。

#### 2.2 创建OS用户

##### 2.2.1 执行**bash /usr/bin/create\_out\_sshduser.sh -a "*<新创建用户名>*"** （新创建的用户名称需要满足Linux用户名要求，不能含有~！@￥%&等特殊符号）。

##### 2.2.2 界面提示“Please input password:”后，输入新创建用户的密码（密码需要满足复杂度要求，至少一个大写字母，一个小写字母，一个数字和一个特殊符号，长度14位以上）。

##### 2.2.3 界面提示“Are you sure you want to change the password upon your first login (yes/no)”后，输入**yes**开启登录强制修改密码功能（此用户用于对接第三方系统，开启后需要第三方系统对接配合修改，如果第三方无法支持此功能可输入**no**）；输入**no**关闭登录强制修改密码功能。

##### 2.2.4 界面提示：“add user ***<新创建用户名>*** success”则创建用户成功。若创建失败，请根据提示信息检查创建的用户名是否含有特殊字符，密码是否满足复杂度要求。

#### 2.3 OS用户创建完成后，可以执行如下命令查看用户相关信息。

#### 2.4 使用新创建的OS用户通过“putty.exe”（0.63版本及以上）登录OS管理维护接口IP。

#### OS管理维护接口IP查询方法为：使用mtuser登录到系统管理节点后，执行命令**ifconfig xxx**（xxx指OS管理维护接口），在查询结果中，inet的参数值即为OS管理维护接口IP，查询结果示例如图1所示。

#### **图1** OS管理维护接口IP查询方法

### 如果需要删除创建的OS用户，可以执行：**bash /usr/bin/create\_out\_sshduser.sh -d "*<待删除用户名>*"。**删除操作，会将用户相关的目录内容全部删除，如需保留请提前备份如下目录内容：/home/用户名; /var/mail/用户名; /var/spool/mail/用户名。可以使用**bash /usr/bin/create\_out\_sshduser.sh -h**查看脚本使用的帮助信息。

