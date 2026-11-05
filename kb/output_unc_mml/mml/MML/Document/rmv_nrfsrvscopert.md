# 删除ServingScope路由（RMV NRFSRVSCOPERT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于删除基于服务范围的路由信息。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                     |
|:---------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE         | NF类型     | 可选必选说明：必选参数  参数含义：该参数用于表示支持服务范围路由寻址的NF类型。  数据来源：全网规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无  配置原则：无 |
| SRVSCOPE       | NF服务范围   | 可选必选说明：必选参数  参数含义：该参数用于表示服务范围。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则：无                                                                                                                                                                                                                |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数  参数含义：该参数用于表示当前NRF基于服务范围寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~64。  默认值：无  配置原则：  该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。                                                                                                                                     |

## 使用实例

- 运营商网络为三层组网，最高层PLMN-NRF，中间层H-NRF，最低层L-NRF。L-NRF1归属于H-NRF1，H-HRF1归属于PLMN-NRF。在H-NRF1和PLMN-NRF上分别执行如下命令，删除NF类型为NRF，NF服务范围为city1的路由信息。
  在H-NRF1上执行：

  ```
  RMV NRFSRVSCOPERT: NFTYPE=NRF, SRVSCOPE="city1", NEXTNRFGRPNAME="L-NRF";
  ```
- 在PLMN-NRF上执行：

  ```
  RMV NRFSRVSCOPERT: NFTYPE=NRF, SRVSCOPE="city1", NEXTNRFGRPNAME="H-NRF";
  ```