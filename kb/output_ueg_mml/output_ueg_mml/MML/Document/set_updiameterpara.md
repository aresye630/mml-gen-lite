# 设置Diameter参数（SET UPDIAMETERPARA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF**

该命令用于设置是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送。

如果希望UPF在发送携带Destination-Host AVP的消息时，如果直连路径不存在或直连路径故障，尝试通过Destination-Realm来查找路由发送，则可将该参数使能。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | REALMBASEROUTE   |
|:-------|:-----------------|
| 初始值    | DISABLE          |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称        | 参数说明                                                                                                                             |
|:---------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------|
| REALMBASEROUTE | 基于域名的路由功能开关 | 可选必选说明：可选参数 参数含义：该参数用于控制是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则：无 |

#### 使用实例

UPF在发送携带Destination-Host AVP的消息时，如果不存在到Destination-Host的直连路径，希望按照Destination-Realm来查找路由发送，则需要使能该功能：

```
SET UPDIAMETERPARA:REALMBASEROUTE=ENABLE;
```