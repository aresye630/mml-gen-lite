# 激活业务体验保障

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

适用于PGW-U、UPF。

## 必备事项

前提条件

* 请仔细阅读GWFD-030202 业务体验保障特性概述。
* UEG完成与周边网元的对接。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD BWMCONTROLLER** | 带宽管理控制器名称（BWMCNAME） | bwm\_ctrl | 本端规划 | 推荐配置：  * CIR = 0.5 \* PIR （最大带宽建议为保证带宽的2倍） * CBS >=CIR \* 1.5 \* 1000 / 8 （保证1.5秒数据的队列缓存能力） * PBS >= PIR \* 1.5 \* 1000 / 8 （保证1.5秒数据的队列缓存能力） |
|  | 带宽管理控制类型（CTRLTYPE） | CAR | 本端规划 |  |
|  | 承诺信息速率（千比特/秒）（CIR） | 2000000 | 本端规划 |  |
|  | 承诺突发能缓存信息的数量（字节）（CBS） | 320000000 | 本端规划 |  |
|  | 峰值信息速率（千比特/秒）（PIR） | 4000000 | 本端规划 |  |
|  | 峰值突发能缓存信息的数量（字节）（PBS） | 800000000 | 本端规划 |  |
|  | 绿色（GREEN） | PASS | 本端规划 |  |
|  | 黄色（YELLOW） | PASS | 本端规划 |  |
|  | 红色（RED） | DISCARD | 本端规划 |  |
|  | BWM CAR优先级是否敏感（PRIORITYISAWARE） | DISABLE | 本端规划 |  |
| **SET BANDWIDTHMNG** | 带宽管理生效范围（RANGE） | SYSTEM | 本端规划 | - |
|  | 承诺信息速率最低保护值（千比特每秒）（CIRMINTHRES） | 30000 | 本端规划 |  |
|  | 峰值信息速率最低保护值（千比特每秒）（PIRMINTHRES） | 500000 | 本端规划 |  |
| **ADD BWMUSERGROUP** | 用户组类型（USERGROUPTYPE） | SPECIFIC\_GROUP | 本端规划 | - |
|  | 用户组名称（USERGROUPNAME） | ug\_test | 本端规划 |  |
|  | 用户组优先级（USERGROUPPRI） | 1 | 本端规划 |  |
|  | 用户级业务类型（USERLEVSRVTYPE） | NONTOS | 本端规划 |  |
|  | 用户组级业务类型（USERGLEVSRVTYPE） | NONTOS | 本端规划 |  |
| **ADD BWMRULE** | 用户组类型（USERGROUPTYPE） | SPECIFIC\_GROUP | 已配置数据中获取 | BwmController已通过  **ADD BWMCONTROLLER**命令配置。  说明：  该带宽管理功能不区分用户的业务类型，无需和BWM Service关联。 |
|  | 用户组名称（USERGROUPNAME） | ug\_test | 已配置数据中获取 |  |
|  | 带宽管理规则类型（BWMRULETYPE） | GROUP\_DEFAULT | 本端规划 |  |
|  | 上行带宽管理控制器名称一（UPBWMCTRLNAME1） | bwm\_ctrl | 已配置数据中获取 |  |
|  | 下行带宽管理控制器名称一（DNBWMCTRLNAME1） | bwm\_ctrl | 已配置数据中获取 |  |
| **ADD SNSSAI** | 切片/服务类型（SST） | 10 | 本端规划 | 业务体验保障使用的切片。 |
|  | 切片区分码（SD） | 123456 | 本端规划 |  |
| **ADD SNSSAIBWMUSRG** | 用户组名称  （USERGROUPNAME） | ug\_test | 已配置数据中获取 | 切片绑定的带宽用户组名称，已经通过**ADD BWMUSERGROUP**命令配置。 |
|  | 切片/服务类型（SST） | 10 | 已配置数据中获取 | 已经通过**ADD SNSSAI**命令配置。 |
|  | 切片区分码  （SD） | 123456 | 已配置数据中获取 |  |
| **ADD VPNINST** | VPN实例名（VPNINSTANCE） | vpn\_bwm | 本端规划 | N3逻辑接口使用的VPN实例。 |
| **ADD LOGICINF** | 逻辑接口名称（NAME） | n3if1/1/1 | 本端规划 | - |
|  | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 |  |
|  | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 192.168.1.1 | 本端规划 |  |
|  | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 本端规划 |  |
|  | VPN实例名称（VPNINSTANCE） | vpn\_bwm | 已配置数据中获取 | 使用的VPN实例已经通过**ADD VPNINST**命令配置。 |
| **ADD SNSSAIUPINTF** | 切片/服务类型（SST） | 10 | 已配置数据中获取 | 使用的切片已经通过**ADD SNSSAI**命令配置。 |
|  | 切片区分码（SD） | 12345 | 已配置数据中获取 |  |
|  | N3逻辑接口名称（N3LOGICINF） | n3if1/1/1 | 已配置数据中获取 | 使用的N3逻辑接口已经通过**ADD LOGICINF**命令配置。 |
| **ADD APN** | APN名称（APN） | apn-test | 本端规划 | 配置业务体验保障使用的APN/DNN。 |
|  | 绑定VPN  （HASVPN） | DISABLE | 本端规划 |  |
|  | 绑定IPv6 VPN  （HASVPNIPV6） | DISABLE | 本端规划 |  |
| **ADD APNBINDBWMUSRG** | 用户组名称（USERGROUPNAME） | ug\_test | 已配置数据中获取 | 已经通过**ADD BWMUSERGROUP**命令配置。 |
|  | APN名称（APN） | apn-test | 已配置数据中获取 | 已经通过**ADD APN**命令配置。 |

## 操作步骤

1. 配置业务体验保障使用的带宽管理业务。
   1. 配置带宽管理控制器。

      **ADD BWMCONTROLLER**
   2. 配置BWM控制器中的用户组级业务带宽配置数据基于整机生效。

      **SET BANDWIDTHMNG**
   3. 定义带宽管理用户组，配置优先级和业务类型。

      **ADD BWMUSERGROUP**
   4. 配置一条用户组级带宽控制规则。

      **ADD BWMRULE**
2. 配置基于切片的带宽控制。
   1. 配置UPF网络切片选择标识。

      **ADD SNSSAI**
   2. 将切片与带宽管理用户组绑定。

      **ADD SNSSAIBWMUSRG**
   3. **（可选）**配置N3接口。

      **ADD VPNINST**

      **ADD LOGICINF**

      可以基于实际需求，考虑利用UEG已经配置好的N3接口。这种情况下此步骤可跳过。
   4. 将切片与N3接口绑定。

      **ADD SNSSAIUPINTF**
3. 配置基于DNN的带宽控制。
   1. 配置APN/DNN。

      **ADD APN**
   2. 将APN/DNN下的用户包含到带宽管理业务中。

      **ADD APNBINDBWMUSRG**

## 任务示例

任务描述

为了保障业务体验，分别配置基于切片的带宽控制和基于DNN的带宽控制。

脚本

//配置带宽管理业务。

```
ADD BWMCONTROLLER:BWMCNAME="bwm_ctrl",CTRLTYPE=CAR,CIR=2000000,CBS=320000000,PIR=4000000,PBS=
800000000,GREEN=PASS,YELLOW=PASS,RED=DISCARD,PRIORITYISAWARE=DISABLE;
```

```
SET BANDWIDTHMNG:RANGE=SYSTEM,CIRMINTHRES=300000,PIRMINTHRES=500000;
```

```
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="ug_test",USERGROUPPRI=1,USERLEVSRVTYPE=NONTOS,USERGLEVSRVTYPE=NONTOS;
```

```
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="ug_test",BWMRULETYPE=GROUP_DEFAULT,UPBWMCTRLNAME1="
bwm_ctrl",DNBWMCTRLNAME1="bwm_ctrl";
```

//配置基于切片的带宽控制。

```
ADD SNSSAI: SST=10,SD="123456";
```

```
ADD SNSSAIBWMUSRG:USERGROUPNAME="ug_test",SST=10,SD="123456";
```

```
ADD VPNINST:VPNINSTANCE="vpn_bwm";
ADD LOGICINF: NAME="n3if1/1/1", IPVERSION=IPV4, IPV4ADDRESS1="192.168.1.1", IPV4MASK1="255.255.255.255", VPNINSTANCE="vpn_bwm";
```

```
ADD SNSSAIUPINTF: SST=10, SD="123456",N3LOGICINF="n3if1/1/1";
```

//配置基于DNN的带宽控制。

```
ADD APN: APN="apn-test",HASVPN=DISABLE,HASVPNIPV6=DISABLE;
```

```
ADD APNBINDBWMUSRG:USERGROUPNAME="ug_test",APN="apn-test";
```

版权所有 © 华为技术有限公司
