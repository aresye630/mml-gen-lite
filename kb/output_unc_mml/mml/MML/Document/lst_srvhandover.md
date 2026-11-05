# 查询业务切换策略(LST SRVHANDOVER)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

该命令用于查询业务切换策略信息。切换策略控制就是根据业务级别、用户级别确定用户在2G和3G网络中的切换策略，来引导2G和3G的网络业务承载和网络负荷。切换策略可以由运营商配置。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:-------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRVLVL | 业务级别   | 可选必选说明：可选参数 参数含义：该参数需根据用户PDP上下文QoS中的流量等级（Traffic class）、下行保证速率（Guaranteed bit rate for downlink）和发送控制优先级（Traffic handling priority）确定。 取值范围：“CONVERSATION(Conversation)”：流量等级为Conversational class。“STREAMINGGBRMORE25KBPS(StreamGBRMore25kbps)”：流量等级为Streaming class，下行保证速率大于等于25kbit/s。“STREAMINGGBRLESS24KBPS(StreamGBRLess24kbps)”：流量等级为Streaming class，下行保证速率小于24kbit/s。“INTERACTIVETRAFFICPRI1(InteractiveTrafficPri1)”：流量等级为Interactive class，发送控制优先级为1。“INTERACTIVETRAFFICPRI2(InteractiveTrafficPri2)”：流量等级为Interactive class，发送控制优先级为2。“INTERACTIVETRAFFICPRI3(InteractiveTrafficPri3)”：流量等级为Interactive class，发送控制优先级为3。“BACKGROUND(Background)”：流量等级为Background class。 默认值：无 |
| USRPRI | 用户级别   | 可选必选说明：可选参数 参数含义：待查询的用户签约QoS属性中的分配保留优先级（Allocation/Retention Priority）。 取值范围： “HIGHLEVELUSER(高端用户)”：分配/保留优先级为1。“NORMALUSER(普通用户)”：分配/保留优先级为2。“LOWLEVELUSER(低端用户)”：分配/保留优先级为3。“NONE(None)”：通用用户级别，表示该用户没有用户级别，设置的门限就是该业务级别所有用户级别的切换策略。 默认值：无  说明： 在相同业务级别下，配置不同的用户级别，其中配置了“通用用户级别”，表示在相同的业务级别下，对已配置用户级别之外的所有用户级别都使用“通用用户级别”的策略。                                                                                                                                                                                                                                                                                                                                                           |

#### 使用实例

查询业务级别为“BACKGROUND(Background)”，用户级别为“HIGHLEVELUSER(高端用户)”的业务切换策略：

```
%%LST SRVHANDOVER:SRVLVL=BACKGROUND, USRPRI=HIGHLEVELUSER;%%
RETCODE = 0  操作成功。

业务切换配置表
--------------
                 业务级别  =  Background
                 用户级别  =  高端用户
        WCDMA业务切换策略  =  建议切换到GPRS
         GPRS业务切换策略  =  建议切换到WCDMA
(结果个数 = 1)

---    END
```

#### 输出结果说明

请参考**ADD SRVHANDOVER**命令的参数标识。