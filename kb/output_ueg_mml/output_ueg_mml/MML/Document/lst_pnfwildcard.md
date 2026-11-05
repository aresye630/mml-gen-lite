# 查询对端NF的通配策略（LST PNFWILDCARD）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、NEF、NWDAF、SCF**

该命令用于查询对端NF的通配策略。指定NFType时，输出该对端NF的对应通配策略。不指定NFType时，输出所有对端NF的通配策略。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE | NF类型   | 可选必选说明：可选参数  参数含义：该参数用于指定对端NF类型。  数据来源：本端规划 取值范围： “NfInvalid（NfInvalid）”：NfInvalid“NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NfUDN（NfUDN）”：NfUDN“NfNWDAF（NfNWDAF）”：NfNWDAF  默认值：无  配置原则：无 |

## 使用实例

运营商A需要查询NFTYPE为NfSMF的对端NF的通配策略。

```
%%LST PNFWILDCARD: NFTYPE=NfSMF;%%
RETCODE = 0  操作成功

结果如下
--------
                       NF类型  =  NfSMF
             非漫游SUPI配置通配开关  =  OFF
             非漫游SUPI缓存通配开关  =  ON
	       漫游SUPI配置通配开关  =  OFF
	       漫游SUPI缓存通配开关  =  ON
             非漫游GPSI配置通配开关  =  OFF
             非漫游GPSI缓存通配开关  =  ON
	       漫游GPSI配置通配开关  =  OFF
	       漫游GPSI缓存通配开关  =  ON
              非漫游TAI配置通配开关  =  ON
              非漫游TAI缓存通配开关  =  ON
	        漫游TAI配置通配开关  =  ON
	        漫游TAI缓存通配开关  =  ON
             非漫游PLMN配置通配开关  =  ON
             非漫游PLMN缓存通配开关  =  ON
	       漫游PLMN配置通配开关  =  ON
	       漫游PLMN缓存通配开关  =  ON
              非漫游DNN配置通配开关  =  ON
              非漫游DNN缓存通配开关  =  ON
		漫游DNN配置通配开关  =  ON
		漫游DNN缓存通配开关  =  ON
      非漫游WildcardDnn配置通配开关  =  OFF
      非漫游WildcardDnn缓存通配开关  =  OFF
        漫游WildcardDnn配置通配开关  =  OFF
        漫游WildcardDnn缓存通配开关  =  OFF
               非漫游NS配置通配开关  =  ON
               非漫游NS缓存通配开关  =  ON
		 漫游NS配置通配开关  =  ON
		 漫游NS缓存通配开关  =  ON
非漫游Routing Indicator配置通配开关  =  ON
非漫游Routing Indicator缓存通配开关  =  ON
  漫游Routing Indicator配置通配开关  =  ON
  漫游Routing Indicator缓存通配开关  =  ON
             CLIENTTYPE配置通配开关  =  ON
             CLIENTTYPE缓存通配开关  =  ON
          非漫游GROUPID配置通配开关  =  ON
          非漫游GROUPID缓存通配开关  =  ON
	    漫游GROUPID配置通配开关  =  ON
            漫游GROUPID缓存通配开关  =  ON
           非漫游服务区配置通配开关  =  ON
	     漫游服务区配置通配开关  =  ON
			
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                      | 输出项解释                                                                                                                                                                   |
|:---------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NF类型                       | 该参数用于指定对端NF类型。                                                                                                                                                          |
| 非漫游SUPI配置通配开关              | 该参数用于指定非漫游场景本地配置查询中对端NF的SUPI通配开关。当本地配置中此NF没有配置SUPI时，用户携带SUPI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                |
| 非漫游SUPI缓存通配开关              | 该参数用于指定非漫游场景缓存查询中对端NF的SUPI通配开关。当缓存中此NF没有SUPI时，用户携带SUPI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                     |
| 漫游SUPI配置通配开关               | 该参数用于指定漫游场景本地配置查询中对端NF的SUPI通配开关。当本地配置中此NF没有配置SUPI时，用户携带SUPI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                 |
| 漫游SUPI缓存通配开关               | 该参数用于指定漫游场景缓存查询中对端NF的SUPI通配开关。当缓存中此NF没有SUPI时，用户携带SUPI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                      |
| 非漫游GPSI配置通配开关              | 该参数用于指定非漫游场景本地配置查询中对端NF的GPSI通配开关。当本地配置中此NF没有配置GPSI时，用户携带GPSI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                |
| 非漫游GPSI缓存通配开关              | 该参数用于指定非漫游场景缓存查询中对端NF的GPSI通配开关。当缓存中此NF没有GPSI时，用户携带GPSI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                     |
| 漫游GPSI配置通配开关               | 该参数用于指定漫游场景本地配置查询中对端NF的GPSI通配开关。当本地配置中此NF没有配置GPSI时，用户携带GPSI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                 |
| 漫游GPSI缓存通配开关               | 该参数用于指定漫游场景缓存查询中对端NF的GPSI通配开关。当缓存中此NF没有GPSI时，用户携带GPSI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                      |
| 非漫游TAI配置通配开关               | 该参数用于指定非漫游场景本地配置中对端NF的TAI通配开关。本地配置没有配置对端NF的TAI时，当用户携带TAI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                    |
| 非漫游TAI缓存通配开关               | 该参数用于指定非漫游场景缓存查询中对端NF的TAI通配开关。缓存中此NF没有TAI时，当用户携带TAI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                        |
| 漫游TAI配置通配开关                | 该参数用于指定漫游场景本地配置中对端NF的TAI通配开关。本地配置没有配置对端NF的TAI时，当用户携带TAI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                     |
| 漫游TAI缓存通配开关                | 该参数用于指定漫游场景缓存查询中对端NF的TAI通配开关。缓存中此NF没有TAI时，当用户携带TAI来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                         |
| 非漫游PLMN配置通配开关              | 该参数用于指定非漫游场景本地配置中对端NF的PLMN通配开关。本地配置没有配置对端NF的PLMN时，当用户携带PLMN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                 |
| 非漫游PLMN缓存通配开关              | 该参数用于指定非漫游场景缓存查询中对端NF的PLMN通配开关。缓存中此NF没有PLMN时，当用户携带PLMN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                     |
| 漫游PLMN配置通配开关               | 该参数用于指定漫游场景本地配置中对端NF的PLMN通配开关。本地配置没有配置对端NF的PLMN时，当用户携带PLMN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                  |
| 漫游PLMN缓存通配开关               | 该参数用于指定漫游场景缓存查询中对端NF的PLMN通配开关。缓存中此NF没有PLMN时，当用户携带PLMN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                      |
| 非漫游DNN配置通配开关               | 该参数用于指定非漫游场景本地配置中对端NF的DNN通配开关。本地配置没有配置对端NF的DNN时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                    |
| 非漫游DNN缓存通配开关               | 该参数用于指定非漫游场景缓存查询中对端NF的DNN通配开关。缓存中此NF没有DNN时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                        |
| 漫游DNN配置通配开关                | 该参数用于指定漫游场景本地配置中对端NF的DNN通配开关。本地配置没有配置对端NF的DNN时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                     |
| 漫游DNN缓存通配开关                | 该参数用于指定漫游场景缓存查询中对端NF的DNN通配开关。缓存中此NF没有DNN时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                         |
| 非漫游WildcardDnn配置通配开关       | 该参数用于指定非漫游场景本地配置中对端NF的WildcardDnn通配开关。本地配置了对端NF的WildcarDnn（即"*"）时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF且未配置请求的DNN时，此NF不允许被服务发现。                                        |
| 非漫游WildcardDnn缓存通配开关       | 该参数用于指定非漫游场景缓存查询中对端NF的WildcarDnn通配开关。缓存中此NF有WildcardDnn（即"*"）时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF且此NF没有用户请求的DNN时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                      |
| 漫游WildcardDnn配置通配开关        | 该参数用于指定漫游场景本地配置中对端NF的WildcardDnn通配开关。本地配置了对端NF的WildcardDnn（即"*"）时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF且未配置请求的DNN时，此NF不允许被服务发现。                                        |
| 漫游WildcardDnn缓存通配开关        | 该参数用于指定漫游场景缓存查询中对端NF的WildcarDnn通配开关。缓存中此NF有WildcardDnn（即"*"）时，当用户携带DNN来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF且此NF没有用户请求的DNN时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                       |
| 非漫游NS配置通配开关                | 该参数用于指定非漫游场景本地配置中对端NF的NS通配开关。本地配置没有配置对端NF的NS时，当用户携带NS来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                       |
| 非漫游NS缓存通配开关                | 该参数用于指定非漫游场景缓存查询中对端NF的NS通配开关。缓存中此NF没有NS时，当用户携带NS来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                           |
| 漫游NS配置通配开关                 | 该参数用于指定漫游场景本地配置中对端NF的NS通配开关。本地配置没有配置对端NF的NS时，当用户携带NS来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                        |
| 漫游NS缓存通配开关                 | 该参数用于指定漫游场景缓存查询中对端NF的NS通配开关。缓存中此NF没有NS时，当用户携带NS来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                                            |
| 非漫游Routing Indicator配置通配开关 | 该参数用于指定非漫游场景本地配置中对端NF的Routing Indicators通配开关。本地配置没有配置对端NF的Routing Indicators时，当用户携带Routing Indicators来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                       |
| 非漫游Routing Indicator缓存通配开关 | 该参数用于指定非漫游场景缓存查询中对端NF的Routing Indicators通配开关。缓存中此NF没有Routing Indicators时，当用户携带Routing Indicators来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。           |
| 漫游Routing Indicator配置通配开关  | 该参数用于指定漫游场景本地配置中对端NF的Routing Indicators通配开关。本地配置没有配置对端NF的Routing Indicators时，当用户携带Routing Indicators来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                        |
| 漫游Routing Indicator缓存通配开关  | 该参数用于指定漫游场景缓存查询中对端NF的Routing Indicators通配开关。缓存中此NF没有Routing Indicators时，当用户携带Routing Indicators来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。            |
| CLIENTTYPE配置通配开关           | 该参数用于指定本地配置中对端NF的ClientTypes通配开关。本地配置通过ADD PNFLMFINFO/ADD PNFGMLCINFO命令配置LMFINFO/GMLCINFO并且没有配置ClientTypes时，当用户携带ClientType来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。 |
| CLIENTTYPE缓存通配开关           | 该参数用于指定缓存查询中对端NF的ClientTypes通配开关。缓存中此NF包含LMFINFO或者GMLCINFO并且没有ClientTypes时，当用户携带ClientType来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                 |
| 非漫游GROUPID配置通配开关           | 该参数用于指定非漫游场景本地配置中对端NF的GROUPID通配开关。本地配置没有配置对端NF的GROUPID时，当用户携带GROUPID来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                        |
| 非漫游GROUPID缓存通配开关           | 该参数用于指定非漫游场景缓存查询中对端NF的GROUPID通配开关。缓存中此NF没有GROUPID时，当用户携带GROUPID来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                            |
| 漫游GROUPID配置通配开关            | 该参数用于指定漫游场景本地配置中对端NF的GROUPID通配开关。本地配置没有配置对端NF的GROUPID时，当用户携带GROUPID来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                         |
| 漫游GROUPID缓存通配开关            | 该参数用于指定漫游场景缓存查询中对端NF的GROUPID通配开关。缓存中此NF没有GROUPID时，当用户携带GROUPID来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。对NRF返回的服务发现结果不生效。                                             |
| 非漫游服务区配置通配开关               | 该参数用于指定本地配置查询中对端NF的服务区通配开关。当本地配置中此NF没有配置服务区时，用户携带服务区来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                        |
| 漫游服务区配置通配开关                | 该参数用于指定漫游场景本地配置查询中对端NF的服务区通配开关。当本地配置中此NF没有配置服务区时，用户携带服务区来服务发现，取值为ON时，此NF允许被服务发现；取值为OFF时，此NF不允许被服务发现。                                                                    |