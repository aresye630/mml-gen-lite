---
id: ''
name: 安装SSU服务
ne_type: UDG
type: feature
description: 仅当UDG网元需要部署智能业务时，才需要安装SSU(Smart Service Unit)服务。  **安装SSU服务****场景**：  * **场景一****（静态上线）**：SSU服务和UDG网元**同时实例化**。如果有**功耗限制**，**需要**参照安装SAPO服务同时上线SAPO服务。如果无功耗限制 ，则可以不部署SAPO服务。实例化UDG前填写如下VNFD参数。   + 配置VM：基于X86虚拟机（SSU\_C16\_Num，SSU\_C16 Redundancy Num）。基于ARM虚拟机(SSU\_C16\_ARM\_Num，SSU\_C16\_ARM Redundancy Num)。   + 配置Pod：“SSUCTRL\_Instance\_Num”，“SSU\_Instance\_Num”。   + 配置NF：     - FunctionSet List参数需添加“VAB”。例如：添加后为"UDG/VAB"；当多个可选服务一起静态上线时，服务之间以“/”拼接，例如："UDG/RPT/VAB"。     - whether to initialize vab\_stack设置为true。 * **场景二****（动态上线）**：**先**实例化UDG，如果有**功耗限制**，**需要**参照安装SAPO服务完成SAPO服务的安装，以降低功耗，**然后**再参考本章节，动态上线SSU服务。如果无功耗限制 ，则可以不部署SAPO服务。
risk_level: ''
doc_source: ["网络部署","软件安装","基于NFVO安装UDG（SDN）","安装可选服务","安装SSU服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
仅当UDG网元需要部署智能业务时，才需要安装SSU(Smart Service Unit)服务。**安装SSU服务****场景**：* **场景一****（静态上线）**：SSU服务和UDG网元**同时实例化**。如果有**功耗限制**，**需要**参照安装SAPO服务同时上线SAPO服务。如果无功耗限制 ，则可以不部署SAPO服务。实例化UDG前填写如下VNFD参数。  + 配置VM：基于X86虚拟机（SSU\_C16\_Num，SSU\_C16 Redundancy Num）。基于ARM虚拟机(SSU\_C16\_ARM\_Num，SSU\_C16\_ARM Redundancy Num)。  + 配置Pod：“SSUCTRL\_Instance\_Num”，“SSU\_Instance\_Num”。  + 配置NF：    - FunctionSet List参数需添加“VAB”。例如：添加后为"UDG/VAB"；当多个可选服务一起静态上线时，服务之间以“/”拼接，例如："UDG/RPT/VAB"。    - whether to initialize vab\_stack设置为true。* **场景二****（动态上线）**：**先**实例化UDG，如果有**功耗限制**，**需要**参照安装SAPO服务完成SAPO服务的安装，以降低功耗，**然后**再参考本章节，动态上线SSU服务。如果无功耗限制 ，则可以不部署SAPO服务。

## 必备事项
前提条件

* 已经实例化UDG。已经安装后检查，UDG正常工作。
* 有**功耗限制**的场景，**需要**已经完成SAPO服务的安装。如果无功耗限制 ，则可以不部署SAPO服务。
* 准备好部署所需要的镜像文件：X86为“5G-UP-VASs-UDG-VAB-X86\_xx.x.x\_X86.zip ” 。ARM为“5G-UP-VASs-UDG-VAB-ARM\_xx.x.x\_ARM.zip”。
* 如果SSU服务带补丁动态上线，需要准备好补丁包：X86为5G-UP-VASs-UDG-VAB-X86\_xx.x.x.x\_X86.zip和5G-UP-VASs-UDG-VAB-X86\_xx.x.x.x\_PATCH\_X86.zip。ARM为5G-UP-VASs-UDG-VAB-ARM\_xx.x.x.x\_ARM.zip和5G-UP-VASs-UDG-VAB-ARM\_xx.x.x.x\_PATCH\_ARM.zip。
* 准备好部署所需要的tosca模板：X86为“UDG\_TOSCA\_VAB\_XX\_X86\_xx.x.x.zip”。ARM为“UDG\_TOSCA\_VAB\_XX\_ARM\_xx.x.x.zip”。tosca模板包请从路径：技术支持>产品软件>云核心网>Mobile Packet Core>5G Packet Core>UDG>UDG xx.x.x下获取。
* 已经完成检查软件包完整性。

* 当系统进行动态上下线操作期间，不允许再同时进行扩缩容操作。同理，当系统进行扩缩容期间，不允许再进行动态上下线操作。
* 上下线本服务时，不能同时上下线其他部件。
* 当动态上线一个服务的任务失败；必须先动态下线此服务，再重新触发动态上线任务。如果是动态下线失败，只能继续重新触发动态下线任务。
* SSU服务动态上线所配套的LCM版本要求不低于V100R023C10SPC100，若当前LCM版本低于该要求，则需要升级LCM版本。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties: {}
  examples: {}
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 全部展开

### 1 动态上线本服务前，必须根据客户的业务容量和设备现状进行严格的**扩容评估**。

### 确保上线服务所需的I层资源、License资源、各类网络资源（如外联口网络）是充足的，如果不充足，则要**先扩容这些资源**，然后**再上线本服务**。

### 由华为网设工程师进行网络设计，规划计算资源、存储资源、网络资源。

### 将规划数据合入《NFV LLD文档》，作为后续操作的输入。

#### 1.1 **计算资源**：承载虚拟机的主机（服务器）、主机组、虚拟机名称、虚拟机个数、容器名称、容器个数。

#### 1.2 **存储资源**：承载本服务的磁盘空间。

#### 1.3 **网络资源**：承载虚拟机的网络。承载容器的网络。承载业务的物理网口、业务网络。例如虚拟机的Base网络、容器Base网络、外联口网络、外联口Subport。

### 2 检查**软件包**，确保已经上传依赖的软件包。

### 登录MAE-VNF LCM/U2020 VNF LCM，单击“包管理 > VNFD > 单击VNFD模板，查看VNFD模板详情 > 依赖的服务镜像”。

#### 2.1 若“5G-UP-VASs-UDG-VAB-X86\_xx.x.x\_X86.zip”、5G-UP-VASs-UDG-VAB-X86\_xx.x.x.x\_X86.zip（补丁包，可选）、5G-UP-VASs-UDG-VAB-X86\_xx.x.x.x\_PATCH\_X86.zip（补丁包，可选）或者“5G-UP-VASs-UDG-VAB-ARM\_xx.x.x\_ARM.zip”、5G-UP-VASs-UDG-VAB-ARM\_xx.x.x.x\_ARM.zip（补丁包，可选）、“5G-UP-VASs-UDG-VAB-ARM\_xx.x.x.x\_PATCH\_ARM.zip”（补丁包，可选）的状态为“已经存在”，说明已经上传软件包，则跳过步骤 3，执行后续步骤。

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

### 4 （可选）如果UDG网元版本为**20.10.2.1**，需执行如下操作，上传**patchmgr**服务镜像包。其他版本不需要执行该操作。

#### 4.1 请从Support网站**UDG VAB**下获取**patchmgr**服务镜像包。

#### X86为**patchmgr\_23.1.6.B191.tar.gz**，ARM为**patchmgr\_23.1.6.B192.tar.gz**。

#### 4.2 登录FusionStage Portal，单击主菜单的“软件中心 > 软件仓库”。在左树菜单单击“镜像仓库”，右侧界面单击“上传镜像”按钮，将下载准备好的**patchmgr**服务镜像包上传到对应的网元仓库中。

#### **图2** 上传镜像

#### 4.3 登录UDG CSP Portal，MML界面输入**RST POD**命令，其中“**网元ID**”填写为0，“**Pod复位类型**”选择byType，“**Pod类型**”填写为**patchmgr**，“**强制复位**”选择true，然后单击“执行”按钮，在“确认”弹窗中选择“是”，等待约五分钟左右， **patchmgr**服务镜像即可替换完成。

#### **图3** 执行MML

### 5 参考《UDG中心侧扩缩容指导书(基于LCM)》或《UDG中心侧扩缩容指导书(基于NFVO)》，完成扩容操作，扩容出计算资源、存储资源、网络资源。

### 6 配置堆栈。

#### 6.1 登录MANO（MAE/VNF LCM）业务面客户端。

##### 6.1.1 在浏览器地址栏中输入以下地址后按回车键，弹出MANO（MAE/VNF LCM）客户端界面。

##### **https://MANO（MAE/VNF LCM）业务的IP地址:端口号/**（例如https://10.50.12.104:31943/）

##### 6.1.2 输入用户名和密码。

##### 系统默认的用户名和密码是“admin/Changeme\_123”，如果已修改MANO（MAE/VNF LCM）客户端用户名和密码，请使用新设置的用户名和密码登录。

##### 6.1.3 单击“登录”，进入MANO（MAE/VNF LCM）系统界面。

#### 6.2 配置堆栈。

##### 6.2.1 选择菜单栏“VNF生命周期管理 >扩缩容管理 > 手动扩缩容”，进入“手动扩缩容”窗口。

##### 6.2.2 选择待操作的VNF，单击右侧“操作”列的“堆栈上下线”图标。

##### 6.2.3 在弹出的界面中“操作”选择“上线”，选择对应“模板”（“UDG\_TOSCA\_VAB\_XX\_X86\_xx.x.x.zip”或“UDG\_TOSCA\_VAB\_XX\_ARM\_xx.x.x.zip”），根据实际规划依次填写SSU相关参数，SSU相关参数如下表所示。**注意不需要勾选**“进行虚拟机扩缩容”。

##### 6.2.4 单击“下一步”后，按实际规划填写与确认参数取值，在弹出的确认界面点击“确认”，自动跳转到“扩缩容任务”界面，可以查看上线堆栈进度。

##### 不在此表中的参数，不建议修改，使用默认值就可以。

##### | 参数名称 | 含义 | 来源 | 取值样例 |

##### | --- | --- | --- | --- |

##### | Language | 语言类型。  枚举类型。 * english：英文版本。 * chinese：中文版本。  说明：  Language参数必须修改为与主网元语言保持一致。 | 本端规划。 | chinese |

##### | Project\_Name | FusionStage上创建的项目名称。  本参数对应FusionStage：资源管理 > 项目管理 > 项目列表。  说明：  本参数仅支持小写取值。  本参数必须小于38个字符。 | 网设工具 > NFV LLD文档 > **计算资源设计** > PaaS Lite资源设计 > 项目(Project/Namespace)。 | dc1\_upf01 |

##### | ssuctrl-pod\_instance\_num | 系统初始实例化ssuctrl pod的总数。 | 由配置器或网设工具生成pod数量。  * 当使用网设工具生成VNFD时，网设工具会从配置器获取pod数量，然后填写到VNFD中。 * 当采用人工修改VNFD时，需从配置器获取pod数量，手工填入VNFD。 | 2 |

##### | ssu-pod\_instance\_num | 系统初始实例化此类ssu pod的总数。 |  | 2 |

##### | VNF\_TLS\_MODE | 网元内部服务间传输模式。用于控制VNF内ACS（配置）服务和HAFETCD（可靠性）服务之间通信的传输模式。 | 取值与UDG参数 VNF\_Internal\_Comm\_Mode保持一致。 | Prefer\_Performance |

##### | SWR Registry address | 镜像仓库地址。  * IPv4场景下填写镜像仓库IP。 IPv4场景下，本参数对应FusionStage：软件中心 > 软件仓库 > 镜像仓库 > 任选一个镜像 > 版本 > 拉取地址。 * IPv6场景下固定填写镜像仓库域名registry.fusionstage.local。 | 网设工具 > NFV LLD文档 > **I层IP对接设计** > FusionStage > paas-lb01& paas-lb02或PaaSCore-1&PaaSCore-2 > app\_manage\_plane > IP地址。 | IPv4样例：172.16.1.19  IPv6样例：registry.fusionstage.local |

##### 6.2.5 选择菜单栏“VNF生命周期管理 >扩缩容管理 > 手动扩缩容”，进入“扩缩容任务”窗口。在任务列表中找到SSU的任务，查看“进度”及“状态”列，当进度达到100%且状态为“成功”时，SSU动态上线完成。

##### 6.2.6 如果动态上线失败，请联系华为技术支持解决。

### 7 登录UDG CSP Portal。

### 8 执行命令，确认已经成功实例化SSU Pod。

### 回显为“处理结果=处理成功”。

### 回显pod个数和规划一致，且“Pod状态”为“Running”。

### 9 执行命令，查询进程的状态。

### 预期结果：“未就绪进程数”和“故障进程数”均为0。

