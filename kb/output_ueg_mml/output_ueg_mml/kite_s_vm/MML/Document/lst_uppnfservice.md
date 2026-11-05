# 查询对端NF服务实例信息（LST UPPNFSERVICE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询本地配置的对端NF实例支持的服务实例信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询对端NF的服务实例信息，NF实例标识为LMF\_Instance\_0，服务实例标识为Service\_Instance\_0：

```
LST UPPNFSERVICE:;
```

```
RETCODE = 0  操作成功

对端NF服务实例信息
------------------
NF实例标识                            服务实例标识        服务名称  协议模式  服务实例状态  优先级  容量  负载  

b17ba20e-4524-4ae4-bb70-d33ebf722dcd  Service_instance_0  NamfComm  http      Registered    0       100   0     
b17ba20e-4524-4ae4-bb70-d33ebf722dcd  Service_instance_1  NamfLoc   http      Registered    0       100   0     
f8e93edd-51f2-4197-9506-51f802fc3855  Service_instance_5  NudmUecm  http      Registered    0       100   0     
(结果个数 = 3)

---    END
```

#### 输出结果说明

参见ADD UPPNFSERVICE的参数说明。