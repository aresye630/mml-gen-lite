# 查询QosGlobal配置（LST QOSGLOBAL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于显示全局的QoS信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询QosGlobal配置：

```
LST QOSGLOBAL:;
```

```
RETCODE = 0  操作成功。

全局QoS配置信息
---------------
                      QoS功能开关  =  不使能
               下行与上行带宽比例  =  3
    具有最高优先级的non-GBR QCI值  =  5
                    Qos Profile名  =  globalqos
具有最高优先级的non-GBR PTT QCI值  =  69
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见SET QOSGLOBAL的参数说明。