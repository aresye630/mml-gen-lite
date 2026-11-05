# 查询组成员（LST PGRPMBR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询某个组成员信息，包括基本信息（组成员标识、组用户标识）和配额信息（组成员的共享配额信息、组用户签约的配额信息）。

## 注意事项

- 如果组成员没有共享配额，结果不返回配额信息。
- 如果组成员或者组用户已过了配额复位时间，则查询的返回结果为进行复位操作后的结果。
- 支持使用组成员的第二标识查询，查询结果显示组用户和组成员的第一标识。

## 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                          |
|:--------------|:-------|:------------------------------------------------------------------------------|
| USRIDENTIFIER | 成员用户标识 | 用于指定查询哪一个组成员信息。 取值范围：长度不超过255的字符串。 默认值：无。  说明： 该参数必须先由ADD PSUB命令定义，然后才能在此处索引。 |

## 使用实例

查询组成员信息，“成员用户标识”为“46010381014\*\*\*\*”：

```
LST PGRPMBR: USRIDENTIFIER="46010381014****";
```

```
%%LST PGRPMBR: USRIDENTIFIER="zu9";%%
RETCODE = 0 Operation succeeded

Basic Information
Member Subscriber ID   Group Subscriber ID
zu9                    zu8

Quota Information
Quota Name                        Service Name                      Monitor Key                       Initial Value         Balance               Consumption           Type             Quota Class   Last Reset Date Time       Next Reset Date Time       Status    QuotaFlag     Reset Cause           Allocable Quota Value      Current Cumulate Times            Cumulate Balance Value            Customer Attribute                             Expired Time            SequenceID            Used Flag            Extended Attribute            Extended Attribute 1            Create Time            Group Subscriber ID
zq8                               zs8                               165498897                         102400                102400                0                     Service Level    Volume        2019-03-13 14:24:35        NULL                       Normal    0             NULL                  NULL                       0                                 0                                 --------------zq8----cuspara-------            NULL                    NULL                  NULL                 NULL                          NULL                            NULL                   zu8
zq8                               zs8                               165498897                         8000                  8000                  0                     Service Level    Volume        2019-03-13 14:24:35        NULL                       Normal    1             NULL                  NULL                       0                                 0                                 --------------zq8----cuspara-------            NULL                    NULL                  NULL                 NULL                          NULL                            NULL                   zu8
zq8                               zs8                               165498897                         102400                102400                0                     Service Level    Volume        2019-03-13 14:24:35        NULL                       Normal    0             NULL                  NULL                       0                                 0                                 --------------zq8----cuspara-------            NULL                    NULL                  NULL                 NULL                          NULL                            NULL                   zu8 

Total count = 1

There is together 1 report
---    END
```

## 输出结果说明

| 输出项名称                  | 输出项解释                                                                                                                                                                                                        |
|:-----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Member Subscriber ID   | 表示组成员标识。 取值范围：长度不超过255的字符串。                                                                                                                                                                                  |
| Group Subscriber ID    | 表示组用户标识。 取值范围：长度不超过255的字符串。                                                                                                                                                                                  |
| Quota Name             | 表示配额的名称。 取值范围：长度不超过32的字符串。                                                                                                                                                                                   |
| Service Name           | 表示业务的名称。 取值范围：长度不超过64的字符串。                                                                                                                                                                                   |
| Monitor Key            | 表示配额的监控键值。 取值范围：由0～9、a～z、A～Z以及“-”组成的长度为1～32字节的字符串。 当配额的“类型”为“业务级”时，必须设置此参数。参数取值不能为“2147483647”、“4294967295”和“NULL”。 当配额的“类型”为“会话级”时，此参数为选配。若对端PCEF支持3GPP R9协议，需要配置此参数。参数取值不能为“2147483647”。 该参数取值需要和GGSN保持一致。 |
| Initial Value          | 表示初始分配到的配额值，单位为KB。 取值范围：1～4294967294。                                                                                                                                                                        |
| Balance                | 表示剩余的配额值，单位为KB。 取值范围：0～4294967294。                                                                                                                                                                           |
| Consumption            | 表示已消费的配额值，单位为KB。 取值范围：0～4294967294。                                                                                                                                                                          |
| Type                   | 表示配额的累积类型。 取值范围：“Service Level”：表示收集并计算特定业务的使用情况，如FTP、HTTP等。“Session Level”：表示不区分业务，收集并计算整个IP会话中所有业务的使用量总和。                                                                                                  |
| Quota Class            | 表示配额类型，包括流量、时长、在线时长三种配额类型。  说明： 在基于组共享使用量的动态策略控制场景下，由于组业务不支持关联类型为时长或在线时长的配额，因此这里返回的配额类型只有流量类型。                                                                                                               |
| Last Reset Date Time   | 表示配额本周期开始时间。 取值范围： NULL1970-01-01 00:00:00～2037-12-31 23:59:59：表示1970年01月01日00时00分00秒到2037年12月31日23时59分59秒之间的时间。                                                                                             |
| Next Reset Date Time   | 表示配额下次复位的时间。 取值范围： NULL1970-01-01 00:00:00～2037-12-31 23:59:59：表示1970年01月01日00时00分00秒到2037年12月31日23时59分59秒之间的时间。                                                                                             |
| Status                 | 表示配额状态，即根据需要触发额度事件时已使用的配额占总配额的百分比所划分的十二个级别，它们分别是：Normal、Level1、Level2、Level3、Level4、Level5、Level6、Level7、Level8、Level9、Level10和Exhaust。 例如：“Status = Exhaust”，表示配额耗尽。                                        |
| QuotaFlag              | 表示此配额是不是虚拟配额信息。 取值范围：0：表示此配额不是虚拟配额。1：表示此配额是虚拟配额。                                                                                                                                                             |
| Reset Cause            | 表示配额最近一次复位的触发源。 取值范围： NULL：表示配额未发生复位。Online Reset：表示最近一次复位的触发源是在线复位或者上线复位。Offline Reset：表示最近一次复位的触发源是离线复位。Provisioning Reset：表示最近一次复位的触发源是营帐复位。                                                              |
| Allocable Quota Value  | 表示可分配配额值，单位为KB。 取值范围：0～4294967294。  说明： 以下情况，该字段无效，固定显示为NULL： 此配额为虚拟配额此配额的业务为非组业务此配额的“组配额分配方式”为“缺省分配”                                                                                                        |
| Current Cumulate Times | 当配额的“剩余额处理方式”配置为“累积”和“累积次数”参数不为“0”时参数有效，表示组成员用户虚拟配额的已累积次数。 取值范围：0～2147483645。                                                                                                                                |
| Cumulate Balance Value | 当配额的“剩余额处理方式”配置为“累积”和“累积次数”参数不为“0”时参数有效，表示组成员用户虚拟配额的累计值，单位为KB或秒。 取值范围：0～4294967294。                                                                                                                          |
| Customer Attribute     | 表示配额的自定义属性。 取值范围：长度为不超过64字节的字符串。                                                                                                                                                                             |
| Expired Time           | 表示配额实例的过期时间。 取值范围： NULL：表示配额实例不过期。1970-01-01 00:00:00～2037-12-31 23:59:59：表示1970年01月01日00时00分00秒到2037年12月31日23时59分59秒之间的时间。  说明： 当查询的配额未关联到“重复订购方式”为“多配额记录重复订购”的业务时，该字段无效，固定显示为NULL。                         |
| SequenceID             | 表示配额的实例序号。 取值范围： NULL0～254  说明： 当查询的配额未关联到“重复订购方式”为“多配额记录重复订购”的业务时，该字段无效，固定显示为NULL。                                                                                                                          |
| Used Flag              | 表示配额实例是否已使用的标识。 取值范围： NULL0：用户配额实例未使用1：用户配额实例已使用 说明： 当查询的配额未关联到“重复订购方式”为“多配额记录重复订购”的业务时，该字段无效，固定显示为NULL。                                                                                                     |
| Extended Attribute     | 表示配额的扩展属性。 取值范围：长度为不超过64字节的字符串。                                                                                                                                                                              |
| Extended Attribute 1   | 表示配额的扩展属性1。 取值范围：长度为不超过64字节的字符串。                                                                                                                                                                             |
| Create Time            | 表示配额实例的创建时间。 取值范围： NULL：表示没有创建配额实例。1970-01-01 00:00:00～2037-12-31 23:59:59：表示1970年01月01日00时00分00秒到2037年12月31日23时59分59秒之间的时间。  说明： 当查询的配额未关联到“重复订购方式”为“多配额记录重复订购”的业务时，该字段无效，固定显示为NULL。                        |