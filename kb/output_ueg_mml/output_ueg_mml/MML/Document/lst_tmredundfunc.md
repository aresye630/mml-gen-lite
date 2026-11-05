# 查询全局异地容灾配置（LST TMREDUNDFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C**

该命令用来查询全局异地容灾配置。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询全局异地容灾配置：

```
LST TMREDUNDFUNC:;
RETCODE = 0 Operation Success.

Global Redundancy Configuration
-------------------------------
Status Notification Interval = 20
(Number of results = 1)
--- END
```

## 输出结果说明

| 输出项名称    | 输出项解释     |
|:---------|:----------|
| 状态通知时间间隔 | 状态通知时间间隔。 |