# 删除FQDN路由（RMV NRFFQDNRT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于删除FQDN路由信息。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                     |
|:---------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE         | NF类型     | 可选必选说明：必选参数  参数含义：该参数用于表示支持FQDN路由寻址的NF类型。  数据来源：全网规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无  配置原则：无 |
| FQDNSUFFIX     | 域名后缀     | 可选必选说明：必选参数  参数含义：该参数用于表示域名的最长匹配后缀。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，FQDN后缀不能以“.”开始，也不能以“.”结束。  默认值：无  配置原则：无                                                                                                                                         |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数  参数含义：该参数用于表示当前NRF基于域名的最长后缀匹配寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~64。  默认值：无  配置原则：  该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。                                                                                                                              |

## 使用实例

运营商网络为三层网络，最高层PLMN-NRF，中间层H-NRF，最底层L-NRF。L-NRF1归属于H-NRF1，H-NRF1归属于PLMN-NRF。在H-NRF1和PLMN-NRF上分别执行如下命令，删除NF类型为PCF，域名后缀为"huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org"的路由信息。

```
RMV NRFFQDNRT: NFTYPE=SMF, FQDNSUFFIX="huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org", NEXTNRFGRPNAME="L-NRF1";
```