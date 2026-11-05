# 增加BGP多源对等体（ADD BGPMULTIPEER）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用于创建BGP多源对等体。当需要支持多个接口处理单元上的同网段IP地址与远端的同一个IP地址建立多个对等体关系时，可以执行此命令。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为32768。
- 该命令依赖于ADD BGPPEER。
- 在私网下增加BGP多源对等体时候，BGP对等体必须存在并且地址族类型为noaf。
- 该命令执行前需要执行ADD BGPPEER或MOD BGPPEER命令指定本端对等体连接方式为只连接，即参数CONNECTMODE取枚举值connectOnly。
- 该命令执行前需要执行ADD BGPPEERAF或MOD BGPPEERAF命令指定本端多源对等体路由只迭代源接口，即参数ISSOURELAYNEIGHINTER取值为TRUE。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称    | 参数说明                                                                                                                                            |
|:-------------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| VRFNAME      | VPN实例名称 | 可选必选说明：可选参数 参数含义：该参数用于指定VPN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_                                                                 |
| PEERADDR     | 对等体地址   | 可选必选说明：必选参数 参数含义：该参数用于指定建立对等体的接口地址。 数据来源：对端协商 取值范围：IPv4地址类型。 默认值：无                                                                              |
| SOURCEIFNAME | 源接口名称   | 可选必选说明：必选参数 参数含义：该参数用于指定建立对等体的源接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：仅支持Ethernet及其子接口类型，不区分大小写。                                    |
| ISIGNORE     | 是否忽略    | 可选必选说明：可选参数 参数含义：该参数用于指定是否忽略与指定对等体建立会话。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：FALSE 配置原则：一旦配置为TRUE，会中断邻居，且以后再也无法建立连接，BGP多源对等体状态显示为Idle。 |

#### 使用实例

增加BGP多源对等体：

```
SET BGP:ASNUM="100",BGPENABLE=TRUE;
ADD L3VPNINST:VRFNAME="vrf1";
ADD VPNINSTAF:VRFNAME="vrf1",AFTYPE=ipv4uni;
ADD BGPVRF:VRFNAME="vrf1";
ADD BGPPEER:VRFNAME="vrf1",ADDRESSTYPE=noaf,PEERADDR="10.2.2.2",REMOTEAS="100";
ADD BGPMULTIPEER:VRFNAME="vrf1",PEERADDR="10.2.2.2",SOURCEIFNAME="Ethernet66/0/3";
```