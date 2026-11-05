# 增加BGP对等体组条件路由匹配前缀（ADD BGPPEERGROUPAFPRE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用于添加BGP对等体组条件路由匹配前缀。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 该命令执行的前提需要BGPPEERGROUPAF中参数DEFAULTRTADVENABLE为TRUE，DEFAULTRTMATCHMODE为match all或match any。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识             | 参数名称            | 参数说明                                                                                                           |
|:-----------------|:----------------|:---------------------------------------------------------------------------------------------------------------|
| VRFNAME          | VPN实例名称         | 可选必选说明：可选参数 参数含义：该参数用于指定VPN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE           | 地址族类型           | 可选必选说明：必选参数 参数含义：该参数用于指定VRF的地址族类型。 数据来源：本端规划 取值范围：枚举类型。 ipv4uni：IPv4地址族。 默认值：无                                 |
| GROUPNAME        | 对等体组名称          | 可选必选说明：必选参数 参数含义：该参数用于指定相应的对等体组。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～47。 默认值：无 配置原则：使用LST BGPPEERGROUP命令查看可用对等体组名。   |
| DEFAULTRTADDRESS | 指定一个缺省路由条件匹配的前缀 | 可选必选说明：必选参数 参数含义：该参数用于指定满足所有条件路由时发送的缺省地址前缀。 数据来源：本端规划 取值范围：IPv4地址类型。 默认值：无                                     |
| DEFAULTRTMASK    | 指定一个缺省路由条件匹配的掩码 | 可选必选说明：必选参数 参数含义：该参数用于指定缺省前缀的掩码长度。 数据来源：本端规划 取值范围：整数类型，取值范围为0～32。 默认值：无 配置原则：和DEFAULTRTADDRESS配合使用。            |

#### 使用实例

为对等体组添加条件路由匹配前缀：

```
SET BGP:ASNUM="100",BGPENABLE=TRUE;
ADD BGPPEERGROUP:VRFNAME="_public_",AFTYPE=public,GROUPNAME="asdf";
MOD BGPPEERGROUPAF:VRFNAME="_public_",AFTYPE=ipv4uni,GROUPNAME="asdf",DEFAULTRTADVENABLE=TRUE,DEFAULTRTMATCHMODE=matchall;
ADD BGPPEERGROUPAFPRE:VRFNAME="_public_",AFTYPE=ipv4uni,GROUPNAME="asdf",DEFAULTRTADDRESS="10.11.11.11",DEFAULTRTMASK=32;
```