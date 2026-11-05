# 查询基于IMEI选择GGSN/P-GW配置(LST GWSELBYIMEI)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询基于IMEI选择GGSN/P-GW配置记录。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称     | 参数说明                                                                                  |
|:---------|:---------|:--------------------------------------------------------------------------------------|
| IMEIGPID | IMEI群组标识 | 可选必选说明：可选参数 参数含义：该参数用于指示IMEI群组标识，UNC需要为这些类型终端选择特定GGSN/P-GW。 数据来源：本端规划 取值范围：1~50 默认值：无 |

#### 使用实例

查询IMEI群组标识为1的基于IMEI选择P-GW/GGSN配置：

LST GWSELBYIMEI: IMEIGPID=1;

```
%%LST GWSELBYIMEI:IMEIGPID=1;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
IMEI群组标识  =  1
    定制标识  =  CAT6
(结果个数 = 1)

---    END
```

查询所有基于IMEI选择P-GW/GGSN配置：

LST GWSELBYIMEI:;

```
%%LST GWSELBYIMEI:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
IMEI群组标识  =  1
    定制标识  =  CAT6
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**ADD GWSELBYIMEI**的参数说明。