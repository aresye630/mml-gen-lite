# 查询ServingScope路由（LST NRFSRVSCOPERT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NRF**

该命令用于查询基于服务范围的路由信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识           | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                     |
|:---------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE         | NF类型     | 可选必选说明：可选参数  参数含义：该参数用于表示支持服务范围路由寻址的NF类型。  数据来源：全网规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无  配置原则：无 |
| SRVSCOPE       | NF服务范围   | 可选必选说明：可选参数  参数含义：该参数用于表示服务范围。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则：无                                                                                                                                                                                                                |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数  参数含义：该参数用于表示当前NRF基于服务范围寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~64。  默认值：无  配置原则：  该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。                                                                                                                                     |

## 使用实例

- 查询所有的基于服务范围的路由信息：

  ```
  LST NRFBSFINDEXRT:;
  %%LST NRFBSFINDEXRT:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  NF类型 NF服务范围 归属NRF组名称
  NRF    city1      L-NRF
  NRF    city1      H-NRF
  (结果个数 = 2)
  ```
- 查询NF类型为NRF, NF服务范围为"scope01",归属NRF组名称为H-NRF的路由信息：

  ```
  LST NRFSRVSCOPERT: NFTYPE=NRF, SRVSCOPE="city1", NEXTNRFGRPNAME="H-NRF";
  %%LST NRFSRVSCOPERT:NFTYPE=NRF, SRVSCOPE="city1", NEXTNRFGRPNAME="H-NRF";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
         NF类型 = NRF
     NF服务范围 = city1
  归属NRF组名称 = H-NRF
  (结果个数 = 1)
  ```

## 输出结果说明

| 输出项名称    | 输出项解释                                                 |
|:---------|:------------------------------------------------------|
| NF类型     | 该参数用于表示支持服务范围路由寻址的NF类型。                               |
| NF服务范围   | 该参数用于表示服务范围。                                          |
| 归属NRF组名称 | 该参数用于表示当前NRF基于服务范围寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。 |