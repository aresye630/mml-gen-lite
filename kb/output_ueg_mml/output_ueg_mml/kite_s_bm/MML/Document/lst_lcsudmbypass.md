# 查询LCS UDM Bypass配置（LST LCSUDMBYPASS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询系统当前的LCS UDM Bypass配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询LCS UDM Bypass配置：

```
LST LCSUDMBYPASS:;
```

```
RETCODE = 0  操作成功

LCS UDM Bypass配置
----------------------------
 定位流程UDM Bypass开关  =  去使能
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET LCSUDMBYPASS的参数说明。