# 查询RCS业务(LST HRCSSERVICE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户的RCS签约信息。

## 注意事项

“IMSI”和“MSISDN”是可选参数，必须输入且只能有一个参数出现。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                          |
|:-------|:-------|:------------------------------|
| IMSI   | IMSI   | 用于标识查询哪个IMSI对应用户的RCS业务签约信息。   |
| ISDN   | MSISDN | 用于标识查询哪个MSISDN对应用户的RCS业务签约信息。 |

## 使用实例

查询RCS签约信息。IMSI：460009876543210。

```
LST HRCSSERVICE: IMSI="460009876543210";
```

```
%%LST HRCSSERVICE: IMSI="460009876543210";%%
RETCODE = 0 SUCCESS0001:操作成功

IMSI            ISDN          IMPROVISIONINGSTATUS IMACTIVATIONSTATUS FSPROVISIONINGSTATUS FSACTIVATIONSTATUS VSPROVISIONINGSTATUS VSACTIVATIONSTATUS RCSTCACCEPTTS RCSTCREQSTATUS WHOLESALEID SEGMENTID RCSWELCOMEMSGSENT SIFCID1 SIFCID2 SIFCID3 DEVICE_CN IMEI FIRSTIMSREGTS LASTIMSREGTS FIRSTRCSCONFIGTS LASTRCSCONFIGTS PWASSIGNDATE    SERVICESATTR DEVICESATTR_CN DEVICESATTR
460009876543210 8613955555555 1                    1                  1                    1                  1                    1                                3              1234        0         0                 4099    4353    4609    0                                                                          20131205174050Z                             

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|       错误码 | 错误码解释                      | 原因分析                                               | 处理建议                                             |
|----------:|:---------------------------|:---------------------------------------------------|:-------------------------------------------------|
| 900003466 | 关联的IMS用户未开户或者和IMPI关联关系不存在。 | 未执行ADD HIMSI与IMSI建立关联关系。未执行ADD HISDN与MSISDN建立关联关系。 | 通过ADD HIMSI与IMSI建立关联关系。通过ADD HISDN与MSISDN建立关联关系。 |
| 900003472 | RCS业务不存在。                  | 未签约RCS业务。                                          | 通过ADD HRCSSERVICE命令签约RCS业务。                      |

以下列出的是未包含在本命令输入参数中的输出项，其他输出项的详细说明请参见参数说明。

| 输出项名称                | 输出项解释                                                                                    |
|:---------------------|:-----------------------------------------------------------------------------------------|
| IMPROVISIONINGSTATUS | 用于显示是否给该用户提供了聊天业务。                                                                       |
| IMACTIVATIONSTATUS   | 用于显示聊天业务对于该用户是否是可用的。                                                                     |
| FSPROVISIONINGSTATUS | 用于显示是否给该用户提供了文件共享业务。                                                                     |
| FSACTIVATIONSTATUS   | 用于显示文件共享业务对于该用户是否是可用的。                                                                   |
| VSPROVISIONINGSTATUS | 用于显示是否给该用户提供了视频共享业务。                                                                     |
| VSACTIVATIONSTATUS   | 用于显示视频共享业务对于该用户是否是可用的。                                                                   |
| RCSTCACCEPTTS        | 用于显示网络中用户接受Rcs-e条款的时间。                                                                   |
| RCSTCREQSTATUS       | 用于显示RCS条款和条款接受请求的状态。下面的值已经被定义： 0-未处理 1-TC 接受 2-TC 拒绝 3-TC 接受，待激活 其它的值是为了拓展运用，可以解释为TC未接受。 |
| WHOLESALEID          | 用于RCS服务特性和每个分发标识服务标记的区分。这一元素表示了用户与第三方的合约关系（例如：网络实际的操作者）。                                 |
| SEGMENTID            | 用于RCS服务特性的区分。这一元素显示了分配给用户的计费方式（例如：0：预付费，1：后付费）。                                          |
| RCSWELCOMEMSGSENT    | 用于显示是否已经给用户发送明确的RCS欢迎消息。                                                                 |
| SIFCID1～3            | 用于显示共享的IFC用户标识。                                                                          |
| DEVICE_CN            | 用于显示设备的连接节点。                                                                             |
| IMEI                 | 用于显示最后一个使用的设备的私有用户标识。                                                                    |
| FIRSTIMSREGTS        | 用于显示首个对于私有用户标识的设备管理活动的时间戳。                                                               |
| LASTIMSREGTS         | 用于显示最后一个对于私有用户标识的设备管理活动的时间戳。                                                             |
| FIRSTRCSCONFIGTS     | 用于显示首个私有用户标识的IMS/RCS注册活动的时间戳。                                                            |
| LASTRCSCONFIGTS      | 用于显示最后一个私有用户标识的IMS/RCS注册活动的时间戳。                                                          |
| PWASSIGNDATE         | 用于显示用户密码分配的时间，需要预先在HCS-RCS中申请密码分配策略。                                                     |
| SERVICESATTR         | 用于显示服务的附加可用多值属性。                                                                         |
| DEVICESATTR_CN       | 用于显示设备连接节点的附加可用多值属性。                                                                     |
| DEVICESATTR          | 用于显示设备的附加可用多值属性。                                                                         |