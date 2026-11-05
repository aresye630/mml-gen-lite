# 查询API GW HTTP参数（LST APIGWHTTPPARA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、MPF**

该命令用于查询API GW HTTP请求参数。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询API GW HTTP请求参数：

```
LST APIGWHTTPPARA:;
```

```
RETCODE = 0  操作成功

API GW HTTP配置
---------------
会话时长  =  300
超时时间  =  300
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET APIGWHTTPPARA的参数说明。