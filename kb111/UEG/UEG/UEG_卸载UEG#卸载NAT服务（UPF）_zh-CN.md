---
id: ''
name: 卸载NAT服务（UPF）
ne_type: UEG
type: feature
description: 当运营商不需要NAT服务或NAT服务动态上线失败时，可以单独卸载NAT pod，从而下线NAT服务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG软件安装（风筝S）","安装UPF（独立部署）","基于中心NFVO (Orchestrator)安装（UPF）","NFVO安装UEG（非SDN场景）","卸载UEG","卸载NAT服务（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST FWSOFTPARA')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商不需要NAT服务或NAT服务动态上线失败时，可以单独卸载NAT pod，从而下线NAT服务。

## 必备事项
前提条件

已经完成网络设计，已规划下线NAT pod的类型和数量。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_fwsoftpara_list:
      type: items
      properties:
        PARAMETERSTYPE:
          name: '参数类型'
          type: string
          enum:
          - DWORD
          - DWORD_EX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDINDEX:
          name: 'DWORD索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'DWORD取值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_fwsoftpara_list_1:
      type: items
      properties:
        PARAMETERSTYPE:
          name: '参数类型'
          type: string
          enum:
          - DWORD
          - DWORD_EX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDINDEX:
          name: 'DWORD索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'DWORD取值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_fwsoftpara_list:
    - PARAMETERSTYPE: DWORD
      DWORDINDEX: 521
      DWORDVALUE: 1
    set_fwsoftpara_list_1:
    - PARAMETERSTYPE: DWORD
      DWORDINDEX: 521
      DWORDVALUE: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 执行**SET FWSOFTPARA**命令，开启Service Fabric的**DWORD\_521**软参，即系统故障时不触发容灾导致的联动复位。

```jinja2
{%- for item in set_fwsoftpara_list -%}
    SET FWSOFTPARA:
    {#- --- 必选参数 --- -#}
    PARAMETERSTYPE={{item.PARAMETERSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD' -%}
        DWORDINDEX={{item.DWORDINDEX}},
    {%- endif -%}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 执行**LST FWSOFTPARA**命令，确认Service Fabric软参值是否为1。

### 如果软参值为1，请执行后续步骤。如果软参值不是1，请联系华为技术支持。

### 2 下线NAT堆栈。

#### 2.1 登录MANO（MAE/VNF LCM）业务面客户端。

##### 2.1.1 在浏览器地址栏中输入以下地址后按回车键，弹出MANO（MAE/VNF LCM）客户端界面。

##### **https://MANO（MAE/VNF LCM）业务的IP地址:端口号/**（例如https://10.50.12.104:31943/）

##### 2.1.2 输入用户名和密码。

##### 系统默认的用户名和密码是“admin/Changeme\_123”，如果已修改MANO（MAE/VNF LCM）客户端用户名和密码，请使用新设置的用户名和密码登录。

##### 2.1.3 单击“登录”，在MAE主界面的“应用”区域，单击“VNF LCM”，进入MANO（MAE/VNF LCM）系统界面。

#### 2.2 卸载NAT堆栈。

##### 2.2.1 选择菜单栏“VNF生命周期管理 >扩缩容管理 > 手动扩缩容”，进入“手动扩缩容”窗口。

##### 2.2.2 选择待操作的VNF，单击右侧“操作”列的“堆栈上下线”图标。

##### 2.2.3 在弹出的界面中“操作”选择“下线”，选择需要下线的“堆栈名称”，**不需要勾选**“进行虚拟机扩缩容”。

##### 2.2.4 单击“下一步”后，在弹出的确认界面点击“确认”，自动跳转到“扩缩容任务”界面，可以查看下线堆栈进度。

### 3 执行**SET FWSOFTPARA**命令，关闭Service Fabric的**DWORD\_521**软参，即系统故障时触发容灾导致的联动复位。

```jinja2
{%- set LST_FWSOFTPARA=getParameterValue('LST FWSOFTPARA') -%}
{%- if LST_FWSOFTPARA=='1' -%}
    {%- for item in set_fwsoftpara_list_1 -%}
        SET FWSOFTPARA:
        {#- --- 必选参数 --- -#}
        PARAMETERSTYPE={{item.PARAMETERSTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
        {%- if item.PARAMETERSTYPE == 'DWORD' -%}
            DWORDINDEX={{item.DWORDINDEX}},
        {%- endif -%}
        {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
        {%- if item.PARAMETERSTYPE == 'DWORD' -%}
            DWORDVALUE={{item.DWORDVALUE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 执行**LST FWSOFTPARA**命令，确认Service Fabric软参值是否为0。

### 如果软参值为0，请执行后续步骤。如果软参值不是0，请联系华为技术支持。

### 4 若动态下线NAT服务后，不再上线NAT服务，则需要缩容NAT自身VM，释放VM资源。

