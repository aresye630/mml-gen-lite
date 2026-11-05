# 查询自动扩缩容监测的虚机资源（LST SCALELOADMON）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于自动扩缩容场景下，查询监测的虚机资源。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查看自动扩缩容的资源检测项，执行如下命令：

```
%%LST SCALELOADMON:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
scale in/out load resource category  =  SM session memory resource
(Number of results = 1)
```

## 输出结果说明

| 输出项名称       | 输出项解释               |
|:------------|:--------------------|
| 自动扩缩容上报资源种类 | 该参数用于指定自动扩缩容上报资源种类。 |