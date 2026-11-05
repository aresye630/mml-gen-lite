# 查询北向NF实例信息（LST UNCVNFINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、MME、SMSF、CHF**

该命令用于查询北向NF实例信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NRMNETYPE     | 北向网元设备类型 | 可选必选说明：可选参数  参数含义：北向网元设备类型。  数据来源：本端规划 取值范围： “AMF（AMF）”：AMF“SMF（SMF）”：SMF，PGWC，SGWC，GGSNC“NRF（NRF）”：NRF“NSSF（NSSF）”：NSSF“MME（MME）”：MME“SMSF（SMSF）”：SMSF“CHF（CHF）”：CHF“AMF_MME_SGSN（AMF_MME_SGSN）”：AMF，MME，SGSN“AMF_MME（AMF_MME）”：AMF，MME“MME_SGSN（MME_SGSN）”：MME，SGSN“SMFONLY（SMFONLY）”：SMF“SMF_PGWC（SMF_PGWC）”：SMF，PGWC“SMF_PGWC_SGWC（SMF_PGWC_SGWC）”：SMF，PGWC，SGWC“PGWC_SGWC_GGSNC（PGWC_SGWC_GGSNC）”：PGWC，SGWC，GGSNC“ProxySGWC（ProxySGWC）”：ProxySGWC“CCG（CCG）”：CCG“SMF_SGWC（SMF_SGWC）”：SMF_SGWC“SAEGWC（SAEGWC）”：SAEGWC“ProxySMF_ProxySGWC_PGWC（ProxySMF_ProxySGWC_PGWC）”：ProxySMF，ProxySGWC，PGWC“SMF_PGWC_GGSNC（SMF_PGWC_GGSNC）”：SMF，PGWC，GGSNC  默认值：无  配置原则：无 |
| VNFINSTANCEID | 北向VNF实例号 | 可选必选说明：可选参数  参数含义：北向VNF实例号，该值从LCM通过VNF总览中选择对应的VNF，获取对应的VNF ID的值。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~64。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## 使用实例

查询所有UNC北向网元实例信息:

```
%%LST UNCVNFINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
北向网元设备类型  =  AMF
   北向VNF实例号  =  13204e79601644eb942eb4ae7dd6419b
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称    | 输出项解释                                          |
|:---------|:-----------------------------------------------|
| 北向网元设备类型 | 北向网元设备类型。                                      |
| 北向VNF实例号 | 北向VNF实例号，该值从LCM通过VNF总览中选择对应的VNF，获取对应的VNF ID的值。 |