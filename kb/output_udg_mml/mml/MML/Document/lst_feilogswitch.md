# 查询调测日志开关（LST FEILOGSWITCH）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用来查询调测日志开关配置。

#### 注意事项

- 该命令仅适用于NP卡加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-----------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MODULENAME | 模块名    | 可选必选说明：可选参数。 参数含义：该参数用于指定模块名称。 数据来源：本端规划。 取值范围：枚举类型。 BFD：BFD。 BFDEVENT：BFD-EVENT。 CPUDEFEND：CPU-DEFEND。 FEIIPSEC：FEI-IPSEC。 FIM：FIM。 FIMSTAT：FIM-STAT。 FRAME：FRAME。 FRAMEERROR：FRAME-ERROR。 FRAMEMESSAGE：FRAME-MESSAGE。 FRAMEPERFORMANCE：FRAME-PERFORMANCE。 FWDSMOOTH：FWD-SMOOTH。 GRE：GRE。IPTRACE：IP-TRACE。 IPV4：IPV4。 IPV4ARP：IPV4-ARP。 IPV4NEXTHOP：IPV4-NEXTHOP。 IPV6ND：IPV6-ND。 IPV6NEXTHOP：IPV6-NEXTHOP。 IPV6ROUTE：IPV6-ROUTE。 MC：MC。 MCBRIEF：MC-BRIEF。 QOS：QOS。 FFM：FFM。 TBLMCST：TBLM-CST。 TBLMFRM：TBLM-FRM。 TBLMTPI：TBLM-TPI。 PKT：PKT。TBLMAPI：TBLM-API。IPV4AT：IPV4-AT。IPV6NDH：IPV6-NDH。MPLS：MPLS。IPEOP：IPEOP。FEMP：FEMP。FEMPFABRIC：FEMP-FABRIC。 默认值：无。 |

#### 使用实例

- 查询调测日志开关配置：

  ```
  LST FEILOGSWITCH:;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下
  --------
  模块名  开关  

  BFD     ON       
  QOS     OFF   
  (结果个数 = 2)

  ---    END
  ```

#### 输出结果说明

参见**SET FEILOGSWITCH**的参数说明。