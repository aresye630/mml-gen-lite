# 显示NCS服务信息（DSP NCSINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于显示网元实例信息的NCS服务信息。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                                     |
|:--------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMDTYPE | 命令类型   | 可选必选说明：必选参数 参数含义：用于标识NCS服务信息的命令类型。 取值范围： NFDISCDATANFSUBSCRIBEDATAPCFREGRSPINFO 默认值：无 配置原则：无                                                                             |
| NFTYPE  | 网元类型   | 可选必选说明：条件可选参数，当“命令类型”取值为“NFDISCDATA”或“NFSUBSCRIBEDATA”时，该参数可选。 参数含义：用于标识一个网元实例的NF类型。 取值范围： CHF(CHF)BSF(BSF)NWDAF(NWDAF)SCP(SCP)AMF(AMF)UDR(UDR)PCF(PCF) 默认值：无 配置原则：无     |
| NFINSID | 网元实例标识 | 可选必选说明：可选参数 参数含义：用于标识网元实例信息中的网元实例标识，该参数为UUIDv4格式。UUIDv4格式为“xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”，例如：4947a69a-f61b-4bc1-b9da-47c9c5d14b64。 取值范围：长度不超过36的字符串。 默认值：无 配置原则：无 |

## 使用实例

显示NCS服务信息结果。

1. 显示“命令类型”为“NFDISCDATA”的信息。

   ```
   DSP NCSINFO: CMDTYPE=NFDISCDATA
   ```

   ```
   %%DSP NCSINFO: CMDTYPE=NFDISCDATA;%%
   RETCODE = 0  操作成功

   操作结果如下 
   ------------------------ 
   NCS实例号             NCS状态     网元实例标识                          NF类型   查询条件                                                                                                                                                     有效期限    有效期结束时间       
   18436344549140880816  STANDBY     4947a69a-f61b-4bc1-b9da-47c9c5d14b72  CHF      {"target-nf-type":"CHF","requester-nf-type":"PCF","service-names":["nchf-spendinglimitcontrol"],"gpsi":"msisdn-139989950311001","requester-features":"20"}   300         2024-05-30T17:21:40Z  
   18436344549140868528  ACTIVE      4947a69a-f61b-4bc1-b9da-47c9c5d14b72  CHF      {"target-nf-type":"CHF","requester-nf-type":"PCF","service-names":["nchf-spendinglimitcontrol"],"gpsi":"msisdn-139989950311001","requester-features":"20"}   300         2024-05-30T17:21:40Z  
   (结果个数 = 2)

   ---    END
   ```
2. 显示“命令类型”为“NFSUBSCRIBEDATA”的信息。

   ```
   DSP NCSINFO: CMDTYPE=NFSUBSCRIBEDATA
   ```

   ```
   %%DSP NCSINFO: CMDTYPE=NFSUBSCRIBEDATA;%%
   RETCODE = 0  操作成功

   操作结果如下 
   ------------------------
   NCS实例号             NCS状态     网元实例标识                          NF类型   NRF的URL                                            NRF的location                                                            服务名称      有效期结束时间             AMF集合ID   订阅ID                                请求通知事件                                        接收订阅通知的URI                    SCP域  
   18436344549140868528  ACTIVE      4947a69a-f61b-4bc1-b9da-47c9c5d14b72  CHF      http://10.255.255.1:8080/nnrf-nfm/v1/subscriptions  http://*/nnrf-nfm/v1/subscriptions/4947a69a-f61b-4bc1-b9da-47c9c5d14b72  NULL          2024-05-30T17:20:51+08:00  NULL        4947a69a-f61b-4bc1-b9da-47c9c5d14b72  NF_DEREGISTERED, NF_REGISTERED, NF_PROFILE_CHANGED  /npcf-nfm/v1/notification-discovery  SCPDomain01      
   18436344549140880816  STANDBY     4947a69a-f61b-4bc1-b9da-47c9c5d14b72  CHF      http://10.255.255.1:8080/nnrf-nfm/v1/subscriptions  http://*/nnrf-nfm/v1/subscriptions/4947a69a-f61b-4bc1-b9da-47c9c5d14b72  NULL          2024-05-30T17:20:51+08:00  NULL        4947a69a-f61b-4bc1-b9da-47c9c5d14b72  NF_DEREGISTERED, NF_REGISTERED, NF_PROFILE_CHANGED  /npcf-nfm/v1/notification-discovery  SCPDomain01      
   (结果个数 = 2)

   ---    END
   ```
3. 显示“命令类型”为“PCFREGRSPINFO”的信息。

   ```
   DSP NCSINFO: CMDTYPE=PCFREGRSPINFO
   ```

   ```
   %%DSP NCSINFO: CMDTYPE=PCFREGRSPINFO;%%
   RETCODE = 0  操作成功

   操作结果如下 
   ------------------------
        NCS实例号  =  18436344549140868528
          NCS状态  =  ACTIVE
     网元实例标识  =  b26a3e37-fdc4-4978-8c6f-749dcdb24ed9
   心跳定时器时长  =  300
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义如表 输出项解释

| 输出项名称        | 输出项解释                                     |
|:-------------|:------------------------------------------|
| NCS实例号       | 用于表示网元实例信息中的NCS实例号。                       |
| NCS状态        | 用于表示网元实例信息中的NCS状态。                        |
| 网元类型         | 用于表示网元实例类型。 取值范围： CHFBSFNWDAFSCPAMFUDRPCF |
| 网元实例标识       | 用于表示网元实例信息中网元实例的标识。                       |
| 查询条件         | 用于表示查询条件。                                 |
| 有效期限         | 用于表示订阅有效期限。                               |
| 有效期结束时间      | 用于表示订阅有效期结束时间。                            |
| NRF的URL      | 用于表示网元实例信息的NRF的URL。                       |
| NRF的Location | 用于表示网元实例信息的NRF的Location。                  |
| 服务名称         | 用于表示订阅条件中携带的服务名称。                         |
| AMF集合ID      | 用于表示订阅条件中携带的AMF集合ID。                      |
| 订阅ID         | 用于表示订阅响应消息返回的订阅ID。                        |
| 请求通知事件       | 用于表示PCF向NRF订阅的NF的通知事件。                    |
| 接收订阅通知的URI   | 用于表示PCF接收NRF订阅通知的URI。                     |
| 心跳定时器时长      | 用于表示PCF实例在注册成功后，NRF返回给PCF的心跳周期。           |
| SCP域         | 用于表示一条SCP域配置信息。                           |