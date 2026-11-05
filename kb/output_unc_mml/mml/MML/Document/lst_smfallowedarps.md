# 查询5G用户允许的ARP列表（LST SMFALLOWEDARPS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

该命令用于查询5G用户允许的ARP列表。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识     | 参数名称    | 参数说明                                                                                      |
|:---------|:--------|:------------------------------------------------------------------------------------------|
| QOSINDEX | 用户QOS索引 | 可选必选说明：可选参数  参数含义：该参数表示允许用户接入的ARP列表索引。  数据来源：本端规划  取值范围：整数类型，取值范围是0~65535。  默认值：无  配置原则：无 |

## 使用实例

如果想查询所有的5G用户允许的ARP列表，执行如下命令:

```
%%LST SMFALLOWEDARPS:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
          QOSINDEX  =  2
ARP Priority Level  =  ARP Priority Level 1&ARP Priority Level 2&ARP Priority Level 3&ARP Priority Level 4&ARP Priority Level 5&ARP Priority Level 6&ARP Priority Level 7&ARP Priority Level 8&ARP Priority Level 9&ARP Priority Level 10&ARP Priority Level 11&ARP Priority Level 12&ARP Priority Level 13&ARP Priority Level 14&ARP Priority Level 15
ARP Priority Level  =  NULL
           ARP PVI  =  NULL
(Number of results = 1)

---    END
```

## 输出结果说明

| 输出项名称     | 输出项解释                    |
|:----------|:-------------------------|
| 用户QOS索引   | 该参数表示允许用户接入的ARP列表索引。     |
| ARP的优先级别  | 该参数用于指定组成QoS控制的ARP优先级。   |
| ARP的抢占能力  | 该参数用于指定组成QoS控制的ARP抢占能力。  |
| ARP的被抢占能力 | 该参数用于指定组成QoS控制的ARP被抢占能力。 |