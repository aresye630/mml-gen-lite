---
id: ''
name: 一键式上线IPSec服务（UPF）
ne_type: UEG
type: feature
description: IPsec(Internet Protocol Security)是IETF制定的一系列协议，通过对数据流中的每个IP包进行鉴权和加密，为IP数据报提供了高质量的、可互操作的、基于密码技术的安全性。  仅当UEG网元需要部署IPsec功能时，才需要安装IPsec服务。  **一键式上线IPSec服务**：**先**实例化UEG，**然后**再参考本章节，一键式上线IPSec服务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG软件安装（风筝S）","安装UPF（独立部署）","基于中心NFVO (Orchestrator)安装（UPF）","NFVO安装UEG（非SDN场景）","安装可选服务","一键式上线IPSec服务（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
IPsec(Internet Protocol Security)是IETF制定的一系列协议，通过对数据流中的每个IP包进行鉴权和加密，为IP数据报提供了高质量的、可互操作的、基于密码技术的安全性。仅当UEG网元需要部署IPsec功能时，才需要安装IPsec服务。**一键式上线IPSec服务**：**先**实例化UEG，**然后**再参考本章节，一键式上线IPSec服务。

## 必备事项
前提条件

* LCM版本不低于V100R024C10。
* 已经实例化UEG。已经安装后检查，UEG正常工作。
* 准备好部署所需要的镜像文件：X86为UEG-IPsec\_xx.x.x\_Docker\_X86.zip。ARM为UEG-IPsec\_xx.x.x\_Docker\_ARM.zip。
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
          description: ''
          data_source: '本端规划'
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
  examples:
    opr_oneclickdeploy_list:
    - OPRTYPE: FEATUREENABLE
      NODETYPELIST: 'PBU_P-I_C4:VM个数'
      PODTYPELIST: 'ipsecexec-c4-pod:pod个数/ipsecctl-pod:pod个数'
      FUNCTIONSETNAME: 'IPSec'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 动态上线本服务前，必须根据客户的业务容量和设备现状进行严格的**扩容评估**。

### 确保上线服务所需的I层资源、License资源、各类网络资源（如外联口网络）是充足的，如果不充足，则要**先扩容这些资源**，然后**再上线本服务**。

### 由华为网设工程师进行网络设计，规划计算资源、存储资源、网络资源。

### 将规划数据合入《NFV LLD文档》，作为后续操作的输入。

#### 1.1 **计算资源**：承载虚拟机的主机（服务器）、主机组、虚拟机名称、虚拟机个数、容器名称、容器个数。

#### 1.2 **存储资源**：承载本服务的磁盘空间。

#### 1.3 **网络资源**：承载虚拟机的网络。承载容器的网络。承载业务的物理网口、业务网络。例如虚拟机的Base网络、容器Base网络、外联口网络、外联口Subport。

### 2 检查**软件包，**确保已经上传依赖的软件包。

### 登录MAE-VNF LCM/U2020 VNF LCM，单击“包管理 > VNFD > 单击VNFD模板，查看VNFD模板详情 > 依赖的服务镜像”。

#### 2.1 若“UEG-IPsec\_xx.x.x\_Docker\_X86.zip”“UEG-IPsec\_xx.x.x\_Docker\_ARM.zip” 软件包的状态为“已经存在”，说明已经上传软件包，则跳过3，执行后续步骤。

#### 2.2 若软件包的状态为“等待上传”，则需要执行3。

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

### 5 执行**DSP POD**命令，查询出：UEG网元IPSec是否已实例化。

#### 5.1 如果所查到的IPsec Pod数**为无数据**；则继续执行后续步骤，需要将该Pod填写为规划值，执行命令后，将会实例化此Pod。

#### 5.2 如果所查到的原IPsec Pod数为**非0**；则说明该Pod已实例化完毕。

##### 5.2.1 当查询pod个数为**非0**，且**不等于规划值**，请参考《UEG扩缩容指导书》，**在VNF LCM上扩容**pod个数为规划值。

##### 5.2.2 当查询pod个数为**非0**，且**与规划值相等**，表示当前服务已完成实例化，无需执行后续步骤。

### 6 执行**OPR ONECLICKDEPLOY**命令，一键式上线IPSec的VM和Pod。以PBU\_P-I\_C4虚拟机为例，其他虚拟机请替换为配套pod。

```jinja2
{%- for item in opr_oneclickdeploy_list -%}
    OPR ONECLICKDEPLOY:
    {#- --- 必选参数 --- -#}
    OPRTYPE={{item.OPRTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：OPRTYPE=INDEPSTACKENABLE/FEATUREENABLE/FEATUREDISABLE 时必选 --- -#}
    {%- if item.OPRTYPE in ['INDEPSTACKENABLE', 'FEATUREENABLE', 'FEATUREDISABLE'] -%}
        FUNCTIONSETNAME="{{item.FUNCTIONSETNAME}}",
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
```

#### 6.1 参数“OPRTYPE”填写为“FEATUREENABLE”。

#### 6.2 参数“NODETYPELIST”填写为网设VM的规划值。例如：VM1:num1。

#### 6.3 参数“PODTYPELIST”填写为网设pod的规划值，例如：pod1:num1/pod2:num2/pod3:num3。

#### 网络规划时会给出虚拟机名称、虚拟机数量、Pod名称、Pod数量。其中虚拟机名称和Pod名称**有成套关系**。

#### 6.4 参数“FUNCTIONSETNAME”填写为“IPSec”。

### 7 执行**DSP ONECLICKDEPLOYHIST**命令，确认一键式上线IPSec服务的回显为“处理结果=处理成功”。

### 8 执行命令，确认pod已上线。

### 回显pod个数和规划一致，且“Pod状态”为“Running”。

### 9 执行命令，查询进程的状态。

### 预期结果：“进程状态”为Ready。

