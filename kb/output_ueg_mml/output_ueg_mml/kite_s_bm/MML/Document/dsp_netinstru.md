# 查询网络实例对应RU信息(DSP NETINSTRU)

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询网络实例对应RU信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                       |
|:------------|:-------|:-------------------------------------------------------------------------------------------|
| NETINSTNAME | 网络实例名称 | 可选必选说明：可选参数。 参数含义：要查询的网络实例的名称。 数据来源：本端规划。 默认值：无。 取值范围：长度为1～63的字符串。 配置原则：不支持空格和符号'?'，区分大小写。 |

#### 使用实例

查询网络实例NetInstanceDefault对应的RU信息。

```
DSP NETINSTRU: NETINSTNAME="NetInstanceDefault";
```

```
%%DSP NETINSTRU: NETINSTNAME="NetInstanceDefault";%%
RETCODE = 0  操作成功。

结果如下
-------------------------
网络实例名称       网络实例ID     ScaleGroup名称     ScaleGroup ID      RU ID     VNFC类型
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  64        CSLB_VNFC
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  65        CSLB_VNFC
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  65        VNRS_VNFC
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  64        VNRS_VNFC  
(结果个数 = 4)
---    END
```

#### 输出结果说明

| 输出项名称         | 输出项解释                                              |
|:--------------|:---------------------------------------------------|
| 网络实例名称        | 查询的网络实例的名称。 取值范围：字符串类型，长度1~63。                     |
| 网络实例ID        | 查询的网络实例的ID。 取值范围：整数类型，取值范围为0～4。                    |
| ScaleGroup名称  | 查询的网络实例的ScaleGroup名称。 取值范围：字符串类型，长度1~63。           |
| ScaleGroup ID | 查询的网络实例的ScaleGroupID。 取值范围：整数类型，取值范围为0～4294967294。 |
| RU ID         | 查询的网络实例对应RU的ID。 取值范围：整数类型，取值范围为0～4294967294。       |
| VNFC类型        | 查询的网络实例对应RU的VNFC类型。 取值范围：字符串类型，长度1~63。             |