# 查询LMF消息控制参数（LST LMFMSGCTRL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询系统当前的超时时间参数，定位算法类型开关状态以及发送Positioning Deactivation消息开关状态等功能。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询LMF消息控制参数：

```
LST LMFMSGCTRL:;
```

```
RETCODE = 0 操作成功

LMF消息控制参数
---------------
                                    Tx定时器时长（秒）  =  3
                         LCS单次定位流程超时时长（秒）  =  3
                                      携带算法类型开关  =  去使能
                  发送Positioning Deactivation消息开关  =  使能
                                  定位结果直接上报开关  =  去使能
                                           TRP功能开关  =  去使能
                                  订阅位置变更消息开关  =  去使能
       低功耗终端LCS Periodic-Triggered Invoke消息开关  =  去使能
                           低功耗终端LPP Abort消息开关  =  去使能
      低功耗终端LPP RequestLocationInformation消息开关  =  去使能
                LMF连续收到EventNotify失败响应消息次数  =  6
               LMF连续未收到MEASUREMENT REPORT消息次数  =  5
                            周期定位Tx定时器时长（秒）  =  6
                              订阅注册状态变更消息开关  =  去使能
 普通终端LCS Periodic-Triggered Invoke消息开关  =  去使能
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET LMFMSGCTRL的参数说明。