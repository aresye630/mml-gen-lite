# 查询闭锁类业务(LST CBAR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来查询该用户签约闭锁业务的控制权信息、闭锁类业务的类型、应用的基本业务群以及各种闭锁业务的签约激活情况。

当用户定制了呼叫闭锁业务时，呼叫闭锁密码被应用，用户的初始密码为1234。如果提供初始密码，在手机上修改或者直接在数据管理控制台修改。

## 注意事项

IMSI、ISDN是条件可选参数，有且只能有一个出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                                                                            |
|:------------|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，6～15位的十进制数字。 可选参数。                                                                                                                                                                                                                                                                                                            |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，1～15位的十进制数字。 可选参数。                                                                                                                                                                                                                                                                                                          |
| BSG         | 基本业务组     | 区分闭锁业务在哪种基本业务上激活。 可选参数。 取值范围： ALL(0)：All Applicable Services(TS1X，TS2X，TS6X，BS2X，BS3X)， 所有可应用的基本业务 。TS1X(1)：Telephony Service，话音业务。TS2X(2)：Short Message Service，短消息业务。TS6X(3)：Facsimile Service Group，传真业务。BS2X(4)：Asynchronous Bearer Service，异步承载业务。BS3X(5)：Synchronous Bearer Service，同步承载业务。TSDX(6): Custom supplementary service，自定义补充业务。 |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                                                                                                                              |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                                                                                                                                                                                                                                                                               |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                                                                                                                                                                                                                                                                             |

## 使用实例

查询IMSI号码为460000009123456在语音业务上激活的闭锁业务。例如：

```
LST CBAR: IMSI="460000009123456",BSG=TS1X;
```

```
%%LST CBAR: IMSI="460000009123456";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000009123456
                          ISDN = 2013521
                         CBCOU = SUBSCRIBER
                   CBCOUReason = NotcaredReason
BAOC
                        ALL BS = NOTPROV
BOIC
                        ALL BS = NOTPROV
BOICExHC
                        ALL BS = NOTPROV
BAIC
                        ALL BS = NOTPROV
BICROAM
                        ALL BS = NOTPROV
BORO
                        ALL BS = NOTPROV

Total count = 10

There is together 1 report

---    END
```