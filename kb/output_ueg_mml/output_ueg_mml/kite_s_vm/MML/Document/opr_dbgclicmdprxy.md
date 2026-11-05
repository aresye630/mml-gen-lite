# 通过命令代理执行命令行调试命令（OPR DBGCLICMDPRXY）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令通过命令代理执行命令行调试命令。

#### 注意事项

- 该命令执行后立即生效。
- 该命令用于收集定位信息，需要谨慎执行，请在华为工程师指导下执行。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称    | 参数说明                                                                                                         |
|:----------------|:--------|:-------------------------------------------------------------------------------------------------------------|
| CLICMDSTRING    | 调试命令字符串 | 可选必选说明：必选参数 参数含义：该参数用于指定可以通过命令代理执行的命令行调试命令。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～2048。仅支持单条调试命令。 默认值：无              |
| SERVICEINSTANCE | 服务实例    | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### 使用实例

通过命令代理执行命令行调试命令：

```
OPR DBGCLICMDPRXY: CLICMDSTRING="display ml-string ml-id AB2",SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功
结果如下:
--------
调试命令执行结果返回信息  =  
Warning: Enter diagnose view, return user view with Ctrl+Z.
Info: The diagnose view is used to debug system hardware and software. Misuse of certain commands in this view may affect system performance. Therefore, use these commands with the guidance of Huawei engineers.
ML级别:     3 
测试例不是jitter，pathjitter或icmpjitter类型，不能以毫秒为单位设置interval。
(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称        | 输出项解释             |
|:-------------|:------------------|
| 调试命令执行结果返回信息 | 用于显示调试命令执行结果返回信息。 |