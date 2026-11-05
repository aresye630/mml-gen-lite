# 查询EIR配置(LST EIR)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

此命令用于查询EIR（Equipment Identity Register）表记录。MME（Mobility Management Entity）根据EIR表记录选择EIR。

#### 注意事项

此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询系统内EIR表记录：

LST EIR:;

```
%%LST EIR:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
            EIR域名  =  example01.com
          EIR主机名  =  example01.com
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见**ADD EIR**的参数说明。