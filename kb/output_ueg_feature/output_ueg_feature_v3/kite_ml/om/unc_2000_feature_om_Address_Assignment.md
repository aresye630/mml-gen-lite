# 配置静态IP地址网段与UPF的绑定

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

可以在本地配置静态IP地址网段与UPF的绑定关系，当用户接入网络时，对静态IP地址用户、Radius分配IP地址用户可以基于配置的网段绑定关系为用户选择指定的UPF。

适用于PGW-C、SMF。

## 必备事项

前提条件

* 请仔细阅读GWFD-020804 地址分配方式特性概述。
* 本特性与UEG配合使用生效，要求UEG上配置的用户静态地址网段信息必须在包含在UEG上配置的地址池内，请参考UEG中的**GWFD-010104 地址分配方式**。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD CPADDRPOOL** | 地址池名称（POOLNAME） | pool01 | 本端规划 | 为采用静态地址分配方式的用户配置对应的地址池。 |
|  | IP地址类型（IPVERSION） | IPV4 | 本端规划 |  |
|  | POOLTYPE（地址池类型） | UDM | 本端规划 |  |
|  | CHECKIPVALID（检查地址合法性） | Enable | 本端规划 |  |
| **ADD CPSECTION** | Pool名称（POOLNAME） | pool01 | 本端规划 | 配置本地地址池里的地址段 |
|  | Section序号（SECTIONNUM） | 1 | 本端规划 |  |
|  | IP类型（IPVERSION） | IPv4 | 本端规划 |  |
|  | IPV4开始地址（V4STARTIP） | 10.0.0.0 | 全网规划 |  |
|  | IPV4结束地址（V4ENDIP） | 10.1.2.3 | 全网规划 |  |
| **ADD ADDRPOOLGRP** | POOLGRPNAME（地址池组名称） | poolgroup1 | 本端规划 | 配置地址池组。 |
|  | POOLGRPTYPE（地址池类型） | UDM | 本端规划 |  |
| **ADD POOLBINDGRP** | POOLGRPNAME（地址池组名称） | poolgroup1 | 已配置数据中获取 | 已通过**ADD ADDRPOOLGRP**配置。 |
|  | POOLNAME（地址池名称） | pool01 | 已配置数据中获取 | 已通过 **ADD CPADDRPOOL**配置。 |
| **SET EDGESMCOMMFUNC** | RDSSTATICIPSW（Raidus静态IP功能开关） | ENABLE | 本端规划 | 配置Raidus静态IP功能开关。 |
| **ADD RDSSTATICIPPARA** | IMSI（用户IMSI号） | 123456789012345 | 本端规划 | 配置Radius静态IP地址。 |
|  | APN（APN名称） | huawei.com | 本端规划 |  |
|  | ADDRTYPE（地址类型） | IPv4 | 对端协商 |  |
|  | IPV4ADDRESS（静态IPv4地址） | 192.168.10.10 | 对端协商 |  |
| **ADD UPNODE** | UPF实例名称（NFINSTANCENAME） | UPF\_Instance\_1 | 全网规划 | 配置静态地址用户使用的UPF。  已通过**ADD PNFPROFILE**配置。 |
|  | 地址分配属性（ADDRALLOCMODE） | INHERIT | 本端规划 | - |
| **ADD ADDRUPGROUP** | UPF组名称（UPFGRPNAME） | upfgroup1 | 本端规划 | 配置静态地址用户使用的UPF组。 |
|  | UPF组类型（UPFGRPTYPE） | UDM | 本端规划 | - |
| **ADD UPFBINDGRP** | UPFGRPNAME（UPF组名称） | upfgroup1 | 已配置数据中获取 | 已通过**ADD ADDRUPGROUP**配置。 |
|  | UPFID（UPF实例标识） | UPF\_Instance\_1 | 已配置数据中获取 | 已通过**ADD UPNODE**配置。 |
| **ADD CPPOOLGRPMAP** | MAPPINGNAME（映射名称） | mapping01 | 本端规划 | - |
|  | POOLGRPNAME（地址池组名称） | poolgroup1 | 已配置数据中获取 | 已通过**ADD ADDRPOOLGRP**配置。 |
|  | UPFGRPNAME（UPF组名称） | upfgroup1 | 已配置数据中获取 | 已通过**ADD ADDRUPGROUP**配置。 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 创建本地静态地址地址池。

   **ADD CPADDRPOOL**
3. 如果需要开启静态地址用户的白名单检查功能，需要配置地址池与APN的绑定关系。接入该APN的静态地址用户激活时，根据用户地址查找对应的地址池，然后根据地址池为用户选择对应的UPF。

   **ADD POOLBINDAPN**
4. 配置本地地址池里的地址段。

   **ADD CPSECTION**

   * 本地地址池：本地负责分配地址的地址池。本地地址池下需要配置地址段，一个本地地址池最多可以配置64个地址段。
   * 配置地址池后，必须配置地址段。如果不配置地址段，将导致用户激活失败。
5. 配置地址池组名称。

   **ADD ADDRPOOLGRP**
6. 配置地址池与地址池组绑定。

   **ADD POOLBINDGRP**
7. （可选）打开Raidus静态IP功能开关。

   **SET EDGESMCOMMFUNC**
8. （可选）配置Radius静态IP地址。

   **ADD RDSSTATICIPPARA**

   当UDM和Radius未向用户分配有效IP地址时，可通过SMF本地配置的IP地址为用户分配地址，此时可以执行步骤7、8。
9. 配置静态地址用户使用的UPF。

   **ADD UPNODE**
10. 配置静态地址用户使用的UPF组。

    **ADD ADDRUPGROUP**
11. 配置UPF与UPF组绑定。

    **ADD UPFBINDGRP**
12. 配置地址池组与UPF组绑定。

    **ADD CPPOOLGRPMAP**

    * 会话建立流程中，当静态IP地址网段绑定的UPF与SMF选择的主锚点UPF不一致时，优先使用SMF选择的主锚点UPF建立会话。
    * 如果已有会话的主锚点UPF与静态IP地址绑定的UPF不一致时，可以根据**SET STATICADDRPARA**命令中的开关配置时间扫描会话去活。

## 任务示例

任务描述

某企业用户接入网络时，为用户分配的IP地址采用静态IP地址分配方式。开启静态地址用户的白名单检查功能，需要为10.0.0.0~10.1.2.3地址段内的用户选择到UPF名称为UPF\_Instance\_1的园区UPF。UPF\_Instance\_1上已经配置包含网段10.0.0.0~10.1.2.3的地址池信息，需要在UEG上配置静态IP地址段10.0.0.0~10.1.2.3到UPF\_Instance\_1的关系，为用户选择到指定UPF。

脚本

//创建本地地址池。

```
ADD CPADDRPOOL: POOLNAME="pool01", IPVERSION=IPv4, POOLTYPE=UDM, CHECKIPVALID=Enable;
```

//配置地址池与APN的绑定关系。

```
ADD POOLBINDAPN:APN="huawei.com",POOLNAME="pool01";
```

//配置本地地址池里的IPv4地址段。

```
ADD CPSECTION: POOLNAME="pool01", SECTIONNUM=1, IPVERSION=IPv4, V4STARTIP="10.0.0.0", V4ENDIP="10.1.2.3";
```

//配置地址池组名称。

```
ADD ADDRPOOLGRP: POOLGRPNAME="poolgroup1", POOLGRPTYPE=UDM;
```

//配置地址池与地址池组绑定。

```
ADD POOLBINDGRP: POOLGRPNAME="poolgroup1", POOLNAME="pool01";
```

//打开Raidus静态IP功能开关。

```
SET EDGESMCOMMFUNC: RDSSTATICIPSW=ENABLE;
```

//配置Radius静态IP地址。

```
ADD RDSSTATICIPPARA: IMSI="123456789012345", APN="huawei.com", ADDRTYPE=IPv4, IPV4ADDRESS="192.168.10.10";
```

//配置静态地址用户使用的UPF。

```
ADD UPNODE: NFINSTANCENAME="UPF_Instance_1", ADDRALLOCMODE=INHERIT;
```

//配置静态地址用户使用的UPF组。

```
ADD ADDRUPGROUP: UPFGRPNAME="upfgroup1", UPFGRPTYPE=UDM;
```

//配置UPF与UPF组绑定。

```
ADD UPFBINDGRP: UPFGRPNAME="upfgroup1", UPFID="UPF_Instance_1";
```

//配置地址池组与UPF组绑定。

```
ADD CPPOOLGRPMAP: MAPPINGNAME="mapping01", POOLGRPNAME="poolgroup1", UPFGRPNAME="upfgroup1";
```

版权所有 © 华为技术有限公司
