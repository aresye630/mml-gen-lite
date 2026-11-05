# 显示5G小区广播订阅信息（DSP NGCBSSUB）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询CBCF发起的5G小区广播订阅信息。

## 注意事项

- 若CBCF发送的Namf\_Communication\_NonUeN2InfoSubscribe Request消息没有携带nfId信元，则执行命令时返回的“CBCF实例标识”参数为“NULL”。
- 若CBCF发送的Namf\_Communication\_NonUeN2InfoSubscribe Request消息没有携带globalRanNodeList信元，则执行命令时返回的“基站标识”以及“CBCF订阅的PLMN”参数为“NULL”。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识   | 参数名称         | 参数说明                                                                                                                                            |
|:-------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| CBCID  | CBCF实例标识     | 可选必选说明：可选参数  参数含义：该参数用于指定发起订阅的CBCF的NF实例标识。若需要查询的订阅记录无CBCF的NF实例标识，建议使用输入参数CBURI查询订阅信息。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~40。不区分大小写。  默认值：无  配置原则：无 |
| CBURI  | Callback URI | 可选必选说明：可选参数  参数含义：该参数用于指定CBCF下发订阅时携带的Callback URI。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~512。  默认值：无  配置原则：无                                          |

## 使用实例

查询实例标识为“CBCF\_Instance\_0”的CBCF发起的5G小区广播订阅信息，执行如下命令：

```
%%DSP NGCBSSUB:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                    CBCF实例标识  =  CBCF_Instance_0
                        基站标识  =  24-123456
                  CBCF订阅的PLMN  =  12303
           CBCF订阅的N2InfoClass  =  N2 PWS类型的PWS信息
                          订阅ID  =  12345678
                    Callback URI  =  http://xxxxx/xxx
              CBCF下发订阅的时间  =  2025-01-02T15:04:05Z07:00
         AMF与CBCF之间的路由模式  =  Direct
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称              | 输出项解释                                                                                                                                                                                             |
|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CBCF实例标识           | 该参数用于指定发起订阅的CBCF的NF实例标识。若需要查询的订阅记录无CBCF的NF实例标识，建议使用输入参数CBURI查询订阅信息。                                                                                                                               |
| 基站标识               | 该参数用于指定CBCF订阅的基站标识。 当订阅消息Namf_Communication_NonUeN2InfoSubscribe Request携基站标识时，该参数由bitLength和gNBValue组成，例如：24-123456。 当订阅消息Namf_Communication_NonUeN2InfoSubscribe Request不携基站标识时, 该参数显示为"NULL" 。 |
| CBCF订阅的PLMN        | 该参数用于指定CBCF订阅的PLMN。                                                                                                                                                                               |
| CBCF订阅的N2InfoClass | 该参数用于指定CBCF订阅的N2InfoClass。 取值说明： N2InfoClassPWS（N2 PWS类型的PWS信息）N2InfoClassPWSBCAL（N2广播完成区域列表或广播取消区域列表）N2InfoClassPWSRF（N2重启指示或失败指示）N2InfoClassINVALID（无效值）                                        |
| 订阅ID               | 该参数用于指定AMF为本次订阅生成的订阅ID。                                                                                                                                                                           |
| Callback URI       | 该参数用于指定CBCF下发订阅时携带的Callback URI。                                                                                                                                                                  |
| CBCF下发订阅的时间        | 该参数用于指定CBCF下发订阅的时间。                                                                                                                                                                               |
| AMF与CBCF之间的路由模式    | 该参数用于指定AMF与CBCF之间的AMF与CBCF之间的路由模式。                                                                                                                                                                |