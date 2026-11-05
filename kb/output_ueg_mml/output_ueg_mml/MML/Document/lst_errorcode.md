# 查询错误码（LST ERRORCODE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

此命令用于显示配置错误码信息。

#### 注意事项

- 该命令执行后立即生效。
- 输入ERRORCODENAME查询指定记录，如果不输入ERRORCODENAME表示查询所有记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                                         |
|:--------------|:-------|:---------------------------------------------------------------------------------------------|
| ERRORCODENAME | 错误码名称  | 可选必选说明：可选参数 参数含义：该参数用于设置错误码配置名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。 默认值：无 配置原则：无 |

#### 使用实例

查询所有错误码：

```
LST ERRORCODE:;
```

```
%%LST ERRORCODE:;%%
RETCODE = 0  Operation succeeded

Error Code
----------
Error Code Name  Error Code Range Operation  Error Code Start Value  Error Code End Value  

e1               Less Than or Equal To       0                       10                    
testerrorcode    Less Than or Equal To       0                       5                     
(Number of results = 2)
```

#### 输出结果说明

参见ADD ERRORCODE的参数说明。