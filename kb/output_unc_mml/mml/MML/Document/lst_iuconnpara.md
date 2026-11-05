# 查询Iu连接控制参数(LST IUCONNPARA)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

该命令用于查询Iu连接控制参数。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询IUCONNPARA参数：

LST IUCONNPARA:;

```
%%LST IUCONNPARA:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------
   Follow on without PDP场景Iu连接管理 (s)  =  10
      Follow on with PDP场景Iu连接管理 (s)  =  10
No follow on without PDP场景Iu连接管理 (s)  =  0
   No follow on with PDP场景Iu连接管理 (s)  =  0
                      SMS流程Iu连接管理(s)  =  65535
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**SET IUCONNPARA**的参数说明。