---
id: ''
name: 安装UPDIAM服务
ne_type: UDG
type: feature
description: 仅当UDG网元需要部署“GWFD-112003 智网接入”特性时，才需要安装UPDIAM服务。  仅部分VNFD模板支持UPDIAM服务。如需安装UPDIAM服务，请先联系华为技术支持确认使用的VNFD模板是否支持。  安装UPDIAM服务场景：  * **场景一****（静态上线）**：UDG网元和UPDIAM服务**同时实例化**。实例化UDG前填写如下VNFD参数。   + 配置VM：基于X86虚拟机（PBU\_E-D\_Num）。基于ARM虚拟机(PBU\_E-D\_ARM\_Num)。   + 配置NF：FunctionSet List参数需添加“UPDIAM”。例如：添加后为"UDG/UPDIAM"；当多个可选服务一起静态上线时，服务之间以“/”拼接，例如："UDG/RPT/UPDIAM"。   + 配置Pod：“UPDIAMCTRL\_Instance\_Num”，“UPDIAM\_Instance\_Num”。 * **场景二****（动态上线）**：**先**实例化UDG，**然后**再参考本章节，动态上线UPDIAM服务。
risk_level: ''
doc_source: ["网络部署","软件安装","基于VNF LCM安装UDG（非SDN）","安装可选服务","安装UPDIAM服务"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('DSP POD')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
仅当UDG网元需要部署“GWFD-112003 智网接入”特性时，才需要安装UPDIAM服务。仅部分VNFD模板支持UPDIAM服务。如需安装UPDIAM服务，请先联系华为技术支持确认使用的VNFD模板是否支持。安装UPDIAM服务场景：* **场景一****（静态上线）**：UDG网元和UPDIAM服务**同时实例化**。实例化UDG前填写如下VNFD参数。  + 配置VM：基于X86虚拟机（PBU\_E-D\_Num）。基于ARM虚拟机(PBU\_E-D\_ARM\_Num)。  + 配置NF：FunctionSet List参数需添加“UPDIAM”。例如：添加后为"UDG/UPDIAM"；当多个可选服务一起静态上线时，服务之间以“/”拼接，例如："UDG/RPT/UPDIAM"。  + 配置Pod：“UPDIAMCTRL\_Instance\_Num”，“UPDIAM\_Instance\_Num”。* **场景二****（动态上线）**：**先**实例化UDG，**然后**再参考本章节，动态上线UPDIAM服务。

## 必备事项
前提条件

* 已经实例化UDG。已经安装后检查，UDG正常工作。
* UPDIAM服务依赖的软件包为UDG\_xx.x.x\_DockerUDG\_X86.zip或UDG\_xx.x.x\_DockerUDG\_ARM.zip。在安装UDG时已经上传本软件包，因此无需再次上传软件包。

* 当系统进行动态上下线操作期间，不允许再同时进行扩缩容操作。同理，当系统进行扩缩容期间，不允许再进行动态上下线操作。
* 上下线本服务时，不能同时上下线其他部件。
* 当动态上线一个服务的任务失败；必须先动态下线此服务，再重新触发动态上线任务。如果是动态下线失败，继续重新触发动态下线任务。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
    - PODINSTANCENUM: 'updiamctrl-pod:2/updiam-pod:2'
      FUNCTIONSETNAME: 'UPDIAM'
      EXTENDEDATTR: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 动态上线本服务前，必须根据客户的业务容量和设备现状进行严格的**扩容评估**。

### 确保上线服务所需的I层资源、License资源、各类网络资源（如外联口网络）是充足的，如果不充足，则要**先扩容这些资源**，然后**再上线本服务**。

### 由华为网设工程师进行网络设计，规划计算资源、存储资源、网络资源。

### 将规划数据合入《NFV LLD文档》，作为后续操作的输入。

### **计算资源**：承载虚拟机的主机（服务器）、主机组、虚拟机名称、虚拟机个数、容器名称、容器个数。

### **存储资源**：承载本服务的磁盘空间。

### **网络资源**：承载虚拟机的网络。承载容器的网络。承载业务的物理网口、业务网络。例如虚拟机的Base网络、容器Base网络、外联口网络、外联口Subport。

### 2 参考《UDG中心侧扩缩容指导书(基于LCM)》或《UDG中心侧扩缩容指导书(基于NFVO)》，完成扩容操作，扩容出计算资源、存储资源、网络资源、VM和POD。上线可选服务时可只扩容VM，无需扩容POD。可选服务所用VM可参见扩容指导书内非基础业务扩容规格确定章节**。**

### 由华为工程师登录华为Support网站，在技术支持>知识库>云核心网>Mobile Packet Core>5G Packet Core>UDG>技术指导，中搜索《UDG中心侧扩缩容指导书(基于LCM)》或《UDG中心侧扩缩容指导书(基于NFVO)》。

### 非SDN组网模式下使用《UDG中心侧扩缩容指导书(基于LCM)》，SDN组网模式请使用《UDG中心侧扩缩容指导书(基于NFVO)》。

### 3 登录UDG OM Portal。

### 4 执行命令，查询pod是否存在。

#### 4.1 如果所查到的原Pod数**为0**；说明系统中并没有实例化该服务，请执行后续步骤，进行实例化该服务。

#### 4.2 如果所查到的原Pod数为**非0**；则说明该Pod已实例化完毕。

##### 4.2.1 当查询pod个数为**非0**，且**不等于规划值**，请参考《UDG基于LCM的扩缩容指导》，**在VNF LCM上扩容**pod个数为规划值。

##### 4.2.2 当查询pod个数为**非0**，且**与规划值相等**，表示当前服务已完成实例化，无需执行后续步骤。

### 5 执行命令，动态上线UPDIAM的Pod。

```jinja2
{%- set DSP_POD=getParameterValue('DSP POD') -%}
{%- if DSP_POD=='0' -%}
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
{%- endif -%}
```

### （1）无需配置“EXTENDEDATTR(扩展属性)”参数。

### （2）参数“FUNCTIONSETNAME”填写为“UPDIAM”。

### （3）参数“PODINSTANCENUM”填写为网设规划值，例如：pod1:num1/pod2:num2/pod3:num3

### 6 执行命令，确认已经成功实例化UPDIAM的Pod。

### 回显为“处理结果=处理成功”。

### 回显pod个数和规划一致，且“Pod状态”为“Running”。

### 7 执行命令，查询进程的状态。

### 预期结果：“未就绪进程数”和“故障进程数”均为0。

