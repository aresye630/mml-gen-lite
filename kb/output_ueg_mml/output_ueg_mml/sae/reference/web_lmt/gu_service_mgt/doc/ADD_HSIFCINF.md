# 增加共享iFC模板信息(ADD HSIFCINF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

本命令属于高危命令，执行不当会使引用该模板的用户数据被同步修改，因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于向HSS的业务数据库的指定的共享iFC模板中添加iFC信息。

当运营商需要向所有引用指定共享iFC模板的用户增加一个新业务时，操作员可以使用**ADD HSIFCINF**命令向该模板增加一个新的共享iFC模板信息，以增加对新业务的触发规则。在该命令中，关键参数“PARTIND”需要与对端网元协商。

为同一个共享iFC模板增加多个iFC模板信息时，该命令需要执行多次。配置举例请参考使用实例3。

## 注意事项

- 每个共享iFC模板中最多可以添加16个iFC的信息。
- 在HSS中，所有共享iFC模板内的iFC模板信息总数不能超过5000条。
- 如果操作员在指定共享iFC模板中增加了一条共享iFC模板信息，则所有引用该模板的用户都将增加这条共享iFC模板信息，可能会影响用户业务，请操作员在执行该操作之前仔细确认任务的可行性。

## 参数说明

| 参数标识          | 参数名称                              | 参数说明                                                                                                                                                                                                                                                                       |
|:--------------|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN         | HLR序列号                            | 用于标识一个HLR序列号，系统可以通过该索引找到需要增加共享iFC模板信息的共享iFC模板。操作员可以使用LST HTPLINF命令查询获得。 可选必选说明：可选参数 取值范围：0~255 默认值：无。 说明：当该参数不输入时，系统默认初始设置值为0。                                                                                                                                             |
| SIFCTPLID     | 共享iFC模板ID                         | 用于标识一个共享iFC模板ID索引，系统可以通过该索引找到需要增加共享iFC模板信息的共享iFC模板。操作员可以使用LST HTPLINF命令查询获得。 可选必选说明：必选参数                                                                                                                                                                                   |
| IFCNAME       | iFC名称                             | 用于标识所要添加共享IFC模板的IFC信息名称。 可选必选说明：可选参数 取值范围：长度不超过64的字符串 默认值：无。                                                                                                                                                                                                               |
| PRIORITY      | 优先级                               | 用于指定一个新共享iFC的优先级。需要指出的是，该参数数字越小，优先级越高，0代表最高优先级。 可选必选说明：必选参数 取值范围：0～65535 默认值：无。                                                                                                                                                                                            |
| PARTIND       | 业务相关性                             | 指定共享iFC是与注册业务相关还是与非注册业务相关。 可选必选说明：可选参数 取值范围： REGISTERED(Registered)：与注册业务相关，即当用户当前注册状态为注册时，触发该共享iFC。UNREGISTERED(Unregistered)：与未注册业务相关，即当用户当前注册状态为未注册时，触发该共享iFC。PARTIND_DEFAULT(Default)：以上两种状态都会触发业务。 默认值：PARTIND_DEFAULT(Default)。                                      |
| SERVER        | 共享iFC的AS地址                        | 用于指定共享iFC所要触发的AS地址。该参数的配置规则是：地址格式必须为SIP格式。需要和对端网元（AS）配置的地址一致，若不一致，HSS将无法完成发往对端网元的业务处理。 可选必选说明：必选参数 取值范围：由字母、十进制数字、“.”、“:”、“;”、“=”、“?”、“@”、“&”等特殊字符或转义字符“\”组成的长度不超过127的字符串。 默认值：无。 配置约束：该参数的配置需要满足SIP标准协议，如果输入中包含“;”和“=”，则在这些特殊字符前添加转义字符“\”。                                |
| DEFHND        | 默认处理方式                            | 用于指定一个触发指定AS失败后的处理方式。 可选必选说明：可选参数 取值范围： SESSION_CONTINUED(Session continued)：会话继续。SESSION_TERMINATED(Session terminated)：会话中止。DEFHANDLING_DEFAULT(Default handling)：由AS决定如何处理该会话。 默认值：DEFHANDLING_DEFAULT(Default handling)。                                               |
| SERVINFO      | 业务信息                              | 用于指明该共享iFC的描述。 可选必选说明：可选参数 取值范围：长度不超过127的字符串 默认值：无。                                                                                                                                                                                                                        |
| INCLUDEREGREQ | 携带第一方注册请求                         | 用于指定S-CSCF发起第三方注册时，是否携带第一方注册的请求消息内容。 可选必选说明：可选参数 取值范围： NO(No)：不携带。YES(Yes)：携带。 默认值：无。 说明：执行该命令并且不输入该参数时，系统会设置初始值“NO(No)”。                                                                                                                                                  |
| TRIGPT        | 触发点                               | 用于指定该共享iFC的触发点。触发点用来决定是否去触发应用服务器。它的运算规则有两种：结合范式CNF（Conjunctive Normal Form）和非结合范式DNF（Disjunctive Normal Form），这两种运算规则总称正规表达式。若是没有触发点实例，则表明是无条件触发到申请服务器上。 可选必选说明：可选参数 取值范围：长度不超过3072的字符串 默认值：无。 配置原则：该参数的配置需要满足结合范式CNF和非结合范式DNF运算规则，如果输入中包含特殊字符（\";,'=），则在这些特殊字符前添加转义字符“\”。 |
| INCLUDEREGRSP | iFC是否携带IncludeRegisterResponse标志位 | 用于指定S-CSCF发起第三方注册时，iFC是否携带IncludeRegisterResponse标志位。该参数取值需要与网络中S-CSCF对接的AS设备协商确定。 可选必选说明：可选参数 取值范围：NO(No)：不携带。YES(Yes)：携带。 默认值：无。 说明：执行该命令并且不输入该参数时，系统会设置初始值“NO(No)”。                                                                                                     |

## 使用实例

1. 增加共享iFC模板中的iFC信息，“共享iFC模板ID”为“10”，“优先级”为“10”，“业务相关性”为“REGISTERED(Registered)”，“共享iFC的AS地址”为“sip:as.huawei.com”，“默认处理方式”为“SESSION\_CONTINUED(Session continued)”，“业务信息”为“as”，“携带第一方注册请求”为“NO”，“触发点”为“Triffer point”，“iFC是否携带IncludeRegisterResponse标志位”为“NO”：

   ```
   ADD HSIFCINF: SIFCTPLID=10, PRIORITY=10, PARTIND=REGISTERED, SERVER="sip:as.huawei.com", DEFHND=SESSION_CONTINUED, SERVINFO="as", INCLUDEREGREQ=NO, TRIGPT="Triffer point", INCLUDEREGRSP=NO;
   ```
2. 增加共享iFC模板中的iFC信息，“共享iFC模板ID”为“11”，“优先级”为“5”，“业务相关性”为“PARTIND\_DEFAULT(Default)”，“共享iFC的AS地址”为“sip:as.huawei.com”，“默认处理方式”为“SESSION\_CONTINUED(Session continued)”，“业务信息”为“AS HOST”：

   ```
   ADD HSIFCINF: SIFCTPLID=11, PRIORITY=5, PARTIND=PARTIND_DEFAULT, SERVER="sip:as.huawei.com", DEFHND=SESSION_CONTINUED, SERVINFO="AS HOST";
   ```
3. 为ID为1的共享iFC模板添加3个共享iFC信息，其操作举例如下：

   ```
   /*配置共享iFC模板*/ 
   ADD HSIFCTPL: TPLID=1, TPLNAME="Template_1", COMMENT="Template_1";

   /*配置共享iFC模板详细信息*/ 
   ADD HSIFCINF: SIFCTPLID=1, PRIORITY=90, PARTIND=REGISTERED, SERVER="sip:ats-0.home1.com", DEFHND=SESSION_CONTINUED, TRIGPT="<TriggerPoint><ConditionTypeCNF>0</ConditionTypeCNF><SPT><ConditionNegated>0</ConditionNegated><Group>5</Group><Method>REGISTER</Method></SPT></TriggerPoint>";
   ADD HSIFCINF: SIFCTPLID=1, PRIORITY=211, PARTIND=PARTIND_DEFAULT, SERVER="sip:ats-0.home1.com\;orig", DEFHND=SESSION_CONTINUED, TRIGPT="<TriggerPoint><ConditionTypeCNF>1</ConditionTypeCNF><SPT><ConditionNegated>0</ConditionNegated><Group>0</Group><Method>INVITE</Method></SPT><SPT><ConditionNegated>0</ConditionNegated><Group>1</Group><SessionCase>0</SessionCase></SPT><SPT><ConditionNegated>0</ConditionNegated><Group>1</Group><SessionCase>3</SessionCase></SPT><SPT><ConditionNegated>1</ConditionNegated><Group>2</Group><SIPHeader><Header>P-Served-User</Header></SIPHeader></SPT><SPT><ConditionNegated>1</ConditionNegated><Group>3</Group><RequestURI>.*cic=.*</RequestURI></SPT><SPT><ConditionNegated>1</ConditionNegated><Group>4</Group><SIPHeader><Header>User-Agent</Header><Content>.*FstUC.*</Content></SIPHeader></SPT><SPT><ConditionNegated>1</ConditionNegated><Group>5</Group><SIPHeader><Header>P-Access-Network-Info</Header><Content>3P.C</Content></SIPHeader></SPT></TriggerPoint>";
   ADD HSIFCINF: SIFCTPLID=1, PRIORITY=236, PARTIND=PARTIND_DEFAULT, SERVER="sip:ats-0.home1.com", DEFHND=SESSION_CONTINUED, TRIGPT="<TriggerPoint><ConditionTypeCNF>1</ConditionTypeCNF><SPT><ConditionNegated>0</ConditionNegated><Group>0</Group><Method>INVITE</Method></SPT><SPT><ConditionNegated>0</ConditionNegated><Group>1</Group><SessionCase>1</SessionCase></SPT><SPT><ConditionNegated>0</ConditionNegated><Group>1</Group><SessionCase>2</SessionCase></SPT><SPT><ConditionNegated>1</ConditionNegated><Group>3</Group><RequestURI>.*cic=.*</RequestURI></SPT><SPT><ConditionNegated>1</ConditionNegated><Group>4</Group><SIPHeader><Header>P-Access-Network-Info</Header><Content>3P.C</Content></SIPHeader></SPT></TriggerPoint>";
   ADD HSIFCINF: SIFCTPLID=1, PRIORITY=99, PARTIND=REGISTERED, SERVER="sip:ats-0.home1.com", DEFHND=SESSION_CONTINUED, TRIGPT="<TriggerPoint><ConditionTypeCNF>1</ConditionTypeCNF><SPT><ConditionNegated>0</ConditionNegated><Group>0</Group><Method>SUBSCRIBE</Method></SPT><SPT><ConditionNegated>0</ConditionNegated><Group>1</Group><SIPHeader><Header>Event</Header><Content>ua-profile.*</Content></SIPHeader></SPT><SPT><ConditionNegated>0</ConditionNegated><Group>1</Group><SIPHeader><Header>Event</Header><Content>call-completion.*</Content></SIPHeader></SPT><SPT><ConditionNegated>0</ConditionNegated><Group>1</Group><SIPHeader><Header>Event</Header><Content>ccbs.*</Content></SIPHeader></SPT></TriggerPoint>";
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|       错误码 | 消息解释          | 原因分析                                                                                             | 处理建议                                                                                                                                                                                                            |
|----------:|:--------------|:-------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 900003023 | 指定优先级的IFC已经存在 | 原因为下列情况中的一种： 同一共享iFC模板下，输入的“优先级”在该模板中已存在。同一Service Profile信息模板下，绑定的多个共享iFC模板或iFC模板中已存在相同优先级的iFC。 | 执行LST HSIFCINF查询该共享iFC模板下已存在的优先级，重新输入“优先级”参数，确保与已有的iFC优先级不重复再执行该命令。执行LST HSPTPL查询Service Profile信息模板下绑定的共享iFC模板ID和iFC模板ID，再执行LST HSIFCINF和LST HIFCTPL查询共享iFC模板和iFC模板下已存在的优先级，重新输入“优先级”参数，确保与已有的iFC优先级不重复再执行该命令。 |