---
id: ''
name: Bi接口配置
ne_type: UNC
type: feature
description: 该任务用于指导操作人员完成Bi口的IP资源数据的配置。配置Bi口后可以通过PULL或者PUSH模式向计费中心分发话单。  PULL模式下计费中心主动到NCG取话单。此时NCG作为FTP/SFTP的服务器端，计费中心作为FTP/SFTP的客户端；PUSH模式下NCG采用FTP/SFTP协议分发第二份最终话单到计费中心。此时NCG作为FTP/SFTP的客户端，计费中心作为FTP/SFTP的服务器端。大多数情况下，NCG采用PULL方式分发话单。  PULL方式下，NCG默认开放“/opt/CG\_VNFC/run/vrpv8/product/backsave/”目录下的话单给计费中心，下级相对目录因运营商不同而不同。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案","NCG配置","Bi接口配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务用于指导操作人员完成Bi口的IP资源数据的配置。配置Bi口后可以通过PULL或者PUSH模式向计费中心分发话单。PULL模式下计费中心主动到NCG取话单。此时NCG作为FTP/SFTP的服务器端，计费中心作为FTP/SFTP的客户端；PUSH模式下NCG采用FTP/SFTP协议分发第二份最终话单到计费中心。此时NCG作为FTP/SFTP的客户端，计费中心作为FTP/SFTP的服务器端。大多数情况下，NCG采用PULL方式分发话单。PULL方式下，NCG默认开放“/opt/CG\_VNFC/run/vrpv8/product/backsave/”目录下的话单给计费中心，下级相对目录因运营商不同而不同。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ipresource_list:
      type: items
      properties:
        IPRID:
          name: 'IP资源标识'
          type: string
          maxLength: 32
          required: true
          description: '该命令用于增加NCG话单接收、分发和备份时所使用的IP地址等信息。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        IPRPURPOSE:
          name: 'IP资源用途'
          type: string
          enum:
          - Bi
          - Ga
          - Omi
          - OmiAndBi
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RUID:
          name: 'RU的ID'
          type: integer
          minimum: 64
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: '虚拟网络名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rst_vnfc_list:
      type: items
      properties:
        SERVICEINSTANCE:
          name: '服务实例'
          type: string
          maxLength: 255
          required: true
          description: '该命令用于重启系统。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISFORCEOPER:
          name: '强制操作标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_cdrdistr_list:
      type: items
      properties:
        CDRDISTRID:
          name: '分发任务标识'
          type: string
          maxLength: 32
          required: true
          description: '+ 该命令用于配置第二份最终话单的分发任务，包括话单分发的方式、采用的协议、计费中心（本文档中又称BS（Billing System））IP地址等信息。 + 该命令使用PULL模式时，BS取走话单后应立即删除取走的话单，防止保存的话单数量过多导致磁盘空间不足。'
          data_source: ''
          pattern: ''
          default: ''
        ISSINGLEBI:
          name: '是否开启Bi口SingleIP功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        TRANSMODE:
          name: '分发方式'
          type: string
          enum:
          - LOCAL
          - PULL
          - PUSH
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OTPTYPE:
          name: '非SinglePULL传输协议类型'
          type: string
          enum:
          - FTP
          - SFTP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OUSERNAME:
          name: '开放给BS侧的用户名'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPASSWORD:
          name: '开放给BS侧的密码'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPASSWD:
          name: '确认密码'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVOTPTYPE:
          name: 'SinglePULL传输协议类型'
          type: string
          enum:
          - FTP
          - SFTP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATRANSMODE:
          name: '分发方式'
          type: string
          enum:
          - LOCAL
          - PULL
          - PUSH
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHMODE:
          name: 'SFTP认证方式'
          type: string
          enum:
          - KEY
          - KEYBD
          - PASSWORD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: PASSWORD
        ODESTPATH:
          name: '开放给BS的路径'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AGID:
          name: '接入网元分组标识'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CMRRULE:
          name: '分发话单压缩方式'
          type: string
          enum:
          - GZIP
          - UNCOMPRESS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: UNCOMPRESS
        DATELIST:
          name: '分发日期列表'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTLAPATH:
          name: '目的侧日志稽核文件的保存路径'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESTPATH:
          name: '目的路径'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISTHREADNUM:
          name: '非SingleIP辅助分发线程数量'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        DISTRDELAY:
          name: '分发延迟告警时间'
          type: integer
          minimum: 0
          maximum: 10080
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 30
        ENDTIME:
          name: '分发结束时间'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISCUTOMDISTR:
          name: '是否自定义分发'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        ISMVFILE:
          name: '是否将文件转移至本地路径'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        ISOMIIP:
          name: '是否使用OMI IP'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        ISTMPFILE:
          name: '是否创建临时文件'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        LDTPNAME:
          name: '日志稽核模板文件名称'
          type: string
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOGAUDIT:
          name: '是否开启日志稽核功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        MNAME:
          name: '模块名'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCFILEFILT:
          name: '文件名后缀过滤规则'
          type: string
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCHFI:
          name: '分发文件的定时扫描间隔'
          type: integer
          minimum: 10
          maximum: 604800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 30
        STARTTIME:
          name: '分发开始时间'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STORDAYS:
          name: '目的侧话单文件的保存天数'
          type: integer
          minimum: 0
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        TIMELIST:
          name: '分发时间点列表'
          type: string
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPTYPE:
          name: '非SinglePUSH传输协议类型'
          type: string
          enum:
          - FTP
          - SFTP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRANSPER:
          name: '分发周期'
          type: string
          enum:
          - EVERYDAY
          - MONTHLY
          - WEEKLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: EVERYDAY
  examples:
    add_ipresource_list:
    - IPRID: 'biV4'
      IPRPURPOSE: Bi
      RUID: 64
      IPTYPE: IPV4
      IPV4: '172.16.1.10'
      VPNNAME: 'Bi-test'
      IPV6: 'fc01:f111:2222:3333:4444:5555:2111:161'
    rst_vnfc_list:
    - SERVICEINSTANCE: 'CG_VNFC_999'
      ISFORCEOPER: TRUE
    add_cdrdistr_list:
    - CDRDISTRID: 'test_distr_5G'
      ISSINGLEBI: NO
      TRANSMODE: PULL
      OTPTYPE: FTP
      OUSERNAME: 'ftpuser'
      OPASSWORD: '*****'
      CPASSWD: '*****'
      SVOTPTYPE: ''
      ATRANSMODE: ''
      AUTHMODE: PASSWORD
      ODESTPATH: ''
      AGID: ''
      CMRRULE: UNCOMPRESS
      DATELIST: ''
      DESTLAPATH: ''
      DESTPATH: ''
      DISTHREADNUM: ''
      DISTRDELAY: 30
      ENDTIME: ''
      ISCUTOMDISTR: NO
      ISMVFILE: NO
      ISOMIIP: NO
      ISTMPFILE: YES
      LDTPNAME: ''
      LOGAUDIT: NO
      MNAME: ''
      SRCFILEFILT: ''
      SRCHFI: 30
      STARTTIME: ''
      STORDAYS: ''
      TIMELIST: ''
      TPTYPE: ''
      TRANSPER: EVERYDAY
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置本端服务端IP信息。

```jinja2
{%- for item in add_ipresource_list -%}
    ADD IPRESOURCE:
    {#- --- 必选参数 --- -#}
    IPRID="{{item.IPRID}}",
    IPRPURPOSE={{item.IPRPURPOSE}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPRPURPOSE=Bi/Omi/OmiAndBi 时必选 --- -#}
    {%- if item.IPRPURPOSE in ['Bi', 'Omi', 'OmiAndBi'] -%}
        RUID={{item.RUID}},
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### CG\_VNFC的每个RU都需要配置BI IP。

### 2 重启CG服务。

```jinja2
{%- for item in rst_vnfc_list -%}
    RST VNFC:
    {#- --- 必选参数 --- -#}
    SERVICEINSTANCE="{{item.SERVICEINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ISFORCEOPER is not none -%}
        ISFORCEOPER={{item.ISFORCEOPER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置话单分发任务。

```jinja2
{%- for item in add_cdrdistr_list -%}
    ADD CDRDISTR:
    {#- --- 必选参数 --- -#}
    CDRDISTRID="{{item.CDRDISTRID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ISSINGLEBI is not none -%}
        ISSINGLEBI={{item.ISSINGLEBI}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ISSINGLEBI=NO 时必选 --- -#}
    {%- if item.ISSINGLEBI == 'NO' -%}
        TRANSMODE={{item.TRANSMODE}},
    {%- endif -%}
    {#- --- 条件必选：TRANSMODE=PULL 时必选 --- -#}
    {%- if item.TRANSMODE == 'PULL' -%}
        OTPTYPE={{item.OTPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：OTPTYPE=FTP/SFTP 时必选 --- -#}
    {%- if item.OTPTYPE in ['FTP', 'SFTP'] -%}
        OUSERNAME="{{item.OUSERNAME}}",
    {#- --- 条件必选：SVOTPTYPE=FTP/SFTP 时必选 --- -#}
    {%- elif item.SVOTPTYPE in ['FTP', 'SFTP'] -%}
        OUSERNAME="{{item.OUSERNAME}}",
    {%- endif -%}
    {#- --- 条件必选：OTPTYPE=FTP/SFTP 时必选 --- -#}
    {%- if item.OTPTYPE in ['FTP', 'SFTP'] -%}
        OPASSWORD="{{item.OPASSWORD}}",
    {#- --- 条件必选：SVOTPTYPE=FTP/SFTP 时必选 --- -#}
    {%- elif item.SVOTPTYPE in ['FTP', 'SFTP'] -%}
        OPASSWORD="{{item.OPASSWORD}}",
    {%- endif -%}
    {#- --- 条件必选：OTPTYPE=FTP/SFTP 时必选 --- -#}
    {%- if item.OTPTYPE in ['FTP', 'SFTP'] -%}
        CPASSWD="{{item.CPASSWD}}",
    {#- --- 条件必选：SVOTPTYPE=FTP/SFTP 时必选 --- -#}
    {%- elif item.SVOTPTYPE in ['FTP', 'SFTP'] -%}
        CPASSWD="{{item.CPASSWD}}",
    {%- endif -%}
    {#- --- 条件必选：ISSINGLEBI=YES 时必选 --- -#}
    {%- if item.ISSINGLEBI == 'YES' -%}
        ATRANSMODE={{item.ATRANSMODE}},
    {%- endif -%}
    {#- --- 条件必选：ATRANSMODE=LOCAL 时必选 --- -#}
    {%- if item.ATRANSMODE == 'LOCAL' -%}
        DESTPATH="{{item.DESTPATH}}",
    {#- --- 条件必选：SVTPTYPE=FTP/SFTP 时必选 --- -#}
    {%- elif item.SVTPTYPE in ['FTP', 'SFTP'] -%}
        DESTPATH="{{item.DESTPATH}}",
    {#- --- 条件必选：TPTYPE=FTP/SFTP 时必选 --- -#}
    {%- elif item.TPTYPE in ['FTP', 'SFTP'] -%}
        DESTPATH="{{item.DESTPATH}}",
    {#- --- 条件必选：TRANSMODE=LOCAL 时必选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        DESTPATH="{{item.DESTPATH}}",
    {%- endif -%}
    {#- --- 条件必选：TPTYPE=FTP/SFTP 时必选 --- -#}
    {%- if item.TPTYPE in ['FTP', 'SFTP'] -%}
        ISCUTOMDISTR={{item.ISCUTOMDISTR}},
    {#- --- 条件必选：TRANSMODE=LOCAL 时必选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        ISCUTOMDISTR={{item.ISCUTOMDISTR}},
    {%- endif -%}
    {#- --- 条件必选：TRANSMODE=PUSH/LOCAL 时必选 --- -#}
    {%- if item.TRANSMODE in ['PUSH', 'LOCAL'] -%}
        MNAME="{{item.MNAME}}",
    {%- endif -%}
    {#- --- 条件必选：ATRANSMODE=PULL 时必选 --- -#}
    {%- if item.ATRANSMODE == 'PULL' -%}
        SVOTPTYPE={{item.SVOTPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：TRANSMODE=PUSH 时必选 --- -#}
    {%- if item.TRANSMODE == 'PUSH' -%}
        TPTYPE={{item.TPTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：OTPTYPE=SFTP 时可选 --- -#}
    {%- if item.OTPTYPE == 'SFTP' -%}
        {%- if item.AUTHMODE is not none -%}
            AUTHMODE={{item.AUTHMODE}},
        {%- endif -%}
    {#- --- 条件可选：SVOTPTYPE=SFTP 时可选 --- -#}
    {%- elif item.SVOTPTYPE == 'SFTP' -%}
        {%- if item.AUTHMODE is not none -%}
            AUTHMODE={{item.AUTHMODE}},
        {%- endif -%}
    {#- --- 条件可选：SVTPTYPE=SFTP 时可选 --- -#}
    {%- elif item.SVTPTYPE == 'SFTP' -%}
        {%- if item.AUTHMODE is not none -%}
            AUTHMODE={{item.AUTHMODE}},
        {%- endif -%}
    {#- --- 条件可选：TPTYPE=SFTP 时可选 --- -#}
    {%- elif item.TPTYPE == 'SFTP' -%}
        {%- if item.AUTHMODE is not none -%}
            AUTHMODE={{item.AUTHMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVTPTYPE=FTP/SFTP 时可选 --- -#}
    {%- if item.SVTPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.CMRRULE is not none -%}
            CMRRULE={{item.CMRRULE}},
        {%- endif -%}
    {#- --- 条件可选：TPTYPE=FTP/SFTP 时可选 --- -#}
    {%- elif item.TPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.CMRRULE is not none -%}
            CMRRULE={{item.CMRRULE}},
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        {%- if item.CMRRULE is not none -%}
            CMRRULE={{item.CMRRULE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVTPTYPE=FTP/SFTP 时可选 --- -#}
    {%- if item.SVTPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.DATELIST is not none -%}
            DATELIST="{{item.DATELIST}}",
        {%- endif -%}
    {#- --- 条件可选：TPTYPE=FTP/SFTP 时可选 --- -#}
    {%- elif item.TPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.DATELIST is not none -%}
            DATELIST="{{item.DATELIST}}",
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        {%- if item.DATELIST is not none -%}
            DATELIST="{{item.DATELIST}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVTPTYPE=FTP/SFTP 时可选 --- -#}
    {%- if item.SVTPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.DESTLAPATH is not none -%}
            DESTLAPATH="{{item.DESTLAPATH}}",
        {%- endif -%}
    {#- --- 条件可选：TPTYPE=FTP/SFTP 时可选 --- -#}
    {%- elif item.TPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.DESTLAPATH is not none -%}
            DESTLAPATH="{{item.DESTLAPATH}}",
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        {%- if item.DESTLAPATH is not none -%}
            DESTLAPATH="{{item.DESTLAPATH}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TRANSMODE=PUSH 时可选 --- -#}
    {%- if item.TRANSMODE == 'PUSH' -%}
        {%- if item.DISTHREADNUM is not none -%}
            DISTHREADNUM={{item.DISTHREADNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TRANSMODE=PUSH 时可选 --- -#}
    {%- if item.TRANSMODE == 'PUSH' -%}
        {%- if item.DISTRDELAY is not none -%}
            DISTRDELAY={{item.DISTRDELAY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVTPTYPE=FTP/SFTP 时可选 --- -#}
    {%- if item.SVTPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.ENDTIME is not none -%}
            ENDTIME="{{item.ENDTIME}}",
        {%- endif -%}
    {#- --- 条件可选：TPTYPE=FTP/SFTP 时可选 --- -#}
    {%- elif item.TPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.ENDTIME is not none -%}
            ENDTIME="{{item.ENDTIME}}",
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        {%- if item.ENDTIME is not none -%}
            ENDTIME="{{item.ENDTIME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ATRANSMODE=PUSH 时可选 --- -#}
    {%- if item.ATRANSMODE == 'PUSH' -%}
        {%- if item.ISMVFILE is not none -%}
            ISMVFILE={{item.ISMVFILE}},
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=PUSH 时可选 --- -#}
    {%- elif item.TRANSMODE == 'PUSH' -%}
        {%- if item.ISMVFILE is not none -%}
            ISMVFILE={{item.ISMVFILE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TRANSMODE=PULL 时可选 --- -#}
    {%- if item.TRANSMODE == 'PULL' -%}
        {%- if item.ISOMIIP is not none -%}
            ISOMIIP={{item.ISOMIIP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ATRANSMODE=PUSH 时可选 --- -#}
    {%- if item.ATRANSMODE == 'PUSH' -%}
        {%- if item.ISTMPFILE is not none -%}
            ISTMPFILE={{item.ISTMPFILE}},
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=PUSH 时可选 --- -#}
    {%- elif item.TRANSMODE == 'PUSH' -%}
        {%- if item.ISTMPFILE is not none -%}
            ISTMPFILE={{item.ISTMPFILE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVTPTYPE=FTP/SFTP 时可选 --- -#}
    {%- if item.SVTPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.LDTPNAME is not none -%}
            LDTPNAME="{{item.LDTPNAME}}",
        {%- endif -%}
    {#- --- 条件可选：TPTYPE=FTP/SFTP 时可选 --- -#}
    {%- elif item.TPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.LDTPNAME is not none -%}
            LDTPNAME="{{item.LDTPNAME}}",
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        {%- if item.LDTPNAME is not none -%}
            LDTPNAME="{{item.LDTPNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVTPTYPE=FTP/SFTP 时可选 --- -#}
    {%- if item.SVTPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.LOGAUDIT is not none -%}
            LOGAUDIT={{item.LOGAUDIT}},
        {%- endif -%}
    {#- --- 条件可选：TPTYPE=FTP/SFTP 时可选 --- -#}
    {%- elif item.TPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.LOGAUDIT is not none -%}
            LOGAUDIT={{item.LOGAUDIT}},
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        {%- if item.LOGAUDIT is not none -%}
            LOGAUDIT={{item.LOGAUDIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ISSPULLCUTOM=YES 时可选 --- -#}
    {%- if item.ISSPULLCUTOM == 'YES' -%}
        {%- if item.ODESTPATH is not none -%}
            ODESTPATH="{{item.ODESTPATH}}",
        {%- endif -%}
    {#- --- 条件可选：OTPTYPE=FTP/SFTP 时可选 --- -#}
    {%- elif item.OTPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.ODESTPATH is not none -%}
            ODESTPATH="{{item.ODESTPATH}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ATRANSMODE=PUSH 时可选 --- -#}
    {%- if item.ATRANSMODE == 'PUSH' -%}
        {%- if item.SRCFILEFILT is not none -%}
            SRCFILEFILT="{{item.SRCFILEFILT}}",
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=PUSH/LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE in ['PUSH', 'LOCAL'] -%}
        {%- if item.SRCFILEFILT is not none -%}
            SRCFILEFILT="{{item.SRCFILEFILT}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ATRANSMODE=PUSH 时可选 --- -#}
    {%- if item.ATRANSMODE == 'PUSH' -%}
        {%- if item.SRCHFI is not none -%}
            SRCHFI={{item.SRCHFI}},
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=PUSH/LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE in ['PUSH', 'LOCAL'] -%}
        {%- if item.SRCHFI is not none -%}
            SRCHFI={{item.SRCHFI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVTPTYPE=FTP/SFTP 时可选 --- -#}
    {%- if item.SVTPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.STARTTIME is not none -%}
            STARTTIME="{{item.STARTTIME}}",
        {%- endif -%}
    {#- --- 条件可选：TPTYPE=FTP/SFTP 时可选 --- -#}
    {%- elif item.TPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.STARTTIME is not none -%}
            STARTTIME="{{item.STARTTIME}}",
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        {%- if item.STARTTIME is not none -%}
            STARTTIME="{{item.STARTTIME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVTPTYPE=FTP/SFTP 时可选 --- -#}
    {%- if item.SVTPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.STORDAYS is not none -%}
            STORDAYS={{item.STORDAYS}},
        {%- endif -%}
    {#- --- 条件可选：TPTYPE=FTP/SFTP 时可选 --- -#}
    {%- elif item.TPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.STORDAYS is not none -%}
            STORDAYS={{item.STORDAYS}},
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        {%- if item.STORDAYS is not none -%}
            STORDAYS={{item.STORDAYS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVTPTYPE=FTP/SFTP 时可选 --- -#}
    {%- if item.SVTPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.TIMELIST is not none -%}
            TIMELIST="{{item.TIMELIST}}",
        {%- endif -%}
    {#- --- 条件可选：TPTYPE=FTP/SFTP 时可选 --- -#}
    {%- elif item.TPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.TIMELIST is not none -%}
            TIMELIST="{{item.TIMELIST}}",
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        {%- if item.TIMELIST is not none -%}
            TIMELIST="{{item.TIMELIST}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SVTPTYPE=FTP/SFTP 时可选 --- -#}
    {%- if item.SVTPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.TRANSPER is not none -%}
            TRANSPER={{item.TRANSPER}},
        {%- endif -%}
    {#- --- 条件可选：TPTYPE=FTP/SFTP 时可选 --- -#}
    {%- elif item.TPTYPE in ['FTP', 'SFTP'] -%}
        {%- if item.TRANSPER is not none -%}
            TRANSPER={{item.TRANSPER}},
        {%- endif -%}
    {#- --- 条件可选：TRANSMODE=LOCAL 时可选 --- -#}
    {%- elif item.TRANSMODE == 'LOCAL' -%}
        {%- if item.TRANSPER is not none -%}
            TRANSPER={{item.TRANSPER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 接入网元分组标识: 条件必选(分发方式=LOCAL; 是否Bi口SingleIP PUSH自定义分发=NO; 分发方式=PUSH|LOCAL) / 条件可选(是否Bi口SingleIP PULL自定义分发=NO) --- -#}
    {%- if (item.ATRANSMODE == 'LOCAL') or (item.ISSPUSHCUTOM == 'NO') or (item.TRANSMODE in ['PUSH', 'LOCAL']) -%}
        AGID="{{item.AGID}}",
    {%- elif (item.ISSPULLCUTOM == 'NO') -%}
        {%- if item.AGID is not none -%}
            AGID="{{item.AGID}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### PULL模式下，登录用户名和密码可以自行规划。

### 使用FTP传输协议方式时，传输数据时不加密，安全性低。使用SFTP传输协议方式时，会对传输数据进行加密，安全性较高。建议和计费中心协商选择SFTP协议。

