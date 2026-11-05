# 查询DDN消息参数以及Delay信元处理开关（LST DDNATTR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C**

该命令用来查询Downlink Data Notification消息中是否支持携带EBI和ARP信元，以及控制SGW-C是否基于DownlinkData Notification Ack消息和Modify Bearer Request消息中的Delay信元进行处理。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询Downlink Data Notification消息中的是否支持携带EBI和ARP信元，以及SGW-C是否支持对DownlinkData Notification Ack消息和Modify Bearer Request消息中Delay信元进行处理：

```
%%LST DDNATTR:;%%
RETCODE = 0  操作成功

结果如下
--------
          携带EBI  =  不使能
            EBI值  =  触发DDN消息的承载
          携带ARP  =  不使能
            ARP值  =  触发DDN消息的承载
Delay信元处理开关  =  关闭
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称       | 输出项解释                                                                                                                                 |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| 携带EBI       | 设置系统是否支持在Downlink Data Notification消息中携带EBI信元。                                                                                        |
| EBI值        | 设置Downlink Data Notification消息中的EBI信元取值原则。                                                                                            |
| 携带ARP       | 设置系统是否支持在Downlink Data Notification消息中携带ARP信元。                                                                                        |
| ARP值        | 设置Downlink Data Notification消息中的ARP信元取值原则。                                                                                            |
| Delay信元处理开关 | 该参数用于控制SGW-C是否支持对DownlinkData Notification Ack消息和Modify Bearer Request消息中Delay信元进行处理。如果支持处理，SGW-C会指示SGW-U针对本MME-SGW所在路径所有用户会话延迟发送DDN。 |