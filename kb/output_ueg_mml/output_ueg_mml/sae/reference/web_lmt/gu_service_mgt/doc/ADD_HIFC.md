# 增加iFC(ADD HIFC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中为指定IMPU或指定PUSI相关的Service Profile添加一个新的iFC（Initial Filter Criteria）。

## 注意事项

- 参数“IMPU”和参数“PUSI”必须存在且只能存在一个。
- 一个IMPU或PUSI最多可以添加16个iFC信息。
- 当使用该命令添加非共享iFC时，局点配置不相同的非共享iFC数量与S-CSCF设备限制的个数相关。如果对端设备是华为CSC3300，则不能超过1025。如果对端设备是其他厂商提供的设备，则需要确认对端设备限制的最大数量。

## 参数说明

| 参数标识          | 参数名称                              | 参数说明                                                                                                                                                                                                                       |
|:--------------|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPU          | IMPU                              | 用于指定一个需要增加iFC的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无                                                                                                                                          |
| PUSI          | PUSI                              | 用于指定一个需要增加iFC信息的PUSI，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 缺省值：无                                                                                                                                        |
| PRIORITY      | 优先级                               | 用于指定一个新iFC的优先级。 取值范围：0～65535 缺省值：无                                                                                                                                                                                         |
| PARTIND       | 业务相关性                             | 用于指定iFC是与注册业务相关还是与非注册业务相关。 取值范围： REGISTERED(Registered)：与注册业务相关UNREGISTERED(Unregistered)：与未注册业务相关PARTIND_DEFAULT(Default)：以上两种状态都会触发的业务 缺省值：PARTIND_DEFAULT                                                               |
| SERVER        | AS地址                              | 用于指定一个用来指明该iFC所要触发的AS地址，配置原则是：格式必须为SIP格式。 取值范围：长度不超过127的字符串 缺省值：无                                                                                                                                                          |
| DEFHND        | 默认处理方式                            | 用于指定一个触发指定AS失败后的处理方式。 取值范围： SESSION_CONTINUED(Session continued)：会话继续SESSION_TERMINATED(Session terminated)：会话中止DEFHANDLING_DEFAULT(Default handling)：由AS决定如何处理该会话，当取该值时，HSS下发给S-CSCF的iFC中将不包含这个参数 缺省值：DEFHANDLING_DEFAULT |
| SERVINFO      | 业务信息                              | 用于指明该iFC的描述。 取值范围：长度不超过127的字符串 缺省值：无                                                                                                                                                                                       |
| INCLUDEREGREQ | 携带第一方注册请求                         | 用于指定S-CSCF发起第三方注册时，是否携带第一方注册的请求消息内容。 取值范围：NO(No)：不携带。YES(Yes)：携带。 默认值：无。 说明：执行该命令并且不输入该参数时，系统会设置初始值“NO(No)”。                                                                                                               |
| TRIGPT        | 触发点                               | 用于指定该iFC的触发点。 取值范围：长度不超过3072的字符串 缺省值：无 配置原则：该参数的配置需要满足结合范式CNF和非结合范式DNF运算规则，如果输入中包含特殊字符（\";,'=），则在这些特殊字符前添加转义字符“\”。                                                                                                         |
| INCLUDEREGRSP | iFC是否携带IncludeRegisterResponse标志位 | 用于指定S-CSCF发起第三方注册时，iFC是否携带IncludeRegisterResponse标志位。该参数取值需要与网络中S-CSCF对接的AS设备协商确定。 取值范围：NO(No)：不携带。YES(Yes)：携带。 默认值：无。 说明：执行该命令并且不输入该参数时，系统会设置初始值“NO(No)”。                                                                 |

## 使用实例

增加iFC。IMPU：sip:impuinfo@huawei.com，优先级：1，业务相关性：REGISTERED，AS地址：sip:server1@huawei.com，默认处理方式：SESSION\_CONTINUED，业务信息：Service Information，携带第一方注册请求：NO，触发点：Triffer point。

```
ADD HIFC: IMPU="sip:impuinfo@huawei.com", PRIORITY=1, PARTIND=REGISTERED, SERVER="sip:server1@huawei.com", DEFHND=SESSION_CONTINUED, SERVINFO="Service Information", INCLUDEREGREQ=NO, TRIGPT="Triffer point";
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示

| 错误码          | 错误码解释        | 原因分析                      | 处理建议                                                                                                                        |
|:-------------|:-------------|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| ERR900003021 | IFC的数量已经达到上限 | 一个IMPU或PUSI添加的iFC记录超过16个。 | 根据实际情况，如需给IMPU或PUSI增加iFC，处理步骤如下： 执行LST HIFC命令，查询已存在的iFC记录。执行RMV HIFC命令，删除不必要的iFC记录。执行本命令给IMPU或PUSI增加iFC，确保增加的iFC记录数在规定范围之内。 |