# 查询BGP的错误信息（DSP BGPERRORDISCARD）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询BGP的错误信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                  |
|:--------------|:--------|:------------------------------------------------------------------------------------------------------|
| VRFNAME       | VPN实例名称 | 可选必选说明：可选参数 参数含义：VPN名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| REMOTEADDRESS | 对端地址    | 可选必选说明：可选参数 参数含义：对端地址。 数据来源：对端协商 取值范围：IPv4地址类型。 默认值：无                                                 |
| SOURCEIFNAME  | 多源接口名称  | 可选必选说明：可选参数 参数含义：多源对等体的接口名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：仅支持Ethernet及其子接口类型，不区分大小写。   |

#### 使用实例

查询BGP的错误信息：

```
DSP BGPERRORDISCARD:;
```

```
RETCODE = 0  操作成功。

结果如下
------------------------
BGP的错误信息  =
BGP Discard Info Counts:
Routes received with cluster ID loop : 0
Routes received with as path count over limit : 0
Routes advertised with as path count over limit : 0
Routes received with As loop : 0
Routes received with Zero RD(0:0) : 0
Routes received with no prefix : 0
Routes received with error path-attribute : 0
Routes received with originator ID loop : 0

BGP Discard info:(IPv4 Unicast)
Routes received with cluster ID loop : 0
Routes received with as path count over limit : 0
Routes advertised with as path count over limit : 0
Routes received with As loop : 0
Routes received with Zero RD(0:0) : 0
Routes received with error path-attribute : 0
Routes received with originator ID loop : 0

No discard record.

BGP Discard info:(IPv4 VPNv4)
Routes received with cluster ID loop : 0
Routes received with as path count over limit : 0
Routes advertised with as path count over limit : 0
Routes received with As loop : 0
Routes received with Zero RD(0:0) : 0
Routes received with error path-attribute : 0
Routes received with originator ID loop : 0

No discard record.

(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称    | 输出项解释     |
|:---------|:----------|
| BGP的错误信息 | BGP的错误信息。 |