# 设置LDP BFD配置（SET LDPBFD）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用于设置LDP BFD配置。使能LDP BFD功能后，可以对LDP Tunnel进行快速的故障检测，提高整网可靠性。

#### 注意事项

- 该命令执行后立即生效。
- 可选参数至少选一项。
- 配置该命令前，需要通过SET MPLSSITE全局使能MPLS能力。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| LDPBFDENABLE   | LDPBFDTRIGGERTUNNEL   |   DETCTMULTFORTNL |
|:---------------|:----------------------|------------------:|
| False          | NONE                  |                 3 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识                | 参数名称                               | 参数说明                                                                                                                                                                                    |
|:--------------------|:-----------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LDPBFDENABLE        | LDP BFD能力                          | 可选必选说明：可选参数 参数含义：该参数用于指定LDP BFD能力。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无 配置原则：配置该参数前，需要通过SET BFD全局使能BFD能力。                                                                    |
| LDPBFDTRIGGERTUNNEL | BFD For LDP Tunnel触发策略             | 可选必选说明：可选参数 参数含义：该参数用于指定检测LDP Tunnel的BFD触发策略。 数据来源：本端规划 取值范围：枚举类型。 NONE：无触发策略。HOST：触发方式为主机地址。FEC_LIST：触发方式为FEC列表。IP_PREFIX：触发方式为IP前缀列表。 默认值：无 配置原则：配置该参数前，需要通过SET BFD全局使能BFD能力。         |
| TUNNELIPPREFIXNAME  | BFD For LDP Tunnel的IP前缀名称          | 可选必选说明：条件必选参数 前提条件：该参数在“LDPBFDTRIGGERTUNNEL”配置为“IP_PREFIX”时为必选参数。 参数含义：该参数用于指定IP前缀名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～169。 默认值：无 配置原则：所用的IP前缀名需提前配好。通过LST PREFIXFILTERNODE查看当前已存在的IP前缀列表。 |
| TNLFECLISTNAME      | BFD For LDP Tunnel FEC列表名称         | 可选必选说明：条件必选参数 前提条件：该参数在“LDPBFDTRIGGERTUNNEL”配置为“FEC_LIST”时为必选参数。 参数含义：该参数用于指定FEC列表的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：所用的FEC列表名称需提前配好。通过LST LDPFECLIST查看当前已存在的FEC列表。      |
| MINTXINTVFORTNL     | BFD For LDP Tunnel的BFD最小发送时间间隔（ms） | 可选必选说明：可选参数 参数含义：该参数用于指定BFD会话最小发送时间间隔。 数据来源：本端规划 取值范围：整数类型，取值范围为30～1000。 默认值：无 配置原则：如果不配置此参数，则实际生效值为200。可以通过DSP BFDSESSION查看。                                                           |
| MINRXINTVFORTNL     | BFD For LDP Tunnel的BFD最小接收时间间隔（ms） | 可选必选说明：可选参数 参数含义：该参数用于指定BFD会话最小接收时间间隔。 数据来源：本端规划 取值范围：整数类型，取值范围为30～1000。 默认值：无 配置原则：如果不配置此参数，则实际生效值为200。可以通过DSP BFDSESSION查看。                                                           |
| DETCTMULTFORTNL     | BFD For LDP Tunnel的BFD可容忍丢失次数      | 可选必选说明：可选参数 参数含义：该参数用于指定BFD会话可容忍丢失次数。如果BFD会话在设置的检测周期内没有收到对端发来的BFD报文，则认为链路发生了故障，BFD会话的状态将会置为Down。 数据来源：本端规划 取值范围：整数类型，取值范围为3～50。 默认值：无 配置原则：如果不配置此参数，则实际生效值为3。可以通过DSP BFDSESSION查看。      |

#### 使用实例

设置LDP BFD配置：

```
SET LDPBFD:LDPBFDENABLE=TRUE,LDPBFDTRIGGERTUNNEL=HOST,MINTXINTVFORTNL=45,MINRXINTVFORTNL=45,DETCTMULTFORTNL=40;
```