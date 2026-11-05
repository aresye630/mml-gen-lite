# 查询SGSN/MME选择策略(LST PESELPLCY)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询SGSN/MME选择策略。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询SGSN/MME选择策略。

**LST PESELPLCY:;**

```
%%LST PESELPLCY:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
对等网元识别模式  =  掩码模式
        比特掩码  =  0x8000
    MME Group ID  =  0x0
MME Group ID范围  =  0x0
  使用RNC ID域名  =  YES
     使用ID TYPE  =  YES
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见 **SET PESELPLCY**的参数说明。