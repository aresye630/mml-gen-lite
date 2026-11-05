# 显示GB性能统计实时结果(DSP RTMPERFCNTGB)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 参考信息

#### 命令功能

**适用网元：MME**

该命令用于实时查看GB\_VNFC当前性能统计的情况，即查询某一对象实例的某一单元下所有指标的当前性能统计值。

#### 注意事项

- 系统最多支持5个用户并发执行该命令。
- 由于各进程、各类型指标的采样点不能完全统一，因此指标结果存在一定的误差，统计误差最大不超过该指标在10s内的统计变化值。
- 测量周期前10s执行该命令查看性能统计，“查询结果”会返回“Result is UnReliable”，如果出现了此现象，可等待10s再查询。
- 使用该命令查询之前需要先在U2020/MAE上创建基于该测量对象实例的话统统计任务，等待5min后再执行相应查询命令。基于SGSN对象的话统指标不需要创建统计任务，该对象的测量单元可直接查询。
- 此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:-------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MOC    | 测量对象   | 可选必选说明：必选参数。 参数含义：测量对象类ID。 数据来源：本端规划。 取值范围：“NSE(Gb接口NSE)”“SGSN(USN function)”“BSSID(Gb接口BSSID)”“CELL(小区号)”“IMSI(IMSI号码)”“RU(资源单元)”“IP_NSVCI_ENDPOINT(Gb接口端点IP NSVC)”“ScaleGroup(ScaleGroup)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MOI    | 实例名称   | 可选必选说明：必选参数。 参数含义：测量对象实例。 数据来源：本端规划。 前提条件：该测量实例已经在U2020/MAE上话统测量管理（通过“性能->测量管理”菜单打开）中下发，SGSN对象类实例除外。 取值范围：1~63位字符串 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| MUID   | 测量单元   | 可选必选说明：必选参数。 参数含义：测量对象对应的测量单元。 数据来源：本端规划。 取值范围： 该参数在“MOC”参数设置为“NSE(Gb接口NSE)”时：“PERF_TYPE_GB_NSE(指定NSE NS)”“PERF_TYPE_GB_BSSGP_NSE(指定NSE BSSGP)” 该参数在“MOC”参数设置为“SGSN(USN function)”时：“PERF_TYPE_GB_LLC(SGSN LLC)”“PERF_TYPE_GB_SNDCP(SGSN SNDCP)”“PERF_TYPE_GB_BSSGP_ALL(SGSN BSSGP)”“PERF_TYPE_GB_NS(SGSN NS)”“PERF_TYPE_GB_CIPHER(SGSN 加密)”“PERF_TYPE_GB_RESOURCE(SGSN Gb资源)”“PERF_TYPE_GB_IP_NS(NS子层IP测量)”“PERF_TYPE_IP_PACKETS(转发面报文统计)”“PERF_TYPE_REDUNDANCY(设备级容灾业务)” 该参数在“MOC”参数设置为“IP_NSVCI_ENDPOINT(Gb接口端点IP NSVC)”时：“PERF_TYPE_GB_LLC(SGSN LLC)” 该参数在“MOC”参数设置为“RU(资源单元)”时：“PERF_TYPE_RU_CPU_RESOURCE(资源单元CPU资源_GB)” 该参数在“MOC”参数设置为“ScalGroup(ScalGroup)”时:“PERF_TYPE_SCALEGROUP_WORKLOAD(ScalGroup负载_GB)” |

#### 使用实例

查询“SGSN”对象的“NS子层IP测量”单元下的所有指标的当前实时统计值：

DSP RTMPERFCNTGB:MOC=SGSN,MOI="0",MUID=PERF\_TYPE\_GB\_IP\_NS;

```
%%DSP RTMPERFCNTGB: MOC=SGSN, MOI="0", MUID=PERF_TYPE_GB_IP_NS;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
Measurement Result

Result is Reliable!

NS Uplink packets received from IP(ENTRIES) = 0
NS Uplink data Kbytes received from IP(KBytes) = 0
NS Downlink packets sent to IP(ENTRIES) = 0
NS Downlink data Kbytes sent to IP(KBytes) = 0
NS Uplink IP packets discarded(ENTRIES) = 0
NS Uplink IP data Kbytes discarded(KBytes) = 0
NS Downlink IP packets discarded(ENTRIES) = 14
NS Downlink IP data Kbytes discarded(KBytes) = 0

(Number of results = 2)

---    END
```

#### 参考信息

| 测量对象类                           | 对象实例数据获取参考   | 对象实例输入格式                  | 输入格式示例                                     |
|:--------------------------------|:-------------|:--------------------------|:-------------------------------------------|
| NSE：Gb接口NSE                     | LST PERFNSE  | NSE标识                     | "12"                                       |
| SGSN：USN function               | 0            | "0"                       | "0"                                        |
| IMSI：IMSI号码                     | IMSI号码       | IMSI号码                    | "123031600000002"                          |
| RU: 资源单元                        | DSP RU       | 资源单元名称                    | "USN_SP_RU_0064"                           |
| CELL：小区号                        | LST CELL     | 小区号                       | "123054804041026(123-05-18436-4-4134)"     |
| BSSID：Gb接口BSSID                 | LST NSE      | BSS编号                     | "133"                                      |
| IP_NSVCI_ENDPOINT：Gb接口端点IP NSVC | DSP IPNSVC   | 本端IP地址：本端端口号：对端IP地址：对端端口号 | "192.168.152.1:31201:192.168.152.20:31201" |
| ScalGroup:ScalGroup 名字          | DSP WORKLOAD | ScaleGroup的名字             | "SG1_USN"                                  |