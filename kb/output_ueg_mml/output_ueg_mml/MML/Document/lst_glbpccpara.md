# 查询全局PCC参数（LST GLBPCCPARA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询全局PCC配置参数。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询全局PCC配置参数：

```
LST GLBPCCPARA:;
```

```
RETCODE = 0  操作成功

PCC全局参数信息
---------------
                     本地用户动态PCC功能  =  不使能
                     漫游用户动态PCC功能  =  不使能
                     拜访用户动态PCC功能  =  不使能
                    缺省离线计费统计方式  =  流量
                            缺省上报级别  =  Rating Group
                                公共策略  =  PCRF-PCF
                   PCC本端主机名选择模式  =  负荷分担
                              本端主机名  =  NULL
         Pre-emption-Vulnerability缺省值  =  允许
                 承载绑定ARP扩展参数开关  =  不使能
         Gx接口不回复UE侧QoS请求时的处理  =  接受请求的QoS
                  Monitoring-Key解析方式  =  UNSIGNED32
                         URL分类集成开关  =  禁止
            Pre-emption-Capability缺省值  =  禁止
                    选择PCRF/PCF失败动作  =  缺省
 选择PCRF/PCF失败回滚为Local PCC用户类型  =  回滚为本地PCC用户
选择PCRF/PCF失败回滚为RADIUS PCC用户类型  =  回滚为本地PCC用户
                 Initial流程故障处理动作  =  激活失败
  Initial流程故障回滚为Local PCC用户类型  =  回滚为本地PCC用户
 Initial流程故障回滚为RADIUS PCC用户类型  =  回滚为本地PCC用户
                  Update流程故障处理动作  =  继续与PCRF/PCF交互
   Update流程故障回滚为Local PCC用户类型  =  回滚为本地PCC用户
                          N7接口特性列表  =  应用程序检测和控制&网络位置信息&在线报告区域&PendingTransaction&PolicyUpdateWhenUESuspends&RAN侧支持信息&接入网NAS原因值&共享资源&SessionRule失败处理&使用量监控控制
                             选择PCF方式  =  DNN&GPSI&IMSI&PLMN&SNSSAIS
                     本地PCC策略选择模式  =  本地PCC策略不激活
                  流量上报失败时处理动作  =  使用UPDATEFAILACT参数配置
                    Revalidation发送速率  =  25
                          重定向功能开关  =  使能
                     N7 Failover功能开关  =  允许
                         远端查询PCF开关  =  不使能
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET PCCFUNC、SET PCCFAILACTION、SET PCCFLOWCONTROL的参数说明。