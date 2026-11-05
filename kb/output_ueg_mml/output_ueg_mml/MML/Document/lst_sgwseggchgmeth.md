# 查询SGW IMSI/MSISDN Group Charge Method（LST SGWSEGGCHGMETH）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-C**

该命令用于查询SGW基于号段组的计费方式。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

根据需求，查询SGW基于号段组的计费方式：

```
LST SGWSEGGCHGMETH:;
```

```
RETCODE = 0  操作成功。

serving-gateway计费方式配置信息
-------------------------------
IMSI/MSISDN号码段组名称    IMSI/MSISDN号码段组优先级    IMSI/MSISDN号段组离线计费开关

huawei                     10                           禁止                         
test                       5                            允许                         
(结果个数 = 2)
---    END
```

#### 输出结果说明

参见ADD SGWSEGGCHGMETH的参数说明。