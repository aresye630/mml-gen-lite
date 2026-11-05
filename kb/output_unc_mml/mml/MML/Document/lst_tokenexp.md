# 查询Token有效期（LST TOKENEXP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NRF**

该命令用于查询NF的Token有效期时长。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                  |
|:--------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CFGTYPE | 生效范围   | 可选必选说明：可选参数  参数含义：该参数表示Token有效期的生效范围。  数据来源：本端规划 取值范围： “WHOLESYS（整系统）”：基于整系统配置Token有效期。“BYNFTYPE（NF类型）”：基于NF类型配置Token有效期。“BYFQDN（FQDN）”：基于FQDN配置Token有效期。  默认值：无  配置原则：无                                                                                                                                                              |
| NFTYPE  | NF类型   | 可选必选说明：该参数在"CFGTYPE"配置为"BYNFTYPE"时为条件可选参数。  参数含义：该参数表示Token有效期作用的NF类型。  数据来源：本端规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）  默认值：无  配置原则：无 |
| FQDN    | FQDN   | 可选必选说明：该参数在"CFGTYPE"配置为"BYFQDN"时为条件可选参数。  参数含义：该参数表示Token有效期作用的FQDN。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。FQDN不能以“.”开始，也不能以“.”结束。  默认值：无  配置原则：无                                                                                                                                              |

## 使用实例

- 查询整系统的Token有效期时长：

  ```
  LST TOKENEXP: CFGTYPE=WHOLESYS;
  %%LST TOKENEXP: CFGTYPE=WHOLESYS;%%
  RETCODE = 0  操作成功

  结果如下
  --------
            NF类型  =  NULL
              FQDN  =  NULL
  有效期时长(分钟)  =  60
  (结果个数 = 1)
  ```
- 查询FQDN为mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org的NF的Token的有效期时长：

  ```
  LST TOKENEXP: CFGTYPE=BYFQDN, FQDN="mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org";
  %%LST TOKENEXP: CFGTYPE=BYFQDN, FQDN="mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org";%%
  RETCODE = 0 操作成功

  结果如下
  ------------------------
            NF类型  =  NULL
              FQDN  =  mmec12.mmegi8001.mme.epc.mnc000.mcc123.3gppnetwork.org
  有效期时长（分钟）= 30
  (结果个数 = 1)
  ```

## 输出结果说明

| 输出项名称     | 输出项解释                     |
|:----------|:--------------------------|
| NF类型      | 该参数表示Token有效期作用的NF类型。     |
| FQDN      | 该参数表示Token有效期作用的FQDN。     |
| 有效期时长(分钟) | 该参数表示配置的Token有效期时长，单位为分钟。 |