# 显示NF访问记录（DSP REGNFACCESSREC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NRF**

查询系统中已保存的NF在NRF上的访问记录。

若要查询系统中保存的所有NF在NRF上的访问记录，请不要输入任何参数。

若要查询特定访问类型的访问记录，请输入“访问类型”参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                       |
|:-----------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACCESSTYPE | 访问类型   | 可选必选说明：可选参数  参数含义：该参数表示NF的访问类型。  数据来源：本端规划 取值范围： REGISTER（注册）DEREGISTER（去注册）SUB（订阅）UPSUB（更新订阅）UNSUB（去订阅）UPDATE（全量更新）PATCH（部分更新）NOTIFY（订阅通知）  默认值：无  配置原则：无 |

## 使用实例

- 当希望查询系统中保存的注册类型在NRF上的访问记录时，配置此命令。

  ```
  DSP REGNFACCESSREC:ACCESSTYPE=REGISTER;
  %%DSP REGNFACCESSREC: ACCESSTYPE=REGISTER;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  访问类型  访问时间                          NF类型  NF实例标识  订阅标识  其他信息  源IP地址       目的IP地址  用户代理            HTTP响应的via头域  报文长度(字节)  处理时延(毫秒)  响应结果  NF关键属性数量                                                                 Pod名称                   内部资源号

  注册      2020-10-17 11:00:04.08306279 +08  AMF     ff02-1      NULL      NULL      192.168.9.194  NULL        Go-http-client/2.0  NULL    672             1               201       NfStatus:register;SNssais(1);Tai(1);TaiRange(1);TotalNum:3;                    nrf-pod-6bc75768cb-6s86p  118
  注册      2020-10-17 11:15:38.969336564 +0  AMF     ff02-1      NULL      NULL      192.168.9.194  NULL        Go-http-client/2.0  NULL    672             3               201       NfStatus:register;SNssais(1);Tai(1);TaiRange(1);TotalNum:3;                    nrf-pod-6bc75768cb-6s86p  118
  注册      2020-10-17 11:03:48.324626402 +0  SMF     ff01-1      NULL      NULL      192.168.9.194  NULL        Go-http-client/2.0  NULL    1425            1               201       NfStatus:register;SNssais(1);Tai(2);TaiRange(2);DnnSmfInfoList(2);TotalNum:7;  nrf-pod-6bc75768cb-6s86p  78
  (结果个数 = 3)

  ---    END
  ```
- 当希望查询系统中保存的所有类型在NRF上的访问记录时，配置此命令。

  ```
  DSP REGNFACCESSREC:;
  %%DSP REGNFACCESSREC:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  访问类型  访问时间                          NF类型  NF实例标识  订阅标识                                  其他信息                                                   源IP地址       目的IP地址     用户代理            HTTP响应的via头域  报文长度(字节)  处理时延(毫秒)  响应结果  NF关键属性数量                                                                 Pod名称                   内部资源号

  订阅      2020-10-17 11:00:04.348097579 +0  AMF     NULL        0044001a65cda6d4bfef4865b1d6666395d4f3e7  http://192.168.9.194:5552/nnrf-nfm/v1/nf-instances/ff02-1  192.168.9.194  NULL           Go-http-client/2.0  NULL  0               2               201       NULL                                                                           nrf-pod-6bc75768cb-6s86p  68
  去订阅    2020-10-17 11:00:07.431575255 +0  NULL    NULL        0044001a65cda6d4bfef4865b1d6666395d4f3e7  NULL                                                       192.168.9.194  NULL           Go-http-client/2.0  NULL  0               0               204       NULL                                                                           nrf-pod-6bc75768cb-6s86p  68
  订阅      2020-10-17 11:03:48.558431697 +0  AMF     NULL        0044001a60066461bf4840e29ae71c29f768d76e  http://192.168.9.194:5552/nnrf-nfm/v1/nf-instances/ff02-1  192.168.9.194  NULL           Go-http-client/2.0  NULL  0               0               201       NULL                                                                           nrf-pod-6bc75768cb-6s86p  68
  更新订阅  2020-10-17 11:03:48.818431069 +0  AMF     NULL        0044001a60066461bf4840e29ae71c29f768d76e  NULL                                                       192.168.9.194  NULL           Go-http-client/2.0  NULL  0               0               200       NULL                                                                           nrf-pod-6bc75768cb-6s86p  68
  注册      2020-10-17 11:03:48.324626402 +0  SMF     ff01-1      NULL                                      NULL                                                       192.168.9.194  NULL           Go-http-client/2.0  NULL  1425            1               201       NfStatus:register;SNssais(1);Tai(2);TaiRange(2);DnnSmfInfoList(2);TotalNum:7;  nrf-pod-6bc75768cb-6s86p  78
  去注册    2020-10-17 11:03:49.022358689 +0  SMF     ff01-1      NULL                                      NULL                                                       192.168.9.194  NULL           Go-http-client/2.0  NULL  0               0               204       NULL                                                                           nrf-pod-6bc75768cb-6s86p  78
  订阅通知  2020-10-17 11:03:50.911243626 +0  AMF     ff01-1      0044001a60066461bf4840e29ae71c29f768d76e  http://192.168.9.194:5552/nnrf-nfm/v1/nf-instances/ff02-1  NULL           192.168.9.194  NULL                NULL  63              233             204       NULL                                                                           nrf-pod-6bc75768cb-6s86p  78
  (结果个数 = 7)

  ---    END
  ```

## 输出结果说明

| 输出项名称        | 输出项解释                                                                                                                                                                                                                                                       |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 访问类型         | 该参数表示NF的访问类型。 取值说明： REGISTER（注册）DEREGISTER（去注册）SUB（订阅）UPSUB（更新订阅）UNSUB（去订阅）UPDATE（全量更新）PATCH（部分更新）NOTIFY（订阅通知）                                                                                                                                              |
| 访问时间         | 该参数表示NF的访问时间，使用UTC时间格式表示。                                                                                                                                                                                                                                   |
| NF类型         | 该参数表示访问的NF的类型。 取值说明： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）CUSTOM_OCS（CUSTOM_OCS）DRA（DRA）SCP（SCP） |
| NF实例标识       | 该参数表示访问的NF实例标识。                                                                                                                                                                                                                                             |
| 订阅标识         | 该参数表示NF订阅请求的订阅标识，当访问类型是订阅/去订阅时，该参数有效。                                                                                                                                                                                                                       |
| 其他信息         | 该参数表示NF访问记录的其他信息。                                                                                                                                                                                                                                           |
| 源IP地址        | 该参数表示请求方NF的IP地址信息。                                                                                                                                                                                                                                          |
| 目的IP地址       | 该参数表示接收订阅通知的NF IP地址信息。                                                                                                                                                                                                                                      |
| 用户代理         | 该参数表示请求消息中HTTP头域中的用户代理。                                                                                                                                                                                                                                     |
| HTTP响应的via头域 | 该参数用于表示HTTP响应消息中的via头域，HTTP响应的via头域包含了所有处理HTTP请求的NRF的IP地址。                                                                                                                                                                                                  |
| 报文长度(字节)     | 该参数表示NRF接收到的请求消息（包含注册、全量更新以及非心跳的部分更新）或发送的通知消息的报文长度。                                                                                                                                                                                                         |
| 处理时延(毫秒)     | 该参数表示NRF处理请求消息或对端网元处理订阅通知的时延。                                                                                                                                                                                                                               |
| 响应结果         | 该参数表示NRF处理请求消息或对端网元处理订阅通知的响应结果。                                                                                                                                                                                                                             |
| NF关键属性数量     | 该参数表示所有NF关键属性数量的总和和各个属性的数量。                                                                                                                                                                                                                                 |
| Pod名称        | 该参数表示服务发现业务处理所在Pod的名称。                                                                                                                                                                                                                                      |
| 内部资源号        | 该参数表示服务发现处理所在的内部资源号。                                                                                                                                                                                                                                        |