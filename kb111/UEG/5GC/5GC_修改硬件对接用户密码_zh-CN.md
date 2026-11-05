---
id: ''
name: 修改硬件对接用户密码
ne_type: UEG
type: feature
description: CSP管理硬件的过程中，使用了Administrator、DmsMgmt和eventAccount三个相关帐户。  其中，Administrator是用于登录服务器iBMC系统的管理员帐户，该帐户默认密码参考硬件服务器用户操作手册默认密码章节。CSP系统加密存储了该帐户的默认值。在服务器初次接入CSP系统时，CSP通过使用默认帐户信息登录到服务器iBMC系统，并在服务器iBMC系统中创建DmsMgmt帐户。DmsMgmt帐户默认密码为随机密码，CSP系统加密存储了该帐户的密码。后续所有的设备管理流程均通过DmsMgmt帐户进行认证，比如获取服务器状态信息等。eventAccount帐户是CSP接收服务器上报告警时，校验该告警来源的服务器是否合法的认证凭证，eventAccount帐户默认密码为随机密码，并且每60天会重新随机密码。  如果接入服务器的DmsMgmt帐户信息在iBMC系统中被更改，用户可参考本章修改CSP中存储的DmsMgmt帐户信息。  如果用户需要统一修改eventAccount帐户信息，可参考本章节进行修改。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","运维安全配置","修改硬件对接用户密码"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","运维安全配置","修改硬件对接用户密码"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置安全数据","核心网网元安全加固","UEG安全加固","裸机容器模式UEG安全加固","安全配置建议","必选配置","运维安全配置","修改硬件对接用户密码"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","必选配置","运维安全配置","修改硬件对接用户密码"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-S","子园区UEG-S安全加固配置","安全配置建议","必选配置","运维安全配置","修改硬件对接用户密码"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
CSP管理硬件的过程中，使用了Administrator、DmsMgmt和eventAccount三个相关帐户。其中，Administrator是用于登录服务器iBMC系统的管理员帐户，该帐户默认密码参考硬件服务器用户操作手册默认密码章节。CSP系统加密存储了该帐户的默认值。在服务器初次接入CSP系统时，CSP通过使用默认帐户信息登录到服务器iBMC系统，并在服务器iBMC系统中创建DmsMgmt帐户。DmsMgmt帐户默认密码为随机密码，CSP系统加密存储了该帐户的密码。后续所有的设备管理流程均通过DmsMgmt帐户进行认证，比如获取服务器状态信息等。eventAccount帐户是CSP接收服务器上报告警时，校验该告警来源的服务器是否合法的认证凭证，eventAccount帐户默认密码为随机密码，并且每60天会重新随机密码。如果接入服务器的DmsMgmt帐户信息在iBMC系统中被更改，用户可参考本章修改CSP中存储的DmsMgmt帐户信息。如果用户需要统一修改eventAccount帐户信息，可参考本章节进行修改。

## 必备事项
前提条件

已登录OM Portal。
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

### 1 登录OM Portal，选择“应用管理 > MML”。

### 2 执行**LST OMIP**查询系统当前物理IP地址。

### 3 使用**mtuser**用户通过**putty**登录系统管理节点，执行**su - root**切换至root用户。

### 如果**LST OMIP**中查询到多个物理IP地址，使用任意一个IP地址登录系统管理节点即可。

### 4 执行**bash /opt/tools/dms\_conf\_modify.sh**，根据系统提示信息，修改对应用户的密码。

### host-192-168-0-2:/home/mtuser # bash /opt/tools/dms_conf_modify.sh

### *********************************************************************

### *************************** WARNING *********************************

### *********************************************************************

### * This shell script is used to modify the password of DmsMgmt and eventAccount user *

### * You need enter parameters.                                      *

### * If you want to quit, please press "Ctrl + c".                     *

### *********************************************************************

### Please input the DMS user name ended with Enter:       //输入需要修改的帐户

### Please input the new password ended with Enter:        //输入DmsMgmt账户新密码，eventAccount账户不需要执行此步骤

### Please re-enter new password ended with Enter:          //再次输入DmsMgmt账户新密码，eventAccount账户不需要执行此步骤

### Send request message to cspdevicemanager.

### success,0                                               //修改成功

### *********************************************************************

### 若屏幕出现**success,0**，表明该用户的密码修改成功。

### 若屏幕出现**failed，*****错误码***，表明用户的密码修改失败，需要根据表1查询失败原因。

### **表1** 错误码列表

### | 错误码 | 原因 |

### | --- | --- |

### | 1 | 输入的新密码为空。 |

### | 2 | 系统内部错误。 |

### | 3 | 输入的帐户非硬件对接用户（eventAccount或DmsMgmt）。 |

### | 4 | 新密码和再次输入新密码不一致。 |

