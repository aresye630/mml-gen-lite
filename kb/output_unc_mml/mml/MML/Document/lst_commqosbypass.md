# 查询BYPASS场景QoS描述的通用配置（LST COMMQOSBYPASS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

该命令用于查询BYPASS场景QoS描述的通用配置。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询BYPASS场景QoS描述的通用配置：

```
%%LST COMMQOSBYPASS:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
General QoS Description Switch  =  DISABLE
             5G User QoS Index  =  0
(Number of results = 1)

---    END
```

## 输出结果说明

| 输出项名称     | 输出项解释                 |
|:----------|:----------------------|
| 通用QoS描述开关 | 该参数用来指定是否开启通用QoS描述开关。 |
| 5G用户QoS索引 | 该参数表示用户QoS索引。         |