# 配置VXLAN隧道及分流规则

- 操作场景
- 必备事项
- 操作流程
- 操作步骤
- 验证方法

## 操作场景

UEG作为主锚点UPF或辅锚点UPF，与MPF对接时，需要配置VXLAN隧道及分流规则（分流到MPF的规则）。

UPF与MPF通过VXLAN（VXLAN-GPE）隧道互通。为简化描述，使用VXLAN替代VXLAN-GPE。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
- 请了解UEG各类接口的类型及命名规范，具体内容请参见逻辑接口介绍（UPF）。

数据

在UPF（UEG）上配置Nxuc逻辑接口数据后，通过配置VXLAN隧道数据（表1）和分流到MPF的规则数据（表2），为UPF与MPF之间的数据路径建立逻辑连接。UPF处理过程如下：UPF检测数据报文是否匹配分流到MPF的规则，若匹配，则UPF将VPN映射成VNI并封装报文，然后将数据报文通过VXLAN隧道分流到MPF。

- 根据UE选择转发给哪个MPF：需要配置APN和VXLAN隧道组绑定**ADD VXLANBINDAPN**。如下数据中带“01”（如vxlan\_grp01）/“1”（如VTEP1）的数据，使用APN绑定的VXLAN隧道转发数据。如app跨站点是负荷分担部署场景，可根据UE选择转发给哪个MPF。
- 根据UE访问的目的IP选择转发给哪个MPF：需要配置rule和VXLAN隧道组绑定（**ADD VXLANBINDRULE**）。如下数据中带“02”（如vxlan\_grp02）/“2”（如VTEP2）的数据，使用rule绑定的VXLAN隧道转发数据。如app跨站点是主备关系且MPF只能访问本DC的APP Server场景，必须根据UE访问的目的IP选择转发给哪个MPF。

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别               | 参数名称                     | 取值样例                       | 获取方法     | 说明                                                                                                     |
|:-----------------|:-------------------------|:---------------------------|:---------|:-------------------------------------------------------------------------------------------------------|
| ADD VXLANGRP     | VXLAN隧道组名称（GRPNAME）      | vxlan_grp01vxlan_grp02     | 本端规划     | VXLAN链路组名称，网元内不能重复。 此处规划的vxlan_grp01用于和APN绑定，vxlan_grp02用于和rule绑定。 rule绑定的VXLAN链路组优先级高于APN绑定的VXLAN链路组。 |
| ADD VXLANGRP     | VXLAN隧道源接口（SRCINTF）      | Nxucif1/1/0                | 已配置数据中获取 | UPF与MPF互通场景，此处使用的是UPF上Nxuc接口。                                                                          |
| ADD VXLANGRP     | 健康检查开关（HEARTBEAT）        | ENABLE                     | 本端规划     | 使能心跳检查功能。                                                                                              |
| ADD VXLANGRP     | 时间阈值（秒）（TIMETHRESHOLD）   | 6                          | 本端规划     | 两次心跳检测间的时间阈值。                                                                                          |
| ADD VXLANGRP     | 心跳检查成功次数（HEARTSUCCLIMIT） | 3                          | 本端规划     | 设置隧道状态为up所需的心跳检测连续成功次数。                                                                                |
| ADD VXLANGRP     | 心跳检查失败次数（HEARTFAILLIMIT） | 3                          | 本端规划     | 设置隧道状态为down所需的心跳检测连续失败次数。                                                                              |
| ADD VXLANGRP     | Ping探测超时时长（秒）（TIMEOUT）   | 2                          | 本端规划     | 设置心跳检测的超时时长，该值需要小于TimeThreshold。                                                                       |
| ADD VTEP         | VXLAN隧道端点名称（VTEPNAME）    | VTEP1VTEP2                 | 本端规划     | VXLAN隧道端点名称，网元内不能重复。 此处规划的VTEP1用于和vxlan_grp01绑定，VTEP2用于和vxlan_grp02绑定。                                 |
| ADD VTEP         | IP协议版本（IPVERSION）        | IPV4                       | 本端规划     | UPF与MPF互通场景，此处使用的是MPF上Nxua逻辑接口的IP地址。                                                                   |
| ADD VTEP         | 隧道端点的IPv4地址（VTEPIPV4）    | 10.10.100.110.10.100.2     | 与对端协商    | UPF与MPF互通场景，此处使用的是MPF上Nxua逻辑接口的IP地址。                                                                   |
| ADD VTEPBINDGRP  | VXLAN组名称（VXLANGRPNAME）   | vxlan_grp01vxlan_grp02     | 已配置数据中获取 | VTEP绑定VXLAN隧道组。                                                                                        |
| ADD VTEPBINDGRP  | VTEP名称（VTEPNAME）         | VTEP1VTEP2                 | 已配置数据中获取 | VTEP绑定VXLAN隧道组。                                                                                        |
| ADD VTEPBINDGRP  | 主备用类型（PRIFLAG）           | PRIMARY                    | 固定取值     | VTEP绑定VXLAN隧道组。                                                                                        |
| ADD VXLANBINDAPN | APN（APN）                 | apn-op                     | 已配置数据中获取 | 基于APN绑定一个链路组。UPF与MPF互通场景，UPF将命中Rule的报文发送到MPF的Nxua接口。 可选数据，使用APN绑定的VXLAN隧道转发数据时需要规划。                    |
| ADD VXLANBINDAPN | VXLAN组名称（VXLANGRPNAME）   | vxlan_grp01                | 已配置数据中获取 | 基于APN绑定一个链路组。UPF与MPF互通场景，UPF将命中Rule的报文发送到MPF的Nxua接口。 可选数据，使用APN绑定的VXLAN隧道转发数据时需要规划。                    |
| ADD VPNVNIMAP    | VPN实例（VPNINSTANCE）       | VPN_LocalDN01VPN_LocalDN02 | 已配置数据中获取 | 与APN绑定的VPN实例相同。                                                                                        |
| ADD VPNVNIMAP    | Rule开关（RULESWITCH）       | DISABLEENABLE              | 本端规划     | 基于用户VPN映射到VNI时设置为“DISABLE”；基于VPN+RULE映射到VNI时设置为“ENABLE”。                                               |
| ADD VPNVNIMAP    | 规格名称（RULENAME）           | -rule_trafficfwd02         | 本端规划     | 基于VPN+RULE映射到VNI时需要设置。                                                                                 |
| ADD VPNVNIMAP    | VNI（VNI）                 | 12                         | 全网规划     | 配置VxLan隧道标识。 如需了解VXLAN-GPE报文格式，请跳转到VXLAN-GPE。                                                          |

表2中以匹配三四层过滤条件（APP Server IP地址）为例进行介绍。

| 类别               | 参数名称                        | 取值样例                                           | 获取方法     | 说明                                                                                                                                                                      |
|:-----------------|:----------------------------|:-----------------------------------------------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD FILTER       | 过滤器名字（FILTERNAME）           | filter_trafficfwd01filter_trafficfwd02         | 本端规划     | 配置三四层过滤条件。该IP地址是APP服务器的IP地址。 此处的分流到MPF的规则，以三四层条件中的服务器地址完全匹配为例进行介绍。 访问此处指定的APP服务器（192.168.1.1/192.168.1.2）时，流量将通过VXLAN隧道发送到MPF；访问此处没有指定的APP服务器（如192.168.2.2）时，则流量不经过MPF。 |
| ADD FILTER       | 三四层IPv4协议输入类型（L34PROTTYPE）  | STRING                                         | 本端规划     | 配置三四层过滤条件。该IP地址是APP服务器的IP地址。 此处的分流到MPF的规则，以三四层条件中的服务器地址完全匹配为例进行介绍。 访问此处指定的APP服务器（192.168.1.1/192.168.1.2）时，流量将通过VXLAN隧道发送到MPF；访问此处没有指定的APP服务器（如192.168.2.2）时，则流量不经过MPF。 |
| ADD FILTER       | 三四层协议类型（L34PROTOCOL）        | ANY                                            | 本端规划     | 配置三四层过滤条件。该IP地址是APP服务器的IP地址。 此处的分流到MPF的规则，以三四层条件中的服务器地址完全匹配为例进行介绍。 访问此处指定的APP服务器（192.168.1.1/192.168.1.2）时，流量将通过VXLAN隧道发送到MPF；访问此处没有指定的APP服务器（如192.168.2.2）时，则流量不经过MPF。 |
| ADD FILTER       | 服务器IP地址配置模式（SVRIPMODE）      | IP                                             | 本端规划     | 配置三四层过滤条件。该IP地址是APP服务器的IP地址。 此处的分流到MPF的规则，以三四层条件中的服务器地址完全匹配为例进行介绍。 访问此处指定的APP服务器（192.168.1.1/192.168.1.2）时，流量将通过VXLAN隧道发送到MPF；访问此处没有指定的APP服务器（如192.168.2.2）时，则流量不经过MPF。 |
| ADD FILTER       | 服务器IP地址（SVRIP）              | 192.168.1.1192.168.1.2                         | 已配置数据中获取 | 配置三四层过滤条件。该IP地址是APP服务器的IP地址。 此处的分流到MPF的规则，以三四层条件中的服务器地址完全匹配为例进行介绍。 访问此处指定的APP服务器（192.168.1.1/192.168.1.2）时，流量将通过VXLAN隧道发送到MPF；访问此处没有指定的APP服务器（如192.168.2.2）时，则流量不经过MPF。 |
| ADD FILTER       | 服务器IP地址掩码类型（SVRIPMASKTYPE）  | LENGTHTYPE                                     | 本端规划     | 配置三四层过滤条件。该IP地址是APP服务器的IP地址。 此处的分流到MPF的规则，以三四层条件中的服务器地址完全匹配为例进行介绍。 访问此处指定的APP服务器（192.168.1.1/192.168.1.2）时，流量将通过VXLAN隧道发送到MPF；访问此处没有指定的APP服务器（如192.168.2.2）时，则流量不经过MPF。 |
| ADD FILTER       | 服务器IP地址掩码长度（SVRIPMASKLEN）   | 32                                             | 本端规划     | 配置三四层过滤条件。该IP地址是APP服务器的IP地址。 此处的分流到MPF的规则，以三四层条件中的服务器地址完全匹配为例进行介绍。 访问此处指定的APP服务器（192.168.1.1/192.168.1.2）时，流量将通过VXLAN隧道发送到MPF；访问此处没有指定的APP服务器（如192.168.2.2）时，则流量不经过MPF。 |
| ADD FLOWFILTER   | 流过滤器名称（FLOWFILTERNAME）      | FlowFilter_trafficfwd01FlowFilter_trafficfwd02 | 本端规划     | 流过滤器。                                                                                                                                                                   |
| ADD FLTBINDFLOWF | 流过滤器名称（FLOWFILTERNAME）      | FlowFilter_trafficfwd01FlowFilter_trafficfwd02 | 已配置数据中获取 | 绑定的三四层过滤条件已通过ADD FILTER命令配置。                                                                                                                                            |
| ADD FLTBINDFLOWF | 过滤器名字（FILTERNAME）           | filter_trafficfwd01filter_trafficfwd02         | 已配置数据中获取 | 绑定的三四层过滤条件已通过ADD FILTER命令配置。                                                                                                                                            |
| ADD RULE         | 规则名称（RULENAME）              | rule_trafficfwd01rule_trafficfwd02             | 本端规划     | 转发规则。                                                                                                                                                                   |
| ADD RULE         | 策略类型（POLICYTYPE）            | WORKER                                         | 固定取值     | -                                                                                                                                                                       |
| ADD RULE         | 流过滤器或流过滤器组选择(FILTERINGMODE) | FLOWFILTER                                     | 本端规划     | -                                                                                                                                                                       |
| ADD RULE         | 流过滤器名称（FLOWFILTERNAME）      | FlowFilter_trafficfwd01FlowFilter_trafficfwd02 | 已配置数据中获取 | 绑定的FlowFilter已通过ADD FLOWFILTER命令配置。                                                                                                                                     |
| ADD RULE         | 通用Rule子策略名称（WORKERNAME）     | traffic-fd                                     | 固定取值     | 必须使用样例值。UPF依赖该配置将命中规则的数据报文通过VXLAN隧道转发到MPF。                                                                                                                              |
| ADD USERPROFILE  | 用户模板名称（USERPROFILENAME）     | up_test                                        | 全网规划     | 该参数与SMF上的PCC类型的Userprofile名称必须相同。                                                                                                                                       |
| ADD RULEBINDING  | 规则名称（RULENAME）              | rule_trafficfwd01rule_trafficfwd02             | 已配置数据中获取 | UserProfile绑定的业务规则，已通过ADD RULE命令配置完成。                                                                                                                                   |
| ADD RULEBINDING  | 用户模板名称（USERPROFILENAME）     | rule_trafficfwd                                | 已配置数据中获取 | 已通过ADD USERPROFILE配置完成。                                                                                                                                                 |
| SET APNTRAFDFUNC | APN（APN）                    | apn-op                                         | 已配置数据中获取 | -                                                                                                                                                                       |
| SET APNTRAFDFUNC | 流量转发开关（TRAFFICFDSW）         | ENABLE                                         | 固定取值     | -                                                                                                                                                                       |

根据UE访问的目的IP选择转发给哪个MPF时，需要规划表3中的数据。UPF根据UE访问的APP Server IP（192.168.1.2），选择指定的VXLAN隧道（vxlan\_grp02），即将数据报文发送给指定的MPF（10.10.100.2）。

| 类别                | 参数名称                   | 取值样例              | 获取方法     | 说明                           |
|:------------------|:-----------------------|:------------------|:---------|:-----------------------------|
| ADD VXLANBINDRULE | 规则名称（RULENAME）         | rule_trafficfwd02 | 已配置数据中获取 | 使用ADD RULE命令定义的规则名称。         |
| ADD VXLANBINDRULE | VXLAN组名称（VXLANGRPNAME） | vxlan_grp02       | 已配置数据中获取 | 使用ADD VXLANGRP命令定义的VXLAN组名称。 |

文档

获取网设LLD文档。

## 操作流程

- 根据UE选择转发给哪个MPF时，请配置•配置VXLAN隧道（UPF）\_基于APN绑定隧...和•配置分流到MPF的规则（UPF）\_基于APN绑...。
- 根据UE访问的目的IP选择转发给哪个MPF时，请配置•配置VXLAN隧道（UPF）\_基于Rule绑定...和•配置分流到MPF的规则（UPF）\_基于Rule...。

## 操作步骤

配置VXLAN隧道（UPF）\_基于APN绑定隧道

根据UE选择转发给哪个MPF时需要配置，如APP Server跨站点负荷分担部署时可使用该方案。

1. 配置VXLAN隧道组。

   ```
   ADD VXLANGRP: GRPNAME="vxlan_grp01", SRCINTF="Nxucif1/1/0", HEARTBEAT=ENABLE, TIMETHRESHOLD=6, HEARTSUCCLIMIT=3, HEARTFAILLIMIT=3, TIMEOUT=2;
   ```
2. 配置VXLAN隧道端点（VTEP）。

   ```
   ADD VTEP: VTEPNAME="VTEP1", IPVERSION=IPV4, VTEPIPV4="10.10.100.1";
   ```
3. 配置VXLAN端点绑定VXLAN隧道组。

   ```
   ADD VTEPBINDGRP: VXLANGRPNAME="vxlan_grp01", VTEPNAME="VTEP1", PRIFLAG=PRIMARY;
   ```
4. 配置VXLAN隧道组绑定APN。

   ```
   ADD VXLANBINDAPN: APN="apn-op", VXLANGRPNAME="vxlan_grp01";
   ```
5. 配置VPN到VNI的映射。

   ```
   ADD VPNVNIMAP: VPNINSTANCE="VPN_LocalDN01", RULESWITCH=DISABLE, VNI=1;
   ```

配置分流到MPF的规则（UPF）\_基于APN绑定隧道

根据UE选择转发给哪个MPF时需要配置，如APP Server跨站点负荷分担部署时可使用该方案。

6. 配置过滤器。

   ```
   ADD FILTER: FILTERNAME="filter_trafficfwd01", L34PROTTYPE=STRING, L34PROTOCOL=ANY, SVRIPMODE=IP, SVRIP="192.168.1.1", SVRIPMASKTYPE=LENGTHTYPE, SVRIPMASKLEN=32, SVRSTARTPORT=0, SVRENDPORT=65535;
   ```
7. 配置流过滤器。

   ```
   ADD FLOWFILTER: FLOWFILTERNAME="FlowFilter_trafficfwd01", TETHERDETFLAG=NONE, FLOWFILTERTYPE=USERCONFIG;
   ```
8. 配置过滤器和流过滤器绑定。

   ```
   ADD FLTBINDFLOWF: FLOWFILTERNAME="FlowFilter_trafficfwd01", FILTERNAME="filter_trafficfwd01";
   ```
9. 配置规则。

   ```
   ADD RULE: RULENAME="rule_trafficfwd01", POLICYTYPE=WORKER, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="FlowFilter_trafficfwd01", PRIORITY=65535, WORKERNAME="traffic-fd";
   ```
10. 配置Userprofile。

    ```
    ADD USERPROFILE: USERPROFILENAME="up_test";
    ```
11. 配置规则绑定Userprofile。

    ```
    ADD RULEBINDING: USERPROFILENAME="up_test", RULENAME="rule_trafficfwd01";
    ```
12. 开启流量转发开关。

    ```
    SET APNTRAFDFUNC: APN="apn-op", TRAFFICFDSW=ENABLE;
    ```

配置VXLAN隧道（UPF）\_基于Rule绑定隧道

根据UE访问的目的IP选择转发给哪个MPF时需要配置，如APP Server跨站点主备部署，且MPF只能访问本DC的APP Server时可使用该方案。

13. 配置VXLAN隧道组。

    ```
    ADD VXLANGRP: GRPNAME="vxlan_grp02", SRCINTF="Nxucif1/1/0", HEARTBEAT=ENABLE, TIMETHRESHOLD=6, HEARTSUCCLIMIT=3, HEARTFAILLIMIT=3, TIMEOUT=2;
    ```
14. 配置VXLAN隧道端点（VTEP）。

    ```
    ADD VTEP: VTEPNAME="VTEP2", IPVERSION=IPV4, VTEPIPV4="10.10.100.2";
    ```
15. 配置VXLAN端点绑定VXLAN隧道组。

    ```
    ADD VTEPBINDGRP: VXLANGRPNAME="vxlan_grp02", VTEPNAME="VTEP2", PRIFLAG=PRIMARY;
    ```

配置分流到MPF的规则（UPF）\_基于Rule绑定隧道

根据UE访问的目的IP选择转发给哪个MPF时需要配置，如APP Server跨站点主备部署，且MPF只能访问本DC的APP Server时可使用该方案。

16. 配置过滤器。

    ```
    ADD FILTER: FILTERNAME="filter_trafficfwd02", L34PROTTYPE=STRING, L34PROTOCOL=ANY, SVRIPMODE=IP, SVRIP="192.168.1.2", SVRIPMASKTYPE=LENGTHTYPE, SVRIPMASKLEN=32, SVRSTARTPORT=0, SVRENDPORT=65535;
    ```
17. 配置流过滤器。

    ```
    ADD FLOWFILTER: FLOWFILTERNAME="FlowFilter_trafficfwd02", TETHERDETFLAG=NONE, FLOWFILTERTYPE=USERCONFIG;
    ```
18. 配置过滤器和流过滤器绑定。

    ```
    ADD FLTBINDFLOWF: FLOWFILTERNAME="FlowFilter_trafficfwd02", FILTERNAME="filter_trafficfwd02";
    ```
19. 配置规则。

    ```
    ADD RULE: RULENAME="rule_trafficfwd02", POLICYTYPE=WORKER, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="FlowFilter_trafficfwd02", PRIORITY=65535, WORKERNAME="traffic-fd";
    ```
20. 配置Userprofile。如已配置，请跳过本步骤。

    ```
    ADD USERPROFILE: USERPROFILENAME="up_test";
    ```
21. 配置规则绑定Userprofile。

    ```
    ADD RULEBINDING: USERPROFILENAME="up_test", RULENAME="rule_trafficfwd02";
    ```
22. 配置VXLAN隧道组绑定rule。

    ```
    ADD VXLANBINDRULE:RULENAME="rule_trafficfwd02", VXLANGRPNAME="vxlan_grp02";
    ```
23. 配置VPN+RULE到VNI的映射。

    ```
    ADD VPNVNIMAP: VPNINSTANCE="VPN_LocalDN01", RULESWITCH=ENABLE, RULENAME="rule_trafficfwd02", VNI=2;
    ```
24. 开启流量转发开关。

    ```
    SET APNTRAFDFUNC: APN="apn-op", TRAFFICFDSW=ENABLE;
    ```

## 验证方法

1. 执行**DSP VXLANGRPSTAT**，查看VXLAN隧道组可用服务器数目是否正确。

   当一个VXLAN隧道组中的“VXLAN Group 可用服务器数目”和“VXLAN Group 服务器数目”相等时，说明VXLAN组隧道链路可用服务器数目正确。

   - 正确，请执行2。
   - 不正确，且“VXLAN Group 可用服务器数目”为“0”时，请参考ALM-81082 VXLAN组不可用(风筝S)/ALM-81079 VXLAN组不可用(风筝M或L)处理。
   - 不正确，且“VXLAN Group 可用服务器数目”不为“0”时，请参考ALM-81113 VXLAN链路异常处理。
2. 执行**DSP VTEPSTAT**，查看VXLAN组隧道端点状态是否正常。

   当一个VXLAN隧道组中的VTEP的“地址信息”正确，且“服务器状态”为“正常”时，说明VXLAN组隧道端点状态正常。

   - 正常，调测结束。
   - 异常，请执行3。
3. 收集信息并寻求技术支持。
   1. 在“MML命令行-UEG”窗口上执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。