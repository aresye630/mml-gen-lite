---
id: ''
name: 调整物理数据库的自动备份存储方式
ne_type: UEG
type: feature
description: 物理数据库备份能够将数据备份到虚拟机硬盘或者第三方备份服务器，系统默认将数据备份到虚拟机硬盘上。运营商出于对数据安全的考虑，或是根据现网要求，调整物理数据库的自动备份存储方式：  * 将物理数据库备份设置到第三方备份服务器上，可以拥有较大的存储空间以存储更多的备份文件。 * 将物理数据库备份设置到第三方备份服务器上，以便集中对于备份数据统一管理。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG USCDB数据备份与恢复（风筝L）","备份与恢复用户手册","备份与恢复原理及基本操作","物理数据库备份与恢复","基本操作","自动备份配置调整","调整物理数据库的自动备份存储方式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
物理数据库备份能够将数据备份到虚拟机硬盘或者第三方备份服务器，系统默认将数据备份到虚拟机硬盘上。运营商出于对数据安全的考虑，或是根据现网要求，调整物理数据库的自动备份存储方式：* 将物理数据库备份设置到第三方备份服务器上，可以拥有较大的存储空间以存储更多的备份文件。* 将物理数据库备份设置到第三方备份服务器上，以便集中对于备份数据统一管理。

## 必备事项
前提条件

用于提供备份服务的第三方服务器的运行状态正常且没有安全漏洞，如果是FTP服务器要求支持SSL加密。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_backup_list:
      type: items
      properties:
        BAKSWH:
          name: '自动备份开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BAKDAY:
          name: '自动备份时间点'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM&SS'
        STOTIM:
          name: '保存的最大周期的个数'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STOTYP:
          name: '备份数据保存方式'
          type: string
          enum:
          - NOSTOSERVER
          - FTPSERVER
          - SFTPSERVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVER:
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
        LIPV4:
          name: '本地IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVPNNAME:
          name: 'IP地址的VPN名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FTPIPV4:
          name: '服务器IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FTPUSR:
          name: '服务器用户名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FTPPAS:
          name: '服务器密码'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FTPPATH:
          name: '服务器路径'
          type: string
          maxLength: 512
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FTPPORT:
          name: '服务器端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHTYPE:
          name: '鉴权类型'
          type: string
          enum:
          - PASSWORD
          - PUBLICKEY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_backup_list:
    - BAKSWH: 自动备份开关
      BAKDAY: '自动备份时间点'
      STOTIM: 保存的最大周期的个数
      STOTYP: 备份数据保存方式
      IPVER: IP类型
      LIPV4: '本地IPV4地址'
      IPVPNNAME: 'IP地址的VPN名称'
      FTPIPV4: '服务器IPV4地址'
      FTPUSR: '服务器用户名'
      FTPPAS: '服务器密码'
      FTPPATH: '服务器路径'
      FTPPORT: 服务器端口号
      AUTHTYPE: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

### 2 执行**MOD BACKUP**命令设置备份文件存放的第三方备份服务器。

### 以IP类型为IPv4举例：

```jinja2
{%- for item in mod_backup_list -%}
    MOD BACKUP:
    {#- --- 可选参数 --- -#}
    {%- if item.BAKSWH is not none -%}
        BAKSWH={{item.BAKSWH}},
    {%- endif -%}
    {%- if item.STOTIM is not none -%}
        STOTIM={{item.STOTIM}},
    {%- endif -%}
    {%- if item.STOTYP is not none -%}
        STOTYP={{item.STOTYP}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：STOTYP=FTPSERVER/SFTPSERVER 时必选 --- -#}
    {%- if item.STOTYP in ['FTPSERVER', 'SFTPSERVER'] -%}
        IPVER={{item.IPVER}},
    {%- endif -%}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        LIPV4="{{item.LIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：STOTYP=FTPSERVER/SFTPSERVER 时必选 --- -#}
    {%- if item.STOTYP in ['FTPSERVER', 'SFTPSERVER'] -%}
        IPVPNNAME="{{item.IPVPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        FTPIPV4="{{item.FTPIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：STOTYP=FTPSERVER/SFTPSERVER 时必选 --- -#}
    {%- if item.STOTYP in ['FTPSERVER', 'SFTPSERVER'] -%}
        FTPUSR="{{item.FTPUSR}}",
    {%- endif -%}
    {#- --- 条件必选：STOTYP=FTPSERVER 时必选 --- -#}
    {%- if item.STOTYP == 'FTPSERVER' -%}
        FTPPAS="{{item.FTPPAS}}",
    {#- --- 条件必选：AUTHTYPE=PASSWORD 时必选 --- -#}
    {%- elif item.AUTHTYPE == 'PASSWORD' -%}
        FTPPAS="{{item.FTPPAS}}",
    {%- endif -%}
    {#- --- 条件必选：STOTYP=FTPSERVER/SFTPSERVER 时必选 --- -#}
    {%- if item.STOTYP in ['FTPSERVER', 'SFTPSERVER'] -%}
        FTPPATH="{{item.FTPPATH}}",
    {%- endif -%}
    {#- --- 条件必选：STOTYP=FTPSERVER/SFTPSERVER 时必选 --- -#}
    {%- if item.STOTYP in ['FTPSERVER', 'SFTPSERVER'] -%}
        FTPPORT={{item.FTPPORT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BAKSWH=ON 时可选 --- -#}
    {%- if item.BAKSWH == 'ON' -%}
        {%- if item.BAKDAY is not none -%}
            BAKDAY={{item.BAKDAY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 执行**LST BACKUP**命令对物理库自动备份存储方式进行查询修改是否成功。

### **相关命令**

### * **MOD BACKUP**

### * **LST BACKUP**

