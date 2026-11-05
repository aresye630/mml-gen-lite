---
id: ''
name: 安装IISA服务
ne_type: UDG
type: feature
description: '## 操作场景  操作场景  仅当UDG网元需要部署智能业务感知功能时，才需要安装IISA服务。智能业务感知功能相关功能介绍请参考：UDG 智能业务感知专题。  * UDG 20.16.2版本仅在安装了20.16.2.6及更高版本补丁时才能上线IISA服务。 * 仅部分VNFD模板支持IISA服务。如需安装IISA服务，请先联系华为技术支持确认使用的VNFD模板是否支持。  版本配套需满足以下版本才能支持IISA服务功能：  | 部件名称 | 依赖版本 | | --- | --- | | MAE-CN | V100R024C10SPC220及以后版本 | | VNFM-Agent | MAE-CN VNFM-Agent V100R025C10SPC120及以后版本（遵循版本标准配套） | | FusionSphere | 24.1.3 + SPH20及以后版本（遵循版本标准配套） | | FusionStage | 25.1.0及以后版本（遵循版本标准配套） | | UDG | 20.16.0及以后版本 |  安装IISA服务场景：  * **场景一****（静态上线）**：UDG网元和IISA服务**同时实例化**。实例化UDG前填写如下VNFD参数。   + 配置智能业务感知主机所在机框与连接板所在机框互联参数：     - NP卡场景：配置“Inter-Subrack NP Direct Connect Port”。     - 标卡场景：配置“NPFabricTrunkCfg”。   + 配置IISA服务的独立业务主机组：配置Cluster\_Mpu\_Id，参考“网设工具 > NFV LLD文档 > **计算资源设计** > DC配置规划 > Host Aggregate名称”。   + 配置PBU\_P-N\_C4N2\_ARM虚机指定NUMA1部署：配置NUMA\_ID\_PBU\_P-N\_C4N2\_ARM值，指定为1。   + 配置VM：基于ARM虚拟机：TPU\_MPU\_ARM和PBU\_P-N\_C4N2\_ARM\_Num。   + 配置Pod：“IISA\_Instance\_Num”，“IISACTRL\_Instance\_Num”，      “PBU\_P-N\_C4N2\_Instance\_Num”，“NPCTRL\_Instance\_Num”（仅ARM标卡模版需要配置该参数，NP卡模版不涉及该参数）。   + 配置NF：     - FunctionSet List参数需添加“IISA”。例如：添加后为"UDG/IISA"；当多个可选服务一起静态上线时，服务之间以“/”拼接，例如："UDG/RPT/IISA"。        **表1** 虚拟机与pod对应关系        | Pod名称 | 功能说明 | 所属微服务 | 运行VM（ARM） |       | --- | --- | --- | --- |       | iisa-pod | 提供智能业务感知业务服务功能。 | IISA | TPU\_MPU\_ARM |       | iisactrl-pod | 提供智能业务感知业务服务的管理功能。 |  |  |       | femu-c4n2-pod | 提供NP卡管理功能。 | NPM (Network Processor Management) | PBU\_P-N\_C4N2\_ARM |       | npctrl-pod | 提供NP卡引擎的统一管理功能。  说明：仅ARM标卡场景需要部署该Pod。 |  | PBU\_A\_ARM/PBU\_Ax\_ARM |        **表2** 虚机、Pod数量        | 参数 | 备注 |       | --- | --- |       | TPU\_MPU\_ARM\_Num | 每个推理单板上，部署虚机TPU\_MPU\_ARM 6个。  如果推理单板数为N，则该参数值设置为6\*N。 |       | IISA\_Instance\_Num | 每个推理单板上，部署iisa-pod 6个。  如果推理单板数为N，则该参数值设置为6\*N。 |       | IISACTRL\_Instance\_Num | 如果推理单板数为1，则iisactrl-pod部署6个；如果推理单板数大于1，则该参数值设置为7。 |       | PBU\_P-N\_C4N2\_ARM\_Num | 每个推理单板上，部署虚机PBU\_P-N\_C4N2\_ARM 1个。  如果推理单板数为N，则该参数值设置为N。 |       | PBU\_P-N\_C4N2\_Instance\_Num | 每个推理单板上，部署femu-c4n2-pod 1个。  如果推理单板数为N，则该参数值设置为N。 |       | NPCTRL\_Instance\_Num | 仅ARM标卡模版需要配置该参数，NP卡模版不涉及该参数。 |        基于以上表格中参数值设置规则，对《NFV LLD文档》中对应的虚机、Pod数量进行确认。如果不一致，请联系华为技术支持处理。 * **场景二****（动态上线）**：**先**实例化UDG，**然后**再参考本章节，动态上线IISA服务。'
risk_level: ''
doc_source: ["网络部署","软件安装","基于VNF LCM安装UDG（非SDN）","安装可选服务","安装IISA服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
## 操作场景操作场景仅当UDG网元需要部署智能业务感知功能时，才需要安装IISA服务。智能业务感知功能相关功能介绍请参考：UDG 智能业务感知专题。* UDG 20.16.2版本仅在安装了20.16.2.6及更高版本补丁时才能上线IISA服务。* 仅部分VNFD模板支持IISA服务。如需安装IISA服务，请先联系华为技术支持确认使用的VNFD模板是否支持。版本配套需满足以下版本才能支持IISA服务功能：| 部件名称 | 依赖版本 || --- | --- || MAE-CN | V100R024C10SPC220及以后版本 || VNFM-Agent | MAE-CN VNFM-Agent V100R025C10SPC120及以后版本（遵循版本标准配套） || FusionSphere | 24.1.3 + SPH20及以后版本（遵循版本标准配套） || FusionStage | 25.1.0及以后版本（遵循版本标准配套） || UDG | 20.16.0及以后版本 |安装IISA服务场景：* **场景一****（静态上线）**：UDG网元和IISA服务**同时实例化**。实例化UDG前填写如下VNFD参数。  + 配置智能业务感知主机所在机框与连接板所在机框互联参数：    - NP卡场景：配置“Inter-Subrack NP Direct Connect Port”。    - 标卡场景：配置“NPFabricTrunkCfg”。  + 配置IISA服务的独立业务主机组：配置Cluster\_Mpu\_Id，参考“网设工具 > NFV LLD文档 > **计算资源设计** > DC配置规划 > Host Aggregate名称”。  + 配置PBU\_P-N\_C4N2\_ARM虚机指定NUMA1部署：配置NUMA\_ID\_PBU\_P-N\_C4N2\_ARM值，指定为1。  + 配置VM：基于ARM虚拟机：TPU\_MPU\_ARM和PBU\_P-N\_C4N2\_ARM\_Num。  + 配置Pod：“IISA\_Instance\_Num”，“IISACTRL\_Instance\_Num”，    “PBU\_P-N\_C4N2\_Instance\_Num”，“NPCTRL\_Instance\_Num”（仅ARM标卡模版需要配置该参数，NP卡模版不涉及该参数）。  + 配置NF：    - FunctionSet List参数需添加“IISA”。例如：添加后为"UDG/IISA"；当多个可选服务一起静态上线时，服务之间以“/”拼接，例如："UDG/RPT/IISA"。      **表1** 虚拟机与pod对应关系      | Pod名称 | 功能说明 | 所属微服务 | 运行VM（ARM） |      | --- | --- | --- | --- |      | iisa-pod | 提供智能业务感知业务服务功能。 | IISA | TPU\_MPU\_ARM |      | iisactrl-pod | 提供智能业务感知业务服务的管理功能。 |  |  |      | femu-c4n2-pod | 提供NP卡管理功能。 | NPM (Network Processor Management) | PBU\_P-N\_C4N2\_ARM |      | npctrl-pod | 提供NP卡引擎的统一管理功能。  说明：仅ARM标卡场景需要部署该Pod。 |  | PBU\_A\_ARM/PBU\_Ax\_ARM |      **表2** 虚机、Pod数量      | 参数 | 备注 |      | --- | --- |      | TPU\_MPU\_ARM\_Num | 每个推理单板上，部署虚机TPU\_MPU\_ARM 6个。  如果推理单板数为N，则该参数值设置为6\*N。 |      | IISA\_Instance\_Num | 每个推理单板上，部署iisa-pod 6个。  如果推理单板数为N，则该参数值设置为6\*N。 |      | IISACTRL\_Instance\_Num | 如果推理单板数为1，则iisactrl-pod部署6个；如果推理单板数大于1，则该参数值设置为7。 |      | PBU\_P-N\_C4N2\_ARM\_Num | 每个推理单板上，部署虚机PBU\_P-N\_C4N2\_ARM 1个。  如果推理单板数为N，则该参数值设置为N。 |      | PBU\_P-N\_C4N2\_Instance\_Num | 每个推理单板上，部署femu-c4n2-pod 1个。  如果推理单板数为N，则该参数值设置为N。 |      | NPCTRL\_Instance\_Num | 仅ARM标卡模版需要配置该参数，NP卡模版不涉及该参数。 |      基于以上表格中参数值设置规则，对《NFV LLD文档》中对应的虚机、Pod数量进行确认。如果不一致，请联系华为技术支持处理。* **场景二****（动态上线）**：**先**实例化UDG，**然后**再参考本章节，动态上线IISA服务。

## 必备事项
前提条件

前提条件

前提条件

* 已经实例化UDG。已经安装后检查，UDG正常工作。
* 准备好部署所需要的镜像文件：UDG-IISA\_xx.x.x\_Docker\_ARM.zip。
* 如果IISA服务带补丁动态上线，需要准备好补丁包：UDG-IISA\_xx.x.x.x\_Docker\_ARM.zip、UDG-IISA\_xx.x.x.x\_Docker\_PATCH\_ARM.zip。
* 已经完成检查软件包完整性。

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
          data_source: ''
          pattern: ''
          default: ''
        FUNCTIONSETNAME:
          name: '网络功能集名称'
          type: string
          minLength: 0
          maxLength: 1024
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    opr_featureenable_list:
    - PODINSTANCENUM: 'iisa-pod:pod个数/iisactrl-pod:pod个数'
      FUNCTIONSETNAME: 'IISA'
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

### 2 参考《UDG边缘侧扩缩容指导书（扩容机框）》，基于《NFV LLD文档》，完成机框扩容、IISA主机扩容，并完成VNF扩容前改造。

### 参考《UDG边缘侧扩缩容指导书（扩容机框）》章节“**1.1 使用场景** > **表2 针对融合智能业务感知服务上线扩容机框、主机，请按顺序执行如下章节**”，执行对应章节操作。

### VNF扩容前改造操作：

#### 2.1 NP卡场景：需要参考“配置NP级联接口”章节，完成对应MML命令配置，使两个机框之间的级联接口生效。

#### 2.2 标卡场景：需要参考“配置NP与DC-GW互联口”章节，完成对应MML命令配置，使NP与DC-GW互联口生效。

### 注意：VNF扩容前改造操作，如果配置不完整或不正确，会导致主机间通信异常，导致后续扩容虚机、Pod失败，请务必按照操作指导正确配置。

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

### **图1** 同步文件到边缘站点

### 4 参考《UDG边缘侧扩缩容指导书（扩容机框）》，完成扩容操作，扩容出计算资源、存储资源、网络资源。

### 上线IISA服务前，需要先完成npctrl-pod扩容（仅ARM标卡模版需要，NP卡模版不需要），再完成PBU\_P-N\_C4N2\_ARM虚机扩容、femu-c4n2-pod扩容。

### 完成扩容femu-c4n2-pod后，请检查网元是否存在新增告警。如果存在新增告警，请务必按照对应告警指导解决后再进行后续操作。如果存在“ALM-100338 Fabric平面状态为Down”的告警，会导致后续上线IISA服务失败。请先检查VNF扩容前改造操作中，框间级联口是否正确配置。如果确认配置正确，请联系华为技术支持解决。

### 5 登录UDG OM Portal。

### 6 执行命令，动态上线IISA的Pod。

```jinja2
{%- for item in opr_featureenable_list -%}
    OPR FEATUREENABLE:
    {#- --- 必选参数 --- -#}
    PODINSTANCENUM="{{item.PODINSTANCENUM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FUNCTIONSETNAME is not none -%}
        FUNCTIONSETNAME="{{item.FUNCTIONSETNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 无需配置“EXTENDEDATTR(扩展属性)”参数，参数“FUNCTIONSETNAME”填写为“IISA”。

### 7 执行命令，确认已经成功实例化IISA的Pod。

### 回显为“处理结果=处理成功”。

### 回显pod个数和规划一致，且“Pod状态”为“Running”。

### 8 执行命令，查询进程的状态。

### 预期结果：“未就绪进程数”和“故障进程数”均为0。

