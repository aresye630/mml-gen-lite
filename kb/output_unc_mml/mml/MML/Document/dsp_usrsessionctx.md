# 显示指定用户的会话信息（DSP USRSESSIONCTX）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

显示指定用户的会话信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识         | 参数名称    | 参数说明                                                                                                  |
|:-------------|:--------|:------------------------------------------------------------------------------------------------------|
| IMSI         | IMSI    | 可选必选说明：必选参数  参数含义：该参数用于指定国际移动用户标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。  默认值：无  配置原则：无 |
| PDUSESSIONID | PDU会话标识 | 可选必选说明：可选参数  参数含义：该参数用于指定PDU会话标识。  数据来源：全网规划  取值范围：整数类型，取值范围是1~15。  默认值：无  配置原则：无                     |

## 使用实例

显示IMSI为123038000100001用户的会话信息，执行如下命令：

```
%%DSP USRSESSIONCTX:IMSI="123038000100001";%%
RETCODE = 0  操作成功

操作结果如下
------------
PDU会话标识  切片信息  漫游用户归属地切片信息  DNN           RAB状态  EBI ARP映射关系  SM上下文索引  接入类型  归属SMF的Instance ID  拜访SMF的Instance ID  中间SMF的Instance ID  网络切片Instance ID  N11接口的容灾状态  	PDU会话的漫游类型  替换切片信息

5            0-000000  0-000001                huawei.com    否       NULL             1234567890    3GPP接入  smf_instance_10       NULL                  NULL                  NULL                 NotTakeover        	Home Routed        NULL
6            1-111111  2-000011                0168apn1.com  否       NULL             1234567890    3GPP接入  smf_instance_11       NULL                  NULL                  NULL                 PreemptionTakeover  	Home Routed        NULL
7            1-111111  2-000011                0168apn1.com  否       NULL             1234567890    3GPP接入  smf_instance_11       NULL                  NULL                  NULL                 CompleteTakeover		Local Breakout     NULL
(结果个数 = 3)

---    END
```

## 输出结果说明

| 输出项名称             | 输出项解释                                                                                                                                                       |
|:------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PDU会话标识           | 该参数用于指定PDU会话标识。                                                                                                                                             |
| 切片信息              | 该参数用于标识PDU会话的切片信息。对于非漫游用户标识本网PDU会话切片信息。对于漫游用户标识拜访地PDU会话切片信息。                                                                                                |
| 漫游用户归属地切片信息       | 该参数用于标识漫游用户归属地PDU会话的切片信息。                                                                                                                                   |
| DNN               | 该参数用于标识PDU的DNN信息。                                                                                                                                           |
| RAB状态             | 该参数用于标识PDU的RAB状态。 取值说明： TRUE(TRUE)FALSE(FALSE)                                                                                                              |
| EBI ARP映射关系       | 该参数用于标识PDU的EBI与ARP的映射信息。                                                                                                                                    |
| SM上下文索引           | 该参数用于标识SM上下文索引。                                                                                                                                             |
| 接入类型              | 该参数用于标识接入类型。 取值说明： “THREEGPPACCESS（3GPP接入）”：3GPP接入“NON_3GPP_ACCESS（非3GPP接入）”：非3GPP接入                                                                        |
| 归属SMF的Instance ID | 该参数用于标识归属SMF的Instance ID。                                                                                                                                   |
| 拜访SMF的Instance ID | 该参数用于标识拜访SMF的Instance ID。                                                                                                                                   |
| 中间SMF的Instance ID | 该参数用于标识中间SMF的Instance ID。                                                                                                                                   |
| 网络切片Instance ID   | 该参数用于标识网络切片的Instance ID。                                                                                                                                    |
| 重选本地SMF标识         | 该参数用于标识AMF是否需要将本PDU会话重建到本地SMF。此功能用以减少国际漫游或省间漫游用户的流量迂回，降低传输时延。 取值说明： “YES（是）”：表示AMF需要将本PDU会话重建到本地SMF。“NO（否）”：表示AMF不需要将本PDU会话重建到本地SMF，或者已经完成重建。               |
| N11接口的容灾状态        | 该参数表示N11接口的容灾状态。 如果返回"O-AMF Takeover"，则表示O-AMF在该接口上已接管UE上下文。 如果返回"R-AMF Takeover"，则表示R-AMF在该接口上已接管UE上下文。                                                    |
| PDU会话的漫游类型        | 该参数用于表示PDU会话的漫游类型。 如果显示"Undetermined"，则表示未明确当前PDU会话的漫游类型。 如果显示"Home Routed"，则表示当前PDU会话为Home Routed漫游类型。 如果显示"Local Breakout"，则表示当前PDU会话为Local Breakout漫游类型。 |
| 替换切片信息            | 该参数用于标识PDU会话的替换切片信息。                                                                                                                                        |