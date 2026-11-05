# 查询QOS测量IP地址对(LST QOSIP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于查询QoS测量的IP地址对数据，查询的结果显示所有的QoS IP地址对信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询QoS IP地址对：

```
LST QOSIP:;
```

```
%%LST QOSIP:;%%
RETCODE = 0  操作成功

操作结果如下
----------
 IP地址类型  本端IP地址         对端IP地址        本端IPV6地址         对端IPV6地址      

 IPV4        192.168.165.198    192.168.165.199   NULL                 NULL                 
 IPV4        10.2.2.5           10.2.2.6          NULL                 NULL                 
 IPV6        NULL               NULL              fc00:1:0:1:1:0:1:11  fc00:3:0:33:3:3:33:FFFF
 IPV6        NULL               NULL              fc00:2:E:E:B:0:0:0   fc00:D:D:D3:3:3:3:321   
(结果个数 = 4)

---    END
```