# 查询网元实例动态信息(DSP UDMNFSRV)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询某个网元实例的动态信息。

## 注意事项

- 当查询的报文大于20KB时，需要将报文拆分显示：
  - 如果是因为查询结果中包含过多号段导致的报文大于20KB，则号段会被拆分为多条显示。其中非号段类的网元实例信息在一条记录中显示，且每一条记录中包含2个号段。
  - 如果不是因为查询结果中包含过多号段导致的报文大于20KB，则会直接截取20KB报文信息进行分记录显示。

- 当查询的报文中“当前注册网元实例信息”长度超过120个字符时，查询结果会自动换行。

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                                                             |
|:------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSNAME   | 网元实例名称 | 可选必选说明：必选参数。 参数含义：用于指示系统按照哪个网元实例名称查询网元实例动态信息。 取值范围：长度不超过32位的字符串，只允许输入0～9，a～z，A～Z，“-”和“_”。 默认值：无。 配置原则：操作员可以通过LST UDMNFSRV命令查询获得。                                                                 |
| NFINSID     | 网元实例标识 | 可选必选说明：可选参数。 参数含义：用于指示系统按照哪个网元实例标识查询网元实例动态信息。 取值范围：该参数为UUIDv4格式。 UUIDv4格式为“xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”，例如：4947a69a-f61b-4bc1-b9da-47c9c5d14b64。 默认值：无。 配置原则：操作员可以通过LST UDMNFSRV命令查询获得。 |
| DSPLOCATION | 查询位置   | 可选必选说明：必选参数。 参数含义：用于指示系统按照哪种位置查询网元实例动态信息。 取值范围： LOCAL（本端）REMOTE（远端） 默认值：LOCAL（本端）。 配置原则：无。                                                                                                       |

## 使用实例

1. 查询“网元实例名称”为“udm-application-002”，“查询位置”为“LOCAL（本端）”的网元实例动态信息，其中“当前注册网元实例信息”长度超过120字符：

   ```
   DSP UDMNFSRV: NFINSNAME="udm-application-002", DSPLOCATION=LOCAL;
   ```

   ```
   %%DSP UDMNFSRV: NFINSNAME="udm-application-002", DSPLOCATION=LOCAL;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   网元实例名称         网元实例标识                          查询位置  当前注册状态  NRF名称  当前注册网元实例信息                                                                                                             

   udm-application-002  f471a043-37b1-4698-ad1c-6987011cf05e  本端      正在注册状态  nrf-01   {"nfInstanceId":"f471a043-37b1-4698-ad1c-6987011cf05e","nfType":"UDM","nfStatus":"REGISTERED","fqdn":"huawei.com","priority":5,  
   udm-application-002  f471a043-37b1-4698-ad1c-6987011cf05e  本端      正在注册状态  nrf-01   "load":0}                                                                                                                        
   (结果个数 = 2)

   共有2个结果
   共有2个报告
   ---    END
   ```
2. 查询“网元实例名称”为“udm\_nfsrv1”，“查询位置”为“LOCAL（本端）”的网元实例动态信息，且查询的报文大于20KB，将报文进行拆分显示（此处由于篇幅限制因此只显示部分报文样例）：

   ```
   DSP UDMNFSRV: NFINSNAME="udm_nfsrv1", DSPLOCATION=LOCAL;
   ```

   ```
   %%DSP UDMNFSRV: NFINSNAME="udm_nfsrv1", DSPLOCATION=LOCAL;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   网元实例名称  网元实例标识                          查询位置  当前注册状态  NRF名称       当前注册网元实例信息                                                                                                                       

   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  {"nfServices":[{"serviceInstanceId":"07c24efa-a14b-4b4c-8c73-1c83bb2a5451","serviceName":"nudm-sdm","versions":[{"apiVersionInUri":"v1",   
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "apiFullVersion":"21.1.0"}],"scheme":"http","nfServiceStatus":"REGISTERED","ipEndPoints":[{"port":8080,"ipv4Address":"192.168.100.1",     
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "transport":"TCP"}],"priority":5,"load":0}],"nfInstanceId":"6d62adeb-a541-4a12-b057-a7856ff321f8","nfType":"UDM","nfStatus":"REGISTERED",  
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "plmnList":[{"mcc":"455","mnc":"46"}],"sNssais":[{"sst":6,"sd":"010101"}],"ipv4Addresses":["192.168.100.1"],"udmInfo":{"groupId":"aaa1",  
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "supiRanges":[{"start":"46000000001","end":"46000000001"},{"start":"46000000002","end":"46000000002"},{"start":"46000000003",              
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "end":"46000000003"},{"start":"46000000004","end":"46000000004"},{"start":"46000000005","end":"46000000005"},{"start":"46000000006",       
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "end":"46000000006"},{"start":"46000000007","end":"46000000007"},{"start":"46000000008","end":"46000000008"},{"start":"46000000009",       
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "end":"46000000009"},{"start":"46000000010","end":"46000000010"},{"start":"46000000011","end":"46000000011"},{"start":"46000000012",       
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "end":"46000000012"},{"start":"46000000013","end":"46000000013"},{"start":"46000000014","end":"46000000014"},{"start":"46000000015",       
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "end":"46000000015"},{"start":"46000000016","end":"46000000016"},{"start":"46000000017","end":"46000000017"},{"start":"46000000018",       
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "end":"46000000018"},{"start":"46000000019","end":"46000000019"},{"start":"46000000020","end":"46000000020"},{"start":"46000000021",       
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "end":"46000000021"},{"start":"46000000022","end":"46000000022"},{"start":"46000000023","end":"46000000023"},{"start":"46000000024",       
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "end":"46000000024"},{"start":"46000000025","end":"46000000025"},{"start":"46000000026","end":"46000000026"},{"start":"46000000027",       
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "end":"46000000027"},{"start":"46000000028","end":"46000000028"},{"start":"46000000029","end":"46000000029"},{"start":"46000000030",       
   udm_nfsrv1    6d62adeb-a541-4a12-b057-a7856ff321f8  本端      正在注册状态  udm_nrfinfo1  "end":"46000000030"},{"start":"46000000031","end":"46000000031"}]},"priority":5,"load":0,"nfServicePersistence":true}                      
   (结果个数 = 15)

   共有47个结果
   共有3个报告
   ---    END
   ```
3. 查询“网元实例名称”为“udm\_nfsrv2”，“查询位置”为“REMOTE（远端）”的网元实例动态信息：

   ```
   DSP UDMNFSRV: NFINSNAME="udm_nfsrv2", DSPLOCATION=REMOTE;
   ```

   ```
   %%DSP UDMNFSRV: NFINSNAME="udm_nfsrv2", DSPLOCATION=REMOTE;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   网元实例名称         网元实例标识                          查询位置  当前注册状态  NRF名称                       当前注册网元实例信息                                                                                                                                          

   udm_nfsrv2       8f45b7cc-f1c7-11ea-9393-fa163eec0412  远端      正常工作状态  APP-snxasnNRF001BHW-01BHW011  "mnc":"03"},{"mcc":"460","mnc":"02"}],"sNssais":[{"sst":1,"sd":"ffffff"},{"sst":1,"sd":"222222"}],"fqdn":"dc2udm.node.5gc.mnc000.mcc460.3gppnetwork.org",     
   udm_nfsrv2       8f45b7cc-f1c7-11ea-9393-fa163eec0412  远端      正常工作状态  APP-snxasnNRF001BHW-01BHW011  "ipv4Addresses":["192.168.91.105"],"priority":1,"udmInfo":{"groupId":"udm","supiRanges":[{"start":"460020000000000","end":"460029999999999"},                     
   udm_nfsrv2       8f45b7cc-f1c7-11ea-9393-fa163eec0412  远端      正常工作状态  APP-snxasnNRF001BHW-01BHW011  {"start":"460030000000000","end":"460030000099999"}]},"nfServicePersistence":true,"nfServices":[{"serviceInstanceId":"cd294f6e-f1c8-11ea-9393-fa163eec0412",  
   udm_nfsrv2       8f45b7cc-f1c7-11ea-9393-fa163eec0412  远端      正常工作状态  APP-snxasnNRF001BHW-01BHW011  "serviceName":"nudm-sdm","versions":[{"apiVersionInUri":"v1","apiFullVersion":"1.PreR15.1.0"}],"scheme":"http","nfServiceStatus":"REGISTERED",                
   udm_nfsrv2       8f45b7cc-f1c7-11ea-9393-fa163eec0412  远端      正常工作状态  APP-snxasnNRF001BHW-01BHW011  "fqdn":"dc2udm.node.5gc.mnc000.mcc460.3gppnetwork.org","ipEndPoints":[{"ipv4Address":"192.168.100.2","transport":"TCP","port":80}],                              
   udm_nfsrv2       8f45b7cc-f1c7-11ea-9393-fa163eec0412  远端      正常工作状态  APP-snxasnNRF001BHW-01BHW011  "priority":1,"load":0},{"serviceInstanceId":"cd29509b-f1c8-11ea-9393-fa163eec0412","serviceName":"nudm-uecm","versions":[{"apiVersionInUri":"v1",             
   udm_nfsrv2       8f45b7cc-f1c7-11ea-9393-fa163eec0412  远端      正常工作状态  APP-snxasnNRF001BHW-01BHW011  "apiFullVersion":"1.PreR15.1.0"}],"scheme":"http","nfServiceStatus":"REGISTERED","fqdn":"dc2udm.node.5gc.mnc000.mcc460.3gppnetwork.org",                      
   udm_nfsrv2       8f45b7cc-f1c7-11ea-9393-fa163eec0412  远端      正常工作状态  APP-snxasnNRF001BHW-01BHW011  "ipEndPoints":[{"ipv4Address":"192.168.91.182","transport":"TCP","port":80}],"priority":1,"load":0},{"serviceInstanceId":"cd2951c2-f1c8-11ea-9393-fa163eec0412", 
                                                                                                                                       
   (结果个数 = 8)

   共有8个结果
   共有1个报告
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数。各参数含义如表1所示。

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 输出项名称      | 输出项解释                                                         |
|:-----------|:--------------------------------------------------------------|
| 当前注册状态     | 用于返回网元实例信息的当前注册状态。 取值范围： 正常工作状态服务暂停状态未注册状态正在注册状态正在去注册状态正在更新状态 |
| 当前注册网元实例信息 | 用于返回当前网元实例信息。                                                 |
| NRF名称      | 用于返回当前网元所属的NRF。                                               |

|    错误码 | 错误码解释           | 原因分析                                             | 处理建议                                            |
|-------:|:----------------|:-------------------------------------------------|:------------------------------------------------|
| 360041 | 参数值不合法。         | 输入的“网元实例标识”参数值不合法。                               | 请参照ADD UDMNFSRV填写正确的“网元实例标识”信息。                 |
| 360103 | 查询服务实例注册信息失败。   | 网元服务之间通信超时或失败。                                   | 请联系华为技术支持。                                      |
| 360149 | 网元实例未成功注册到NRF上。 | UDM到NRF的链路状态异常，导致输入的“网元实例名称”参数对应的网元实例未成功注册到NRF上。 | 使用命令DSP UDMHTTPLNK查询链路状态信息，若返回链路异常，请联系华为技术支持处理。 |