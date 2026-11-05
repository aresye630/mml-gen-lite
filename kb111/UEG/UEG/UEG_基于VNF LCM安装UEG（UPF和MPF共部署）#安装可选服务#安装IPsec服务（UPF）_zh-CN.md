---
id: ''
name: 安装IPsec服务（UPF）
ne_type: UEG
type: feature
description: IPsec(Internet Protocol Security)是IETF制定的一系列协议，通过对数据流中的每个IP包进行鉴权和加密，为IP数据报提供了高质量的、可互操作的、基于密码技术的安全性。  仅当UEG网元需要部署IPsec功能时，才需要安装IPsec服务。  安装IPsec服务场景：  * **场景一**（静态上线）：IPsec服务和UEG网元**同时实例化**。实例化UEG前填写如下VNFD参数。   + 配置VM：     - 基于X86虚拟机：        PBU\_P-I\_M\_Num（仅UEG S），PBU\_P-I\_M Redundancy Num（仅UEG S）；PBU\_P-I\_Num，PBU\_P-I Redundancy Num；PBU\_P-I\_C4\_Num， PBU\_P-I\_C4 Redundancy Num。     - 基于ARM虚拟机：        PBU\_P-I\_M\_ARM\_Num（仅UEG S），PBU\_P-I\_M\_ARM Redundancy Num（仅UEG S）；PBU\_P-I\_ARM\_Num，PBU\_P-I\_ARM Redundancy Num；PBU\_P-I\_C4\_ARM\_Num， PBU\_P-I\_C4\_ARM Redundancy Num。   + 配置Pod：IPSECCTL\_Instance\_Num，IPSECEXEC\_Instance\_Num，IPSECEXEC\_C4\_Instance\_Num，IPSECEXEC\_M\_Instance\_Num（仅UEG S）。    **表1** IPsec虚拟机和pod对应关系    | 虚拟机 | 允许在单个主机上部署的此类虚拟机最大个数 | 转发pod |   | --- | --- | --- |   | PBU\_P-I | PBU\_P-I Redundancy Num | IPSECCTL\_Instance\_Num、IPSECEXEC\_Instance\_Num |   | PBU\_P-I\_C4 | PBU\_P-I\_C4 Redundancy Num | IPSECCTL\_Instance\_Num、IPSECEXEC\_C4\_Instance\_Num |   | PBU\_P-I\_M | PBU\_P-I\_M Redundancy Num | IPSECCTL\_Instance\_Num、  IPSECEXEC\_M\_Instance\_Num |    上述虚机每次上线只选择一种，配套的参数**有成套关系**，例如根据网设数据**成套配置**上述参数，其他参数都配置为0。以PBU\_P-I\_C4为例：    正确样例：PBU\_P-I\_C4=2、PBU\_P-I\_C4 Redundancy Num=1、IPSECESEC\_C4\_Instance\_Num=2    错误样例：PBU\_P-I\_C4=2、PBU\_P-I\_C4 Redundancy Num=1、IPSECEXEC\_Instance\_Num=2    以上是VNFD模板中IPsec虚拟机和容器的参数全集，在单个plan文件中，只会有部分VNFD参数，以实际的plan中所呈现的VNFD参数为准。    请以网设给出的虚拟机和容器规划来配置VNFD参数。 * **场景二**（动态上线）：**先**实例化UEG并扩容出IPsec服务自身VM（PBU\_P-I\_C4），**然后**再参考本章节，动态上线IPsec服务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG软件安装（风筝S）","安装UPF和MPF（共部署）","基于VNF LCM安装UEG（UPF和MPF共部署）","安装可选服务","安装IPsec服务（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
IPsec(Internet Protocol Security)是IETF制定的一系列协议，通过对数据流中的每个IP包进行鉴权和加密，为IP数据报提供了高质量的、可互操作的、基于密码技术的安全性。仅当UEG网元需要部署IPsec功能时，才需要安装IPsec服务。安装IPsec服务场景：* **场景一**（静态上线）：IPsec服务和UEG网元**同时实例化**。实例化UEG前填写如下VNFD参数。  + 配置VM：    - 基于X86虚拟机：      PBU\_P-I\_M\_Num（仅UEG S），PBU\_P-I\_M Redundancy Num（仅UEG S）；PBU\_P-I\_Num，PBU\_P-I Redundancy Num；PBU\_P-I\_C4\_Num， PBU\_P-I\_C4 Redundancy Num。    - 基于ARM虚拟机：      PBU\_P-I\_M\_ARM\_Num（仅UEG S），PBU\_P-I\_M\_ARM Redundancy Num（仅UEG S）；PBU\_P-I\_ARM\_Num，PBU\_P-I\_ARM Redundancy Num；PBU\_P-I\_C4\_ARM\_Num， PBU\_P-I\_C4\_ARM Redundancy Num。  + 配置Pod：IPSECCTL\_Instance\_Num，IPSECEXEC\_Instance\_Num，IPSECEXEC\_C4\_Instance\_Num，IPSECEXEC\_M\_Instance\_Num（仅UEG S）。  **表1** IPsec虚拟机和pod对应关系  | 虚拟机 | 允许在单个主机上部署的此类虚拟机最大个数 | 转发pod |  | --- | --- | --- |  | PBU\_P-I | PBU\_P-I Redundancy Num | IPSECCTL\_Instance\_Num、IPSECEXEC\_Instance\_Num |  | PBU\_P-I\_C4 | PBU\_P-I\_C4 Redundancy Num | IPSECCTL\_Instance\_Num、IPSECEXEC\_C4\_Instance\_Num |  | PBU\_P-I\_M | PBU\_P-I\_M Redundancy Num | IPSECCTL\_Instance\_Num、  IPSECEXEC\_M\_Instance\_Num |  上述虚机每次上线只选择一种，配套的参数**有成套关系**，例如根据网设数据**成套配置**上述参数，其他参数都配置为0。以PBU\_P-I\_C4为例：  正确样例：PBU\_P-I\_C4=2、PBU\_P-I\_C4 Redundancy Num=1、IPSECESEC\_C4\_Instance\_Num=2  错误样例：PBU\_P-I\_C4=2、PBU\_P-I\_C4 Redundancy Num=1、IPSECEXEC\_Instance\_Num=2  以上是VNFD模板中IPsec虚拟机和容器的参数全集，在单个plan文件中，只会有部分VNFD参数，以实际的plan中所呈现的VNFD参数为准。  请以网设给出的虚拟机和容器规划来配置VNFD参数。* **场景二**（动态上线）：**先**实例化UEG并扩容出IPsec服务自身VM（PBU\_P-I\_C4），**然后**再参考本章节，动态上线IPsec服务。

## 必备事项
前提条件

* 已经实例化UEG。已经安装后检查，UEG正常工作。

* 准备好部署所需要的镜像文件：X86为UEG-IPsec\_xx.x.x\_Docker\_X86.zip。ARM为UEG-IPsec\_xx.x.x\_Docker\_ARM.zip。
* 已经完成检查软件包完整性。

* 当系统进行动态上下线操作期间，不允许再同时进行扩缩容操作。同理，当系统进行扩缩容期间，不允许再进行动态上下线操作。
* 上下线本服务时，不能同时上下线其他部件。
* 当动态上线一个服务的任务失败，必须先动态下线此服务，再重新触发动态上线任务。如果是动态下线失败，只能继续重新触发动态下线任务。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    opr_featureenable_list:
      type: items
      properties:
        PODINSTANCENUM:
          name: 'Pod实例个数列表'
          type: string
          minLength: 0
          maxLength: 1024
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FUNCTIONSETNAME:
          name: '网络功能集名称'
          type: string
          minLength: 0
          maxLength: 1024
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        EXTENDEDATTR:
          name: '扩展属性'
          type: string
          minLength: 0
          maxLength: 1024
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    opr_featureenable_list:
    - PODINSTANCENUM: 'ipsecctl-pod:2/ipsecexec-c4-pod:2'
      FUNCTIONSETNAME: 'IPsec'
      EXTENDEDATTR: '保持空白，无需填写。'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 动态上线本服务前，必须根据客户的业务容量和设备现状进行严格的**扩容评估**。

### 确保上线服务所需的I层资源、License资源、各类网络资源（如外联口网络）是充足的，如果不充足，则要**先扩容这些资源**，然后**再上线本服务**。

### 由华为网设工程师进行网络设计，规划计算资源、存储资源、网络资源。

### 将规划数据合入《NFV LLD文档》，作为后续操作的输入。

#### 1.1 * **计算资源**：承载虚拟机的主机（服务器）、主机组、虚拟机名称、虚拟机个数、容器名称、容器个数。

#### 1.2 * **存储资源**：承载本服务的磁盘空间。

#### 1.3 * **网络资源**：承载虚拟机的网络。承载容器的网络。承载业务的物理网口、业务网络。例如虚拟机的Base网络、容器Base网络、外联口网络、外联口Subport。

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

### **图1** 同步文件到边缘站点

### 4 参考《UEG扩缩容指导书》，完成扩容操作，扩容出计算资源、存储资源、网络资源。上线可选服务时只扩容VM，无需扩容POD。

### 由华为工程师登录华为Support网站，在技术支持>知识库>云核心网>Mobile Packet Core>5G Packet Core>UEG>技术指导，中搜索《UEG扩容指导》选择对应版本号的扩容指导书，再参考指导书内“**基于LCM发起VNF扩容**”或“**基于NFVO发起VNF扩容**”进行扩容操作。

### 5 登录UEG OM Portal。

### 6 执行命令，查询出：UEG网元查询特性上下线历史。

### 7 执行命令，动态上线IPsec Pod。以PBU\_P-I\_C4虚拟机为例，PBU\_P-I虚拟机请替换为配套pod。

```jinja2
{%- for item in opr_featureenable_list -%}
    OPR FEATUREENABLE:
    {#- --- 必选参数 --- -#}
    PODINSTANCENUM="{{item.PODINSTANCENUM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FUNCTIONSETNAME is not none -%}
        FUNCTIONSETNAME="{{item.FUNCTIONSETNAME}}",
    {%- endif -%}
    {%- if item.EXTENDEDATTR is not none -%}
        EXTENDEDATTR="{{item.EXTENDEDATTR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### （1）无需配置“EXTENDEDATTR(扩展属性)”参数。

### （2）参数“FUNCTIONSETNAME”填写为“IPsec”。

### （3）参数“PODINSTANCENUM”填写为网设规划值，例如：pod1:num1/pod2:num2/pod3:num3，该参数说明请参见VNFD参考。网络规划时会给出IPsec的虚拟机名称、虚拟机数量、Pod名称、Pod数量。其中虚拟机名称和Pod名称**有成套关系**。

#### 7.1 如果6查到的原Pod数**为0**；则需要将该Pod填写为规划值，执本命令后，将会实例化此Pod。

#### 7.2 如果6查到的原Pod数为**非0**；则说明该Pod已实例化完毕，**不允许**填写该Pod的数值。

### 当pod个数为**非0**，且**不等于规划值**，请参考《UEG扩缩容指导书》，**在VNF LCM上扩容**pod个数为规划值。

### 8 执行命令，确认已经成功实例化IPsec Pod。

### 回显为“处理结果=处理成功”。

### 执行命令，确认pod已上线。

### 回显pod个数和规划一致，且“Pod状态”为“Running”。

### 9 执行命令，查询进程的状态。

### 预期结果：“进程状态”为Ready。

