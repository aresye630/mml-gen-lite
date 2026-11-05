# 删除Token有效期（RMV TOKENEXP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于删除特定NF的Token有效期。当运营商希望删除特定NF类型/NF实例设置的Token有效期时长，使用系统默认时长时可以使用此命令。

安全层面考虑，NF请求提供某种服务时需要获取授权，以预防和降低权限提升风险。5GC网络的NF间的服务化接口采用Oauth2.0动态Token授权以保证安全，Token可以理解为NF请求访问某服务使用的短期令牌，当且仅当手持令牌时，才能获取所需服务。

## 注意事项

- 该命令执行后立即生效。

- 根据NF类型/NF实例删除Token有效期后，对应的NF会默认使用整系统的Token有效期，整系统的Token有效期默认为60分钟。
- 整系统的Token有效期时长不能通过RMV TOKENEXP命令删除，只能通过MOD TOKENEXP命令修改。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                   |
|:---------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCFGTYPE | 生效范围   | 可选必选说明：必选参数  参数含义：该参数表示Token有效期的生效范围。  数据来源：本端规划 取值范围： “BYNFTYPE（NF类型）”：基于NF类型配置Token有效期。“BYFQDN（FQDN）”：基于FQDN配置Token有效期。  默认值：无  配置原则：无                                                                                                                                                                                               |
| NFTYPE   | NF类型   | 可选必选说明：该参数在"SCFGTYPE"配置为"BYNFTYPE"时为条件必选参数。  参数含义：该参数表示Token有效期作用的NF类型。  数据来源：本端规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无  配置原则：无 |
| FQDN     | FQDN   | 可选必选说明：该参数在"SCFGTYPE"配置为"BYFQDN"时为条件必选参数。  参数含义：该参数表示Token有效期作用的FQDN。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。FQDN不能以“.”开始，也不能以“.”结束。  默认值：无  配置原则：无                                                                                                                                              |

## 使用实例

- 当运营商希望AMF使用系统默认的Token有效期时长，不再使用单独配置的时长时，配置此命令。

  ```
  RMV TOKENEXP: SCFGTYPE=BYNFTYPE, NFTYPE=AMF;
  ```
- 当运营商希望FQDN为mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org的NF使用系统默认的Token有效期时长，不再使用单独配置的时长时，配置此命令。

  ```
  RMV TOKENEXP: SCFGTYPE=BYFQDN, FQDN="mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org";
  ```