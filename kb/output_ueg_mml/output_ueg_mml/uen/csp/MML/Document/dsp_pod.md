# POD查询（DSP POD）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询指定Pod名称或类型的Pod信息。

#### 注意事项

- 支持输入参数全为空时的全量查询；支持按照Pod类型查询时进行模糊匹配。

#### 参数说明

| 参数标识      | 参数名称    | 参数说明                                                                                                                                                                                                        |
|:----------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MEID      | 网元ID    | 可选必选说明：可选参数 参数含义：查询Pod服务所在的网元ID，即应用ID。 取值范围：长度不超过40的字符串。 默认值：无。 配置原则： 可以通过MML命令“LST ME”获取。若不输入，表示查询所有网元的Pod信息。                                                                                              |
| ONREBUILD | 是否待重建   | 可选必选说明：可选参数 参数含义：查询pod的待重建状态。 取值范围： OnRebuild(待重建状态)：查询待重建的pod信息。 Normal(正常状态)：查询正常状态的pod信息。 默认值：无。 配置原则：若不输入，表示查询所有状态的Pod信息。                                                                               |
| TYPE      | Pod查询类型 | 可选必选说明：可选参数 参数含义：查询Pod的方式。 取值范围： byId(Pod名称)：按照Pod名称查询Pod信息。byType(Pod类型)：按照Pod类型查询Pod信息。 默认值：无。 配置原则：无。                                                                                                    |
| PODNAME   | Pod名称   | 可选必选说明：该参数在“Pod查询类型”取值为“Pod名称”时为必选参数。 参数含义：Pod名称。 取值范围：字符串类型，字符串长度范围为3~100个字符。 默认值：无。 配置原则： 服务实例所在Pod名称，该参数仅在“Pod查询类型”取值为“Pod名称”时有效。可以通过执行此命令时不输入“网元ID”且不选择“Pod查询类型”获取所有的“Pod名称”列表。该参数不支持在“Pod名称”列表中模糊匹配查询。 |
| PODTYPE   | Pod类型   | 可选必选说明：该参数在“Pod查询类型”取值为“Pod类型”时为必选参数。 参数含义：Pod类型。 取值范围：字符串类型，字符串长度范围为3~100个字符。 默认值：无。 配置原则： 该参数仅在“Pod查询类型”取值为“Pod类型”时有效。可以通过执行此命令时不输入“网元ID”且不选择“Pod查询类型”获取所有的“Pod类型”列表。该参数支持在“Pod类型”列表中模糊匹配查询。              |

#### 使用实例

1. 根据Pod名称查询Pod信息。

   ```
   %%DSP POD: MEID="0",TYPE=byId, PODNAME="cspommgr-bff8bc85d-j8rhq";%% 
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------ 
       Pod名称  =  cspommgr-bff8bc85d-j8rhq
       Pod类型  =  cspommgr
       Pod状态  =  Running
      节点名称  =  paas-10-186-125-102
      主机名称  =  paas-10-186-125-102
   Pod运行时间  =  5h30m
    是否待重建  =  Normal
   (结果个数 = 1)  

   ---    END
   ```
2. 根据Pod类型查询Pod信息。

   ```
   %%DSP POD: MEID="0",TYPE=byType, PODTYPE="cspommgr";%% 
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------          
   Pod名称                       Pod类型      Pod状态    节点名称             主机名称             Pod运行时间   是否待重建
   cspommgr-bff8bc85d-k58lc      cspommgr     Running    paas-10-186-125-102  paas-10-186-125-102  7h29m         Normal
   cspommgr-bff8bc85d-rjlv7      cspommgr     Running    paas-10-186-125-102  paas-10-186-125-102  7h29m         Normal
   (结果个数 = 2)  

   ---    END
   ```
3. 根据Pod类型模糊匹配查询Pod信息。

   ```
   %%DSP POD: MEID="0", TYPE=byType, PODTYPE="cse";%%
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------ 
   Pod名称                              Pod类型             Pod状态    节点名称             主机名称             Pod运行时间   是否待重建
   cse-etcd-0                           cse-etcd            Running    paas-10-186-125-102  paas-10-186-125-102  7h29m         Normal
   cse-etcd-1                           cse-etcd            Running    paas-10-186-125-103  paas-10-186-125-103  7h29m         Normal
   cse-etcd-2                           cse-etcd            Running    paas-10-186-125-104  paas-10-186-125-104  7h29m         Normal
   cse-service-center-5cc56794c4-g95nh  cse-service-center  Running    paas-10-186-125-105  paas-10-186-125-105  7h29m         Normal
   cse-service-center-5cc56794c4-lpstl  cse-service-center  Running    paas-10-186-125-106  paas-10-186-125-106  7h29m         Normal
   cse-service-center-5cc56794c4-v7fnc  cse-service-center  Running    paas-10-186-125-107  paas-10-186-125-107  7h29m         Normal
   (结果个数 = 6)  

   ---    END
   ```
4. 查询全量Pod信息。

   ```
   %%DSP POD:;%%
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------ 
   Pod名称                              Pod类型                      Pod状态    节点名称             主机名称             Pod运行时间   是否待重建
   alarmnotifyservice-64d554b999-ccwnh  alarmnotifyservice-e1abc260  Running    paas-10-186-125-110  paas-10-186-125-110  7h29m         Normal
   alarmnotifyservice-64d554b999-xzshn  alarmnotifyservice-e1abc260  Running    paas-10-186-125-120  paas-10-186-125-120  7h29m         Normal
   aos-apiserver-5b87c768-8nxpc         aos-apiserver                Running    paas-10-186-125-130  paas-10-186-125-130  7h29m         Normal
   ......
   runlog-5665d8b566-hv46z              runlog                       Running    paas-10-186-125-140  paas-10-186-125-140  7h29m         Normal
   runlog-5665d8b566-pvgps              runlog                       Running    paas-10-186-125-150  paas-10-186-125-150  7h29m         Normal
   (结果个数 = 89)  

   ---    END
   ```
5. 根据Pod名称查询待重建状态Pod信息。

   ```
   %%DSP POD: MEID="0", ONREBUILD=OnRebuild, TYPE=byId, PODNAME="cspommgr-bff8bc85d-j8rhq";%% 
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------ 
       Pod名称  =  cspommgr-bff8bc85d-j8rhq
       Pod类型  =  cspommgr
       Pod状态  =  Running
      节点名称  =  paas-10-186-125-102
      主机名称  =  paas-10-186-125-102
   Pod运行时间  =  5h30m
    是否待重建  =  OnRebuild
   (结果个数 = 1)  

   ---    END
   ```
6. 根据Pod名称查询正常状态Pod信息。

   ```
   %%DSP POD: MEID="0", ONREBUILD=Normal, TYPE=byId, PODNAME="cspommgr-bff8bc85d-j8rhh";%% 
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------ 
       Pod名称  =  cspommgr-bff8bc85d-j8rhh
       Pod类型  =  cspommgr
       Pod状态  =  Running
      节点名称  =  paas-10-186-125-103
      主机名称  =  paas-10-186-125-103
   Pod运行时间  =  5h30m
    是否待重建  =  Normal
   (结果个数 = 1)  

   ---    END
   ```
7. 根据Pod类型查询待重建状态的Pod信息

   ```
   %%DSP POD: MEID="0", ONREBUILD=OnRebuild, TYPE=byType, PODTYPE="cspommgr";%% 
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------          
   Pod名称                       Pod类型      Pod状态    节点名称             主机名称             Pod运行时间   是否待重建
   cspommgr-bff8bc85d-k58lc      cspommgr     Running    paas-10-186-125-102  paas-10-186-125-102  7h29m         OnRebuild
   cspommgr-bff8bc85d-rjlv7      cspommgr     Running    paas-10-186-125-102  paas-10-186-125-102  7h29m         OnRebuild
   (结果个数 = 2)  

   ---    END
   ```
8. 全量查询待重建状态的Pod信息

   ```
   %%DSP POD: ONREBUILD=OnRebuild;%% 
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------          
   Pod名称                       Pod类型      Pod状态    节点名称             主机名称             Pod运行时间   是否待重建
   cspommgr-bff8bc85d-k58lc      cspommgr     Running    paas-10-186-125-102  paas-10-186-125-102  7h29m         OnRebuild
   cspommgr-bff8bc85d-rjlv7      cspommgr     Running    paas-10-186-125-102  paas-10-186-125-102  7h29m         OnRebuild
   (结果个数 = 2)  

   ---    END
   ```

#### 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。输出结果说明如表1 查询结果所示。

命令执行失败则返回相应的错误，参见表2 错误码列表；命令执行异常，请联系技术支持处理。

Pod运行时间的正确显示依赖Csp节点的时钟和FusionStage保持一致。

| 查询结果字段   | 字段解释                                                                                                                                                                                                                                                                                                              |
|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pod名称    | 服务实例Pod名称。                                                                                                                                                                                                                                                                                                        |
| Pod类型    | 服务实例Pod类型，如果无Pod类型，则显示为"NULL"，且不支持根据类型查询和复位此Pod。                                                                                                                                                                                                                                                                  |
| Pod状态    | 服务实例Pod状态： Pending：Pod已被Kubernetes系统接受，但有一个或者多个容器镜像尚未创建。Running：该Pod已经绑定到了一个节点上，Pod中所有的容器都已被创建。Failed：Pod中的所有容器都已终止了，并且至少有一个容器是因为失败终止。Unknown：出于某种原因无法获得Pod的状态，通常是由于与Pod主机通信时出错。Terminating：Pod正在被Kubernetes系统删除。Disabled：Pod内的容器不能对外正常提供业务。Completed：Pod调度完成。Finished：Pod调度成功。Abnormal：Pod内所有的容器都已被创建，容器内进程状态异常。 |
| 节点名称     | 服务实例所在节点的名称。                                                                                                                                                                                                                                                                                                      |
| 主机名称     | 服务实例所在主机的名称                                                                                                                                                                                                                                                                                                       |
| Pod运行时间  | 查询时的当前时间与Pod创建时间的差值。                                                                                                                                                                                                                                                                                              |
| 是否待重建    | 服务实例Pod待重建状态： OnRebuild：该Pod处于待重建状态。 Normal：该Pod处于正常状态。                                                                                                                                                                                                                                                           |

|    错误码 | 错误码解释                            | 原因分析                             | 处理建议                                              |
|-------:|:---------------------------------|:---------------------------------|:--------------------------------------------------|
| 140001 | MML命令请求参数为空。                     | MML下发命令必输参数为空。                   | MML下发命令时请输入全部必输字段。                                |
| 140002 | MML命令不存在。                        | 下发MML操作命令不存在。                    | 确认下发的MML命令存在。                                     |
| 140003 | Pod查询参数不能为空。                     | Pod查询参数为空。                       | 确认Pod查询参数不为空。                                     |
| 140004 | Pod查询参数Pod类型不合法。                 | Pod查询参数Pod类型不合法。                 | 确认Pod查询参数Pod类型是否合法。                               |
| 140005 | 根据Pod名称查询Pod时，Pod名称不能为空。         | 根据Pod名称查询Pod时，Pod名称不能为空。         | 确认Pod名称参数不能为空。                                    |
| 140006 | 根据Pod类型查询Pod时，Pod类型不能为空。         | 根据Pod类型查询Pod时，Pod类型不能为空。         | 确认Pod类型参数不能为空。                                    |
| 140007 | Pod名称和Pod类型只能有一个有值。              | Pod查询时Pod名称和Pod类型不能同时有值。         | 确认Pod名称和Pod类型不能同时有值。                              |
| 140008 | 查询Pod不存在。                        | 查询Pod信息不存在。                      | 通过执行MML命令“DSP POD”（不输入或者选择参数）查询全量Pod，确认Pod信息是否存在。 |
| 140019 | 其他错误。                            | MML查询命令异常。                       | 联系技术支持处理。                                         |
| 140023 | Pod查询参数网元ID校验异常。                 | 查询验证网元ID异常。                      | 确认存在有效的网元ID，进入“首页”，查看输入的网元ID（页面显示为应用ID）下的服务数是否为0。 |
| 140025 | Pod查询参数网元ID不存在。                  | 查询输入参数网元ID不存在。                   | 确认输入参数网元ID为存在网元ID。                                |
| 140026 | Pod查询参数limit不合法。                 | Pod查询参数limit不合法。                 | 联系华为技术支持处理。                                       |
| 140027 | 根据Pod类型查询Pod时，Pod类型长度必须在3到100之间。 | 根据Pod类型查询Pod时，Pod类型长度必须在3到100之间。 | Pod类型字段长度确保在3到100之间。                              |
| 140028 | 根据Pod名称查询Pod时，Pod名称长度必须在3到100之间。 | 根据Pod名称查询时Pod名称字段长度必须在3到100之间。   | Pod名称字段长度确保在3到100之间。                              |
| 140039 | 查询失败。                            | Pod查询失败，无法连接到PaaS。               | 联系华为技术支持处理。                                       |
| 140040 | 部分查询成功。                          | 全量查询时，部分查询成功。                    | 联系华为技术支持处理。                                       |