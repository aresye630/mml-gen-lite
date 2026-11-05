# 增加NF类型路由（ADD NRFNFTYPERT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增NF类型路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

如果针对同一个NF类型配置了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入65535条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                |
|:---------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE         | NF类型     | 可选必选说明：必选参数  参数含义：该参数用于表示NF类型路由寻址的NF类型。  数据来源：本端规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无  配置原则：  该参数值为UDM、AMF、SMF、AUSF、PCF、CHF、BSF、SCP类型时不生效。 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数  参数含义：该参数用于表示当前NRF基于NFTYPE路由寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~64。  默认值：无  配置原则：  该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。                                                                                                                                                                          |

## 使用实例

- 运营商网络为三层组网，最高层PLMN-NRF，中间层H-NRF，最低层L-NRF。L-NRF1归属于H-NRF1，H-HRF1归属于PLMN-NRF。当跨NRF进行服务发现时，NF类型为SMSF，归属于L-NRF1，则需要在H-NRF1和PLMN-NRF上分别配置如下路由信息。在H-NRF1上执行：

  ```
  ADD NRFNFTYPERT:  NFTYPE=SMSF, NEXTNRFGRPNAME="L-NRF1";
  ```
- 在PLMN-NRF上执行：

  ```
  ADD NRFNFTYPERT:  NFTYPE=SMSF, NEXTNRFGRPNAME="H-NRF1";
  ```