---
id: ''
name: 配置OMU OS管理维护接口
ne_type: UEG
type: feature
description: 网元提供OMU OS管理维护接口用于与外部服务器对接，例如网元需要对接外部系统进行安全扫描时，可以参考本章节添加物理IP地址。  * 当网元使用IPV4地址部署，对接外部系统使用IPV6地址时，网元需要为首节点（物理IP1）和第二管理节点（物理IP2）分别添加物理IPV6地址。 * 当网元使用IPV6地址部署，对接外部系统使用IPV4地址时，网元需要为首节点和第二管理节点分别添加物理IPV4地址。 * 当网元和对接外部系统均使用IPV4地址，或者均使用IPV6地址，或者网元为IPV4和IPV6双栈部署时，网元可以使用已配置物理IP地址与外部系统对接，可以通过执行**LST OMIP**查询物理IP信息。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","组网路由配置（裸机容器）","配置OMU OS管理维护接口"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","组网路由配置（裸机容器）","配置OMU OS管理维护接口"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","软件安装与初始配置","部署UEG","电力专网采用风筝S部署模式","UEG初始配置","裸机容器模式UPF初始配置","参考：详细配置指导","组网路由配置","配置OMU OS管理维护接口"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","初始配置与调测","参考：详细配置指导","组网路由配置（裸机容器）","配置OMU OS管理维护接口"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-S","子园区UEG-S初始配置","裸机容器模式UPF初始配置","参考：详细配置指导","组网路由配置","配置OMU OS管理维护接口"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
网元提供OMU OS管理维护接口用于与外部服务器对接，例如网元需要对接外部系统进行安全扫描时，可以参考本章节添加物理IP地址。* 当网元使用IPV4地址部署，对接外部系统使用IPV6地址时，网元需要为首节点（物理IP1）和第二管理节点（物理IP2）分别添加物理IPV6地址。* 当网元使用IPV6地址部署，对接外部系统使用IPV4地址时，网元需要为首节点和第二管理节点分别添加物理IPV4地址。* 当网元和对接外部系统均使用IPV4地址，或者均使用IPV6地址，或者网元为IPV4和IPV6双栈部署时，网元可以使用已配置物理IP地址与外部系统对接，可以通过执行**LST OMIP**查询物理IP信息。

## 必备事项
前提条件

已登录网元OM Portal。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_omip_list:
      type: items
      properties:
        OMIPTYPE:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '用于网元与外部服务器互通。'
          data_source: '全网规划。'
          pattern: ''
          default: IPV4
        OMSETTYPE:
          name: 'IP设置类型'
          type: string
          enum:
          - SET_IP
          - DELETE_PHYSICAL_IP
          - DELETE_FLOAT_IP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SET_IP
        OMHOST1IPV4:
          name: '物理IP1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OMHOST2IPV4:
          name: '物理IP2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OMFIPADDR:
          name: '浮动IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OMNETMASK:
          name: '子网掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OMIPV4GATEWAY:
          name: '默认网关'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_omip_list:
    - OMIPTYPE: IPV4
      OMSETTYPE: SET_IP
      OMHOST1IPV4: '10.10.10.10'
      OMHOST2IPV4: '10.10.10.20'
      OMFIPADDR: '空'
      OMNETMASK: '空'
      OMIPV4GATEWAY: '空'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录网元OM Portal，选择“应用管理 > MML”。

### 2 执行**LST OMIP**（虚机容器）/**LST OMIP**查询系统当前物理IP地址，脚本示例如下。

### 3 当需要添加IP地址时，执行**SET OMIP**（虚机容器）/**SET OMIP**添加物理IP地址。例如系统需要添加IPV4地址时，脚本示例如下。

```jinja2
{%- for item in set_omip_list -%}
    SET OMIP:
    {#- --- 可选参数 --- -#}
    {%- if item.OMIPTYPE is not none -%}
        OMIPTYPE={{item.OMIPTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：OMIPTYPE=IPV4 时可选 --- -#}
    {%- if item.OMIPTYPE == 'IPV4' -%}
        {%- if item.OMSETTYPE is not none -%}
            OMSETTYPE={{item.OMSETTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
    {%- if item.OMSETTYPE == 'SET_IP' -%}
        {%- if item.OMHOST1IPV4 is not none -%}
            OMHOST1IPV4="{{item.OMHOST1IPV4}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
    {%- if item.OMSETTYPE == 'SET_IP' -%}
        {%- if item.OMHOST2IPV4 is not none -%}
            OMHOST2IPV4="{{item.OMHOST2IPV4}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
    {%- if item.OMSETTYPE == 'SET_IP' -%}
        {%- if item.OMIPV4GATEWAY is not none -%}
            OMIPV4GATEWAY="{{item.OMIPV4GATEWAY}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
    {%- if item.OMSETTYPE == 'SET_IP' -%}
        {%- if item.OMNETMASK is not none -%}
            OMNETMASK="{{item.OMNETMASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OMSETTYPE=SET_IP 时可选 --- -#}
    {%- if item.OMSETTYPE == 'SET_IP' -%}
        {%- if item.OMFIPADDR is not none -%}
            OMFIPADDR="{{item.OMFIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 添加物理IP地址后，网元可以使用新增IP地址和默认维护用户“mtuser”对接外部系统。如果需要创建新用户对接外部系统，可参考如下步骤创建OS用户。

### 仅可以在两个管理节点创建OS用户。操作员可以登录OM Portal执行**LST OMIP**命令查看管理节点所在的IP地址。

#### 4.1 Windows操作系统通过“putty.exe”工具登录系统管理节点，Linux操作系统通过终端模拟器登录系统管理节点，执行**su - root**切换至root用户。

#### 4.2 执行**bash /usr/bin/create\_out\_sshduser.sh -a "*<待添加用户名>*"** （添加的用户名称需要满足Linux用户名要求，不能含有~!@$%&等特殊符号）。

#### 4.3 界面提示“please input password:”后，输入待添加用户的密码（密码需要满足复杂度要求，至少一个大写字母，一个小写字母，一个数字和一个特殊符号，长度14位以上）。

#### 4.4 界面提示“Are you sure you want to change the password upon your first login (yes/no)?”后，输入**yes**开启登录强制修改密码功能（此用户用于对接第三方系统，开启后需要第三方系统对接配合修改，如果第三方无法支持此功能可输入**no**）；输入**no**关闭登录强制修改密码功能。

#### 4.5 界面提示：“add user ***<新创建用户名>*** success”则添加用户成功。若添加失败，请根据提示信息检查添加的用户名是否含有特殊字符，密码是否满足复杂度要求。

#### 4.6 添加完成后，可执行**cat /etc/passwd**查看用户相关信息。

### 以上步骤添加的用户默认具有**su - root**以及远程登录系统的权限。

### 新创建的OS用户如果需要删除可以执行：**bash /usr/bin/create\_out\_sshduser.sh -d "*<待删除用户名>*"。（**删除操作，会将用户相关的目录内容全部删除，如需保留请提前备份如下目录内容：/home/用户名; /var/mail/用户名; /var/spool/mail/用户名 ）

### 可以使用**bash /usr/bin/create\_out\_sshduser.sh -h查看脚本使用的帮助信息。**

