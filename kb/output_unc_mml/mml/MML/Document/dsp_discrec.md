# 显示服务发现记录（DSP DISCREC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NRF**

该命令查询系统中保存的NF服务发现记录。

若要查询系统中保存的所有NF服务发现记录，请不要输入任何参数。

若要查询特定请求方NF类型或特定目标NF类型的NF服务发现记录，请输入“请求NF类型”或“目标NF类型”参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                          |
|:-------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REQNFTYPE    | 请求NF类型 | 可选必选说明：可选参数  参数含义：该参数用于表示服务发现的请求方NF类型。  数据来源：本端规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）CBCF（CBCF）MB_SMF（MB_SMF）  默认值：无  配置原则：无 |
| TARGETNFTYPE | 目标NF类型 | 可选必选说明：可选参数  参数含义：该参数用于表示服务发现的目标NF类型。  数据来源：本端规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）CBCF（CBCF）MB_SMF（MB_SMF）  默认值：无  配置原则：无  |

## 使用实例

- 当希望查询请求NF类型为AMF，目标NF类型为AMF时，使用此命令。

  ```
  DSP DISCREC: REQNFTYPE=AMF, TARGETNFTYPE=AMF;
  %%DSP DISCREC: REQNFTYPE=AMF, TARGETNFTYPE=AMF;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  服务发现请求时间                  请求NF类型       目标NF类型      服务发现参数                                    服务发现结果   对端IP             用户代理             HTTP响应的via头域  是否本地发现   服务发现NF数量   NF关键属性数量                              服务发现结果包长(byte)   NRF处理时长(ms)   Pod名称     内部资源号

  2019-12-06 09:47:29.954807534 +0  AMF              AMF             {"targetNfType":"AMF","requesterNfType":"AMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL  TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1208                     33                unc-pod1    1
  2019-12-06 09:40:47.574121992 +0  AMF              AMF             {"targetNfType":"AMF","requesterNfType":"AMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL  TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1218                     36                unc-pod1    2
  (结果个数 = 2)

  ---    END
  ```
- 当希望查询所有NF服务发现记录时，使用此命令。

  ```
  DSP DISCREC:;
  %%DSP DISCREC:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  服务发现请求时间                  请求NF类型       目标NF类型      服务发现参数                                    服务发现结果   对端IP             用户代理             HTTP响应的via头域  是否本地发现   服务发现NF数量   NF关键属性数量                              服务发现结果包长(byte)   NRF处理时长(ms)   Pod名称     内部资源号

  2019-12-06 09:47:29.954807534 +0  AMF              AMF             {"targetNfType":"AMF","requesterNfType":"AMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL    TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1200                     25                unc-pod1    1
  2019-12-06 09:40:47.574121992 +0  AMF              AMF             {"targetNfType":"AMF","requesterNfType":"AMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL    TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1207                     36                unc-pod1    2
  2019-12-06 09:39:41.545648777 +0  SMF              SMF             {"targetNfType":"SMF","requesterNfType":"SMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL    TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1208                     36                unc-pod1    3
  2019-12-06 09:38:45.987464664 +0  SMF              SMF             {"targetNfType":"SMF","requesterNfType":"SMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL    TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1100                     20                unc-pod1    4
  (结果个数 = 4)

  ---    END
  ```

## 输出结果说明

| 输出项名称          | 输出项解释                                                                                                                                                                                                                                                                             |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 请求NF类型         | 该参数用于表示服务发现的请求方NF类型。 取值说明： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）CBCF（CBCF）MB_SMF（MB_SMF） |
| 目标NF类型         | 该参数用于表示服务发现的目标NF类型。 取值说明： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）CBCF（CBCF）MB_SMF（MB_SMF）  |
| 服务发现请求时间       | 该参数用于表示服务发现请求的时间，使用UTC时间格式表示。                                                                                                                                                                                                                                                     |
| 服务发现参数         | 该参数用于表示服务发现请求的具体参数，使用JSON格式显示。                                                                                                                                                                                                                                                    |
| 服务发现结果         | 该参数用于表示服务发现的结果，使用HTTP消息码表示。 取值说明： STA_200（成功_200）STA_307（资源重定向_307）STA_400（请求错误_400）STA_403（禁止访问_403）STA_404（未发现_404）STA_411（长度未定义_411）STA_415（访问不支持_415）STA_500（服务内部错误_500）STA_501（未执行_501）STA_503（服务不可用_503）                                                                    |
| 对端IP           | 该参数表示对端NF作为客户端服务化接口IP。                                                                                                                                                                                                                                                            |
| 用户代理           | 该参数表示服务发现请求中HTTP头域中的用户代理。                                                                                                                                                                                                                                                         |
| HTTP响应的via头域   | 该参数用于表示HTTP响应消息中的via头域，HTTP响应的via头域包含了所有处理HTTP请求的NRF的IP地址。                                                                                                                                                                                                                        |
| 是否本地发现         | 该参数表示服务发现结果是通过本地NRF服务发现还是NRF分层转发发现。如果取值为TRUE，表示本地NRF发现，如果取值为FALSE，表示NRF分层转发发现。 取值说明： TRUE(TRUE)FALSE(FALSE)                                                                                                                                                                       |
| 服务发现NF数量       | 该参数表示服务发现结果中NF的数量。                                                                                                                                                                                                                                                                |
| NF关键属性数量       | 该参数表示服务发现结果中，所有NF关键属性数量的总和和各个属性的数量。                                                                                                                                                                                                                                               |
| 服务发现结果包长(byte) | 该参数表示服务发现结果内部报文长度。                                                                                                                                                                                                                                                                |
| NRF处理时长(ms)    | 该参数表示NRF处理服务发现请求时间。                                                                                                                                                                                                                                                               |
| Pod名称          | 该参数表示服务发现业务处理所在Pod的名称。                                                                                                                                                                                                                                                            |
| 内部资源号          | 该参数表示服务发现处理所在的内部资源号。                                                                                                                                                                                                                                                              |