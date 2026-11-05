# 显示UAC会话数（DSP UACSESSNUM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示UAC会话数。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                               |
|:------------|:--------|:-----------------------------------------------------------------------------------|
| SESSIONTYPE | 单网通会话类型 | 可选必选说明：必选参数 参数含义：该参数用于指定查询的会话类型。 数据来源：本端规划 取值范围： SINGLENET：查询单网通用户类型。 默认值：无 配置原则：无 |

#### 使用实例

显示UAC会话数：

```
DSP UACSESSNUM: SESSIONTYPE=SINGLENET;
```

```
RETCODE = 0  操作成功

UAC会话数信息
-------------
结果  =  
                           Pod Name = mpfuac-pod-2
         UAC User Session Number(s) = 0
                           Pod Name = mpfuac-pod-1
         UAC User Session Number(s) = 2
                           Pod Name = mpfuac-pod-0
         UAC User Session Number(s) = 1

     All UAC User Session Number(s) = 3
(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释     |
|:--------|:----------|
| 结果      | 用于显示查询结果。 |