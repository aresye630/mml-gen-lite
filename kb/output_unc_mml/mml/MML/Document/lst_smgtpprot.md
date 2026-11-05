# 查询会话管理GTP协议功能参数配置（LST SMGTPPROT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于查询会话管理GTP协议功能参数配置。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询会话管理GTP协议参数配置：

```
%%LST SMGTPPROT:;%%
RETCODE = 0  操作成功

结果如下
--------
                         GTP协议版本  =  GTPV2
                       承载级PCO开关  =  不使能
去活消息携带reactivation-request开关  =  不使能
    透明传输reactivation-request开关  =  使能
              S5S8接口支持多承载开关  =  不使能
               S2b接口支持多承载开关  =  不使能
          NB-IoT场景ePCO信元携带方式  =  协商模式
            不携带MSISDN用户激活策略  =  使能
                      PCO携带QoS开关  =  使能
                          Ppd功能开关 = 不使能
         23G网络侧发起的二次激活开关  =  使能
             LTE到GU专有承载切换开关  =  不使能
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                        | 输出项解释                                                                                                                                                                                                                                                             |
|:-----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GTP协议版本                      | 该参数用于指定GTP协议版本。                                                                                                                                                                                                                                                   |
| 承载级PCO开关                     | 该参数用于配置是否支持承载级PCO处理。配置为ENABLE时，SMF作为PGW、S+PGW发送Create Bearer Rquest/Update Bearer Request消息时支持通过承载级的PCO/ePCO携带相关信息，支持单消息多承载；配置为DISABLE时，SMF作为PGW、S+PGW发送Create Bearer Rquest/Update Bearer Request消息时仅支持通过消息级的PCO携带相关信息，不支持单消息多承载。                                |
| 去活消息携带reactivation-request开关 | 表示去活缺省承载消息携带reactivation-requested标识开关。在异常情况下，用户被删除缺省承载，如果没有及时接入网络，用户被叫失败。配置“去活缺省承载消息携带reactivation-requested标识开关”可以在删除缺省承载时，通过去激活请求消息中的cause值携带reactivation-requested标志要求用户重新接入网络，以达到快速的恢复IMS语音业务的目的，故而建议在配置IMS业务的情况下开启本功能开关。仅适用于SGW-C独立部署，并且SGW-C上没有配置语音APN的场景。 |
| 透明传输reactivation-request开关   | 该参数表示当收到携带cause信元值为“reactivation requested”的Delete Bearer Request消息去活缺省承载时，SGW发送的Delete Bearer Request消息中是否携带cause信元值为“reactivation requested”。仅适用于SGW-C独立部署，并且SGW-C上没有配置语音APN的场景。                                                                                |
| S5S8接口支持多承载开关                | 该参数用于设置S5S8接口支持单个GTP消息携带多个承载功能。                                                                                                                                                                                                                                   |
| S2b接口支持多承载开关                 | 该参数用于设置S2b接口支持单个GTP消息携带多个承载功能。                                                                                                                                                                                                                                    |
| NB-IoT场景ePCO信元携带方式           | 该软参用于控制PGW-C在Create Session Response响应消息中携带ePCO原则。                                                                                                                                                                                                                |
| 不携带MSISDN用户激活策略              | 该参数用于指定UNC是否允许不携带MSISDN的用户激活。 如果SET APNACCESSCTRL中也配置了NULLMSISDN开关，业务流程中会优先使用该开关，不会使用本参数的配置。                                                                                                                                                                      |
| PCO携带QoS开关                   | 该参数用于设置PCO/ePCO是否携带QoS信息。配置为ENABLE时PCO信元携带QoS信息，配置为DISABLE时PCO信元不携带QoS信息。                                                                                                                                                                                         |
| Ppd功能开关                      | 该参数用于指定PPD（寻呼策略差异化）功能开关。                                                                                                                                                                                                                                          |
| 不携带IMSI用户激活策略                | 该参数用于指定是否允许不携带IMSI的用户激活。                                                                                                                                                                                                                                          |
| 23G网络侧发起的二次激活开关              | 该参数用来配置是否开启23G网络侧二次激活功能。                                                                                                                                                                                                                                          |
| LTE到GU专有承载切换开关               | 该参数用来配置LTE切GU场景下，是否允许专有承载进行切换。                                                                                                                                                                                                                                    |
| 4G UL CL功能开关                 | 该参数用来配置是否开启4G UL CL功能。                                                                                                                                                                                                                                            |