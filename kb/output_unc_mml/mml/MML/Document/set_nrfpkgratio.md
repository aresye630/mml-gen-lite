# 设置NRF内外包长比例（SET NRFPKGRATIO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

SET NRFBIGPKGPARA中MAXPKGSIZE配置不为0且RATIO参数配置过大，NRF会误判服务发现响应报文大小，导致服务发现失败。

**适用NF：NRF**

该命令用于配置指定NFType对应的内部报文长度和http接口json原始报文长度的比例系数，用于支撑NRF对不同消息进行最大报文长度的处理判断，详细处理规则请参考SET NRFBIGPKGPARA命令中MAXPKGSIZE参数的描述。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

**说明** 

此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| NFTYPE     |   RATIO |
|:-----------|--------:|
| UDM        |      70 |
| UDR        |      70 |
| AUSF       |      70 |
| PCF        |      67 |
| CHF        |      67 |
| CUSTOM_OCS |      67 |
| AMF        |      52 |
| SMF        |      52 |
| BSF        |      75 |
| DEFAULT    |      50 |
| NRF        |      50 |
| NEF        |      50 |
| SMSF       |      67 |
| NSSF       |      50 |
| LMF        |      50 |
| GMLC       |      50 |
| EIR_5G     |      50 |
| SEPP       |      50 |
| UPF        |      50 |
| N3IWF      |      50 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识   | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                 |
|:-------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE | NF类型    | 可选必选说明：必选参数  参数含义：该参数用于表示NRF处理注册/更新的NF类型或服务发现的目标NF类型。  数据来源：全网规划 取值范围： DEFAULT（DEFAULT）NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无。  配置原则：无 |
| RATIO  | 比例系数(%) | 可选必选说明：可选参数  参数含义：该参数用于表示该NFType对应的内部报文长度和http接口json原始报文长度的百分比，即(内部报文长度/http接口json原始报文长度)*100%。其中内部报文是http接口json原始报文转换后的报文，即NRF实际处理的报文。不同的NFType可以分别设置不同的比例，该参数用法详见SET NRFBIGPKGPARA中MAXPKGSIZE参数说明。  数据来源：本端规划  取值范围：整数类型，取值范围是0~100。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFPKGRATIO查询当前参数配置值。  配置原则：  0代表该NFType不限制包长。       |

## 使用实例

设置NF类型为AMF，比例系数为30；

```
SET NRFPKGRATIO: NFType=AMF, RATIO=30;
```