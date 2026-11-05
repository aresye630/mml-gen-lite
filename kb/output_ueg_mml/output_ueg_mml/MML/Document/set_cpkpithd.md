# 设置KPI门限(SET CPKPITHD)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 参考信息

#### 命令功能

**适用网元：SGSN、MME**

该命令用于设置KPI监控功能的KPI门限值。

#### 注意事项

- 请谨慎执行该命令。修改初始设置时，请依据具体情况设置对应指标名称的门限值和最小业务量。
- 该命令设置成功后1分钟内生效。
- 设置KPI门限值前，请先通过命令开启KPI监控功能。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:---------------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MONGRANULARITY | 监控粒度     | 可选必选说明：必选参数 参数含义：该参数用来设置监控粒度。 数据来源：本端规划。 取值范围： “SYSTEM(整系统)”：控制整系统监控粒度“PROCESS(单进程)”：控制单个进程监控粒度 配置原则：系统目前仅支持“PROCESS(单进程)”。 系统初始设置值：请参考系统默认配置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| KPINAME        | KPI名称    | 可选必选说明：必选参数 参数含义：该参数用来设置KPI名称。 数据来源：本端规划。 取值范围： 仅支持以下选项。 “2G_ATTACH_BY_PROC(基于进程的Gb模式附着成功率(网络原因))”：基于进程的Gb模式附着成功率(网络原因)“2G_SGSN_RAU_BY_PROC(基于进程的Gb模式SGSN内路由区更新成功率(网络原因))”：基于进程的Gb模式SGSN内路由区更新成功率(网络原因)“2G_ACTIVE_BY_PROC(基于进程的Gb模式MS激活会话成功率(网络原因))”：基于进程的Gb模式MS激活会话成功率(网络原因)“3G_ATTACH_BY_PROC(基于进程的Iu模式附着成功率(网络原因))”：基于进程的Iu模式附着成功率(网络原因)“3G_SGSN_RAU_BY_PROC(基于进程的Iu模式SGSN内路由区更新成功率(网络原因))”：基于进程的Iu模式SGSN内路由区更新成功率(网络原因)“3G_ACTIVE_BY_PROC(基于进程的Iu模式MS激活会话成功率(网络原因))”：基于进程的Iu模式MS激活会话成功率(网络原因)“3G_SERVICE_REQUEST_BY_PROC(基于进程的Iu模式Service request成功率(网络原因))”：基于进程的Iu模式Service request成功率(网络原因)“4G_ATTACH_BY_PROC(基于进程的S1模式附着成功率(网络原因))”：基于进程的S1模式附着成功率(网络原因)“4G_COMBINE_ATTACH_BY_PROC(基于进程的S1模式联合附着成功率(网络原因))”：基于进程的S1模式联合附着成功率(网络原因)“4G_MME_TAU_BY_PROC(基于进程的S1模式MME内TAU成功率(网络原因))”：基于进程的S1模式MME内TAU成功率(网络原因)“4G_MME_X2_HANDOVER_BY_PROC(基于进程的S1模式MME内X2 Handover成功率(网络原因))”：基于进程的S1模式MME内X2 Handover成功率(网络原因)“4G_MME_S1_HANDOVER_BY_PROC(基于进程的S1模式MME内S1 Handover成功率(网络原因))”：基于进程的S1模式MME内S1 Handover成功率(网络原因)“4G_SERVICE_REQUEST_BY_PROC(基于进程的S1模式 Service request成功率(网络原因))”：基于进程的S1模式 Service request成功率(网络原因)“4G_DEDICATED_BEARER_BY_PROC(基于进程的S1模式专有承载激活成功率(网络原因))”：基于进程的S1模式专有承载激活成功率(网络原因)“4G_EXTENDED_SRV_REQUEST_PROC(基于进程的S1模式Extended Service request成功率)”：基于进程的S1模式Extended Service request成功率 系统初始设置值：请参考系统默认配置。 |
| MONTY          | 监控类型     | 可选必选说明：必选参数 参数含义：该参数用来设置KPI指标监控类型。 数据来源：本端规划。 取值范围： “ABSOLUTE_VALUE(绝对值)”：绝对值“RELATIVE_VALUE(相对值)”：相对值 配置原则：系统目前仅支持“RELATIVE_VALUE(相对值)” 系统初始设置值：请参考系统默认配置。  说明： 绝对值：以某周期实际上报指标值与设置的“绝对门限值”比较，按照多周期系统比较结果来确定是否上报告警。相对值：以间隔周期指标值对比变化率与设置的“相对门限值”进行比较，系统根据比较结果来确定是否上报告警。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| MINTRAFFIC     | 最小业务量    | 可选必选说明：可选参数 参数含义：该参数用来设置最小业务量。当实际业务量小于最小业务量时，监控KPI功能失效。业务量是指业务请求次数的性能指标值。单位为次数。 数据来源：本端规划。 取值范围：1-4294967295 系统初始设置值：请参考系统默认配置。  说明： 请谨慎修改该值。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ABSTHD         | 绝对门限值    | 可选必选说明：条件可选参数 取值范围：0-4294967295 参数含义：该参数手动设置无效，系统根据当前实际业务情况自动设置。 配置原则：系统目前不支持                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| RELATHD        | 相对门限值(%) | 可选必选说明：条件可选参数 参数含义：该参数用来设置监控类型为相对值类型的门限值。如果当前周期（周期为五分钟）、当前周期之后第一个周期以及当前周期之后第二个周期性能指标值分别与当前周期之前第二个周期性能指标值的比值均低于相对门限值，则判断为当前周期故障。目前系统只支持监控进程粒度的成功率指标。 数据来源：本端规划。 取值范围：1-100 系统初始设置值：请参考系统默认配置。  说明： 请谨慎修改该值。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

#### 使用实例

设置监控粒度为单进程，KPI名称为基于进程的Gb模式附着成功率(网络原因)，监控类型为相对值，最小业务量为100，相对值门限为70%。（由于该KPI监控指标为成功率，因此该指标的相对值门限单位为百分比）。

SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=2G\_ATTACH\_BY\_PROC, MONTY=RELATIVE\_VALUE, MINTRAFFIC=100, ABSTHD=70;

#### 参考信息

系统默认配置如下：

```
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=2G_ATTACH_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=2G_SGSN_RAU_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=2G_ACTIVE_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=3G_ATTACH_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=3G_SGSN_RAU_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=3G_ACTIVE_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=3G_SERVICE_REQUEST_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=4G_ATTACH_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=4G_COMBINE_ATTACH_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=4G_MME_TAU_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=4G_MME_X2_HANDOVER_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=4G_MME_S1_HANDOVER_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=4G_SERVICE_REQUEST_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=4G_DEDICATED_BEARER_BY_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
SET CPKPITHD: MONGRANULARITY=PROCESS, KPINAME=4G_EXTENDED_SRV_REQUEST_PROC, MONTY=RELATIVE_VALUE, MINTRAFFIC=100, RELATHD=40;
```