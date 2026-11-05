# 查询零流量计费事件忽略开关（LST ZEROCHGSKIPSW）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于显示零流量计费事件忽略开关。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

要显示零流量计费事件忽略开关：

```
LST ZEROCHGSKIPSW:;
```

```
RETCODE = 0  操作成功。

零流量计费事件忽略配置
----------------
                       零流量计费事件忽略总开关  =  ENABLE
                                    忽略RAT更新  =  DISABLE
                       忽略Serving Node地址改变  =  DISABLE
                                 忽略MS时区改变  =  DISABLE
                  忽略Serving Node PLMN标识改变  =  DISABLE
                                   忽略时间阈值  =  DISABLE
                                       忽略CCFH  =  DISABLE
                                 忽略去激活话单  =  ENABLE
        忽略PS-Furnish-Charging-Information改变  =  DISABLE
                               忽略强制生成话单  =  ENABLE
                   忽略基于位置的计费订阅和取消  =  DISABLE
                                    忽略QoS改变  =  DISABLE
                                    忽略ULI改变  =  DISABLE
                                   忽略费率切换  =  DISABLE
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见SET ZEROCHGSKIPSW的参数说明。