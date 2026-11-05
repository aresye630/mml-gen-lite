# 查询L2TP组的LNS信息（LST L2TPLNSINFO）

- 命令功能
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

用于查询L2TP组绑定的LNS信息。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                             |
|:--------|:-------|:-------------------------------------------------------------------------------------------------|
| GROUPID | L2TP组号 | 可选必选说明：可选参数 参数含义：指定L2TP组号。 数据来源：本端规划 取值范围：整数类型，取值范围为1～1500。 默认值：无 配置原则：该参数使用ADD L2TPGROUP命令配置生成。 |
| LNSNO   | LNS序号  | 可选必选说明：可选参数 参数含义：该参数用于指定添加LNS的序号。 数据来源：本端规划 取值范围：整数类型，取值范围为1～30。 默认值：无 配置原则：无                    |

#### 使用实例

查询L2TP组绑定的LNS信息：

```
LST L2TPLNSINFO:;
```

```
RETCODE = 0 操作成功。

RETCODE = 0  Operation succeeded

L2tp Group Lns Info
----------------------
                   L2TP Group ID  =  1
             LNS Sequence Number  =  1
                   Lns IP version = IPV4
                 LNS IPv4 Address = 10.1.1.1
                 LNS IPv6 Address = ::
                     LNS Password = *****
             Confirm LNS Password = *****
(Number of results = 1)

--- END
```

#### 输出结果说明

参见ADD L2TPLNSINFO的参数说明。