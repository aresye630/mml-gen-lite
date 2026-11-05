# 查询iFC(LST HIFC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于从HSS的业务数据库中查询指定IMPU或PUSI相关的Service Profile中iFC信息。可以:

- 查询指定优先级的iFC，此时操作中PRIORITY参数存在。
- 查询IMPU关联Service Profile中的所有iFC信息，此时操作中的PRIORITY参数缺失。

## 注意事项

参数IMPU和参数PUSI必须存在且只能存在一个。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                               |
|:---------|:-------|:---------------------------------------------------------------------------------------------------|
| IMPU     | IMPU   | 用于指定一个需要查询iFC的IMPU ，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无                 |
| PUSI     | PUSI   | 用于指定一个需要查询iFC信息的PUSI，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无                |
| PRIORITY | 优先级    | 用于指明要查询哪个优先级的iFC，当该参数存在时，查询指定优先级的iFC；当该参数不存在时，查询IMPU关联Service Profile中的所有iFC信息。 取值范围：0～65535 缺省值：无 |

## 使用实例

查询iFC。IMPU：sip:impuinfo@huawei.com。

```
LST HIFC: IMPU="sip:impuinfo@huawei.com";
```

```
%%LST HIFC: IMPU="sip:impuinfo@huawei.com";%%
RETCODE = 0 SUCCESS0001:Operation is successful

PRIORITY              PARTIND              SERVER                DEFHND            SERVINFO           INCLUDEREGREQ      INCLUDEREGRSP      TRIGPT
1                    REGISTERED     sip:server1@huawei.com    SESSION_CONTINUED  Service Information
 2        0                             0                             

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

| 参数标识          | 参数说明                                                               |
|:--------------|:-------------------------------------------------------------------|
| PRIORITY      | 显示iFC的优先级。                                                         |
| PARTIND       | 显示iFC的业务相关性。                                                       |
| SERVER        | 显示iFC的AS地址。                                                        |
| DEFHND        | 显示iFC的默认处理方式。                                                      |
| SERVINFO      | 显示iFC的业务信息。                                                        |
| INCLUDEREGREQ | 显示S-CSCF发起第三方注册时，是否携带第一方注册的请求消息内容：“0”：不携带。“1”：携带。                  |
| INCLUDEREGRSP | 显示S-CSCF发起第三方注册时，iFC是否携带IncludeRegisterResponse标志位：“0”：不携带。“1”：携带。 |
| TRIGPT        | 显示iFC的触发点。                                                         |