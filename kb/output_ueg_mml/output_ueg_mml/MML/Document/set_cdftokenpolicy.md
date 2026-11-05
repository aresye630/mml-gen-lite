# 设置CDF token策略（SET CDFTOKENPOLICY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

当CDFTOKENPOLICY开关配置为使能且设置cdf token权重时，会影响各个cgfa-pod与cgfb-pod或cgfa2-pod与cgfb2-pod之间的token权重分配，从而影响话务量均衡。

**适用NF：NCG**

该命令用于设置cdf token权重上报开关。

当需要上报cdf token权重时，可配置cdf权重开关为使能。

## 注意事项

- 该命令执行后需要重新启动系统才能生效。

- 该命令需重启DCF进程才会生效。重启DCF进程的命令如下：
- RST MSPROCESS: PROCOBJECT=PROCNAME, PROCNAME="CELL\_DCF";

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| WEIGHTSWITCH   |
|:---------------|
| ENABLE         |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称          | 参数说明                                                                                                                                                       |
|:-------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| WEIGHTSWITCH | cdf token权重开关 | 可选必选说明：必选参数  参数含义：设置CDF token权重开关。  数据来源：本端规划 取值范围： “ENABLE（使能）”：需要上报cdf token权重时，需要配置权重开关为使能“DISABLE（不使能）”：不需要上报cdf token权重时，需要配置权重开关为不使能  默认值：无。  配置原则：无 |

## 使用实例

设置cdf token权重开关为使能：

```
+++    UNC/*MEID:0 MENAME:UNC_VNF_ncg001*/        2022-05-24 20:25:44+8:00
O&M    #3935
%%SET CDFTOKENPOLICY: WEIGHTSWITCH=ENABLE;%%
RETCODE = 0  操作成功

---    END
```