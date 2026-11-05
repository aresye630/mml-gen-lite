---
id: ''
name: 一键式上线NAT服务
ne_type: UEG
type: feature
description: NAT(Network Address Translation)服务应用场景：当用户从私有网络（私有IP地址）访问公有网络（公有IP地址）时，使用NAT功能将私有地址转换为公有地址，实现业务访问。  仅当UEG网元需要部署NAT功能，才需要安装NAT服务。  **在CSPedge裸机场景下，需要先**实例化UEG，**然后**再参考本章节，**一键式动态上线**NAT服务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","裸机容器模式","UEG软件安装（风筝S）","UEG软件安装（基于Core Digital Engine-Client）","UEG软件安装（基于Core Digital Engine-Client）","可选服务安装与卸载","一键式上线NAT服务"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('DSP POD')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
NAT(Network Address Translation)服务应用场景：当用户从私有网络（私有IP地址）访问公有网络（公有IP地址）时，使用NAT功能将私有地址转换为公有地址，实现业务访问。仅当UEG网元需要部署NAT功能，才需要安装NAT服务。**在CSPedge裸机场景下，需要先**实例化UEG，**然后**再参考本章节，**一键式动态上线**NAT服务。

## 必备事项
前提条件

* 已经实例化UEG。已经检查系统运行状态，UEG正常工作。
* 准备好部署所需要的镜像文件“5G-UP-VASs-UEG-NAT\_xx.x.x\_EDGE\_X86.zip ” 或“5G-UP-VASs-UEG-NAT\_xx.x.x\_EDGE\_ARM.zip ”。

  NAT的镜像文件请从5G UP VASs下获取。
* 如果NAT服务带补丁动态上线，需要准备好补丁包“5G-UP-VASs-UEG-NAT-Service\_xx.x.x\_PATCH\_EDGE\_X86.zip ” 或“5G-UP-VASs-UEG-NAT-Service\_xx.x.x\_PATCH\_EDGE\_ARM.zip ”。补丁包请从5G UP VASs下获取。
* 准备好部署所需要的tosca模板：
  + **UEG-S**的tosca模板为UEG-NAT\_xx.x.x\_TOSCA\_LITE-E9000H-2\_EDGE\_X86.zip或UEG-NAT\_xx.x.x\_TOSCA\_LITE-E9000H-2\_EDGE\_ARM.zip。
  + tosca模板包请从UEG下获取。

* 一键式上下线本服务时，不能同时一键式上下线其他部件。
* 当一键式动态上线一个服务的任务失败，必须先一键式动态下线此服务，再重新触发一键式动态上线任务。如果是一键式动态下线失败，只能继续重新触发一键式动态下线任务。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    opr_oneclickdeploy_list:
      type: items
      properties:
        OPRTYPE:
          name: '操作类型'
          type: string
          enum:
          - INDEPSTACKENABLE
          - INDEPSTACKDISABLE
          - FEATUREENABLE
          - FEATUREDISABLE
          - SCALEOUT
          - SCALEIN
          - DELETE
          - RETRY
          - ROLLBACK
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        PODTYPELIST:
          name: 'Pod类型列表'
          type: string
          minLength: 0
          maxLength: 256
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FUNCTIONSETNAME:
          name: '方法集名称'
          type: string
          minLength: 0
          maxLength: 256
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        PKGNAME:
          name: '单服务模板名称'
          type: string
          minLength: 0
          maxLength: 256
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    opr_oneclickdeploy_list:
    - OPRTYPE: INDEPSTACKENABLE
      PODTYPELIST: 'natom-pod:pod个数/natctrl-pod:pod个数/natgcpssgc20-pod:pod个数'
      FUNCTIONSETNAME: 'NAT'
      PKGNAME: 'ueg-nat-xx.x.x-tosca-lite-e9000h-2-edge-arm'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 检查**软件包**，确保已经上传依赖的软件包。

#### 1.1 登录OM Portal，单击“软件中心> 软件仓库 > 应用仓库”单击“添加”进行软件包上传。

#### 1.2 选择“5G-UP-VASs-UEG-NAT\_xx.x.x\_EDGE\_X86.zip ”、“5G-UP-VASs-UEG-NAT-Service\_xx.x.x\_PATCH\_EDGE\_X86.zip”（补丁包，可选），或者“5G-UP-VASs-UEG-NAT\_xx.x.x\_EDGE\_ARM.zip ”、“5G-UP-VASs-UEG-NAT-Service\_xx.x.x\_PATCH\_EDGE\_ARM.zip”（补丁包，可选）进行上传。当软件包状态变为“准备上传”，单击“上传”，完成NAT软件包上传过程。

### 2 上传tosca模板。

#### 2.1 选择“软件中心> 软件仓库 > 流程文件”单击“添加”。

#### 2.2 单击“选择上传文件”，上传tosca模板，设置基本信息，包括“流程文件名称”、“版本”、“发布者”和“描述”，然后单击“创建”。

### 3 执行**DSP POD**命令，查询出：UEG网元NAT是否已实例化。

### 如果所查到的NAT Pod数**为无数据**；则继续执行后续步骤，需要将该Pod填写为规划值，执行命令后，将会实例化此Pod。

### 如果所查到的原NAT Pod数为**非0**；则说明该Pod已实例化完毕，无需继续实例化操作。如果需要继续执行实例化，请先下线NAT pod，再上线新的pod。

### 4 执行**DSP VNFPKGS**命令，查询出NAT服务的软件包名称。

### 5 执行**OPR ONECLICKDEPLOY**命令，一键式上线NAT服务。

```jinja2
{%- set DSP_POD=getParameterValue('DSP POD') -%}
{%- if DSP_POD=='' -%}
    {%- for item in opr_oneclickdeploy_list -%}
        OPR ONECLICKDEPLOY:
        {#- --- 必选参数 --- -#}
        OPRTYPE={{item.OPRTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：OPRTYPE=INDEPSTACKENABLE/FEATUREENABLE/FEATUREDISABLE 时必选 --- -#}
        {%- if item.OPRTYPE in ['INDEPSTACKENABLE', 'FEATUREENABLE', 'FEATUREDISABLE'] -%}
            FUNCTIONSETNAME="{{item.FUNCTIONSETNAME}}",
        {%- endif -%}
        {#- --- 条件必选：OPRTYPE=INDEPSTACKENABLE 时必选 --- -#}
        {%- if item.OPRTYPE == 'INDEPSTACKENABLE' -%}
            PKGNAME="{{item.PKGNAME}}",
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- Pod类型列表: 条件必选(操作类型=INDEPSTACKENABLE|FEATUREENABLE) / 条件可选(操作类型=SCALEOUT|SCALEIN) --- -#}
        {%- if (item.OPRTYPE in ['INDEPSTACKENABLE', 'FEATUREENABLE']) -%}
            PODTYPELIST="{{item.PODTYPELIST}}",
        {%- elif (item.OPRTYPE in ['SCALEOUT', 'SCALEIN']) -%}
            {%- if item.PODTYPELIST is not none -%}
                PODTYPELIST="{{item.PODTYPELIST}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 参数“OPRTYPE”填写为“INDEPSTACKENABLE”。

### 参数“PODTYPELIST”裸机环境下pod个数固定填写为1。

### 参数“FUNCTIONSETNAME”填写为“NAT”。

### 参数“PKGNAME”需配置为**4**查询出的NAT服务软件包名称。

### 6 执行**DSP ONECLICKDEPLOYHIST**命令，确认一键式上线NAT服务的回显为“处理结果=处理成功”。

### 7 登录OM Portal的MML界面。执行命令，确认已经成功实例化NAT Pod。

### 回显pod个数和规划一致，且“Pod状态”为“Running”。

### 8 执行命令，查询进程的状态。

### 预期结果：“未就绪进程数”和“故障进程数”均为0。

