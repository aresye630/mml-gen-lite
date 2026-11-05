---
id: ''
name: 安装VPROBE服务
ne_type: UNC
type: feature
description: 仅当UNC网元需要部署IMR软探针功能，才需要安装VPROBE服务。  安装VPROBE服务场景：  * **场景一****（静态上线）**：UNC网元和VPROBE服务**同时实例化**。实例化UNC前填写如下VNFD参数。   + 配置NF：“Function Set List”添加“VPROBE”。例如，添加后为"AMF/MME/SGSN/GB/VPROBE"。   + 配置VM：基于X86虚拟机PBU\_I-P\_Num。基于ARM虚拟机PBU\_I-P\_ARM\_Num。   + 配置Pod：“VPROBE\_CTRL\_Instance\_Num”，“VPROBE\_EXEC\_Instance\_Num”，“VPROBE\_EXEC-ARM\_Instance\_Num”。 * **场景二****（动态上线）**：**先**实例化UNC并扩容出VPROBE服务自身VM（PBU\_I-P），**然后**再参考本章节，动态上线VPROBE服务。  **表1** VPROBE服务需要配置的虚拟机和pod  | 虚拟机 | pod | | --- | --- | | PBU\_I-P  PBU\_I-P\_ARM | vprobectrl-pod  vprobeexec-pod |
risk_level: ''
doc_source: ["网络部署","软件安装","基于VNF LCM安装UNC（非SDN）","安装可选服务","安装VPROBE服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
仅当UNC网元需要部署IMR软探针功能，才需要安装VPROBE服务。安装VPROBE服务场景：* **场景一****（静态上线）**：UNC网元和VPROBE服务**同时实例化**。实例化UNC前填写如下VNFD参数。  + 配置NF：“Function Set List”添加“VPROBE”。例如，添加后为"AMF/MME/SGSN/GB/VPROBE"。  + 配置VM：基于X86虚拟机PBU\_I-P\_Num。基于ARM虚拟机PBU\_I-P\_ARM\_Num。  + 配置Pod：“VPROBE\_CTRL\_Instance\_Num”，“VPROBE\_EXEC\_Instance\_Num”，“VPROBE\_EXEC-ARM\_Instance\_Num”。* **场景二****（动态上线）**：**先**实例化UNC并扩容出VPROBE服务自身VM（PBU\_I-P），**然后**再参考本章节，动态上线VPROBE服务。**表1** VPROBE服务需要配置的虚拟机和pod| 虚拟机 | pod || --- | --- || PBU\_I-P  PBU\_I-P\_ARM | vprobectrl-pod  vprobeexec-pod |

## 必备事项
前提条件

* 已经实例化UNC。已经安装后检查，UNC正常工作。

* VPROBE服务依赖的软件包为UNC\_xx.x.x\_DockerSF\_X86.zip或UNC\_xx.x.x\_DockerSF\_ARM.zip。在安装UNC时已经上传本软件包，因此无需再次上传软件包。

* 当系统进行动态上下线操作期间，不允许再同时进行扩缩容操作。同理，当系统进行扩缩容期间，不允许再进行动态上下线操作。
* 上下线本服务时，不能同时上下线其他部件。
* 当动态上线一个服务的任务失败；必须先动态下线此服务，再重新触发动态上线任务。如果是动态下线失败，只能继续重新触发动态下线任务。
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
    - PODINSTANCENUM: 'vprobectrl-pod:2/vprobeexec-pod:2'
      FUNCTIONSETNAME: 'VPROBE'
      EXTENDEDATTR: '保持空白，无需填写。'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 动态上线本服务前，必须根据客户的业务容量和设备现状进行严格的**扩容评估**。

### 确保上线服务所需的I层资源、License资源、各类网络资源（如外联口网络）是充足的，如果不充足，则要**先扩容这些资源**，然后**再上线本服务**。

### 由华为网设工程师进行网络设计，规划计算资源、存储资源、网络资源。

### 将规划数据合入《NFV LLD文档》，作为后续操作的输入。

#### 1.1 * **计算资源**：承载虚拟机的主机（服务器）、主机组、虚拟机名称、虚拟机个数、容器名称、容器个数。

#### 1.2 * **存储资源**：承载本服务的磁盘空间。

#### 1.3 * **网络资源**：承载虚拟机的网络。承载容器的网络。承载业务的物理网口、业务网络。例如虚拟机的Base网络、容器Base网络、外联口网络、外联口Subport。

### 2 参考《UNC基于LCM的扩缩容指导》或《UNC基于NFVO的扩缩容指导》，完成扩容操作，扩容出计算资源、存储资源、网络资源。

### 由华为工程师登录华为Support网站，在技术支持>知识库>云核心网>Mobile Packet Core>5G Packet Core>UNC>技术指导，中搜索《UNC基于NFVO的扩缩容指导》《UNC基于LCM的扩缩容指导》。

### 3 登录UNC OM Portal。

### 4 执行命令，查询出：UNC网元支持的FunctionSet的名字，已经实例化完成的Pod类型和Pod个数，是否支持动态上下线。

### 回显为“动态上下线开关=是”。

### 5 执行命令，动态上线VPROBE Pod。

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

### （2）参数“FunctionSet”填写为“VPROBE”。

### （3）参数“PODINSTANCENUM”填写为网设规划值，例如：pod1:num1/pod2:num2/pod3:num3，该参数说明请参见VNFD参考。

#### 5.1 * 如果查到的原Pod数**为0**；则需要将该Pod填写为规划值，执本命令后，将会实例化此Pod。

#### 5.2 * 如果查到的原Pod数为**非0**；则说明该Pod已实例化完毕，**不允许**填写该Pod的数值。

#### 当pod个数为**非0**，且**不等于规划值**，请参考《UNC基于LCM的扩缩容指导》，**在VNF LCM上扩容**pod个数为规划值。

### 6 执行命令，确认已经成功实例化VPROBE Pod。

### 回显为“处理结果=处理成功”。

### 回显pod个数和规划一致，且“Pod状态”为“Running”。

### 7 执行命令，查询进程的状态。

### 预期结果：“未就绪进程数”和“故障进程数”均为0。

### 8 执行命令，确认已经安装VPROBE服务。

### 回显为

### FunctionSet Name  Status

### VPROBE            online

