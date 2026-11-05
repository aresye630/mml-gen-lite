# 查询UE USAGE TYPE群组成员(LST UEUSGTYPEGPMEM)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

该命令用于查询UE USAGE TYPE群组成员。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称              | 参数说明                                                                   |
|:--------------|:------------------|:-----------------------------------------------------------------------|
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：可选参数 参数含义：该参数用于指定UE USAGE TYPE群组标识。 数据来源：本端规划 取值范围：0~1023 默认值：无 |
| BGNUEUSGTYPE  | 起始UE USAGE TYPE   | 可选必选说明：可选参数 参数含义：该参数用于指定UE USAGE TYPE的起始值。 数据来源：本端规划 取值范围：0~255 默认值：无  |

#### 使用实例

查询“UE USAGE TYPE群组标识”为“1”的UE USAGE TYPE群组成员记录：

LST UEUSGTYPEGPMEM: UEUSGTYPEGPID=1;

```
%%LST UEUSGTYPEGPMEM: UEUSGTYPEGPID=1;%%
RETCODE = 0  操作成功

操作结果如下
--------------
UE USAGE TYPE群组标识  =  1
    起始UE USAGE TYPE  =  100
    终止UE USAGE TYPE  =  120
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**ADD UEUSGTYPEGPMEM**的参数说明。