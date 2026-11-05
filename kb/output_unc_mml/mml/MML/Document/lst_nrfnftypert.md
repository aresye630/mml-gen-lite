# 查询NF类型路由（LST NRFNFTYPERT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NRF**

该命令用于查询已配置的NF类型路由信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识           | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                |
|:---------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE         | NF类型     | 可选必选说明：可选参数  参数含义：该参数用于表示NF类型路由寻址的NF类型。  数据来源：本端规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无  配置原则：  该参数值为UDM、AMF、SMF、AUSF、PCF、CHF、BSF、SCP类型时不生效。 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数  参数含义：该参数用于表示当前NRF基于NFTYPE路由寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~64。  默认值：无  配置原则：  该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。                                                                                                                                                                          |

## 使用实例

- 运营商想要查询NF类型为SMSF，归属NRF组名称为L-NRF1的NF类型路由信息。

  ```
  LST NRFNFTYPERT:  NFTYPE=SMSF, NEXTNRFGRPNAME="L-NRF1";
  %%LST NRFNFTYPERT:  NFTYPE=SMSF, NEXTNRFGRPNAME="L-NRF1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
         NF类型  =  SMSF 
  归属NRF组名称  =  L-NRF1
  (结果个数 = 1)
  ```
- 查询所有NF类型路由信息。

  ```
  LST NRFNFTYPERT:;
  %%LST NRFNFTYPERT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NF类型    归属NRF组名称  
  SMSF      L-NRF1  
  NRF       L-NRF2  
  (结果个数 = 2)
  ```

## 输出结果说明

| 输出项名称    | 输出项解释                                                     |
|:---------|:----------------------------------------------------------|
| NF类型     | 该参数用于表示NF类型路由寻址的NF类型。                                     |
| 归属NRF组名称 | 该参数用于表示当前NRF基于NFTYPE路由寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。 |