---
id: ''
name: 手工备份物理数据库
ne_type: UEG
type: feature
description: 在重大操作前为了系统的安全性需要手工对物理数据库进行备份，以保证在操作过程中出现异常时使用已备份的数据快速恢复到重大操作前的运行状态。主要包括以下重大操作前：  * 扩容虚拟机 * 预割接或第一次割接
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG USCDB数据备份与恢复（风筝L）","备份与恢复用户手册","备份与恢复原理及基本操作","物理数据库备份与恢复","基本操作","手动备份和手动恢复","手工备份物理数据库"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在重大操作前为了系统的安全性需要手工对物理数据库进行备份，以保证在操作过程中出现异常时使用已备份的数据快速恢复到重大操作前的运行状态。主要包括以下重大操作前：* 扩容虚拟机* 预割接或第一次割接

## 必备事项
前提条件

NDF（Network Data Function）模块必须已经配置。
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
    bkp_db_list:
      type: items
      properties: {}
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
    bkp_db_list:
    - {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

### 2 执行**LST BACKUP**命令通过检查是否已经存在备份配置信息。

### 如果查询出来的结果中各参数配置不为空，则表示已经配置过备份信息。

### 是 => 4

### 否 => 3

### 3 执行**MOD BACKUP**命令设置备份配置信息。

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

### 参数“备份数据保存方式”设置为“NOSTOSERVER(不保存到服务器)”时，表示将物理数据库的数据备份到虚拟硬盘。

### 参数“备份数据保存方式”设置为“FTPSERVER(保存到FTP服务器)”或“SFTPSERVER(保存到SFTP服务器)”时，表示将物理数据库的数据备份到第三方存储介质。

### 4 在执行**BKP DB**命令备份物理数据库过程中，如果NDF模块发生主备倒换，备份任务将会丢失。此时执行**DSP PHYDB**命令查询物理数据库状态为“Running”，需要在NDF模块倒换完成后重新备份物理数据库。

### 执行**BKP DB**命令备份物理数据库。根据备份数据大小，备份时间需要几分钟到几十分钟。

```jinja2
BKP DB:
;
```

### 5 执行**DSP PHYDB**命令查看物理数据库的备份状态。

### 输出报文中“资源状态”为“Backing up”时，表示数据库正在备份。

### 输出报文中“资源状态”为“Running”时，表示数据库的备份已经完成。

### 6 执行**DSP BKPLIST**命令查看备份的操作结果、备份列表及时间戳信息。

### 输出报文中“操作结果”为“成功”时，表示此次数据库备份任务成功。

