# 增加FQDN路由（ADD NRFFQDNRT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于FQDN最长后缀匹配的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

如果针对同一个FQDN配置了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入10240条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                     |
|:---------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE         | NF类型     | 可选必选说明：必选参数  参数含义：该参数用于表示支持FQDN路由寻址的NF类型。  数据来源：全网规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无  配置原则：无 |
| FQDNSUFFIX     | 域名后缀     | 可选必选说明：必选参数  参数含义：该参数用于表示域名的最长匹配后缀。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，FQDN后缀不能以“.”开始，也不能以“.”结束。  默认值：无  配置原则：无                                                                                                                                         |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数  参数含义：该参数用于表示当前NRF基于域名的最长后缀匹配寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~64。  默认值：无  配置原则：  该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。                                                                                                                              |

## 使用实例

- 运营商网络为三层组网，最高层PLMN-NRF，中间层H-NRF，最底层L-NRF。L-NRF1归属于H-NRF1，H-NRF1归属于PLMN-NRF，当跨NRF进行服务发现时，希望发现的目标NF类型为PCF，域名后缀为"huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org"，归属于L-NRF1，则需要在H-NRF1和PLMN-NRF上分别配置如下路由信息。在H-NRF1上执行：

  ```
  ADD NRFFQDNRT: NFTYPE=SMF, FQDNSUFFIX="huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org", NEXTNRFGRPNAME="L-NRF1";
  ```
- 在PLMN-NRF上执行：

  ```
  ADD NRFFQDNRT: NFTYPE=PCF, FQDNSUFFIX="huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org", NEXTNRFGRPNAME="H-NRF1";
  ```