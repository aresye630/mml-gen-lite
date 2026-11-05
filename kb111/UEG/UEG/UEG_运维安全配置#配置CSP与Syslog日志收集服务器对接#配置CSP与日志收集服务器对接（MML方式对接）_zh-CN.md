---
id: ''
name: 配置CSP与日志收集服务器对接（MML方式对接）
ne_type: UEG
type: feature
description: 为方便用户对日志进行分析和审计，CSP支持通过MML方式与最多三个第三方或华为Syslog日志收集服务器对接，将日志上传到指定的日志收集服务器。本章节介绍CSP与日志收集服务器通过MML命令的对接方法，MML对接方式当前默认使用TLS协议，不支持修改，如需使用TCP协议或UDP协议对接，请通过OM Portal上“系统 > Syslog管理”进行配置。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","虚机容器模式","配置安全数据（风筝S）","安全配置建议","可选配置","运维安全配置","配置CSP与Syslog日志收集服务器对接","配置CSP与日志收集服务器对接（MML方式对接）"]
  - ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","配置安全数据（风筝S）","安全配置建议","可选配置","运维安全配置","配置CSP与Syslog日志收集服务器对接","配置CSP与日志收集服务器对接（MML方式对接）"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","UPF安全数据","安全配置建议","可选配置","运维安全配置","配置CSP与Syslog日志收集服务器对接","配置CSP与日志收集服务器对接（MML方式对接）"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","MPF安全数据","安全配置建议","可选配置","运维安全配置","配置CSP与Syslog日志收集服务器对接","配置CSP与日志收集服务器对接（MML方式对接）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为方便用户对日志进行分析和审计，CSP支持通过MML方式与最多三个第三方或华为Syslog日志收集服务器对接，将日志上传到指定的日志收集服务器。本章节介绍CSP与日志收集服务器通过MML命令的对接方法，MML对接方式当前默认使用TLS协议，不支持修改，如需使用TCP协议或UDP协议对接，请通过OM Portal上“系统 > Syslog管理”进行配置。

## 必备事项
前提条件

* 已登录OM Portal。
* 日志收集服务器已配置Server端数字证书。

  如果对接华为公司的日志收集服务器，则使用系统初始证书即可，无需再配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_syslogtask_list:
      type: items
      properties:
        ENABLE:
          name: '启用状态'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_syslogtask_list:
    - ENABLE: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在OM Portal上选择“应用管理 > MML”，在MML输入框中输入**SET SYSLOGTASK****SET SYSLOGTASK**，单击“执行”。

```jinja2
{%- for item in set_syslogtask_list -%}
    SET SYSLOGTASK:
    {#- --- 必选参数 --- -#}
    ENABLE={{item.ENABLE}},
    ;
{%- endfor -%}
```

### “启用状态”设置为“启用”。

### “IP类型”根据需要选择。

### “日志收集服务器IP地址”和“服务器端口”根据实际填写。

### “日志类型”根据实际填写，系统支持全部上报或者部分上报。

### 2 执行**LST SYSLOGTASK****LST SYSLOGTASK**命令，查看“连接状态”。

### 如果“连接状态”为“连接” => 说明CSP与日志收集服务器对接成功。

### 如果“连接状态”为“断开” => 如果是华为日志收集服务器，请联系华为技术支持，如果是第三方日志收集服务器，请执行3。

### 3 选择“安全 > 证书管理 > 证书与证书集管理”，上传CA证书和设备证书。

### 4 选择“安全 > 证书管理 > 证书应用场景关联”，将3中上传的CA证书、设备证书分别按照表1进行场景关联。

### **表1** 可关联的证书场景

### | 场景证书类型 | 场景描述 |

### | --- | --- |

### | Device | 对接syslog服务器用户设备证书 |

### |  | 对接syslog拓展服务器1用户设备证书 |

### |  | 对接syslog拓展服务器2用户设备证书 |

### |  | 对接syslog拓展服务器3用户设备证书 |

### | CA | 对接syslog服务器用户CA证书 |

### |  | 对接syslog拓展服务器1用户CA证书 |

### |  | 对接syslog拓展服务器2用户CA证书 |

### |  | 对接syslog拓展服务器3用户CA证书 |

### 5 选择“应用管理 > MML”，执行**LST SYSLOGTASK****LST SYSLOGTASK**命令，查看“连接状态”。

### 如果“连接状态”为“连接” => 说明CSP与日志收集服务器对接成功。

### 如果“连接状态”为“断开” => 请联系华为技术支持。

