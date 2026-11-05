# 设置KPI阈值(SET KPITHD)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 参考信息

## 命令功能

该命令为配置类命令，用于设置各重大KPI指标产生“ALM-15073 重要KPI指标值变化超过阈值”告警的变化的阈值。

## 注意事项

无。

## 参数说明

| 参数ID    | 参数名称   | 参数描述                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:--------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SERTYPE | 业务类型   | 用于指定一种业务类型。 取值范围：“234G(234G)” “IMS(IMS)” “NON3GPP(NON3GPP)” “BSFAP(BSF/AP)” 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MU      | 测量单元   | 用于标识KPI监控指标对应的测量单元。 当本命令的参数“业务类型”取值为“234G(234G)”时，该参数取值范围如下：ALL_MAP(全MAP测量)ULR_ULA_SAE(ULR和ULA消息测量)AIR_AIA_SAE(AIR和AIA消息测量)MAR_MAA_SAE(MAR和MAA消息测量)SAR_SAA_SAE(SAR和SAA消息测量)CLR_CLA_SAE(CLR和CLA消息测量)IDR_IDA_SAE(IDR和IDA消息测量) 当本命令的参数“业务类型”取值为“IMS(IMS)”时，该参数取值范围如下：LIR_LIA_IMS(LIR和LIA消息统计)UAR_UAA_IMS(UAR和UAA消息统计)MAR_MAA_IMS(MAR和MAA消息统计)SAR_SAA_IMS(SAR和SAA消息统计)PUR_PUA_IMS(PUR和PUA消息统计)UDR_UDA_IMS(UDR和UDA消息统计)SNR_SNA_IMS(SNR和SNA消息统计)RTR_RTA_IMS(RTR和RTA消息统计)PPR_PPA_IMS(PPR和PPA消息统计)PNR_PNA_IMS(PNR和PNA消息统计) 当本命令的参数“业务类型”取值为“NON3GPP(NON3GPP)”时，该参数取值范围如下：TRUSTED_NON3GPP(可信接入注册测量)AAR_AAA(AAR和AAA测量)DER_DEA(DER和DEA测量)MAR_MAA(MAR和MAA测量)SAR_SAA(SAR和SAA测量)STR_STA(STR和STA测量)PPR_PPA(PPR和PPA测量)RAR_RAA(RAR和RAA测量)RTR_RTA(RTR和RTA测量) 当本命令的参数“业务类型”取值为“BSFAP(BSF/AP)”时，该参数取值范围如下：ZH_INTERFACE(UIM Zh接口消息实时测量)ZN_INTERFACE(UIM Zn接口消息实时测量)ZH_MAR_MAA(UIM Zh接口MAR和MAA实时测量)BIR_BIA(UIM BIR和BIA实时测量) 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                        |
| ETY     | 测量指标   | 仅当本命令的参数“测量单元”取有效值时，该参数有效。用于标识KPI监控的测量指标。该参数的取值与参数“测量单元”取值的对应关系请参见表1。 取值范围：Operation_Success_Rate(操作成功率(转发))Operation_Requests(操作请求)Suc_Resp_Rate_of_ULR(位置更新成功响应率)Suc_Resp_Rate_of_AIR(鉴权成功响应率)Suc_Resp_Rate_of_MAR(非3GPP鉴权成功响应率)Suc_Resp_Rate_of_SAR(非3GPP接入注册成功响应率)Suc_Resp_Rate_of_CLR(取消位置登记成功响应率)Suc_Resp_Rate_of_IDR(插入用户数据成功响应率)Suc_Resp_Perc_of_LIR(被叫用户位置查询请求成功响应率)Suc_Resp_Perc_of_UAR(用户注册状态查询请求成功响应率)Suc_Resp_Perc_of_MAR(用户鉴权请求成功响应率)Suc_Resp_Perc_of_SAR(S-CSCF注册注销通知请求成功响应率)Suc_Resp_Perc_of_PUR(AS更新透明数据请求成功响应率)Suc_Resp_Perc_of_UDR(AS读取用户数据请求成功响应率)Suc_Resp_Perc_of_SNR(AS数据变化订阅请求成功响应率)Suc_Resp_Perc_of_RTR(网络侧注销请求成功响应率)Suc_Resp_Perc_of_PPR(用户数据更新请求成功响应率)Suc_Resp_Perc_of_PNR(HSS发起的订阅通知成功响应率)Suc_Rate_of_TrustedNon-3GPP(可信接入注册成功率)Suc_Resp_Rate_of_AAR(接收的AAR成功响应率)Suc_Resp_Rate_of_DER(接收的DER成功响应率)Suc_Resp_Rate_of_SWx_MAR(发送的MAR成功响应率)Suc_Resp_Rate_of_SWx_SAR(发送的SAR成功响应率)Suc_Resp_Rate_of_SWx_STR(接收的STR成功响应率)Suc_Resp_Rate_of_SWx_PPR(接收的PPR成功响应率)Suc_Resp_Rate_of_SWx_RAR(发送的RAR成功响应率)Suc_Resp_Rate_of_SWx_RTR(接收的RTR成功响应率)Suc_Resp_Rate_of_Zh_Sent(Zh接口响应成功率)Suc_Resp_Rate_of_Zn_Recv(Zn接口接收响应成功率)Suc_Resp_Rate_of_Zn_Sent(Zn接口回复响应成功率)Suc_Resp_Rate_of_Zh_MAR(Zh接口发送的MAR成功响应率)Suc_Resp_Rate_of_Bir_Sent(发送的BIR成功响应率)Suc_Resp_Rate_of_Bir_Recv(接收的BIR成功响应率) 默认值：无。 |
| MOI     | 测量对象   | 仅当本命令的参数“测量单元”取值为“ALL_MAP(全MAP测量)”且参数“测量指标”取值为“Operation_Success_Rate(操作成功率(转发))”或“Operation_Requests(操作请求)”时，该参数有效。用于标识KPI监控的测量对象。 取值范围：SendRoutingInfoForGprs(GPRS取路由消息)UpdateGprsLocation(GPRS位置更新)SendRoutingInfoForSM(短消息取路由信息)SendAuthenticationInfo(取鉴权集)SendRoutingInfo(取路由信息)ProvideRoamingNumber(取漫游号码)UpdateLocation(位置更新)CancelLocation(位置取消)InsertSubscriberData(独立插入用户数据)AuthenticationFailureReport(鉴权失败报告)ProcessUnstructedSSRequest(处理非结构化补充业务操作请求) 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| THD     | 阈值     | 用于标识测量指标变化的阈值。取值越大，系统灵敏度越低，关键KPI指标突变时上报告警的概率越小。取值越小，系统灵敏度越高，关键KPI指标突变时上报告警的概率越大。 单位：％或者个数，与测量指标的单位一致。 取值范围：当参数“测量对象”取值为“AuthenticationFailureReport(鉴权失败报告)”时，取值范围为1～10000。若取值为“10000”，则表示最大程度的降低告警上报的概率。当参数“测量对象”取值为其他值时，取值范围为1～100。若取值为“100”，则表示关闭关键KPI指标突变上报告警的功能。 系统初始设置值：当参数“测量对象”取值为“AuthenticationFailureReport(鉴权失败报告)”时，系统初始设置值为100。当参数“测量对象”取值为其他值时，系统初始设置值为5％。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| JUDETHD | 预判阈值   | 仅当本命令的参数“测量单元”取值为“ALL_MAP(全MAP测量)”且参数“测量指标”取值为“Operation_Requests(操作请求)”时，该参数无效。用于标识KPI监控测量指标对应的业务请求次数指标的取值，即预判指标的取值。如果预判指标达到预判阈值，系统判断KPI监控测量指标是否变化到阈值，从而判断是否上报阈值告警。 取值范围：1～4294967294 系统初始设置值：1000。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## 使用实例

为“业务类型”为“234G(234G)”的指标配置阈值。设置“阈值”为“15”，“预判阈值”为“10”。

```
SET KPITHD: SERTYPE=234G, MU=ALL_MAP, ETY=Operation_Success_Rate, MOI=SendRoutingInfoForGprs, THD=15, JUDETHD=10;
```

## 参考信息

KPI指标列表如下表1所示

| 测量指标                | 测量单元                |
|:--------------------|:--------------------|
| 操作成功率(转发)           | 全MAP测量              |
| 操作请求                | 全MAP测量              |
| 位置更新成功响应率           | ULR和ULA消息测量         |
| 鉴权成功响应率             | AIR和AIA消息测量         |
| 非3GPP鉴权成功响应率        | MAR和MAA消息测量         |
| 非3GPP接入注册成功响应率      | SAR和SAA消息测量         |
| 取消位置登记成功响应率         | CLR和CLA消息测量         |
| 插入用户数据成功响应率         | IDR和IDA消息测量         |
| 被叫用户位置查询请求成功响应率     | LIR和LIA消息统计         |
| 用户注册状态查询请求成功响应率     | UAR和UAA消息统计         |
| 用户鉴权请求成功响应率         | MAR和MAA消息统计         |
| S-CSCF注册注销通知请求成功响应率 | SAR和SAA消息统计         |
| AS更新透明数据请求成功响应率     | PUR和PUA消息统计         |
| AS读取用户数据请求成功响应率     | UDR和UDA消息统计         |
| AS数据变化订阅请求成功响应率     | SNR和SNA消息统计         |
| 网络侧注销请求成功响应率        | RTR和RTA消息统计         |
| 用户数据更新请求成功响应率       | PPR和PPA消息统计         |
| HSS发起的订阅通知成功响应率     | PNR和PNA消息统计         |
| 可信接入注册成功率           | 可信接入注册测量            |
| 接收的AAR成功响应率         | AAR和AAA测量           |
| 接收的DER成功响应率         | DER和DEA测量           |
| 发送的MAR成功响应率         | MAR和MAA测量           |
| 发送的SAR成功响应率         | SAR和SAA测量           |
| 接收的STR成功响应率         | STR和STA测量           |
| 接收的PPR成功响应率         | PPR和PPA测量           |
| 发送的RAR成功响应率         | RAR和RAA测量           |
| 接收的RTR成功响应率         | RTR和RTA测量           |
| Zh接口响应成功率           | UIM Zh接口消息实时测量      |
| Zn接口接收响应成功率         | UIM Zn接口消息实时测量      |
| Zn接口回复响应成功率         | UIM Zn接口消息实时测量      |
| Zh接口发送的MAR成功响应率     | UIM Zh接口MAR和MAA实时测量 |
| 发送的BIR成功响应率         | UIM BIR和BIA实时测量     |
| 接收的BIR成功响应率         | UIM BIR和BIA实时测量     |