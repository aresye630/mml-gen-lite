# 查询Diameter兼容配置(LST DMCMPT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询Diameter兼容配置。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询Diameter兼容配置，运行如下命令：

```
LST DMCMPT:;
```

```
%%LST DMCMPT:;%%
RETCODE = 0  操作成功。

输出结果如下
------------
    是否支持UE-SRVCC-Capability信元  =  支持
                           特性列表  =  UE可达通知
                          特性列表2  =  NULL
                        P-GW ID类型  =  MIP-Home-Agent-Host
              切换后P-GW ID更新策略  =  不更新
                    NOR消息更新参数  =  IMS VoPS参数
                  S6a/S6d-Indicator  =  融合SGSN/MME支持
Homogeneous Support of IMS VoPS信元  =  按照设备能力携带
                   用户能力匹配模式  =  快速匹配
           不允许IMS VoPS的用户处理  =  携带NOT SUPPORT
 T-ADS查询结果与IMS PDN连接状态相关  =  否
                  是否支持NBIoT RAT  =  不支持
                 支持上报的状态列表  =  NULL
                     T6接口特性列表  =  NULL
             未签约DCNR是否允许DCNR  =  否
        是否支持NOR消息上报RAT TYPE  =  不支持
        是否支持LTE-M类型的RAT TYPE  =  NULL
            EPS FB后P-GW ID更新策略  =  不更新
     是否支持UE-DCNR-Capability信元  =  不支持
        是否支持AMF Instance ID信元  =  不支持
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见**SET DMCMPT**的参数标识。