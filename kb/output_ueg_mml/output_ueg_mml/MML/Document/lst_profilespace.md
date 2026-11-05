# 查询Profile Space（LST PROFILESPACE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

本命令用于查询配置的Profile Space实例。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称            | 参数说明                                                                                                |
|:--------------|:----------------|:----------------------------------------------------------------------------------------------------|
| PROFSPACENAME | Profile Space名称 | 可选必选说明：可选参数 参数含义：该参数用于指定ProfileSpace名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

查询ProfileSpace配置，PROFSPACENAME为“profilespace1”：

```
LST PROFILESPACE:PROFSPACENAME="profilespace1";
```

```
RETCODE = 0  操作成功

Profile Space 信息
------------------
Always Allowed Profile名称  =  userprofile1
         Profile Space名称  =  profilespace1
                拼接开关  =  ENABLE
                拼接字符串  =  NULL
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见ADD PROFILESPACE的参数说明。