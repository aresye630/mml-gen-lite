# 修改标准QoS ID配置（MOD STDQOSID）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于修改标准QoS ID配置。

## 注意事项

- 该命令执行后只对新激活用户生效。

- QOSIDSV-QOSIDEV的取值范围要与EXTENDQCIMAP中配置的EXTENDQCI互斥。同一QOSIDTYPE下，QOSIDSV-QOSIDEV的取值范围不能重叠。同时，配置中的标准QoS ID被EXTENQCIATTR中的EXTQCIMAPDEFQCI或者EXTENDQCIMAP中的STANDARDQCI使用时，修改后的配置需要包含被使用的标准QoS ID。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称          | 参数说明                                                                                                                        |
|:-------------|:--------------|:----------------------------------------------------------------------------------------------------------------------------|
| QOSIDTYPE    | QoS ID类型      | 可选必选说明：必选参数  参数含义：该参数用于指定QoS ID类型。  数据来源：本端规划 取值范围： “QCI（QCI）”：QCI“FIVEQI（5QI）”：5QI  默认值：无  配置原则：无                          |
| QOSIDSV      | QoS ID起始值     | 可选必选说明：必选参数  参数含义：该参数用于指定QoS ID起始值。  数据来源：全网规划  取值范围：整数类型，取值范围是10~255。  默认值：无  配置原则：  该参数的值必须小于等于QoS ID的结束值。                |
| QOSIDEV      | QoS ID结束值     | 可选必选说明：可选参数  参数含义：该参数用于指定QoS ID结束值。  数据来源：全网规划  取值范围：整数类型，取值范围是10~255。  默认值：无  配置原则：  该参数的值必须大于等于QoS ID的起始值。                |
| RESOURCETYPE | 标准QoS ID的资源类型 | 可选必选说明：可选参数  参数含义：该参数用于指定标准QoS ID的资源类型。  数据来源：全网规划 取值范围： NONGBR（指定QoS ID的资源类型为Non-GBR）GBR（指定QoS ID的资源类型为GBR）  默认值：无  配置原则：无 |

## 使用实例

修改“标准QoS ID”配置，“65~66”配置为“标准QCI”：

```
MOD STDQOSID:QOSIDTYPE=QCI,QOSIDSV=65,QOSIDEV=66;
```