# 显示RTSDNN参数（LST RTSDNNPARA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

查询通用DNN漫游分流参数。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

使用LST RTSDNNPARA命令查询通用DNN漫游分流参数：

```
LST RTSDNNPARA:;
```

```
RETCODE = 0  Operation succeeded

RTSDNN Parameter
-----------------
                                       Public Network Switch  =  DISABLE
                                      Private Network Switch  =  DISABLE
                                       IPv4 NAT ALG Protocol  =  FTP Protocol&RTSP Protocol
                                       IPv6 NAT ALG Protocol  =  FTP Protocol
              Flow Control Interval for MultiDNN Reports (s)  =  2
                                         Actions for Packets  =  Discard
                     UE IP Address Conflict Detection Switch  =  ENABLE
                           UE IP Address Reallocation Switch  =  ENABLE
                Maximum Number of UE IP Address Reassignment  =  1000
                   Handling Policy on UE IP Address Conflict  =  BYPASS
            Check Interval for the Campus Resource Threshold  =  240
General DNN-based Roaming Traffic Steering Reporting over N4  =  ENABLE
(Number of results = 1)

---    END
```

#### 输出结果说明

参见SET RTSDNNPARA的参数说明。