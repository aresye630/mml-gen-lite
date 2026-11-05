# 查询DNS IP地址资源列表（LST DNSIPRESOURCE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：CloudEPSN**

该命令用于查询DNS的管理接口和业务接口IP地址资源信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询IP地址资源信息：

```
+++    CloudEPSN/*MEID:0 MENAME:APP-VNF-CloudEPSN-X86-B003_IP60*/        2024-02-20 13:05:02
O&M    #3699
%%LST DNSIPRESOURCE:;
```

```
%%
RETCODE = 0  操作成功

结果如下
--------
接口类型  IP地址类型  IPv4地址列表             IPv6地址列表             

Dns       IPv4        192.168.0.1,192.168.0.2  NULL  
Mgt       IPv4和IPv6  NULL                     NULL                     
(结果个数 = 2)

---    END
```

#### 输出结果说明

参见SET DNSIPRESOURCE的参数说明。