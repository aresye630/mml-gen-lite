# 修改iFC(MOD HIFC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中修改指定IMPU或PUSI相关的Service Profile所包含的某个iFC的信息。

## 注意事项

- 参数IMPU和参数PUSI必须存在且只能存在一个。
- 参数NEWPRI、参数PARTIND、参数SERVER、参数DEFHND、参数SERVINFO、参数INCLUDEREGREQ和参数TRIGPT必须至少存在一个。

## 参数说明

| 参数标识          | 参数名称                              | 参数说明                                                                                                                                                                                                                                                             |
|:--------------|:----------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPU          | IMPU                              | 用于指定一个需要修改iFC的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无                                                                                                                                                                                |
| PUSI          | PUSI                              | 用于指定一个需要修改iFC信息的PUSI，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无                                                                                                                                                                              |
| PRIORITY      | 优先级                               | 用于指定所要修改iFC的优先级。 取值范围：0～65535 缺省值：无                                                                                                                                                                                                                              |
| NEWPRI        | 新的优先级                             | 用于指定所要修改的iFC的新优先级。 取值范围：0～65535 缺省值：无                                                                                                                                                                                                                            |
| PARTIND       | 业务相关性                             | 用于指定iFC是与注册业务相关还是与非注册业务相关： REGISTERED：与注册业务相关 UNREGISTERED：与未注册业务相关 PARTIND_DEFAULT：以上两种状态都会触发的业务。 取值范围： REGISTERED(Registered)UNREGISTERED(Unregistered)PARTIND_DEFAULT(Default) 缺省值：无                                                                          |
| SERVER        | AS地址                              | 用于指定该iFC所要触发的AS地址。配置原则是：格式必须为SIP格式。 取值范围：长度不超过127的字符串 缺省值：无                                                                                                                                                                                                      |
| DEFHND        | 默认处理方式                            | 用于指定一个触发指定AS失败后的处理方式： SESSION_CONTINUED：会话继续 SESSION_TERMINATED：会话中止 DEFHANDLING_DEFAULT：由AS决定如何处理该会话，当取该值时，HSS下发给CSCF的iFC中将不包含这个参数。 取值范围： SESSION_CONTINUED(Session continued)SESSION_TERMINATED(Session terminated)DEFHANDLING_DEFAULT(Default handling) 缺省值：无 |
| SERVINFO      | 业务信息                              | 用于指定该iFC的相关描述。 取值范围：长度不超过127的字符串 缺省值：无                                                                                                                                                                                                                           |
| INCLUDEREGREQ | 携带第一方注册请求                         | 用于指定S-CSCF发起第三方注册时，是否携带第一方注册的请求消息内容。 取值范围：NO(No)：不携带。YES(Yes)：携带。 缺省值：无                                                                                                                                                                                          |
| TRIGPT        | 触发点                               | 用于指定该iFC的触发点。 取值范围：长度不超过3072的字符串 缺省值：无 配置原则：该参数的配置需要满足结合范式CNF和非结合范式DNF运算规则，如果输入中包含特殊字符（\";,'=），则在这些特殊字符前添加转义字符“\”。                                                                                                                                               |
| INCLUDEREGRSP | iFC是否携带IncludeRegisterResponse标志位 | 用于指定S-CSCF发起第三方注册时，iFC是否携带IncludeRegisterResponse标志位。该参数取值需要与网络中S-CSCF对接的AS设备协商确定。 取值范围：NO(No)：不携带。YES(Yes)：携带。 默认值：无。                                                                                                                                           |

## 使用实例

修改iFC。IMPU：sip:impuinfo@huawei.com，优先级：1，新的优先级：3。

```
MOD HIFC: IMPU="sip:impuinfo@huawei.com", PRIORITY=1, NEWPRI=3;
```