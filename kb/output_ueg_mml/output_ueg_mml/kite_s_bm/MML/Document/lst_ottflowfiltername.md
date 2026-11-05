# 查询外置规则库OTT flow filter信息（LST OTTFLOWFILTERNAME）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用来显示通过命令行LOD EXTERNALDB加载的外置OTT数据库中定义的Flow Filter的名称。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

运营商查询本地配置的外置流过滤器实例信息：

```
LST OTTFLOWFILTERNAME:;
```

```
RETCODE = 0 操作成功.

外置OTT flow-filter信息：
------------------------
OTTFlowFilterName
f_im
f_voip

(结果个数 = 2)
```

#### 输出结果说明

| 输出项名称         | 输出项解释            |
|:--------------|:-----------------|
| flow-filter名称 | 该参数用于输出流过滤器实例名称。 |