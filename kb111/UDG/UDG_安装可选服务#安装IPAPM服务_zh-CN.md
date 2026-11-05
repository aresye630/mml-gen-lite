---
id: ''
name: 安装IPAPM服务
ne_type: UDG
type: feature
description: TWAMP（Two-Way Active Measurement Protocol）特性用于在IP传输网络下实时检测UDG与对端设备间IP链路QoS变化情况，并将QoS统计结果以性能指标的方式上报到MAE，可以有效地监控IP传输网络QoS，包括时延、抖动和丢包率，及时进行故障检测与定位。  TWAMP功能由IPAPM微服务承载，仅当网元需要TWAMP功能时，才需要安装IPAPM服务。  安装IPAPM服务场景：  * **场景一****（静态上线）**：UDG网元和IPAPM服务**同时实例化**。实例化UDG前填写如下VNFD参数。   + 配置VM：基于X86虚拟机（PBU\_P-T\_Num）。基于ARM虚拟机(PBU\_P-T\_ARM\_Num)。   + 配置Pod：“IPAPMEXEC\_Instance\_Num”，“IPAPMCTRL\_Instance\_Num”。      **表1** Pod及VM对应关系      | Pod类型 | 对应VM类型 | 备注 |     | --- | --- | --- |     | ipapmctrl-pod/ipapmexec-pod | PBU\_P-T/PBU\_P-T\_ARM | - | * **场景二****（动态上线）**：**先**实例化UDG，**然后**再参考本章节，动态上线IPAPM服务。
risk_level: ''
doc_source: ["网络部署","软件安装","基于NFVO安装UDG（SDN）","安装可选服务","安装IPAPM服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
TWAMP（Two-Way Active Measurement Protocol）特性用于在IP传输网络下实时检测UDG与对端设备间IP链路QoS变化情况，并将QoS统计结果以性能指标的方式上报到MAE，可以有效地监控IP传输网络QoS，包括时延、抖动和丢包率，及时进行故障检测与定位。TWAMP功能由IPAPM微服务承载，仅当网元需要TWAMP功能时，才需要安装IPAPM服务。安装IPAPM服务场景：* **场景一****（静态上线）**：UDG网元和IPAPM服务**同时实例化**。实例化UDG前填写如下VNFD参数。  + 配置VM：基于X86虚拟机（PBU\_P-T\_Num）。基于ARM虚拟机(PBU\_P-T\_ARM\_Num)。  + 配置Pod：“IPAPMEXEC\_Instance\_Num”，“IPAPMCTRL\_Instance\_Num”。    **表1** Pod及VM对应关系    | Pod类型 | 对应VM类型 | 备注 |    | --- | --- | --- |    | ipapmctrl-pod/ipapmexec-pod | PBU\_P-T/PBU\_P-T\_ARM | - |* **场景二****（动态上线）**：**先**实例化UDG，**然后**再参考本章节，动态上线IPAPM服务。

## 必备事项
前提条件

前提条件

* 已经实例化UDG。已经安装后检查，UDG正常工作。
* IPAPM服务依赖的软件包为：X86为UDG-IPapm\_xx.x.x\_Docker\_X86.zip。ARM为UDG-IPapm\_xx.x.x\_Docker\_ARM.zip。如果在安装UDG时没有上传本软件包，则需要在上线IPAPM前上传软件包，否则无需再次上传。

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
          description: 'pod类型:上线的pod个数，不同pod类型用/分割。不能带空格。（在IPAPM服务中，ipapmctrl-pod个数固定为2；ipapmexec-pod个数与虚拟机个数保持一致，必须大于等于2，默认值为2。）'
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
          description: '保持空白，无需填写。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    opr_featureenable_list_1:
      type: items
      properties:
        PODINSTANCENUM:
          name: 'Pod实例个数列表'
          type: string
          minLength: 0
          maxLength: 1024
          required: true
          description: 'pod类型:上线的pod个数，不同pod类型用/分割。不能带空格。（在IPAPM服务中，ipapmctrl-pod个数固定为2；ipapmexec-pod个数与虚拟机个数保持一致，必须大于等于2，默认值为2。）'
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
          description: '保持空白，无需填写。'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    opr_featureenable_list:
    - PODINSTANCENUM: 'ipapmctrl-pod:2/ipapmexec-pod:2'
      FUNCTIONSETNAME: 'IPAPM'
      EXTENDEDATTR: ''
    opr_featureenable_list_1:
    - PODINSTANCENUM: 'ipapmctrl-pod:2/ipapmexec-pod:2'
      FUNCTIONSETNAME: 'IPAPM'
      EXTENDEDATTR: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 动态上线本服务前，必须根据客户的业务容量和设备现状进行严格的**扩容评估**。

### 确保上线服务所需的I层资源、License资源、各类网络资源（如外联口网络）是充足的，如果不充足，则要**先扩容这些资源**，然后**再上线本服务**。

### 由华为网设工程师进行网络设计，规划计算资源、存储资源、网络资源。

### 将规划数据合入《NFV LLD文档》，作为后续操作的输入。

#### 1.1 **计算资源**：承载虚拟机的主机（服务器）、主机组、虚拟机名称、虚拟机个数、容器名称、容器个数。

#### 1.2 **存储资源**：承载本服务的磁盘空间。

#### 1.3 **网络资源**：承载虚拟机的网络。承载容器的网络。承载业务的物理网口、业务网络。例如虚拟机的Base网络、容器Base网络、外联口网络、外联口Subport。

### 2 检查**软件包，**确保已经上传依赖的软件包。

### 登录MAE-VNF LCM/U2020 VNF LCM，单击“包管理 > VNFD > 单击VNFD模板，查看VNFD模板详情 > 依赖的服务镜像”。

#### 2.1 若“UDG-IPapm\_xx.x.x\_Docker\_X86.zip”“UDG-IPapm\_xx.x.x\_Docker\_ARM.zip”软件包的状态为“已经存在”，说明已经上传软件包，则跳过步骤 3，执行后续步骤。

#### 2.2 若软件包的状态为“等待上传”，则需要执行步骤 3。

### 3 **上传服务镜像文件**。

### 如果执行LST ME命令查询的架构模式为X86，且LCM上提示ARM的包为必选时，可以忽略“是否必需上传”的提示，无需上传ARM后缀的依赖的服务镜像。

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

### 4 资源扩容。

#### 4.1 参考《UDG中心侧扩缩容指导书(基于LCM)》或《UDG中心侧扩缩容指导书(基于NFVO)》，完成扩容操作，扩容出计算资源、存储资源、网络资源。

#### 4.2 参考《UDG中心侧扩缩容指导书(基于LCM)》或《UDG中心侧扩缩容指导书(基于NFVO)》，完成IPAPM的虚拟机（基于X86虚拟机：PBU\_P-T\_Num。基于ARM虚拟机：PBU\_P-T\_ARM\_Num。）扩容。

### 由华为工程师登录华为Support网站，在技术支持>知识库>云核心网>Mobile Packet Core>5G Packet Core>UDG>技术指导，中搜索《UDG中心侧扩缩容指导书(基于LCM)》或《UDG中心侧扩缩容指导书(基于NFVO)》。

### 非SDN组网模式下使用《UDG中心侧扩缩容指导书(基于LCM)》，SDN组网模式请使用《UDG中心侧扩缩容指导书(基于NFVO)》。

### 5 登录UDG OM Portal。

### 6 执行命令，查询pod是否存在。

#### 6.1 如果所查到的原Pod数**为0**；说明系统中并没有实例化该服务，请执行后续步骤，进行实例化该服务。

#### 6.2 如果所查到的原Pod数为**非0**；则说明该Pod已实例化完毕。

##### 6.2.1 当查询pod个数为**非0**，且**不等于规划值**，请参考《UDG基于LCM的扩缩容指导》，**在VNF LCM上扩容**pod个数为规划值。

##### 6.2.2 当查询pod个数为**非0**，且**与规划值相等**，表示当前服务已完成实例化，无需执行后续步骤。

### 7 执行命令，动态上线IPAPM Pod。

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

### （1）ipapmctrl-pod固定值为2；ipapmexec-pod取值2~8。（ipapmexec-pod取值与VM个数保持一致，VM个数取值范围为2~8，ipapmexec-pod个数限制为2~8。）

### （2）无需配置“EXTENDEDATTR(扩展属性)”参数。

### （3）参数“FUNCTIONSETNAME”填写为“IPAPM”。

### （4）参数“PODINSTANCENUM”填写为网设规划值，例如：pod1:num1/pod2:num2/pod3:num3

```jinja2
{%- for item in opr_featureenable_list_1 -%}
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

### 8 执行命令，确认已经成功实例化IPAPM Pod。

### 回显为“处理结果=处理成功”。

### 回显pod个数和规划一致，且“Pod状态”为“Running”。

### 9 执行命令，查询进程的状态。

### 预期结果：“未就绪进程数”和“故障进程数”均为0。

