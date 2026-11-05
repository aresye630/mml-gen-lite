# 修改iFC信息模板(MOD HIFCTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于在HSS的业务数据库中修改一个iFC基本信息模板，在该操作中系统通过iFC模板ID来唯一标识一条iFC基本信息模板记录，可以修改除TPLID以外的所有参数。

## 注意事项

- 当“默认处理方式”取值为“DEFHANDLING\_DEFAULT”时，HSS下发给CSCF的iFC中将不包含Default handling。

- 待修改的可选参数必须至少设置其中一个，否则HSS返回失败。

## 参数说明

| 参数标识          | 参数名称                              | 参数说明                                                                                                                                                                        |
|:--------------|:----------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN         | HLR序列号                            | 用于标识一个HLR序列号。 取值范围：0~255 默认值：无。 说明：当该参数不输入时，系统默认初始设置值为0。                                                                                                                    |
| TPLID         | iFC模板ID                           | 用于指定需要对哪一个iFC信息模板记录的参数进行修改或调整，操作员可以使用LST HTPLINF操作查询获得。                                                                                                                     |
| TPLNAME       | iFC模板名称                           | 用于具体描述一个iFC信息模板，以便于识别。 取值范围：长度不超过64的字符串，字符串由数字、字母、“.”、“-”或“_”组成。 默认值：无                                                                                                      |
| PRIORITY      | 优先级                               | 用于指定一个新iFC的优先级。 取值范围：0～65535 默认值：无                                                                                                                                          |
| PARTIND       | 业务相关性                             | 用于指定iFC是与注册业务相关还是与非注册业务相关。 取值范围： REGISTERED(Registered)：与注册业务相关UNREGISTERED(Unregistered)：与未注册业务相关PARTIND_DEFAULT(Default)：以上两种状态都会触发的业务 默认值：无                              |
| SERVER        | iFC的AS地址                          | 用于指定iFC所要触发的AS地址，地址格式必须为SIP格式。HSS与对端网元（AS）对接的参数之一，需要和对端网元配置的地址协商一致，若不一致，HSS将无法于完成发往对端网元的业务处理。 取值范围：长度不超过127的字符串 默认值：无                                                       |
| DEFHND        | 默认处理方式                            | 用于指定一个触发指定AS失败后的处理方式。 取值范围： SESSION_CONTINUED(Session continued)：会话继续。SESSION_TERMINATED(Session terminated)：会话中止。DEFHANDLING_DEFAULT(Default handling)：由AS决定如何处理该会话。 默认值：无 |
| SERVINFO      | 业务信息                              | 用于指定该iFC的描述。 取值范围：长度不超过127的字符串 缺省值：无                                                                                                                                        |
| INCLUDEREGREQ | 携带第一方注册请求                         | 用于指定S-CSCF发起第三方注册时，是否携带第一方注册的请求消息内容。 取值范围：NO(No)：不携带。YES(Yes)：携带。 默认值：无                                                                                                     |
| TRIGPT        | 触发点                               | 用于指定该iFC的触发点。 取值范围：长度不超过3072的字符串 默认值：无 配置原则：该参数的配置需要满足结合范式CNF和非结合范式DNF运算规则，如果输入中包含特殊字符（\";,'=），则在这些特殊字符前添加转义字符“\”。                                                          |
| COMMENT       | 模板注释说明                            | 用于具体描述一个iFC信息模板的注释信息，以便于理解和使用。 取值范围：长度不超过512的字符串 默认值：无                                                                                                                      |
| INCLUDEREGRSP | iFC是否携带IncludeRegisterResponse标志位 | 用于指定S-CSCF发起第三方注册时，iFC是否携带IncludeRegisterResponse标志位。该参数取值需要与网络中S-CSCF对接的AS设备协商确定。 取值范围：NO(No)：不携带。YES(Yes)：携带。 默认值：无。                                                      |

## 使用实例

修改iFC信息模板。iFC模板ID：10，iFC模板名称：Modify an iFC Template。

```
MOD HIFCTPL: TPLID=10, TPLNAME="Modify an iFC Template";
```