# 显示PCRF组状态（DSP PCRFGRPSTATUS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用来查询指定PCRF组状态信息，包括PCRF分组内每个PCRF的通信状态和master/slave状态。

#### 注意事项

- 查询PCRF分组状态信息时，前提条件为PCRFGRPNAME在对象PCRFGROUP中已配置。
- 只有当PCRF绑定到PCRF Group并且PCRF有链路时，才可以查询到PCRF Group状态信息。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                            |
|:------------|:--------|:------------------------------------------------------------------------------------------------|
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数 参数含义：该参数用于指定PCRF分组的名字。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

查询PCRF分组状态信息：PCRFGRPNAME为“testpcrfgrp1”：

```
DSP PCRFGRPSTATUS: PCRFGRPNAME="testpcrfgrp1";
```

```
PCRF组状态
----------
PCRF ID    POD名称               PCRF主机名    Gx 状态    Master/Slave    本端主机名
0          uncpod-0116-30-0-195  host1         Abnormal   Master          gxlocal     
1          uncpod-0116-30-0-195  host4         Abnormal   Slave           gxlocal     
(Number of results = 2)
---    END
```

#### 输出结果说明

| 输出项名称        | 输出项解释              |
|:-------------|:-------------------|
| PCRF ID      | 用于表示PCRF组内的PCRF编号。 |
| POD名称        | 用于表示POD名称。         |
| PCRF主机名      | 用于表示PCRF主机名。       |
| Gx状态         | 用于表示Gx状态。          |
| Master/Slave | 用于表示主备模式。          |