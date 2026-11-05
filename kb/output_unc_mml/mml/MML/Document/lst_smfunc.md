# 查询会话管理扩展功能(LST SMFUNC)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查看会话管理扩展功能信息。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询会话管理扩展功能信息：

LST SMFUNC:;

```
%%LST SMFUNC:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                                                             IPv4v6双栈  =  否
                                                   强制启动间接转发方式  =  是
                                                           拓扑选择开关  =  是
                                                        APN限制功能开关  =  否
                                                    APN限制的去激活方式  =  最大
                                                       PDP/PDN Type策略  =  IPv4
                                          3G到4G切换SGW拓扑选择增强开关  =  否
                                                     切换后时区携带策略  =  是
                                   启用HSS签约的APN级APN-OI-Replacement  =  是
                                             LTE场景相同APN选择网关策略  =  使用接口IP
                                              GU场景相同APN选择网关策略  =  使用接口IP
                                                 PRA状态上报携带ULI开关  =  关
                                              移动性管理流程ULI上报开关  =  关
                                                         NetLoc功能开关  =  开
                                                       获取实时位置开关  =  开
                                                           用户位置类型  =  TAI和ECGI
                                                        IMS连接激活策略  =  拒绝激活
                                                      IMS连接拒绝原因值  =  33
                                                   下发给UE的APN-NI来源  =  纠正后的UE请求的APN-NI
                                                    MME支持ePCO信元处理  =  不支持
                                                       ePCO功能开关(NB)  =  关闭
                                                       ePCO功能开关(WB)  =  关闭
                                               LTE场景NSA选择用户面策略  =  UE能力+签约数据
                                                GU场景NSA选择用户面策略  =  MS能力+签约数据
                                                       是否限制最大速率  =  否
                                            MME支持用户面地址的分开部署  =  不支持
                                  支持LTE接口用户面地址选择策略独立控制  =  否
                                   支持GU接口用户面地址选择策略独立控制  =  否
GTPv2消息ULI信元中Macro eNodeB ID和Extended Macro eNodeB ID支持携带策略  =  NULL
                                                      SR流程SGW选择增强  =  关闭
(结果个数 = 1)

---    END
```

#### 输出结果说明

请参考**SET SMFUNC**命令的参数说明。