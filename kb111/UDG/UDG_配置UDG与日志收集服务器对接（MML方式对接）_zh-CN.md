---
id: ''
name: 配置UDG与日志收集服务器对接（MML方式对接）
ne_type: UDG
type: feature
description: 为方便用户对日志进行分析和审计，UDG支持通过MML方式与最多三个第三方或华为Syslog日志收集服务器对接，将日志上传到指定的日志收集服务器。本章节介绍UDG与日志收集服务器通过MML命令的对接方法，MML对接方式当前默认使用TLS协议，不支持修改，如需使用TCP协议或UDP协议对接，请通过OM Portal上“系统 > Syslog管理”进行配置。
risk_level: ''
doc_source: ["网络部署","安全配置","UDG安全配置","安全配置建议","可选配置","运维安全配置","配置UDG与Syslog日志收集服务器对接","配置UDG与日志收集服务器对接（MML方式对接）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为方便用户对日志进行分析和审计，UDG支持通过MML方式与最多三个第三方或华为Syslog日志收集服务器对接，将日志上传到指定的日志收集服务器。本章节介绍UDG与日志收集服务器通过MML命令的对接方法，MML对接方式当前默认使用TLS协议，不支持修改，如需使用TCP协议或UDP协议对接，请通过OM Portal上“系统 > Syslog管理”进行配置。

## 必备事项
前提条件

* 已登录OM Portal。
* 日志收集服务器已配置Server端数字证书。

  如果对接华为公司的日志收集服务器，则使用系统初始证书即可，无需再配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
        CHECKSAN:
          name: 'Syslog服务器端SAN校验'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOGTYPE:
          name: '日志类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTOCOL:
          name: '协议类型'
          type: string
          enum:
          - TLS
          - TCP
          - UDP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVERPORT:
          name: '服务器端口'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_syslogtask_list:
    - ENABLE: ''
      CHECKSAN: ''
      DESC: ''
      IPTYPE: ''
      LOGTYPE: ''
      PROTOCOL: ''
      SERVERPORT: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在OM Portal上选择“应用管理 > MML”，在MML输入框中输入**SET SYSLOGTASK**，单击“执行”。

```jinja2
{%- for item in set_syslogtask_list -%}
    SET SYSLOGTASK:
    {#- --- 必选参数 --- -#}
    ENABLE={{item.ENABLE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ENABLE=ENABLE 时必选 --- -#}
    {%- if item.ENABLE == 'ENABLE' -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：ENABLE=ENABLE 时必选 --- -#}
    {%- if item.ENABLE == 'ENABLE' -%}
        LOGTYPE={{item.LOGTYPE}},
    {%- endif -%}
    {#- --- 条件必选：ENABLE=ENABLE 时必选 --- -#}
    {%- if item.ENABLE == 'ENABLE' -%}
        SERVERPORT={{item.SERVERPORT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ENABLE=ENABLE 时可选 --- -#}
    {%- if item.ENABLE == 'ENABLE' -%}
        {%- if item.CHECKSAN is not none -%}
            CHECKSAN={{item.CHECKSAN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENABLE=ENABLE 时可选 --- -#}
    {%- if item.ENABLE == 'ENABLE' -%}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENABLE=ENABLE 时可选 --- -#}
    {%- if item.ENABLE == 'ENABLE' -%}
        {%- if item.PROTOCOL is not none -%}
            PROTOCOL={{item.PROTOCOL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### “启用状态”设置为“启用”。

### “IP类型”根据需要选择。

### “日志收集服务器IP地址”和“服务器端口”根据实际填写。

### “日志类型”根据实际填写，系统支持全部上报或者部分上报。

### 2 执行**LST SYSLOGTASK**命令，查看“连接状态”。

### 如果“连接状态”为“连接” => 说明UDG与日志收集服务器对接成功。

### 如果“连接状态”为“断开” => 如果是华为日志收集服务器，请联系华为技术支持，如果是第三方日志收集服务器，请执行步骤 3。

### 3 选择“安全 > 证书管理 > 证书与证书集管理”，上传CA证书和设备证书。

### 4 选择“安全 > 证书管理 > 证书应用场景关联”，将步骤 3中上传的CA证书、设备证书分别按照表1进行场景关联。

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

### 5 选择“应用管理 > MML”，执行**LST SYSLOGTASK**命令，查看“连接状态”。

### 如果“连接状态”为“连接” => 说明UDG与日志收集服务器对接成功。

### 如果“连接状态”为“断开” => 请联系华为技术支持。

