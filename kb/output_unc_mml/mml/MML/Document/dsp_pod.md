# POD查询（DSP POD）

- 名词解释
- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

#### 名词解释

Mini Pod：Super Pod中的Pod。

Super Pod：一种资源调度对象，在同一个Super Pod中的Pod可以共享其中的资源（同ResourceBox）。

#### 命令功能

该命令用于查询指定Pod名称或类型的Pod信息。

#### 注意事项

支持输入参数全为空时的全量查询；支持按照Pod类型查询时进行模糊匹配。

#### 参数说明

| 参数标识      | 参数名称    | 参数说明                                                                                                                                                                                                                |
|:----------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MEID      | 网元ID    | 可选必选说明：可选参数 参数含义：查询Pod服务所在的网元ID，即应用ID。 取值范围：长度不超过40的字符串。 默认值：无。 配置原则： 可以通过MML命令LST ME获取。若不输入，表示查询所有网元的Pod信息。                                                                                                        |
| ONREBUILD | 是否待重建   | 可选必选说明：可选参数 参数含义：查询pod的待重建状态。 取值范围： OnRebuild(待重建状态)：查询待重建的pod信息。 Normal(正常状态)：查询正常状态的pod信息。 默认值：无。 配置原则：若不输入，表示查询所有状态的Pod信息。                                                                                       |
| TYPE      | Pod查询类型 | 可选必选说明：可选参数 参数含义：查询Pod的方式。 取值范围： byId（Pod名称）：按照Pod名称查询Pod信息。byType（Pod类型）：按照Pod类型查询Pod信息。 默认值：无。 配置原则：无。                                                                                                            |
| PODNAME   | Pod名称   | 可选必选说明：该参数在“Pod查询类型”取值为“Pod名称”时为必选参数，其余情况非必选。 参数含义：Pod名称。 取值范围：字符串类型，字符串长度范围为3~100个字符。 默认值：无。 配置原则： 服务实例所在Pod名称，该参数仅在“Pod查询类型”取值为“Pod名称”时有效。可以通过执行此命令时不输入“网元ID”且不选择“Pod查询类型”获取所有的“Pod名称”列表。该参数不支持在“Pod名称”列表中模糊匹配查询。 |
| PODTYPE   | Pod类型   | 可选必选说明：该参数在“Pod查询类型”取值为“Pod类型”时为必选参数。 参数含义：Pod类型。 取值范围：字符串类型，字符串长度范围为3~100个字符。 默认值：无。 配置原则： 该参数仅在“Pod查询类型”取值为“Pod类型”时有效。可以通过执行此命令时不输入“网元ID”且不选择“Pod查询类型”获取所有的“Pod类型”列表。该参数支持在“Pod类型”列表中模糊匹配查询。                      |

#### 使用实例

**场景1：不包含Mini Pod和Super Pod**

1. 根据Pod名称查询Pod信息。

   ```
   %%DSP POD: MEID="0",TYPE=byId, PODNAME="helpcenter-6595bd7fb7-fsqzz";%% 
   RETCODE = 0  操作成功 
    
   操作结果如下 
   ------------ 
       Pod名称  =  helpcenter-6595bd7fb7-fsqzz
       Pod类型  =  helpcenter
       Pod状态  =  Running
      节点名称  =  10.186.125.60
      主机名称  =  803AA02C-2197-E611-AAB1-48D5396401E6
   Pod运行时间  =  3d17h
    是否待重建  =  Normal
   (结果个数 = 1)  

   ---    END
   ```
2. 根据Pod类型查询Pod信息。

   ```
   %%DSP POD: MEID="0",TYPE=byType, PODTYPE="helpcenter";%% 
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------ 
   Pod名称                       Pod类型      Pod状态    节点名称       主机名称                               Pod运行时间   是否待重建
   helpcenter-6595bd7fb7-fsqzz   helpcenter   Running    10.186.125.60  803AA02C-2197-E611-AAB1-48D5396401E6   3d17h         Normal   
   helpcenter-6595bd7fb7-qrqjl   helpcenter   Running    10.186.125.80  3DD7DA93-1D50-008E-E811-91465CB1BACF   3d17h         Normal
   (结果个数 = 2)  

   ---    END
   ```
3. 根据Pod类型模糊匹配查询Pod信息。

   ```
   %%DSP POD: MEID="0",TYPE=byType, PODTYPE="cse";%%
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------ 
   Pod名称                              Pod类型             Pod状态    节点名称        主机名称                              Pod运行时间   是否待重建

   cse-etcd-0                           cse-etcd            Running    10.186.125.102  803AA02C-2197-E611-AAB1-48D5396401E6  3d18h         Normal
   cse-etcd-1                           cse-etcd            Running    10.186.125.103  3DD7DA93-1D50-008E-E811-91465CB1BACF  3d18h         Normal
   cse-etcd-2                           cse-etcd            Running    10.186.125.104  92645A88-058E-E611-8891-203DB26977DA  3d18h         Normal
   cse-service-center-5cc56794c4-g95nh  cse-service-center  Running    10.186.125.105  92645A88-058E-E611-8891-203DB26977DA  3d17h         Normal
   cse-service-center-5cc56794c4-lpstl  cse-service-center  Running    10.186.125.106  803AA02C-2197-E611-AAB1-48D5396401E6  3d17h         Normal
   cse-service-center-5cc56794c4-v7fnc  cse-service-center  Running    10.186.125.107  3DD7DA93-1D50-008E-E811-91465CB1BACF  3d17h         Normal
   (结果个数 = 6)  

   ---    END
   ```
4. 查询全量Pod信息。

   ```
   %%DSP POD:;%%
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------ 
   Pod名称                              Pod类型             Pod状态    节点名称        主机名称                              Pod运行时间   是否待重建

   auditlog-6c95885589-pzbfp            auditlog            Running    10.186.125.110  803AA02C-2197-E611-AAB1-48D5396401E6  3d18h         Normal
   auditlog-6c95885589-wng6t            auditlog            Running    10.186.125.120  3DD7DA93-1D50-008E-E811-91465CB1BACF  3d18h         Normal
   backupmgr-75886c9d4b-cnjrd           backupmgr           Running    10.186.125.130  92645A88-058E-E611-8891-203DB26977DA  3d18h         Normal
   ......
   zookeeper-1                          zookeeper           Running    10.186.125.140  803AA02C-2197-E611-AAB1-48D5396401E6  3d18h         OnRebuild
   zookeeper-2                          zookeeper           Running    10.186.125.150  3DD7DA93-1D50-008E-E811-91465CB1BACF  3d18h         OnRebuild
   (结果个数 = 89)  

   ---    END
   ```
5. 根据Pod名称查询待重建状态Pod信息。

   ```
   %%DSP POD: MEID="0", ONREBUILD=OnRebuild, TYPE=byId, PODNAME="helpcenter-6595bd7fb7-fsqzz";%% 
   RETCODE = 0  操作成功 
    
   操作结果如下 
   ------------ 
       Pod名称  =  helpcenter-6595bd7fb7-fsqzz
       Pod类型  =  helpcenter
       Pod状态  =  Running
      节点名称  =  10.186.125.60
      主机名称  =  803AA02C-2197-E611-AAB1-48D5396401E6
   Pod运行时间  =  3d17h
    是否待重建  =  OnRebuild
   (结果个数 = 1)  

   ---    END
   ```
6. 根据Pod类型查询待重建状态的Pod信息。

   ```
   %%DSP POD: ONREBUILD=OnRebuild, TYPE=byType, PODTYPE="fileserver";%% 
   RETCODE = 0  操作成功  
   操作结果如下 
   ------------ 
   Pod名称       Pod类型     Pod状态  节点名称        主机名称                               Pod运行时间   是否待重建    

   fileserver-0  fileserver  Running  10.101.28.154   803AA02C-2197-E611-AAB1-48D5396401E6   143m          OnRebuild       
   fileserver-1  fileserver  Running  10.101.28.23    92645A88-058E-E611-8891-203DB26977DA   143m          OnRebuild   
   (结果个数 = 2)  

   ---    END
   ```
7. 全量查询待重建状态的Pod信息。

   ```
   %%DSP POD: ONREBUILD=OnRebuild;%%
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------ 
   Pod名称                              Pod类型             Pod状态    节点名称        主机名称                              Pod运行时间   是否待重建

   zookeeper-1                          zookeeper           Running    10.186.125.140  803AA02C-2197-E611-AAB1-48D5396401E6  3d18h         OnRebuild
   zookeeper-2                          zookeeper           Running    10.186.125.150  3DD7DA93-1D50-008E-E811-91465CB1BACF  3d18h         OnRebuild
   (结果个数 = 2)  

   ---    END
   ```

**场景2：包含Mini Pod和Super Pod**

1. 根据Pod名称查询Mini Pod信息。

   ```
   %%DSP POD: TYPE=byId, PODNAME="cse-etcd-0";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
       Pod名称  =  cse-etcd-0
       Pod类型  =  cse-etcd
       Pod状态  =  Running
      节点名称  =  csp-c-resourcepool-625b60e6-0-doubleupg04
      主机名称  =  paas-10-186-125-110
   Pod运行时间  =  10h
    是否待重建  =  Normal
   (结果个数 = 1)

   ---    END
   ```
2. 根据Pod名称查询Super Pod信息。

   ```
   %%DSP POD: TYPE=byId, PODNAME="csp-c-resourcepool-625b60e6-0";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
       Pod名称  =  csp-c-resourcepool-625b60e6-0
       Pod类型  =  vnode
       Pod状态  =  Running
      节点名称  =  paas-10-186-125-110
      主机名称  =  paas-10-186-125-110
   Pod运行时间  =  10h
    是否待重建  =  Normal
   (结果个数 = 1)

   ---    END
   ```
3. 根据Pod类型查询Pod信息。

   ```
   %%DSP POD: TYPE=byType, PODTYPE="cse";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   Pod名称                             Pod类型             Pod状态  节点名称                                   主机名称             Pod运行时间   是否待重建

   cse-etcd-0                          cse-etcd            Running  csp-c-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-110  10h           Normal
   cse-etcd-1                          cse-etcd            Running  csp-a-resourcepool-625b60e6-1-doubleupg04  paas-10-186-125-111  10h           Normal
   cse-etcd-2                          cse-etcd            Running  csp-a-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-112  10h           Normal
   cse-service-center-969497985-8m8vh  cse-service-center  Running  csp-c-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-110  10h           Normal
   cse-service-center-969497985-9n5bg  cse-service-center  Running  csp-a-resourcepool-625b60e6-1-doubleupg04  paas-10-186-125-111  2d18h         Normal
   cse-service-center-969497985-wcpcl  cse-service-center  Running  csp-a-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-112  2d18h         Normal
   dcserimage-0-6c878cdf7b-fthk2       dcserimage-0        Running  csp-a-resourcepool-0af34063-0-doubleupg04  paas-10-186-125-110  4d23h         Normal
   dcserimage-0-6c878cdf7b-wng45       dcserimage-0        Running  csp-a-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-111  4d23h         Normal
   (结果个数 = 8)

   ---    END
   ```
4. 根据Pod类型查询vnode类型的Pod信息。

   ```
   %%DSP POD: TYPE=byType, PODTYPE="vnode";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   Pod名称                        Pod类型  Pod状态  节点名称             主机名称             Pod运行时间   是否待重建

   csp-a-resourcepool-625b60e6-0  vnode    Running  paas-10-186-125-110  paas-10-186-125-110  4d23h         Normal
   csp-a-resourcepool-625b60e6-1  vnode    Running  paas-10-186-125-111  paas-10-186-125-111  4d23h         Normal
   csp-c-resourcepool-625b60e6-0  vnode    Running  paas-10-186-125-112  paas-10-186-125-112  10h           Normal
   (结果个数 = 3)

   ---    END
   ```
5. 查询全量Pod信息。

   ```
   %%DSP POD:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   Pod名称                                      Pod类型                     Pod状态  节点名称                                   主机名称             Pod运行时间   是否待重建

   auditlog-775d449666-9zwwl                    auditlog                    Running  csp-a-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-110  44h           Normal
   auditlog-775d449666-fdst5                    auditlog                    Running  csp-a-resourcepool-625b60e6-1-doubleupg04  paas-10-186-125-111  44h           Normal
   backupmgr-0                                  backupmgr                   Running  csp-a-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-112  2d19h         OnRebuild
   csp-a-resourcepool-625b60e6-0                vnode                       Running  paas-10-186-125-110                        paas-10-186-125-110  2d19h         Normal
   csp-a-resourcepool-625b60e6-1                vnode                       Running  paas-10-186-125-111                        paas-10-186-125-111  2d19h         Normal
   csp-c-resourcepool-625b60e6-0                vnode                       Running  paas-10-186-125-112                        paas-10-186-125-112  2d19h         Normal
   ......
   (结果个数 = 98)

   ---    END
   ```

#### 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。输出结果说明如表1 查询结果所示。

命令执行失败则返回相应的错误，参见表2 错误码列表；命令执行异常，请联系技术支持处理。

查询Mini Pod时，显示的节点名称不是Super Pod的名称，而是“Super Pod的名称-当前命名空间的值”。

查询Super Pod时，显示的Pod类型是“vnode”。

| 查询结果字段   | 字段解释                                                                                                                                                                                                                                                                                                              |
|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pod名称    | 服务实例Pod名称。                                                                                                                                                                                                                                                                                                        |
| Pod类型    | 服务实例Pod类型。                                                                                                                                                                                                                                                                                                        |
| Pod状态    | 服务实例Pod状态： Pending：Pod已被Kubernetes系统接受，但有一个或者多个容器镜像尚未创建。Running：该Pod已经绑定到了一个节点上，Pod中所有的容器都已被创建。Failed：Pod中的所有容器都已终止了，并且至少有一个容器是因为失败终止。Unknown：出于某种原因无法获得Pod的状态，通常是由于与Pod主机通信时出错。Terminating：Pod正在被Kubernetes系统删除。Disabled：Pod内的容器不能对外正常提供业务。Completed：Pod调度完成。Finished：Pod调度成功。Abnormal：Pod内所有的容器都已被创建，容器内进程状态异常。 |
| 节点名称     | 服务实例所在节点的名称。                                                                                                                                                                                                                                                                                                      |
| 主机名称     | 服务实例所在主机的名称（对于第三方虚拟化层该字段可能为空）。  说明： 在“主机名称”会变更的情况下，如节点重建、节点迁移、节点扩容以及EOS改造等场景，该字段的更新会延迟5分钟。                                                                                                                                                                                                                        |
| Pod运行时间  | 查询时的当前时间与Pod创建时间的差值。                                                                                                                                                                                                                                                                                              |
| 是否待重建    | 服务实例Pod待重建状态： OnRebuild：该Pod处于待重建状态。 Normal：该Pod处于正常状态。                                                                                                                                                                                                                                                           |

|    错误码 | 错误码解释                            | 原因分析                             | 处理建议                                                                                                                                                                                                       |
|-------:|:---------------------------------|:---------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 140001 | MML命令请求参数为空。                     | MML下发命令必输参数为空。                   | MML下发命令时请输入全部必输字段。                                                                                                                                                                                         |
| 140002 | MML命令不存在。                        | 下发MML操作命令不存在。                    | 确认下发的MML命令存在。                                                                                                                                                                                              |
| 140003 | Pod查询参数不能为空。                     | Pod查询参数为空。                       | 确认Pod查询参数不为空。                                                                                                                                                                                              |
| 140004 | Pod查询参数Pod类型不合法。                 | Pod查询参数Pod类型不合法。                 | 确认Pod查询参数Pod类型是否合法。                                                                                                                                                                                        |
| 140005 | 根据Pod名称查询Pod时，Pod名称不能为空。         | 根据Pod名称查询Pod时，Pod名称不能为空。         | 确认Pod名称参数不能为空。                                                                                                                                                                                             |
| 140006 | 根据Pod类型查询Pod时，Pod类型不能为空。         | 根据Pod类型查询Pod时，Pod类型不能为空。         | 确认Pod类型参数不能为空。                                                                                                                                                                                             |
| 140007 | Pod名称和Pod类型只能有一个有值。              | Pod查询时Pod名称和Pod类型不能同时有值。         | 确认Pod名称和Pod类型不能同时有值。                                                                                                                                                                                       |
| 140008 | 查询Pod不存在。                        | 查询Pod信息不存在。                      | 通过执行MML命令“DSP POD”（不输入或者选择参数）查询全量Pod，确认Pod信息是否存在。                                                                                                                                                          |
| 140019 | 其他错误。                            | MML查询命令异常。                       | 联系技术支持处理。                                                                                                                                                                                                  |
| 140023 | Pod查询参数网元ID校验异常。                 | 查询验证网元ID异常。                      | 确认存在有效的网元ID，进入“首页”，查看输入的网元ID（页面显示为应用ID）下的服务数是否为0。                                                                                                                                                          |
| 140025 | Pod查询参数网元ID不存在。                  | 查询输入参数网元ID不存在。                   | 确认输入参数网元ID为存在网元ID。                                                                                                                                                                                         |
| 140026 | Pod查询参数limit不合法。                 | Pod查询参数limit不合法。                 | 联系华为技术支持处理。                                                                                                                                                                                                |
| 140027 | 根据Pod类型查询Pod时，Pod类型长度必须在3到100之间。 | 根据Pod类型查询Pod时，Pod类型长度必须在3到100之间。 | Pod类型字段长度确保在3到100之间。                                                                                                                                                                                       |
| 140028 | 根据Pod名称查询Pod时，Pod名称长度必须在3到100之间。 | 根据Pod名称查询时Pod名称字段长度必须在3到100之间。   | Pod名称字段长度确保在3到100之间。                                                                                                                                                                                       |
| 140039 | 查询失败。                            | Pod查询失败，无法连接到PaaS。               | Fullstack虚机场景：系统存在ALM-135301 PaasBroker和FusionStage的通信失败或者多条“服务名称”为“PaaSBroker”的ALM-5521 服务中心和服务通信故障（服务所在节点进入bypass或者网络故障等原因）告警未清除时，按照告警帮助清除告警后再执行此命令，若仍执行失败请联系华为技术支持处理。三方CaaS场景和Fullstack裸机场景：联系华为技术支持处理。 |
| 140040 | 部分查询成功。                          | 全量查询时，部分查询成功。                    | 联系华为技术支持处理。                                                                                                                                                                                                |