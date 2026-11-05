# 查询QoS Flow功能（LST QOSFLOWFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

该命令用于查询QoS Flow相关功能。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询QoS Flow功能，执行如下命令：

```
LST QOSFLOWFUNC:;
RETCODE = 0  操作成功

结果如下
--------
 EPS切换到5GS专有GBR类型QoS Flow策略  =  释放专有QoS Flow
插入删除I-SMF专有GBR类型QoS Flow策略  =  不释放专有QoS Flow
 延迟释放专有GBR类型QoS Flow时长(秒)  =  10
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                      | 输出项解释                                                                                                                                      |
|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| EPS切换到5GS专有GBR类型QoS Flow策略 | 该参数用于指定当从EPS切换到5GS携带专有QoS Flow但是没有激活用户面时，专有QoS Flow的处理策略。                                                                                  |
| 插入删除I-SMF专有GBR类型QoS Flow策略 | 该参数用于指定当插入I-SMF时，I-SMF获取到的上下文中包含专有GBR类型QoS Flow但是没有激活用户面时专有QoS Flow的处理策略；或者当删除I-SMF时，A-SMF的上下文中包含专有GBR类型QoS Flow但是没有激活用户面时专有QoS Flow的处理策略。 |
| 延迟释放专有GBR类型QoS Flow时长(秒)   | 该参数用于指定专有GBR类型QoS Flow延时释放时长。当ESPTO5GSQFPLCY或者ISMFQFPLCY设置为DELAY_RELASE时，本参数生效。                                                            |