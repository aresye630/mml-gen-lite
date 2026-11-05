---
id: ''
name: 配置UDM惯性运行数据
ne_type: UEG
type: feature
description: 该任务实现如下操作：  * 中心园区UDM实现园区数据管理功能。 * 中心园区UDM实现用户数据的分拣功能。 * USCDB实现园区定制导出功能。 * 添加SFTP用户，用于与PGW、DMA的交互功能。 * 实现定时导出功能。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置业务数据（风筝M）","惯性运行配置（中心园区控制面）","配置UDM惯性运行数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务实现如下操作：* 中心园区UDM实现园区数据管理功能。* 中心园区UDM实现用户数据的分拣功能。* USCDB实现园区定制导出功能。* 添加SFTP用户，用于与PGW、DMA的交互功能。* 实现定时导出功能。

## 必备事项
前提条件

根据业务实际情况，当园区SFTP Server IP不与PGW WebUI和营帐共VPN，需要使用独立VPN时，须参考《独立VPN改造指导书》进行改造操作。

《独立VPN改造指导书》获取路径如下：登录华为运营商技术支持网站，选择“技术支持>产品支持>云核心网>Mobile Packet Core>5G Convergent Data>UDM>UDM>产品文档>版本文档”下，在对应版本的ReleaseDoc\_CN中的“34.园区配置指导书”路径下获取。

* 园区已完成部署。

* 已升级UDM到20.7.1及以上版本，并已加载最新UDM适配包。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_campusdatafilter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤条件名称'
          type: string
          required: false
          description: '用于标识园区用户数据导出的过滤条件名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERTYPE:
          name: '过滤条件类型'
          type: string
          required: false
          description: '用于标识园区用户数据导出的过滤条件类型。  取值范围：   * IMSIPRE：IMSI前缀过滤条件类型。 * MSISDNPRE：MSISDN前缀过滤条件类型。 * DNN：DNN过滤条件类型。 * SNSSAI：切片过滤条件类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERVALUE:
          name: '过滤条件值'
          type: string
          required: false
          description: '用于标识园区用户数据导出的过滤条件值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_campuscfg_list:
      type: items
      properties:
        CAMPUSNAME:
          name: '园区名称'
          type: string
          required: false
          description: '用于标识园区的名称。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤条件名称'
          type: string
          required: false
          description: '用于标识一条园区配置数据记录的过滤条件名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        K4SNO:
          name: 'K4序列号'
          type: string
          required: false
          description: '用于标识园区的K4序列号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OPSNO:
          name: 'OP序列号'
          type: string
          required: false
          description: '用于标识园区的OP序列号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EXPDATATYPE:
          name: '园区导出数据类型'
          type: string
          required: false
          description: '用于标识园区导出的数据类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FEATURETYPE:
          name: '特性数据类型'
          type: string
          required: false
          description: '用于标识园区导出的用户特性数据类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sftpuser_list:
      type: items
      properties:
        USERTYPE:
          name: '用户类型'
          type: string
          enum:
          - PROV
          - DATAMTN
          required: true
          description: '用于指定SFTP用户的类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERNAME:
          name: '用户名'
          type: string
          maxLength: 31
          required: true
          description: '用于指定通过SFTP登录的用户名。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PWD:
          name: '密码'
          type: string
          maxLength: 31
          required: true
          description: '用于指定通过SFTP登录用户的密码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          maxLength: 31
          required: true
          description: '用于指定通过SFTP服务器登录用户的确认密码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WORKPATH:
          name: '工作路径名称'
          type: string
          maxLength: 127
          required: true
          description: '用于指定SFTP用户的工作目录，该参数为联想参数列表，不能手动输入。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBPATH:
          name: '子工作路径名称'
          type: string
          maxLength: 64
          required: false
          description: '用于指定SFTP用户的子工作目录，该参数必须与**ADD CAMPUSCFG**命令设置的“园区名称”保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PERMISSION:
          name: '权限'
          type: string
          required: true
          description: '用于指定SFTP用户的权限。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '用户描述'
          type: string
          maxLength: 64
          required: false
          description: '用于描述SFTP用户。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cusexpcfg_list:
      type: items
      properties:
        FETYPE:
          name: 'FE类型'
          type: string
          maxLength: 128
          required: true
          description: '用于描述成功加载的插件包FE类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAMPUSNAME:
          name: '园区名称'
          type: string
          maxLength: 63
          required: true
          description: '用于唯一标识一个园区。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SFTPTYPE:
          name: 'SFTP类型'
          type: string
          enum:
          - CLIENT
          - SERVER
          - IMPORTCLIENT
          required: true
          description: '用于指定SFTP类型。  说明：  中心园区UDM作为客户端时，需要将该参数设置为“CLIENT”。  中心园区UDM作为服务端时，需要将该参数设置为“SERVER”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SFTPUSERNAME:
          name: 'SFTP用户名称'
          type: string
          maxLength: 31
          required: false
          description: '用于指定SFTP用户名称。  说明：  当“SFTP类型”设置为“SERVER”时该参数有效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PWD:
          name: '密码'
          type: string
          maxLength: 31
          required: true
          description: '用于指定导出园区文件的加密密码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          maxLength: 31
          required: true
          description: '用于指定导出园区文件的确认密码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rsftpserver_list:
      type: items
      properties:
        SERVERTYPE:
          name: '远端服务器类型'
          type: string
          enum:
          - PROV
          - DATAMTN
          required: true
          description: '用于指定远端SFTP服务器的类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERNAME:
          name: '远端服务器名称'
          type: string
          maxLength: 127
          required: true
          description: '用于指定远端SFTP服务器的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '用于表示IP地址类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERIPV4:
          name: '服务端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '仅当本命令中的“IP类型”参数选择为“IPV4”时该参数有效，用于指定远端SFTP服务器提供服务的IPv4地址，输入的IPv4地址是配置前已获取的服务器IPv4地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERPORT:
          name: '服务端端口'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: '用于指定远端SFTP服务器提供服务的端口号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERNAME:
          name: '用户名称'
          type: string
          maxLength: 31
          required: true
          description: '用于指定远端SFTP服务器提供服务的用户名。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTHTYPE:
          name: '鉴权类型'
          type: string
          enum:
          - PASSWORD
          - PUBLICKEY
          required: false
          description: '用于指示SFTP登录的鉴权模式。'
          data_source: '本端规划'
          pattern: ''
          default: PASSWORD
        PWD:
          name: '密码'
          type: string
          maxLength: 31
          required: false
          description: '用于指定远端SFTP服务器提供服务用户名的密码，输入的密码是第三方服务器按各自密码规则已经设置的密码，当“鉴权类型”设置为“PUBLICKEY（公钥认证）”时，无需设置密码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          maxLength: 31
          required: false
          description: '用于指定远端SFTP服务器提供服务用户名的确认密码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RWORKDIR:
          name: 'SFTP远端工作目录'
          type: string
          maxLength: 127
          required: true
          description: '用于指定远端SFTP服务器上用户名称对应的工作目录。该参数必须与**ADD CAMPUSCFG**命令设置的“园区名称”保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LWORKDIR:
          name: 'SFTP本端工作目录'
          type: string
          maxLength: 127
          required: true
          description: '用于指定USCDB工作目录，该参数为联想参数列表，不能手动输入，其取值为**LST SFTPWORKDIR**命令查询获取的“配置名称”输出参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTOCREATEDIR:
          name: '是否自动创建SFTP远端工作目录'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '用于指定是否在远端SFTP服务器的根目录自动创建“SFTP远端工作目录”参数定义的子目录。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TRANSDIRECTION:
          name: '传输方向'
          type: string
          enum:
          - UPLOAD
          - DOWNLOAD
          - TIMDOWNLOAD
          required: true
          description: '用于指定USCDB传输文件的方向。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALIPV4:
          name: '本端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '用于指定USCDB提供服务DMA的IPv4地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cusexpcfg_list_1:
      type: items
      properties:
        FETYPE:
          name: 'FE类型'
          type: string
          maxLength: 128
          required: true
          description: '用于描述成功加载的插件包FE类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAMPUSNAME:
          name: '园区名称'
          type: string
          maxLength: 63
          required: true
          description: '用于唯一标识一个园区。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SFTPTYPE:
          name: 'SFTP类型'
          type: string
          enum:
          - CLIENT
          - SERVER
          - IMPORTCLIENT
          required: true
          description: '用于指定SFTP类型。  说明：  中心园区UDM作为客户端时，需要将该参数设置为“CLIENT”。  中心园区UDM作为服务端时，需要将该参数设置为“SERVER”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SFTPSERVERNAME:
          name: '远端SFTP服务端名称'
          type: string
          maxLength: 127
          required: false
          description: '用于指定SFTP服务端的名称。 说明：  当“SFTP类型”设置为“CLIENT”时该参数有效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PWD:
          name: '密码'
          type: string
          maxLength: 31
          required: true
          description: '用于指定导出园区文件的加密密码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          maxLength: 31
          required: true
          description: '用于指定导出园区文件的确认密码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_exptask_list:
      type: items
      properties:
        FETYPE:
          name: 'FE类型'
          type: string
          required: false
          description: '用于指定启动哪个FE类型的导出任务。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名称'
          type: string
          required: false
          description: '用于指定导出使用的导出模板名称。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TASKTYPE:
          name: '任务类型'
          type: string
          required: false
          description: '用于指定导出任务的类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CYCLEUNIT:
          name: '周期单位'
          type: string
          required: false
          description: '用于指定任务执行周期的单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CYCLEVALUE:
          name: '周期值'
          type: string
          required: false
          description: '用于指定任务周期。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TIME:
          name: '导出启动时间'
          type: string
          required: false
          description: '用于指定导出任务的启动时间。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_campusdatafilter_list:
    - FILTERNAME: FILTERNAME
      FILTERTYPE: IMSIPRE
      FILTERVALUE: '963589125423'
    add_campuscfg_list:
    - CAMPUSNAME: campus1
      FILTERNAME: FILTERNAME
      K4SNO: '1'
      OPSNO: '1'
      EXPDATATYPE: 5G
      FEATURETYPE: REDCAP
    add_sftpuser_list:
    - USERTYPE: DATAMTN
      USERNAME: 'testname'
      PWD: '***********'
      CFM: '***********'
      WORKPATH: 'DOWNLOADEXPORTFILE'
      SUBPATH: 'campus1'
      PERMISSION: UPLOAD-0&DOWNLOAD-1
      DESCRIPTION: 'userinfo'
    add_cusexpcfg_list:
    - FETYPE: 'SUP-FE'
      CAMPUSNAME: 'campus1'
      SFTPTYPE: SERVER
      SFTPUSERNAME: 'sftpserver2'
      PWD: '***********'
      CFM: '***********'
    add_rsftpserver_list:
    - SERVERTYPE: DATAMTN
      SERVERNAME: 'unicomserver'
      IPVER: IPV4
      SERVERIPV4: '10.94.1.131'
      SERVERPORT: 22
      USERNAME: 'name'
      AUTHTYPE: PASSWORD
      PWD: '***********'
      CFM: '***********'
      RWORKDIR: 'campus1'
      LWORKDIR: 'UPLOADEXPORTFILE'
      AUTOCREATEDIR: TRUE
      TRANSDIRECTION: UPLOAD
      LOCALIPV4: '10.93.1.131'
    add_cusexpcfg_list_1:
    - FETYPE: 'SUP-FE'
      CAMPUSNAME: 'campus1'
      SFTPTYPE: CLIENT
      SFTPSERVERNAME: 'sftpserver1'
      PWD: '***********'
      CFM: '***********'
    add_exptask_list:
    - FETYPE: SUP-FE
      TPLNAME: mem_exp_ueg_common_data
      TASKTYPE: CYCLE
      CYCLEUNIT: DAY
      CYCLEVALUE: '1'
      TIME: 2021&09&23&12&00&00
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 PGW侧园区数据配置步骤。

#### 1.1 登录“UDM业务管理”窗口。

#### 1.2 设置园区用户数据导出的过滤条件。

#### 执行**ADD CAMPUSDATAFILTER**命令，通过“过滤条件名称”、“过滤条件类型”和“过滤条件值”参数设置一条用户数据导出的过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_campusdatafilter_list的变量区（command: ADD CAMPUSDATAFILTER） -#}
<!-- MISSING_MACRO: command=ADD CAMPUSDATAFILTER list_name=add_campusdatafilter_list step_id=1.2 -->
```

#### 1.3 在中心园区UDM中增加一条园区配置数据记录。

#### 执行**ADD CAMPUSCFG**命令，调用**ADD CAMPUSDATAFILTER**命令配置的过滤条件，设置一条园区配置数据记录。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_campuscfg_list的变量区（command: ADD CAMPUSCFG） -#}
<!-- MISSING_MACRO: command=ADD CAMPUSCFG list_name=add_campuscfg_list step_id=1.3 -->
```

### 2 USCDB侧数据配操作步骤。

#### 2.1 登录“USCDB MML命令”界面。

#### 2.2 中心园区UDM导出配置步骤不同，具体有以下两种情况：

##### 2.2.1 如果中心园区UDM将SFTP Server作为服务端，供园区下载数据。

###### 2.2.1.1 设置SFTP Server的园区子目录。

###### 执行**ADD SFTPUSER**命令，添加SFTP用户，通过“子工作路径名称”参数指定SFTP用户的子工作目录，该参数必须与**ADD CAMPUSCFG**命令设置的“园区名称”保持一致，确保每个园区只能访问自己园区的数据，不能访问其它园区的数据，为园区导出提供安全隔离能力。

```jinja2
{%- if is_scenario_as_server -%}
    {%- for item in add_sftpuser_list -%}
        ADD SFTPUSER:
        {#- --- 必选参数 --- -#}
        USERTYPE={{item.USERTYPE}},
        USERNAME="{{item.USERNAME}}",
        PWD="{{item.PWD}}",
        CFM="{{item.CFM}}",
        WORKPATH="{{item.WORKPATH}}",
        PERMISSION={{item.PERMISSION}},
        {#- --- 可选参数 --- -#}
        {%- if item.SUBPATH is not none -%}
            SUBPATH="{{item.SUBPATH}}",
        {%- endif -%}
        {%- if item.DESCRIPTION is not none -%}
            DESCRIPTION="{{item.DESCRIPTION}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.2.1.2 添加园区定制导出配置。

###### 执行**ADD CUSEXPCFG**命令，为不同园区的导出结果文件使用不同的密码加密。此时需要设置“SFTP类型”参数为“SERVER”。

```jinja2
{%- if is_scenario_as_server -%}
    {%- for item in add_cusexpcfg_list -%}
        ADD CUSEXPCFG:
        {#- --- 必选参数 --- -#}
        FETYPE="{{item.FETYPE}}",
        CAMPUSNAME="{{item.CAMPUSNAME}}",
        SFTPTYPE={{item.SFTPTYPE}},
        PWD="{{item.PWD}}",
        CFM="{{item.CFM}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SFTPTYPE=SERVER 时必选 --- -#}
        {%- if item.SFTPTYPE == 'SERVER' -%}
            SFTPUSERNAME="{{item.SFTPUSERNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.2.2 如果中心园区UDM将SFTP Server作为客户端，将园区数据上传到第三方SFTP文件服务器。

###### 2.2.2.1 设置SFTP服务器。

###### 执行**ADD RSFTPSERVER**命令，添加远端SFTP服务器，通过“远端服务器类型”和“远端服务器名称”来指定SFTP服务器。

```jinja2
{%- if is_scenario_as_client -%}
    {%- for item in add_rsftpserver_list -%}
        ADD RSFTPSERVER:
        {#- --- 必选参数 --- -#}
        SERVERTYPE={{item.SERVERTYPE}},
        SERVERNAME="{{item.SERVERNAME}}",
        IPVER={{item.IPVER}},
        SERVERPORT={{item.SERVERPORT}},
        USERNAME="{{item.USERNAME}}",
        RWORKDIR="{{item.RWORKDIR}}",
        LWORKDIR="{{item.LWORKDIR}}",
        TRANSDIRECTION={{item.TRANSDIRECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.AUTHTYPE is not none -%}
            AUTHTYPE={{item.AUTHTYPE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            SERVERIPV4="{{item.SERVERIPV4}}",
        {%- endif -%}
        {#- --- 条件必选：AUTHTYPE=PASSWORD 时必选 --- -#}
        {%- if item.AUTHTYPE == 'PASSWORD' -%}
            PWD="{{item.PWD}}",
        {%- endif -%}
        {#- --- 条件必选：AUTHTYPE=PASSWORD 时必选 --- -#}
        {%- if item.AUTHTYPE == 'PASSWORD' -%}
            CFM="{{item.CFM}}",
        {%- endif -%}
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- if item.IPVER == 'IPV4' -%}
            LOCALIPV4="{{item.LOCALIPV4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SERVERTYPE=DATAMTN 时可选 --- -#}
        {%- if item.SERVERTYPE == 'DATAMTN' -%}
            {%- if item.AUTOCREATEDIR is not none -%}
                AUTOCREATEDIR={{item.AUTOCREATEDIR}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

####### 2.2.2.1.1 参数“服务端IPV4地址”为服务器IP地址，参数“本端IPV4地址”为DMA地址，可通过**LST SRVIPADDR**命令获取。

####### 2.2.2.1.2 参数“SFTP远端工作目录”必须与**ADD CAMPUSCFG**命令设置的“园区名称”保持一致，确保每个园区只能访问自己园区的数据。

###### 2.2.2.2 添加园区定制导出配置。

###### 执行**ADD CUSEXPCFG**命令，为不同园区的导出结果文件使用不同的密码加密。此时需要设置“SFTP类型”参数为“CLIENT”。

```jinja2
{%- if is_scenario_as_client -%}
    {%- for item in add_cusexpcfg_list_1 -%}
        ADD CUSEXPCFG:
        {#- --- 必选参数 --- -#}
        FETYPE="{{item.FETYPE}}",
        CAMPUSNAME="{{item.CAMPUSNAME}}",
        SFTPTYPE={{item.SFTPTYPE}},
        PWD="{{item.PWD}}",
        CFM="{{item.CFM}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SFTPTYPE=CLIENT/IMPORTCLIENT 时必选 --- -#}
        {%- if item.SFTPTYPE in ['CLIENT', 'IMPORTCLIENT'] -%}
            SFTPSERVERNAME="{{item.SFTPSERVERNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 登录“系统管理”窗口，执行**ADD EXPTASK**命令启动定时导出任务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_exptask_list的变量区（command: ADD EXPTASK） -#}
<!-- MISSING_MACRO: command=ADD EXPTASK list_name=add_exptask_list step_id=3 -->
```

