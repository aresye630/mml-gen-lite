# 显示Throttling信息（DSP THROTTLINGINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C**

该命令用于查看包含指定对端MME地址的路径下的DDN Throttling信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识        | 参数名称     | 参数说明                                                                                                                        |
|:------------|:---------|:----------------------------------------------------------------------------------------------------------------------------|
| IPVERSION   | 对端IP地址类型 | 可选必选说明：必选参数  参数含义：该参数用于指定对端IP地址类型。  数据来源：本端规划  取值范围：枚举类型。 “IPV4（IPv4）”：表示地址类型为IPv4。“IPV6（IPv6）”：表示地址类型为IPv6。  默认值：无  配置原则：无 |
| IPV4ADDRESS | 对端IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。  参数含义：该参数用于指定对端的IPv4地址。  数据来源：本端规划  取值范围：IPv4地址类型。  默认值：无  配置原则：无                  |
| IPV6ADDRESS | 对端IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。  参数含义：该参数用于指定对端IPv6地址。  数据来源：本端规划  取值范围：IPv6地址类型。  默认值：无  配置原则：无                   |

## 使用实例

显示对端MME地址为10.194.39.226的Throttling信息：

```
DSP THROTTLINGINFO: IPVERSION=IPV4, IPV4ADDRESS="10.194.39.226";
RETCODE = 0  操作成功

Throttling Information
----------------------
                                PeerAddr = 10.194.39.226
                               LocalAddr = 10.135.21.2
                DDN Throttling StartTime = 2016-09-09 17:55:25
                  DDN Throttling EndTime = 2016-09-10 03:55:25
                 DDN Throttling Delay(s) = 36000
                   DDN Throttling Factor = 100
    Number of High Priority DDN Received = 180
     Number of Low Priority DDN Received = 50
    Number of Low Priority DDN Discarded = 50
  Number of Lowest Priority DDN Received = 20
 Number of Lowest Priority DDN Discarded = 20
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称               | 输出项解释                        |
|:--------------------|:-----------------------------|
| 对端地址                | 该参数用于显示对端地址。                 |
| 本端地址                | 该参数用于显示本端地址。                 |
| DDN Throttling开始时间  | 该参数用于显示DDN Throttling的开始时间。  |
| DDN Throttling结束时间  | 该参数用于显示DDN Throttling的结束时间。  |
| DDN Throttling延迟(秒) | 该参数用于显示DDN Throttling的延迟(秒)。 |
| DDN Throttling因子    | 该参数用于显示DDN Throttling因子。     |
| 高优先级DDN接收数          | 该参数用于显示高优先级DDN接收数。           |
| 低优先级DDN接收数          | 该参数用于显示低优先级DDN接收数。           |
| 低优先级DDN丢弃数          | 该参数用于显示低优先级DDN丢弃数。           |
| 最低优先级DDN接收数         | 该参数用于显示最低优先级DDN接收数。          |
| 最低优先级DDN丢弃数         | 该参数用于显示最低优先级DDN丢弃数。          |