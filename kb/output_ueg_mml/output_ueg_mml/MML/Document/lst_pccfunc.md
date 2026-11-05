# 查询PCC功能（LST PCCFUNC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用于查询动态PCC功能。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询PCC功能配置参数：

```
LST PCCFUNC:;
```

```
RETCODE = 0  操作成功

PCC功能参数
-----------
						   本地用户PCC功能  =  不使能
						   漫游用户PCC功能  =  不使能
						   拜访用户PCC功能  =  不使能
							  缺省上报级别  =  Rating Group
					  缺省离线计费统计方式  =  流量
				   承载绑定ARP扩展参数开关  =  不使能
			  Pre-emption-Capability缺省值  =  禁止
		   Pre-emption-Vulnerability缺省值  =  允许
								  公共策略  =  PCRF-PCF
					 PCC本端主机名选择模式  =  负荷分担
								本端主机名  =  NULL
						   URL分类集成开关  =  禁止
		   Gx接口不回复UE侧QoS请求时的处理  =  接受请求的QoS
					Monitoring-Key解析方式  =  UNSIGNED32
					   本地PCC策略选择模式  =  本地PCC策略不激活
							N7接口特性列表  =  应用程序检测和控制&网络位置信息&在线报告区域&PendingTransaction&PolicyUpdateWhenUESuspends&RAN侧支持信息&接入网NAS原因值&共享资源&SessionRule失败处理&使用量监控控制
							   选择PCF方式  =  DNN&GPSI&IMSI&PLMN&SNSSAIS
							重定向功能开关  =  使能
					   N7 Failover功能开关  =  允许
						   远端查询PCF开关  =  不使能
						   PCF负荷分担参数  =  根据GroupID负荷分担
 UPF组与Diameter本端主机组的绑定关系组名称  =  NULL
					   优先使用N15 PCF开关  =  不使能
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET PCCFUNC的参数说明。