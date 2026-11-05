# 查询指定消息类型固定速率流控信息（LST N2FIXEDFCBYMSG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询指定消息类型的固定速率流控信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:--------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MSGTYPE | 流控消息类型 | 可选必选说明：可选参数  参数含义：该参数用于设置N2接口被流控的消息类型。  数据来源：全网规划 取值范围： “NGSETUP（NG Setup Request）”：表示NG Setup Request消息。“PAGING（Paging）”：表示Paging消息。“REGISTER（Registration Request）”：表示Registration Request消息。“SERVICEREQUEST（Service Request）”：表示Service Request消息。“PATHSWITCH（Path Switch Request）”：表示Path Switch Request消息。“WPWR（Write-Replace Warning Response）”：表示Write-Replace Warning Response消息。“PCR（PWS Cancel Response）”：表示PWS Cancel Response消息。“PRI（PWS Restart Indication）”：表示PWS Restart Indication消息。“PFI（PWS Failure Indication）”：表示PWS Failure Indication消息。  默认值：无  配置原则：无 |

## 使用实例

查询所有流控消息类型流控信息，执行如下命令：

```
%%LST N2FIXEDFCBYMSG:;%%
RETCODE = 0  操作成功

结果如下
--------
流控消息类型                      固定速率流控开关  流控速率门限(个/秒)

NG Setup Request                  开启              500
Paging                            开启              2000
Registration Request              开启              1800
Service Request                   开启              3000
Path Switch Request               开启              8000
Write-Replace Warning Response    开启              1000
PWS Cancel Response               开启              1000
PWS restart Indication            开启              1000
PWS Failure Indication            开启              1000
(结果个数 = 9)

---    END
```

## 输出结果说明

| 输出项名称       | 输出项解释                                            |
|:------------|:-------------------------------------------------|
| 流控消息类型      | 该参数用于设置N2接口被流控的消息类型。                             |
| 固定速率流控开关    | 该参数用于控制N2接口指定消息类型固定速率流控功能。                       |
| 流控速率门限(个/秒) | 该参数用于设置N2接口指定消息的接收/发送流控速率上限。该参数针对单Pod指定消息类型进行流控。 |