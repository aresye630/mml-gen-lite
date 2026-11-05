# 激活VoLTE紧急呼叫（适用于MME）

## 操作场景

本操作指导介绍在运行网络中激活VoLTE紧急呼叫特性的操作过程。

适用于MME。

## 必备事项

前提条件

* 请仔细阅读GWFD-025403 VoLTE紧急呼叫。
* 已完成加载License。
* 部署VoLTE紧急呼叫特性需要在MME、SGW-C、PGW-C、MSC、eNodeB等网元上首先完成基本业务的数据配置。
* 运营商已经通过**ADD HPLMN**、**ADD MVNONET**或**ADD CONNECTPLMN**配置了运营商标识（MNOID/MVNOID/NOID）。
* VOLTE紧急呼叫号码下发会影响终端存储的紧急呼叫号码列表，当终端回落到2/3G发起紧急呼叫时，需要MSC配置紧急呼叫类型和对应号码的映射关系，详细配置请咨询MSC技术支持。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET MMFUNC** | 是否支持紧急号码（EMNUM） | YES（支持） | 全网规划 | 开启紧急呼叫功能。 |
| **ADD EMGCNUM** | 移动国家码（MCC） | 123 | 全网规划 | 配置紧急号码信息。 |
|  | 紧急服务分类（ESC） | FIREBRIGADE |  |  |
|  | 紧急呼叫号码（NUM） | 119 |  |  |
| **ADD EMGCFG** | 运营商标识（NOID） | 128 | 全网规划 | 配置紧急呼叫功能参数。  该NOID必须已经通过****ADD MNO****的“MNOID”或者****ADD MVNO****的“MVNOID”配置。 |
|  | 紧急承载创建模式（EMGMODE） | ALLUE |  |  |
|  | 紧急APN（EMGAPN） | EMG |  |  |
|  | 紧急APN的上行APN AMBR速率（kbit/s）（ULAPNAMBR） | 10000 |  |  |
|  | 紧急APN的下行APN AMBR速率（kbit/s）（DLAPNAMBR） | 10000 |  |  |
|  | 紧急承载的QCI（QCI） | 5 |  |  |
|  | 紧急ARP优先级级别（ARPPRL） | 1 |  |  |
|  | 紧急ARP的Pre-emption Capability（ARPPCI） | YES |  |  |
|  | 紧急ARP的Pre-emption Vulnerability（ARPPVI） | NO |  |  |
| **ADD PGWESTNSR** | PGW的IP地址类型（IPT） | IPV4 | 全网规划 | 配置E-STN-SR和PGW-C关系。  与华为MSC设备对接才需要配置。 |
|  | PGW的IPV4地址（PGWIPV4） | 10.10.10.10 |  |  |
|  | PGW的IPV4地址掩码（IPV4MSK） | 255.255.255.255 |  |  |
|  | SRVCC的紧急会话转移号码（ESTNSR） | 11111 |  |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. 配置紧急号码信息。

   紧急呼叫号码必须是运营商已经规划的号码，需要正确配置。配置错误可能导致UE的紧急呼叫接入错误，例如：

   * 将非紧急呼叫号码配置为紧急呼叫号码，用户被接入至政府部门。
   * 紧急服务分类配置错误，用户被错误接入其他政府部门。
   * VOLTE紧急呼叫号码下发会影响终端存储的紧急呼叫号码列表，当终端回落到2/3G发起紧急呼叫时，需要MSC配置紧急呼叫类型和对应号码的映射关系，详细配置请咨询MSC技术支持。

   **SET MMFUNC**

   **ADD EMGCNUM**
4. 配置下发紧急号码。

   **SET SOFTPARAOFBIT**

   * 需要在GPRS/UMTS网络下发紧急号码时，设置软参DWORD\_EX6 BIT10为0。
   * 需要在EPS网络下发紧急号码时：

     + 如果仅对支持VoLTE语音业务的用户下发紧急呼叫号码，则将DWORD\_EX6 BIT11配置为0，将DWORD\_EX12 BIT16配置为1。
     + 如果对EPS网络下的所有用户下发紧急呼叫号码，则将DWORD\_EX6 BIT11配置为0。
5. 配置紧急呼叫功能参数。

   **ADD EMGCFG**
6. **可选：**配置E-STN-SR和PGW-C关系。

   **ADD PGWESTNSR**

   与华为MSC设备对接才需要配置此步骤。
7. **可选：**配置优化的寻呼参数。

   **SET EMM**

   紧急呼叫的寻呼重发采用优化的寻呼参数，详情参见特性GWFD-025401 VoLTE基础语音业务。
8. **可选：**获取紧急呼叫用户IMEI信息。

   **ADD S1IMEICFG**

   为保证“有USIM卡的受限用户”在鉴权失败的场景下紧急呼叫的SRVCC切换成功，建议MME开启获取IMEI信息功能。
9. **可选：**配置PLMN的用户禁止使用VoLTE紧急呼叫业务。

   如果某PLMN的用户在PS域无法完成VoLTE紧急呼叫，需要配置此步骤使该类用户在CS域重新发起紧急呼叫业务。否则跳过此步骤。
   * 如果是归属地PLMN的用户，则执行如下命令配置。

     **MOD HPLMN**
   * 如果是互联PLMN的用户，则执行如下命令配置。

     **MOD CONNECTPLMN**
   * 如果是MVNO网络的用户，则执行如下命令配置。

     **RMV MVNONET**

     **ADD MVNONET**

## 任务示例

任务描述

某运营商已接入VoLTE网络，且已通过**ADD HPLMN**/**ADD MVNONET**/**ADD CONNECTPLMN**命令为该运营商增加了配置信息，指定运营商的国家码为“123”，运营商的标识（NOID）为128。现在为该运营商启用火警VoLTE紧急呼叫业务，配置火警紧急号码为119。

脚本

//进入“MML命令行-UEG”窗口。

//配置紧急号码信息。

```
SET MMFUNC: EMNUM=YES;
ADD EMGCNUM: MCC="123", ESC=POLICE-0&AMBULANCE-0&FIREBRIGADE-1&MARINEGUARD-0&MOUNTAIN-0, NUM="119";
```

//配置在GPRS/UMTS下发紧急呼叫号码列表。

```
SET SOFTPARAOFBIT: DT=DWORD_EX, PARANUM=6, VALUE=VALUE_0, POSITION=10;
```

//配置在EPC网络下发紧急号码，并且 EPS网络下仅对支持VoLTE语音业务的用户下发紧急呼叫号码。

```
SET SOFTPARAOFBIT: DT=DWORD_EX, PARANUM=6, VALUE=VALUE_0, POSITION=11;
SET SOFTPARAOFBIT: DT=DWORD_EX, PARANUM=12, VALUE=VALUE_1, POSITION=16;
```

//配置紧急呼叫功能参数。

```
ADD EMGCFG: NOID=128, EMGMODE=ALLUE,EMGAPN="EMG", ULAPNAMBR=10000, DLAPNAMBR=10000, QCI=5, ARPPRL=1, ARPPCI=YES, ARPPVI=NO;
```

//（可选）配置E-STN-SR和PGW-C关系。

```
ADD PGWESTNSR: IPT=IPV4, PGWIPV4="10.10.10.10", IPV4MSK="255.255.255.255", ESTNSR="11111";
```

//（可选）配置优化的寻呼参数。

```
SET EMM: HPT3413=2, HPN3413=4, HPPAGINGDELTA=0;
```

//（可选）获取紧急呼叫用户IMEI信息。

```
ADD S1IMEICFG: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456", GETIMEIPLC=IMEISV;
```

//配置PLMN的用户禁止使用VoLTE紧急呼叫业务。

//（可选）配置归属地PLMN的用户禁止使用VoLTE紧急呼叫。执行该命令前请先通过**LST HPLMN**查询当前是否已增加归属地PLMN配置信息。根据查询结果，选择是否配置该参数。

```
MOD HPLMN: MCC="123", MNC="00", EMCBS=NO;
```

//（可选）配置互联PLMN的用户禁止使用VoLTE紧急呼叫。执行该命令前请先通过**LST CONNECTPLMN**查询当前是否已增加互联PLMN配置信息。根据查询结果，选择是否配置该参数。

```
MOD CONNECTPLMN: MCC="123", MNC="00", EMCBS=NO;
```

//（可选）配置MVNO网络的用户禁止使用VoLTE紧急呼叫。执行该命令前请先通过**LST MVNONET**查询当前是否已增加MVNO网络配置信息。根据查询结果，选择是否配置该参数。

```
RMV MVNONET: MVNOID=1;
ADD MVNONET: MVNOMCC="123", MVNOMNC="00", MATCHIMSI="111", MVNOCC="860", MVNOID=1, EMCBS=NO;
```

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2VLEC01", SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
