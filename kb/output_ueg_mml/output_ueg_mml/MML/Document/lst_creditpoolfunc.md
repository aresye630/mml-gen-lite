# 查询Credit Pooling功能（LST CREDITPOOLFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、GGSN**

该命令用以查询配置的Credit Pooling功能参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询配置的Credit Pooling特性功能参数，执行如下命令：

```
%%LST CREDITPOOLFUNC:;%%
RETCODE = 0  操作成功
结果如下
------------------------
          Credit Pooling功能开关 = DISABLE  
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称              | 输出项解释                      |
|:-------------------|:---------------------------|
| Credit Pooling功能开关 | 该参数用于配置Credit Pooling功能开关。 |