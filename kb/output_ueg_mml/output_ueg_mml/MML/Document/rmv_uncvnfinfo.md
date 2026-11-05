# 删除北向NF实例信息（RMV UNCVNFINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、MME、SMSF、CHF**

该命令用于删除北向NF实例信息。

## 注意事项

- 该命令执行后立即生效。

- 删除北向实例会导致该网元不上报北向数据，请谨慎操作。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NRMNETYPE     | 北向网元设备类型 | 可选必选说明：必选参数  参数含义：北向网元设备类型。  数据来源：本端规划 取值范围： “AMF（AMF）”：AMF“SMF（SMF）”：SMF，PGWC，SGWC，GGSNC“NRF（NRF）”：NRF“NSSF（NSSF）”：NSSF“MME（MME）”：MME“SMSF（SMSF）”：SMSF“CHF（CHF）”：CHF“AMF_MME_SGSN（AMF_MME_SGSN）”：AMF，MME，SGSN“AMF_MME（AMF_MME）”：AMF，MME“MME_SGSN（MME_SGSN）”：MME，SGSN“SMFONLY（SMFONLY）”：SMF“SMF_PGWC（SMF_PGWC）”：SMF，PGWC“SMF_PGWC_SGWC（SMF_PGWC_SGWC）”：SMF，PGWC，SGWC“PGWC_SGWC_GGSNC（PGWC_SGWC_GGSNC）”：PGWC，SGWC，GGSNC“ProxySGWC（ProxySGWC）”：ProxySGWC“CCG（CCG）”：CCG“SMF_SGWC（SMF_SGWC）”：SMF_SGWC“SAEGWC（SAEGWC）”：SAEGWC“ProxySMF_ProxySGWC_PGWC（ProxySMF_ProxySGWC_PGWC）”：ProxySMF，ProxySGWC，PGWC“SMF_PGWC_GGSNC（SMF_PGWC_GGSNC）”：SMF，PGWC，GGSNC  默认值：无  配置原则：无 |
| VNFINSTANCEID | 北向VNF实例号 | 可选必选说明：必选参数  参数含义：北向VNF实例号，该值从LCM通过VNF总览中选择对应的VNF，获取对应的VNF ID的值。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~64。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## 使用实例

删除UNC北向网元实例信息，其设备类型为AMF，VNF实例号为13204e79601644eb942eb4ae7dd6419b，执行以下命令：

```
RMV UNCVNFINFO: NRMNETYPE=AMF, VNFINSTANCEID="13204e79601644eb942eb4ae7dd6419b";
```