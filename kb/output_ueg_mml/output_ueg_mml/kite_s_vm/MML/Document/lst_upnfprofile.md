# 查询NF实例概述信息（LST UPNFPROFILE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询配置的NF实例概述信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

运营商A需要查询所有NF实例概述信息：

```
LST UPNFPROFILE:;
```

```
RETCODE = 0  操作成功

NF实例概述信息
--------------
NF实例名称       NF类型  NF状态      http地址实例标识  容量  优先级  负载  

GMLC_Instance_0  NfGMLC  Registered  0                 100   0       0     
LMF_Instance_0   NfLMF   Registered  0                 100   0       0     
(结果个数 = 2)

---    END
```

#### 输出结果说明

参见ADD UPNFPROFILE的参数说明。