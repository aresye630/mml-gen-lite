# 激活公私网协同访问（含共享UPF选择）

- 操作场景
- 对系统的影响
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍部署公私网协同访问特性的操作过程。

如果在初始配置中已经规划SMF是与主锚点、辅锚点和UL CL UPF合一部署的UPF对接，如下准备数据和配置步骤可能在初始配置中就已完成，此时无需重复配置。本章节通过以下准备数据和配置步骤与任务示例说明与该合一UPF对接的配置逻辑。

SMF支持用户通过同一个DNN（Data Network Name）访问公网和私网业务，同时私网之间业务隔离。SMF将为用户优先选择主锚点、辅锚点和UL CL UPF合一部署的UPF，分别建立到主锚点和辅锚点UPF的N4会话，同时访问公网和私网业务。SMF针对不同用户策略配置不同DNAI（Data Network Access Identifier），UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别不同的辅锚点N4会话，实现私网之间业务隔离。

**说明** 

适用于SMF。

## 对系统的影响

该操作对系统正常运行没有影响。

## 必备事项

前提条件

- 请仔细阅读WSFD-223002 公私网协同访问（含共享UPF选择）特性概述。
- 完成加载License。

数据

| 类别                  | 参数名称                      | 取值样例                                     | 获取方法   | 说明                                                                                                      |
|:--------------------|:--------------------------|:-----------------------------------------|:-------|:--------------------------------------------------------------------------------------------------------|
| ADD PNFPROFILE      | NF实例标识（NFINSTANCEID）      | UPF_Instance_0                           | 本端规划   | SMF本端配置共享UPF。                                                                                           |
| ADD PNFPROFILE      | NF类型（NFTYPE）              | NfUPF                                    | 本端规划   | SMF本端配置共享UPF。                                                                                           |
| ADD PNFPROFILE      | NF状态（NFSTATUS）            | Registered                               | 本端规划   | SMF本端配置共享UPF。                                                                                           |
| ADD PNFPROFILE      | 域名（FQDN）                  | upf01.node.mnc003.mcc123.3gppnetwork.org | 全网规划   | SMF本端配置共享UPF。                                                                                           |
| ADD PNFPROFILE      | IP地址类型（IPADDRESSTYPE）     | IPTypeV4                                 | 全网规划   | SMF本端配置共享UPF。                                                                                           |
| ADD PNFPROFILE      | IP地址（IPV4ADDRESS1）        | 192.168.126.11                           | 全网规划   | SMF本端配置共享UPF。                                                                                           |
| ADD PNFNS           | 索引（INDEX）                 | 3                                        | 本端规划   | 配置共享UPF支持的服务切片信息。                                                                                       |
| ADD PNFNS           | NF实例标识（NFINSTANCEID）      | UPF_Instance_0                           | 全网规划   | 配置共享UPF支持的服务切片信息。                                                                                       |
| ADD PNFNS           | 切片/服务类型（SST）              | 1                                        | 全网规划   | 配置共享UPF支持的服务切片信息。                                                                                       |
| ADD PNFNS           | 切片分类器（SD）                 | 010101                                   | 全网规划   | 配置共享UPF支持的服务切片信息。                                                                                       |
| ADD PNFDNN          | 索引（INDEX）                 | 3                                        | 本端规划   | 配置共享UPF支持的DNN。                                                                                          |
| ADD PNFDNN          | NF实例标识（NFINSTANCEID）      | UPF_Instance_0                           | 全网规划   | 配置共享UPF支持的DNN。                                                                                          |
| ADD PNFDNN          | 数据网络名称（DNN）               | Huawei.com                               | 全网规划   | 配置共享UPF支持的DNN。                                                                                          |
| ADD PNFDNAI         | 索引（INDEX）                 | 1                                        | 本端规划   | 配置共享UPF支持的DNAI。                                                                                         |
| ADD PNFDNAI         | NF实例标识（NFINSTANCEID）      | UPF_Instance_0                           | 全网规划   | 配置共享UPF支持的DNAI。                                                                                         |
| ADD PNFDNAI         | 数据网络访问标识（DNAI）            | testdnai                                 | 本端规划   | 配置共享UPF支持的DNAI。                                                                                         |
| ADD PNFDNAI         | 对端NF的DNN索引（PNFDNNINDEX）   | 3                                        | 全网规划   | 配置共享UPF支持的DNAI。                                                                                         |
| ADD UPNODE          | UPF实例名称（NFINSTANCENAME）   | UPF_Instance_0                           | 全网规划   | 配置共享UPF的属性。                                                                                             |
| ADD UPNODE          | UP位置特征（LOCATION）          | Central                                  | 全网规划   | 配置共享UPF的属性。                                                                                             |
| ADD UPNODE          | UP支持功能（UPFUNCTION）        | UlClAndBp                                | 全网规划   | 配置共享UPF的属性。                                                                                             |
| ADD UPNODE          | UPF共享开关（SHAREDUPFSW）      | ENABLE                                   | 本端规划   | 共享UPF场景下本参数取值为“ENABLE”。                                                                                 |
| ADD VIRTUALUPFID    | UPF实例标识（UPFINSTANCEID）    | UPF_Instance_0                           | 全网规划   | 配置虚拟UPF实例标识和DNAI的绑定关系。 共享UPF场景下通过配置虚拟UPF标识辅锚点会话，并且为虚拟UPF配置DNAI，UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别辅锚点N4会话。 |
| ADD VIRTUALUPFID    | 虚拟UPF实例标识（VUPFINSTANCEID） | v_UPF_Instance_0                         | 本端规划   | 配置虚拟UPF实例标识和DNAI的绑定关系。 共享UPF场景下通过配置虚拟UPF标识辅锚点会话，并且为虚拟UPF配置DNAI，UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别辅锚点N4会话。 |
| ADD VUPFIDBINDDNAI  | 虚拟UPF实例标识（VUPFINSTANCEID） | v_UPF_Instance_0                         | 本端规划   | 配置虚拟UPF实例标识和DNAI的绑定关系。 共享UPF场景下通过配置虚拟UPF标识辅锚点会话，并且为虚拟UPF配置DNAI，UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别辅锚点N4会话。 |
| ADD VUPFIDBINDDNAI  | 数据网络访问标识（DNAI）            | testdnai                                 | 全网规划   | 配置虚拟UPF实例标识和DNAI的绑定关系。 共享UPF场景下通过配置虚拟UPF标识辅锚点会话，并且为虚拟UPF配置DNAI，UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别辅锚点N4会话。 |
| ADD UPAREA          | UP位置区名称（AREANAME）         | UPAREA1                                  | 全网规划   | 配置位置区域。                                                                                                 |
| ADD UPAREA          | AREA类型（AREATYPE）          | N2TAI                                    | 全网规划   | 配置位置区域。                                                                                                 |
| ADD UPAREABINDN2TAI | UP位置区名称（AREANAME）         | UPAREA1                                  | 全网规划   | 为位置区添加区域范围。                                                                                             |
| ADD UPAREABINDN2TAI | N2TAI范围开始值（N2BEGINTAI）    | 1230320101                               | 全网规划   | 为位置区添加区域范围。                                                                                             |
| ADD UPAREABINDN2TAI | N2TAI范围结束值（N2ENDTAI）      | 1230320103                               | 全网规划   | 为位置区添加区域范围。                                                                                             |
| ADD PNFSMFSERAREA   | NF实例标识（NFINSTANCEID）      | UPF_Instance_0                           | 全网规划   | 配置共享UPF支持的区域。                                                                                           |
| ADD PNFSMFSERAREA   | SMF服务区域（SMFSERVINGAREA）   | UPAREA1                                  | 全网规划   | 配置共享UPF支持的区域。                                                                                           |

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. SMF本端配置共享UPF。

   **ADD PNFPROFILE**
4. 配置共享UPF支持的服务切片信息。

   **ADD PNFNS**
5. 配置共享UPF支持的DNN。

   **ADD PNFDNN**
6. 配置共享UPF支持的DNAI信息。

   **ADD PNFDNAI**
7. 配置共享UPF的属性。

   **ADD UPNODE**
8. 配置虚拟UPF实例标识和DNAI的绑定关系。

   - 配置虚拟UPF实例。

     **ADD VIRTUALUPFID**
   - 配置虚拟UPF实例和DNAI的绑定关系。

     **ADD VUPFIDBINDDNAI**
9. 配置共享UPF的服务区域。

   - 配置用于SMF本端判定共享UPF归属区域的区域类型。

     **ADD UPAREA**
   - 配置共享UPF归属区域对应的区域范围。

     **ADD UPAREABINDN2TAI**
   - SMF本端配置共享UPF所覆盖的区域。

     **ADD PNFSMFSERAREA**
10. **可选：**配置为指定ULCL用户选择特性共享UPF。当ULCL用户从5G网络接入时，如果要求SMF能够为ULCL用户（例如某校园网用户）优选特性的共享UPF避免N9流量过大时，可以执行本步骤。
    1. 配置指定DNAI的UPF信息。

       **ADD DNAIUPFINFO**
    2. 在APN下开启SMF在分流场景下优先共享UPF开关。设置“SHAREDPRIFLAG”为“ENABLE”。

       **SET APNUPSELPLY**
    3. 配置DNAI粒度的优选共享UPF的开关。如果在2中已经开启APN粒度的优选共享UPF开关，此时本步骤中的“SHAREDPRIFLAG”设置为“INHERIT”即可，如果2中没有设置，需要将本步骤中的“SHAREDPRIFLAG”设置为“ENABLE”。

       **ADD DNAIUPSELPLY**
11. 配置N4接口下发DNAI信元。

    **SET PFCPPVTEXT**

## 任务示例

任务描述

运营商要为某企业园区建立网络，希望接入园区的用户可以使用同一个DNN访问公网以及私网业务。

现网部署共享UPF，即主锚点UPF和“UL CL UPF+辅锚点UPF”合一部署，主锚点对接公网Internet，辅锚点对接本地私网，且为共享UPF规划了UPF服务区域，UPF覆盖的TA区域为“1230320101”~“1230320110”。园区内“1230320101”~“1230320103”是某场馆，运营商希望当用户进入到场馆内时，可以通过手机扫描二维码来享受场馆自动解说的服务，此时可以将场馆的TAI范围绑定对应的DNAI，合一部署的UPF会对用户进入场馆进行场景解说的业务进行分流。

假定该园区的APN为Huawei.com，对应的UPF实例标志分别为UPF\_Instance\_0，对应的IP地址为192.168.126.11。当用户接入时，为用户根据DNN、切片、DNAI等信息选择到共享UPF，实现使用同一个DNN访问公网以及私网业务。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2SUPFS01", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV2SUPFS02", SWITCH=ENABLE;
```

//SMF本端添加共享UPF。

```
ADD PNFPROFILE:NFINSTANCEID="UPF_Instance_0", NFTYPE=NfUPF, NFSTATUS=Registered,FQDN="upf00.node.mnc003.mcc123.3gppnetwork.org",IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="192.168.126.11";
```

//配置共享支持的服务切片信息。

```
ADD PNFNS: INDEX=3, NFINSTANCEID="UPF_Instance_0", SST=1, SD="000001";
```

//配置共享UPF的支持的DNN。

```
ADD PNFDNN:INDEX=3, NFINSTANCEID="UPF_Instance_0", DNN="Huawei.com";
```

//配置共享UPF支持的DNAI信息。

```
ADD PNFDNAI: INDEX=1,NFINSTANCEID="UPF_Instance_0", DNAI="testdnai",PNFDNNINDEX=3;
```

//配置共享UPF的属性。

```
ADD UPNODE:NFINSTANCENAME="UPF_Instance_0", LOCATION=Central, UPFUNCTION=UlClAndBp, SHAREDUPFSW=ENABLE;
```

//配置虚拟UPF实例。

```
ADD VIRTUALUPFID:UPFINSTANCEID="UPF_Instance_0", VUPFINSTANCEID="v_UPF_Instance_0";
```

//配置虚拟UPF实例和DNAI的绑定关系。

```
ADD VUPFIDBINDDNAI:VUPFINSTANCEID="v_UPF_Instance_0", DNAI="testdnai";
```

//配置用于SMF本端判定共享UPF归属区域的区域类型。

```
ADD UPAREA:AREANAME="UPAREA1", AREATYPE=N2TAI;
```

//配置共享UPF归属区域对应的区域范围。

```
ADD UPAREABINDN2TAI:AREANAME="UPAREA1", N2BEGINTAI="12303260101", N2ENDTAI="12303260110";
```

//SMF本端配置共享UPF所覆盖的区域。

```
ADD PNFSMFSERAREA:NFINSTANCEID="UPF_Instance_0", SMFSERVINGAREA="UPAREA1";
```

//配置N4接口下发DNAI信元。

```
SET PFCPPVTEXT: FEATURE=DNAI, SWITCH=ENABLE;
```

//配置场馆的DNAI支持的服务区域。

//配置DNAI的服务区域。

```
ADD DNAREA: AREANAME="DNAREA1", AREATYPE=N2TAI;
```

//配置DNAI服务区名称绑定的5G TAI范围。

```
ADD DNAREABINDN2TAI: AREANAME="DNAREA1", N2BEGINTAI="12303260101", N2ENDTAI="12303260103";
```

//配置DNAI支持的服务区域名称。

```
ADD DNAIBINDDNAREA: DNAI="stadiumdnai", AREANAME="DNAREA1";
```