---
id: ''
name: 安装NAT服务（UPF）
ne_type: UEG
type: feature
description: NAT(Network Address Translation)服务应用场景：当用户从私有网络（私有IP地址）访问公有网络（公有IP地址）时，使用NAT功能将私有地址转换为公有地址，实现业务访问。  仅当UEG网元需要部署NAT功能，才需要安装NAT服务。  **安装NAT服务：先**实例化UEG，**然后**再参考本章节，动态上线NAT服务。  使用NP卡时，不支持NAT可选服务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG软件安装（风筝S）","安装UPF（独立部署）","基于中心NFVO (Orchestrator)安装（UPF）","NFVO安装UEG（SDN场景）","安装可选服务","安装NAT服务（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
NAT(Network Address Translation)服务应用场景：当用户从私有网络（私有IP地址）访问公有网络（公有IP地址）时，使用NAT功能将私有地址转换为公有地址，实现业务访问。仅当UEG网元需要部署NAT功能，才需要安装NAT服务。**安装NAT服务：先**实例化UEG，**然后**再参考本章节，动态上线NAT服务。使用NP卡时，不支持NAT可选服务。

## 必备事项
前提条件

* 已经实例化UEG。已经安装后检查，UEG正常工作。
* 准备好部署所需要的镜像文件“5G-UP-VASs-UEG-NAT\_xx.x.x\_X86.zip ” 或“5G-UP-VASs-UEG-NAT\_xx.x.x\_ARM.zip ”。
* 如果NAT服务带补丁动态上线，需要准备好补丁包5G-UP-VASs-UEG-NAT-Service\_xx.x.x\_PATCH\_X86.zip或5G-UP-VASs-UEG-NAT-Service\_xx.x.x\_PATCH\_ARM.zip。
* 已经完成检查软件包完整性。
* LCM版本不低于V100R023C10SPC100。

* 当系统进行动态上下线操作期间，不允许再同时进行扩缩容操作。同理，当系统进行扩缩容期间，不允许再进行动态上下线操作。
* 上下线本服务时，不能同时上下线其他部件。
* 当动态上线一个服务的任务失败；必须先动态下线此服务，再重新触发动态上线任务。如果是动态下线失败，只能继续重新触发动态下线任务。
* NAT服务动态上线所配套的LCM版本要求不低于V100R022C10SPC200，若当前LCM版本低于该要求，则需要升级LCM版本。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties: {}
  examples: {}
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

### 2 检查**软件包**，确保已经上传依赖的软件包。

### 登录MAE-VNF LCM/U2020 VNF LCM，单击“包管理 > VNFD > 单击VNFD模板，查看VNFD模板详情 > 依赖的服务镜像”。

#### 2.1 若“5G-UP-VASs-UEG-NAT\_xx.x.x\_X86.zip ” 、“5G-UP-VASs-UEG-NAT-Service\_xx.x.x\_PATCH\_X86.zip”（补丁包，可选），或者“5G-UP-VASs-UEG-NAT\_xx.x.x\_ARM.zip ”、“5G-UP-VASs-UEG-NAT-Service\_xx.x.x\_PATCH\_ARM.zip”（补丁包，可选）的状态为“已经存在”，说明已经上传软件包，则执行后续步骤。

#### 2.2 若软件包的状态为“等待上传”，则需要先执行3，再执行后续步骤。

### NAT服务动态上线所配套的LCM版本要求不低于V100R022C10SPC200，若当前LCM版本低于该要求，则需要升级LCM版本。

### 上传镜像后需要同步镜像包到边缘站点。

#### 2.3 在“VNFD”窗口中，**选择已导入的VNFD**。

#### 2.4 单击图标。

#### 2.5 在“边缘站点列表”区域中选择目标站点。

#### 2.6 单击“确定”。

#### **图1** 同步文件到边缘站点

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

#### **图2** 同步文件到边缘站点

### 4 （可选）更新网络堆栈。

### 为避免上线NAT后，影响网卡带宽，**C28\_FS\_SRIOV\_Bonding**和**FS\_SRIOV\_Bonding\_CSAR\_ARM**模板里NAT需要支持fabric-in网络，当使用这两种模板且上线PBU-E-N\_M VM,需要更新网络堆栈操作，其他情况下不需要进行此步骤。

#### 4.1 更新VNFD模板。

##### 4.1.1 使用具备VNF生命周期管理权限的非admin账号或admin账号登录LCM，选择菜单“VNF生命周期管理>VNF总览”。

##### 4.1.2 在显示的网元列表中，对于需要改造的网元，单击它的“操作”栏中的，进入更新VNFD界面。

##### 4.1.3 在更新VNFD界面，选择VNF**当前版本正在使用**的VNFD以及VNFD Plan文件。

##### 4.1.4 在“输入参数”栏中，如果模板中Fabric\_in参数存在取值为“NULL”的情况，需要修改扩容网设规划的目标值。

##### 4.1.5 单击“确定”后，在弹出的“高危”提示框中，勾选“我已明确该操作的风险”，单击“确定”。

##### 4.1.6 回到“VNF总览”页面，单击VNFD名称链接，然后单击“事件记录”按钮，在其中确认VNFD更新成功。如果VNFD更新失败，请联系华为技术支持。

##### 4.1.7 在LCM界面选择菜单“VNF生命周期管理>VNF部署>部署任务”。根据VNF名称搜索，找到扩容的VNF，选择VNFD名称。

##### 4.1.8 查看网元当前的输入参数，确认VNFD中Fabric\_in参数已经成功更新成目标值。

#### 4.2 更新网络堆栈。

##### 4.2.1 使用具备VNF生命周期管理权限的非admin账号或admin账号登录LCM，选择菜单“VNF生命周期管理>VNF更新管理”。

##### 4.2.2 择需要执行更新的VNF，单击“在线更新”。

##### 4.2.3 选择需要的操作，选择“网络堆栈升级”。

#### 4.3 完成堆栈升级后，执行步骤4进行PBU\_E-N或PBU\_E-N\_M VM（ARM形态选择对应的ARM虚拟机）扩容。

### 5 参考《UEG扩容指导书》，完成扩容操作，扩容出计算资源、存储资源、网络资源。

### 由华为工程师登录华为Support网站，在技术支持>知识库>云核心网>Mobile Packet Core>5G Packet Core>UEG>技术指导，中搜索《UEG扩容指导》选择对应版本号的扩容指导书，再参考指导书内“**基于LCM发起VNF扩容**”或“**基于NFVO发起VNF扩容**”进行扩容操作。

### **表1** NAT功能上线VM扩容个数

### | X86 VM名称 | ARM VM名称 | VM数量 | M值（Redundancy Number） |

### | --- | --- | --- | --- |

### | PBU\_E-N/PBU\_E-N\_M | PBU\_E-N\_C6/PBU\_E-N\_C6\_ARM/  PBU\_E-N\_C6\_M/PBU\_E-N\_C6\_M\_ARM  PBU\_E-N\_ARM（仅NP使用） | 参考值：2 | 参考值：1 |

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

##### 6.2.3 在弹出的界面中“操作”选择“上线”，选择对应“模板”后，根据实际规划依次填写NAT相关参数，NAT相关参数如下表所示。**不需要勾选**“进行虚拟机扩缩容”。

##### 6.2.4 单击“下一步”后，按实际规划填写与确认参数取值，在弹出的确认界面点击“确认”，自动跳转到“扩缩容任务”界面，可以查看上线堆栈进度。

##### 不在此表中的参数，不建议修改，使用默认值就可以。

##### | 参数名称 | 含义 | 来源 | 取值样例 |

##### | --- | --- | --- | --- |

##### | Language | 语言类型。  枚举类型。 * english：英文版本。 * chinese：中文版本。  说明：  Language参数必须修改为与主网元语言保持一致。 | 本端规划。 | chinese |

##### | Project\_Name | FusionStage上创建的项目名称。  本参数对应FusionStage：资源管理 > 项目管理 > 项目列表。  说明：  本参数仅支持小写取值。  本参数必须小于38个字符。 | 网设工具 > NFV LLD文档 > **计算资源设计** > PaaS Lite资源设计 > 项目(Project/Namespace)。 | dc1\_ueg01 |

##### | VNF\_Name | VNF名称。 | 网设工具 > NFV LLD文档 > **计算资源设计** > VNF设计 > VNF名称。 | UEG |

##### | natgcp-pod\_instance\_num | 系统初始实例化natgcp pod的总数。 | 由配置器或网设工具生成pod数量。  * 当使用网设工具生成VNFD时，网设工具会从配置器获取pod数量，然后填写到VNFD中。 * 当采用人工修改VNFD时，需从配置器获取pod数量，手工填入VNFD。 | 2 |

##### | natctrl-pod\_instance\_num | 系统初始实例化此类natctrl pod的总数。 |  | 2 |

##### | natom-pod\_instance\_num | 系统初始实例化此类natom pod的总数。 |  | 2 |

##### | natssg-pod\_instance\_num | 系统初始实例化此类natssg pod或natssgm pod的总数。  请根据使用的plan设置其中一种pod即可。 |  | 2 |

##### | natssgm-pod\_instance\_num |  |  | 2 |

##### | natgcpssgc6-pod\_instance\_num | 系统初始实例化此类natgcpssgc6 pod或natgcpssgc6m pod的总数。请根据使用的plan设置其中一种pod即可。  如果配置了natgcpssgc6或natgcpssgc6m pod的数量，则不需要再配置natgcp pod、natssg pod和natssgm pod的数量。 |  | 2 |

##### | natgcpssgc6m-pod\_instance\_num |  |  | 2 |

##### | CSP floating IP | CSP虚拟机外部浮动IPV4地址。  OM双栈或者OM IPV4单栈时填写。OM IPV6单栈时填写NULL。 | 参见““NFV LLD”文档 > “CloudCore业务IP对接设计”页签”。 | 192.168.1.8 |

##### | CSP floating IPV6 | CSP虚拟机外部浮动IPV6地址。  OM双栈或者OM IPV6单栈时填写。OM IPV4单栈时填写为NULL。 |  | fe80:0db8::0:23 |

##### | VNF\_TLS\_MODE | 网元内部服务间传输模式。用于控制VNF内ACS（配置）服务和HAFETCD（可靠性）服务之间通信的传输模式。 | 取值与UEG参数 VNF\_Internal\_Comm\_Mode保持一致。 | Prefer\_Performance |

##### | SWR Registry address | 镜像仓库地址。  * IPv4场景下填写镜像仓库IP。 IPv4场景下，本参数对应FusionStage：软件中心 > 软件仓库 > 镜像仓库 > 任选一个镜像 > 版本 > 拉取地址。 * IPv6场景下固定填写镜像仓库域名registry.fusionstage.local。 | 网设工具 > NFV LLD文档 > **I层IP对接设计** > FusionStage > paas-lb01& paas-lb02或PaaSCore-1&PaaSCore-2 > app\_manage\_plane > IP地址。 | IPv4样例：172.16.1.19  IPv6样例：registry.fusionstage.local |

##### 6.2.5 选择菜单栏“VNF生命周期管理 >扩缩容管理 > 手动扩缩容”，进入“扩缩容任务”窗口。在任务列表中找到NAT任务，查看“进度”及“状态”列，当进度达到100%且状态为“成功”时，NAT动态上线完成。

##### 6.2.6 如果动态上线失败，请联系华为技术支持解决。

### 7 登录UEG CSP Portal。

### 8 执行命令，查询进程的状态。

#### 8.1 **X86场景：**

#### 8.2 **ARM场景:**

#### 预期结果：“未就绪进程数”和“故障进程数”均为0。

