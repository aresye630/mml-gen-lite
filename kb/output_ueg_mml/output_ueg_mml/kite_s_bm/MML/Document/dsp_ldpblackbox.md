# 显示LDP记录的黑匣子信息（DSP LDPBLACKBOX）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示LDP记录的黑匣子信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称         | 参数说明                                                                                                                                                                                               |
|:----------------|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| COMPTYPE        | 组件类型         | 可选必选说明：必选参数 参数含义：该参数用于表示组件类型。 数据来源：本端规划 取值范围：枚举类型。 NEIGH_MANAGER：邻居管理组件。SESS_MANAGER：会话管理组件。LSP_MANAGER：LSP管理组件。 默认值：无                                                                             |
| BLACKBOXTYPE    | 黑匣子类型        | 可选必选说明：条件必选参数 前提条件：该参数在“COMPTYPE”配置为“NEIGH_MANAGER” 或 “SESS_MANAGER”时为必选参数。 参数含义：该参数用于表示黑匣子类型。 数据来源：本端规划 取值范围：枚举类型。 LOCAL：本地信息。COMPONENT：指定组件的信息。SESSION：会话信息。 默认值：无                               |
| LSPBLACKBOXTYPE | LDPM组件的黑匣子类型 | 可选必选说明：条件必选参数 前提条件：该参数在“COMPTYPE”配置为“LSP_MANAGER”时为必选参数。 参数含义：该参数用于表示LDPM组件的黑匣子类型。 数据来源：本端规划 取值范围：枚举类型。 LOCAL：本地信息。COMPONENT：指定组件的信息。 默认值：无                                                        |
| COMPONENTID     | 组件PID或CID    | 可选必选说明：条件必选参数 前提条件：该参数在“BLACKBOXTYPE”配置为“COMPONENT”时为必选参数。 可选必选说明：条件必选参数 前提条件：该参数在“LSPBLACKBOXTYPE”配置为“COMPONENT”时为必选参数。 参数含义：该参数用于表示组件PID或CID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无 |

#### 使用实例

显示LDP的会话管理组件记录的本地信息：

```
DSP LDPBLACKBOX:COMPTYPE=SESS_MANAGER,BLACKBOXTYPE=COMPONENT,COMPONENTID="0x80810086";
```

```
RETCODE = 0  操作成功。

结果如下
--------
LDPM组件记录的黑匣子信息

[M] [11- 7  9:24:13]:[PDPWE3 Comp]Send msg to pwe3, OP: 0, SN: 1, Ret: 0

[M] [11- 7  9:25: 9]:[PDPWE3 Comp]Send msg to pwe3, OP: 6, SN: 2, Ret: 0

[M] [11- 7  9:25: 9]:[PDPWE3 Comp]LDC send PWE3 batch backup end ACK

[M] [11- 7  9:25:14]:[PDPWE3 Comp]Send msg to pwe3, OP: 9, SN: -1, Ret: 0

[M] [11- 7  9:25:14]:[PDPWE3 Comp]Receive pwe3 out msg bd req ack

[M] [11- 7  9:25:14]:[PDPWE3 Comp]Receive pwe3 out msg bd end

[M] [11- 7  9:25:14]:[PDPWE3 Comp]Send msg to pwe3, OP: 10, SN: 3, Ret: 0
(结果个数 = 7)
---    END
```

#### 输出结果说明

| 输出项名称          | 输出项解释               |
|:---------------|:--------------------|
| LDPM组件记录的黑匣子信息 | 用于表示LDPM组件记录的黑匣子信息。 |