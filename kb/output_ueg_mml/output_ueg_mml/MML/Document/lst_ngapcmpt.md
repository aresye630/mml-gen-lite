# 查询NGAP兼容性参数（LST NGAPCMPT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询NGAP（NG Application Protocol）兼容性控制参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询系统中当前配置的NGAP兼容性参数，执行如下命令：

```
%%LST NGAPCMPT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                           是否携带RAT限制信元  =  是
                      是否携带禁止区域信息信元  =  是
                      是否携带服务区域信息信元  =  是
                    是否携带核心网类型限制信元  =  是
                 是否携带Last E-UTRAN PLMN信元  =  是
                        是否携带感兴趣区域列表  =  是
                        感兴趣区域列表携带方式  =  全量
                    互操作原因值是否定制化映射  =  是
                         是否携带GUAMI类型信元  =  是
                     是否携带Masked IMEISV信元  =  是
是否携带Redirection for Voice EPS Fallback信元  =  是
                          是否携带扩展的UE标识  =  是
                              是否携带RFSP信元  =  是
                     Masked IMEISV信元编码方式  =  正序BIT STRING
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                                    | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:-----------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 是否携带RAT限制信元                              | 该参数用于控制AMF是否在给NG-RAN下发的INITIAL CONTEXT SETUP REQUEST、HANDOVER REQUEST或者DOWNLINK NAS TRANSPORT消息中携带RAT Restrictions信元，其中RAT Restrictions是Mobility Restriction List的子信元。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 是否携带禁止区域信息信元                             | 该参数用于控制AMF是否在给NG-RAN下发的INITIAL CONTEXT SETUP REQUEST、HANDOVER REQUEST或者DOWNLINK NAS TRANSPORT消息中携带Forbidden Area Information信元，其中Forbidden Area Information是Mobility Restriction List的子信元。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 是否携带服务区域信息信元                             | 该参数用于控制AMF是否在给NG-RAN下发的INITIAL CONTEXT SETUP REQUEST、HANDOVER REQUEST或者DOWNLINK NAS TRANSPORT消息中携带Service Area Information信元，其中Service Area Information是Mobility Restriction List的子信元。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 是否携带核心网类型限制信元                            | 该参数用于控制AMF是否在给NG-RAN下发的INITIAL CONTEXT SETUP REQUEST、HANDOVER REQUEST或者DOWNLINK NAS TRANSPORT消息中携带Core Network Type Restriction for Serving PLMN和Core Network Type Restriction for Equivalent PLMNs信元，其中Core Network Type Restriction for Serving PLMN和Core Network Type Restriction for Equivalent PLMNs都是Mobility Restriction List的子信元。                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 是否携带Last E-UTRAN PLMN信元                  | 该参数用于控制AMF是否在给NG-RAN下发的INITIAL CONTEXT SETUP REQUEST、HANDOVER REQUEST或者DOWNLINK NAS TRANSPORT消息中携带Last E-UTRAN PLMN Identity信元，其中Last E-UTRAN PLMN Identity是Mobility Restriction List的子信元。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 是否携带感兴趣区域列表                              | 该参数用于控制AMF在给NG-RAN下发的LOCATION REPORTING CONTROL，HANDOVER REQUEST以及INITIAL CONTEXT SETUP REQUEST消息中是否携带Area of Interest List信元。LOCATION REPORTING CONTROL，HANDOVER REQUEST以及INITIAL CONTEXT SETUP REQUEST消息都会携带Location Reporting Request Type信元。Location Reporting Request Type包含的其中两个子信元分别是Area of Interest List和Event Type。 当AOILIST的取值为“YES”时，如果Event Type取值为UE Presence In Aoi或者Stop UE Presence In Aoi（说明存在Area of Interest List），Location Reporting Request Type中必须携带Area of Interest List。当AOILIST的取值为“NO”时，Location Reporting Request Type信元中不能携带Area of Interest List子信元。此时，AMF不能发送Event Type为UE Presence In Aoi或者Stop UE Presence In Aoi类型的LOCATION REPORTING CONTROL消息给基站；AMF给基站下发HANDOVER REQUEST或INITIAL CONTEXT SETUP REQUEST消息中不携带Event Type为UE Presence In Aoi的Location Reporting Request Type信元。 |
| 感兴趣区域列表携带方式                              | 该参数用于控制AMF向NG-RAN发送的LOCATION REPORTING CONTROL消息中携带全量的Area of Interest List信元还是增量的Area of Interest List信元，其中Area of Interest List是Location Reporting Request Type的子信元。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 互操作原因值是否定制化映射                            | 该参数用于控制AMF是否对互操作原因值定制化映射。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 是否携带GUAMI类型信元                            | 该参数用于控制AMF向NG-RAN发送的NG SETUP RESPONSE或者AMF CONFIGURATION UPDATE消息中是否携带GUAMI Type信元。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 是否携带Masked IMEISV信元                      | 该参数用于控制AMF是否在给NG-RAN下发的INITIAL CONTEXT SETUP REQUEST、HANDOVER REQUEST消息中携带Masked IMEISV信元。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 是否携带Redirection for Voice EPS Fallback信元 | 该参数用于控制AMF是否在给NG-RAN发送的INITIAL CONTEXT SETUP REQUEST、HANDOVER REQUEST、PATH SWITCH REQUEST ACKNOWLEDGE消息中携带“Redirection for Voice EPS Fallback”信元。Redirection for Voice EPS Fallback用于给基站指示AMF和UE是否支持重定向方式的语音EPS Fallback流程。AMF根据UE能力、签约数据和本地策略来共同决策Redirection for Voice EPS Fallback信元取值。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 是否携带扩展的UE标识                              | 该参数用于控制AMF是否在给NG-RAN下发的INITIAL CONTEXT SETUP REQUEST、UE CONTEXT MODIFICATION REQUEST、HANDOVER REQUEST、PATH SWITCH REQUEST ACKNOWLEDGE消息中携带Extended UE Identity Index Value信元，其中Extended UE Identity Index Value是Core Network Assistance Information for RRC INACTIVE的子信元。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 是否携带RFSP信元                               | 该参数用于控制AMF向NG-RAN发送的INITIAL CONTEXT SETUP REQUEST、DOWNLINK NAS TRANSPORT或者UE CONTEXT MODIFICATION REQUEST消息中是否携带Index to RAT/Frequency Selection Priority信元。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Masked IMEISV信元编码方式                      | 该参数用于控制AMF在给NG-RAN下发的INITIAL CONTEXT SETUP REQUEST、HANDOVER REQUEST消息中携带Masked IMEISV信元的编码方式。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |