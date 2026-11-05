---
id: ''
name: 一键式上线NAT服务（UPF）
ne_type: UEG
type: feature
description: NAT(Network Address Translation)服务应用场景：当用户从私有网络（私有IP地址）访问公有网络（公有IP地址）时，使用NAT功能将私有地址转换为公有地址，实现业务访问。  仅当UEG网元需要部署NAT功能，才需要安装NAT服务。  **一键式上线NAT服务：先**实例化UEG，**然后**再参考本章节，一键式动态上线NAT服务。  使用NP卡时，不支持NAT可选服务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG软件安装（风筝S）","安装UPF（独立部署）","基于中心NFVO (Orchestrator)安装（UPF）","NFVO安装UEG（非SDN场景）","安装可选服务","一键式上线NAT服务（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('DSP POD')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
NAT(Network Address Translation)服务应用场景：当用户从私有网络（私有IP地址）访问公有网络（公有IP地址）时，使用NAT功能将私有地址转换为公有地址，实现业务访问。仅当UEG网元需要部署NAT功能，才需要安装NAT服务。**一键式上线NAT服务：先**实例化UEG，**然后**再参考本章节，一键式动态上线NAT服务。使用NP卡时，不支持NAT可选服务。

## 必备事项
前提条件

* LCM版本不低于V100R024C10。
* 已经实例化UEG。已经安装后检查，UEG正常工作。
* 准备好部署所需要的镜像文件：X86为“5G-UP-VASs-NAT\_xx.x.x\_X86.zip” 。ARM为“5G-UP-VASs-NAT\_xx.x.x\_ARM.zip”。
* 如果NAT服务带补丁动态上线，需要准备好补丁包5G-UP-VASs-UEG-NAT-Service\_xx.x.x\_PATCH\_X86.zip或5G-UP-VASs-UEG-NAT-Service\_xx.x.x\_PATCH\_ARM.zip。
* 已经完成检查软件包完整性。

* 当系统进行一键式上下线操作期间，不允许再同时进行扩缩容操作。同理，当系统进行扩缩容期间，不允许再进行一键式上下线操作。
* 一键式上下线本服务时，不能同时上下线其他部件。
* 当一键式上线一个服务的任务失败；必须先一键式下线此服务，再重新触发一键式上线任务。如果是一键式下线失败，只能继续重新触发一键式下线任务。
* 一键式动态上线所配套的LCM版本要求不低于V100R024C10，若当前LCM版本低于该要求，则需要升级LCM版本。
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
        NODETYPELIST:
          name: '节点类型列表'
          type: string
          minLength: 0
          maxLength: 256
          required: false
          description: 'VM类型:上线的VM个数。  * X86的VM类型：PBU\_E-N。 * ARM的VM类型：PBU\_E-N\_C6、PBU\_E-N\_C6\_ARM、PBU\_E-N\_C6\_M、PBU\_E-N\_C6\_M\_ARM。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PODTYPELIST:
          name: 'Pod类型列表'
          type: string
          minLength: 0
          maxLength: 256
          required: false
          description: 'pod类型:上线的pod个数，用/分割。不能带空格。'
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
      NODETYPELIST: 'PBU_E-N_C6_ARM:2'
      PODTYPELIST: 'natom-pod:2/natctrl-pod:2/natgcpssgc6-pod:2'
      FUNCTIONSETNAME: 'NAT'
      PKGNAME: 'UEG_TOSCA_NAT_XX_ARM_xx.x.x.zip'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 动态上线本服务前，必须根据客户的业务容量和设备现状进行严格的**扩容评估**。

### 确保上线服务所需的I层资源、License资源、各类网络资源（如外联口网络）是充足的，如果不充足，则要**先扩容这些资源**，然后**再上线本服务**。

### 由华为网设工程师进行网络设计，规划计算资源、存储资源、网络资源。

### 将规划数据合入《NFV LLD文档》，作为后续操作的输入。

### **计算资源**：承载虚拟机的主机（服务器）、主机组、虚拟机名称、虚拟机个数、容器名称、容器个数。

### **存储资源**：承载本服务的磁盘空间。

### **网络资源**：承载虚拟机的网络。承载容器的网络。承载业务的物理网口、业务网络。例如虚拟机的Base网络、容器Base网络、外联口网络、外联口Subport。

### 2 检查**软件包**，确保已经上传依赖的软件包。

### 登录MAE-VNF LCM/U2020 VNF LCM，单击“包管理 > VNFD > 单击VNFD模板，查看VNFD模板详情 > 依赖的服务镜像”。

### 若“5G-UP-VASs-NAT\_xx.x.x\_X86.zip” “5G-UP-VASs-NAT\_xx.x.x\_ARM.zip”的状态为“已经存在”，说明已经上传软件包，则跳过3，执行后续步骤。

### 若软件包的状态为“等待上传”，则需要执行3。

### 3 **上传服务镜像文件**。

#### 3.1 在“依赖的服务镜像”区域，单击“上传”，弹出“上传服务镜像”窗口。

#### 3.2 在“单包”页面，单击“选择文件”，选择依赖的服务镜像包和对应的cms文件。

#### 3.3 单击“完成”。

#### 3.4 上传完成后，“状态”均显示为“已经存在”。上传时长依赖于现场网络情况。

### 上传镜像后需要同步镜像包到边缘站点。

#### 3.5 在“VNFD”窗口中，**选择已导入的VNFD**。

#### 3.6 单击图标。

#### 3.7 在“边缘站点列表”区域中选择目标站点。

#### 3.8 单击“确定”。

#### **图1** 同步文件到边缘站点

### 4 登录UEG OM Portal。

### 5 执行**DSP POD**命令，查询出：UEG网元NAT是否已实例化。

### 如果所查到的NAT Pod数**为无数据**；则继续执行后续步骤，需要将该Pod填写为规划值，执行命令后，将会实例化此Pod。

### 如果所查到的原NAT Pod数为**非0**；则说明该Pod已实例化完毕。

#### 5.1 当查询pod个数为**非0**，且**不等于规划值**，请参考《UEG扩缩容指导书》，**在VNF LCM上扩容**pod个数为规划值。

#### 5.2 当查询pod个数为**非0**，且**与规划值相等**，表示当前服务已完成实例化，无需执行后续步骤。

### 6 执行**DSP VNFPKGS**命令，查询出NAT服务的软件包名称。

### 7 执行**OPR ONECLICKDEPLOY**命令，一键式上线NAT的VM和Pod。以PBU\_E-N\_C6\_ARM虚拟机为例，其他虚拟机请替换为配套pod。

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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：OPRTYPE=INDEPSTACKENABLE/INDEPSTACKDISABLE/FEATUREENABLE/FEATUREDISABLE/SCALEOUT/SCALEIN 时可选 --- -#}
        {%- if item.OPRTYPE in ['INDEPSTACKENABLE', 'INDEPSTACKDISABLE', 'FEATUREENABLE', 'FEATUREDISABLE', 'SCALEOUT', 'SCALEIN'] -%}
            {%- if item.NODETYPELIST is not none -%}
                NODETYPELIST="{{item.NODETYPELIST}}",
            {%- endif -%}
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

### 参数“NODETYPELIST”填写为网设VM的规划值。例如：VM1:num1。

### 参数“PODTYPELIST”填写为网设pod的规划值，例如：pod1:num1/pod2:num2/pod3:num3。

### 如果无待上线NAT服务的增量网设，网设中没有NAT pod的规划值，则natom-pod和natctrl-pod的pod个数固定填写为2，natgcpssgc6-pod使用PBU\_E-N\_C6\_ARM的Estimate\_Number数值。

### 参数“FUNCTIONSETNAME”填写为“NAT”。

### 参数“PKGNAME”需配置为6查询出的NAT服务软件包名称。

### 8 执行**DSP ONECLICKDEPLOYHIST**命令，确认一键式上线NAT服务的回显为“处理结果=处理成功”。

### 9 执行命令，确认pod已上线。

### **X86场景：**

### **ARM场景:**

### 回显pod个数和规划一致，且“Pod状态”为“Running”。

### 10 执行命令，查询进程的状态。

### **X86场景：**

### **ARM场景:**

### 预期结果：“未就绪进程数”和“故障进程数”均为0。

