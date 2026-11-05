# 查询报表服务器状态（DSP RPTSVRSTATUS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

此命令用于查询报表服务器状态。

#### 注意事项

使用ADD RPTSVR添加报表服务器时，当RPTSVRTYPE配置为SUBSCRIPTION，可查询到该链路状态，不受SVRFUNC参数控制。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

假如运营商需要查询报表服务器状态：

```
DSP RPTSVRSTATUS:;
```

```
RETCODE = 0 操作成功

报表服务器状态信息
------------------
报表容器名称    接入点名称    链路状态      IPv4地址       IPv6地址  报表服务器名称   VPN实例名称    端口号       IP类型    报表消息类型
rpt-pod-1       access01      normal       192.168.0.1    ::        und01            test_vpn       10700        IPV4        UFDR     
rpt-pod-1       access02      abnormal     192.168.0.10   ::        und02            test_vpn       10700        IPV4        ADR      
rpt-pod-0       access01      normal       192.168.0.1    ::        und01            test_vpn       10700        IPV4        SUBSCRIPTION     
rpt-pod-0       access02      abnormal     192.168.0.10   ::        und02            test_vpn       10700        IPV4        BASIC

(结果个数 = 4)
--- END
```

#### 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 报表容器名称  | 用于设置报表容器名称。 |
| 链路状态    | 用于设置链路状态。   |
| 报表消息类型  | 报表消息类型。     |

其余输出项请参见ADD RPTSVRADDR的参数说明。