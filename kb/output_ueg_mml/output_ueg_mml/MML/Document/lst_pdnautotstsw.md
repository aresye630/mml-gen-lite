# 查询PDN自动探测开关状态（LST PDNAUTOTSTSW）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

查询PDN自动探测开关状态。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询PDN自动探测开关状态：

```
LST PDNAUTOTSTSW:;
```

```
RETCODE = 0  Operation succeeded

PDN自动探测开关状态
------------------------
PDN Route Auto Test Switch  =  ENABLE
Dns Kpi Fault Test Switch = ENABLE
Path Fault Tracert Test Switch = ENABLE
(结果个数 = 1)
```

#### 输出结果说明

| 输出项名称                          | 输出项解释            |
|:-------------------------------|:-----------------|
| PDN Route Auto Test Switch     | PDN路由自动测试开关。     |
| Dns Kpi Fault Test Switch      | DNS KPI故障自动探测开关。 |
| Path Fault Tracert Test Switch | 路径故障Tracert开关。   |