# 设置调测日志开关（SET FEILOGSWITCH）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用来打开和关闭调测日志的功能。

调测日志开关默认是关闭的。

在需要定位转发异常时，打开该开关可以辅助定位，但打开开关后，对性能有一定的影响。

建议保持该开关为默认的关闭状态。

#### 注意事项

- 该命令执行后立即生效。
- 该命令不支持配置导出。
- 该命令仅适用于NP卡加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:-----------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MODULENAME | 模块名    | 可选必选说明：必选参数 参数含义：该参数用于指定模块名称。 数据来源：本端规划 取值范围：枚举类型。 BFD：BFD。 BFDEVENT：BFD-EVENT。 CPUDEFEND：CPU-DEFEND。 FEIIPSEC：FEI-IPSEC。 FIM：FIM。 FIMSTAT：FIM-STAT。 FRAME：FRAME。 FRAMEERROR：FRAME-ERROR。 FRAMEMESSAGE：FRAME-MESSAGE。 FRAMEPERFORMANCE：FRAME-PERFORMANCE。 FWDSMOOTH：FWD-SMOOTH。 GRE：GRE。IPTRACE：IP-TRACE。 IPV4：IPV4。 IPV4ARP：IPV4-ARP。 IPV4NEXTHOP：IPV4-NEXTHOP。 IPV6ND：IPV6-ND。 IPV6NEXTHOP：IPV6-NEXTHOP。 IPV6ROUTE：IPV6-ROUTE。 MC：MC。 MCBRIEF：MC-BRIEF。 QOS：QOS。 FFM：FFM。 TBLMCST：TBLM-CST。 TBLMFRM：TBLM-FRM。 TBLMTPI：TBLM-TPI。 PKT：PKT。TBLMAPI：TBLM-API。IPV4AT：IPV4-AT。IPV6NDH：IPV6-NDH。MPLS：MPLS。IPEOP：IPEOP。FEMP：FEMP。FEMPFABRIC：FEMP-FABRIC。 默认值：无 |
| SWITCH     | 开关     | 可选必选说明：必选参数 参数含义：该参数用于指定使能开关。 数据来源：本端规划 取值范围：枚举类型。 ON：使能。 OFF：去使能。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

#### 使用实例

- 设置BFD模块的调测日志开关打开：

  ```
  SET FEILOGSWITCH: MODULENAME=BFD, SWITCH=ON;
  ```
- 设置TBLMTPI模块的调测日志开关关闭：

  ```
  SET FEILOGSWITCH: MODULENAME=TBLMTPI, SWITCH=OFF;
  ```