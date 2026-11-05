# 增加APN优先级配置(ADD PDPFILTERAPN)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN**

该命令用于增加APN优先级配置。APN优先级可以用于在RAU或者RELOCATION流程中指示新侧保留PDP的顺序。高优先级APN对应的PDP会优先保留，低优先级APN对应的PDP会在切换后主动删掉。

在GU网络存在无线侧PDP能力不足的情况下，可通过此命令配置APN优先级，当系统通过RAU或者Relocation流程切换到GU网络后主动去激活低优先级的PDP，从而确保高优先级PDP业务不受影响。如不配置APN优先级，无线侧将可能随机删除重要的PDP，造成重要业务中断。

#### 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为1024。
- 此命令功能只适用于Gn/Gp组网形式。
- 不在本命令配置的用户范围的用户，不受此功能限制，即不去激活任何PDP；系统若不存在本命令的配置记录，且已打开**SET PDPFILTERCTL**功能，则对全网用户启用该功能。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                                                                  |
|:---------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE | 用户范围   | 可选必选说明：必选参数 该参数用于指定PDP过滤功能适用的用户范围。参考SET PDPFILTERCTL命令。 数据来源：整网规划 取值范围： “ALL_USER(所有用户)”“LOCAL_USER(本网用户)”“FOREIGN_USER(外网用户)”“IMSI_PREFIX(指定IMSI前缀)” 默认值：无 配置原则： “用户范围”的匹配优先级从高到低为：“IMSI_PREFIX(指定IMSI前缀)”，“LOCAL_USER(本网用户)”或“FOREIGN_USER(外网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE  | IMSI前缀 | 可选必选说明：条件必选参数 参数含义：该参数用于指定IMSI前缀。 前提条件: 该参数在“用户范围”参数配置为“IMSI_PREFIX(指定IMSI前缀)”时生效。 数据来源：整网规划 取值范围：1～15位十进制数字字符串。 默认值：无                                                                                                                                                |
| APNNI    | APNNI  | 可选必选说明：必选参数 参数含义：该参数用于指定APNNI名称。 数据来源：整网规划 取值范围：1～62位字符串。 默认值：无 配置原则： APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。相同“IMSI前缀”的“APNNI”不能相同。                                 |
| PRI      | 优先级    | 可选必选说明：必选参数 该参数用于指定优先级，高优先级的配置对应的PDP会优先保留，高优先级的PDP个数未达到最大PDP保留个数时（最大PDP保留个数通过SET PDPFILTERCTL配置），选择次高优先级配置对应的PDP进行保留。 数据来源：整网规划 取值范围：1~100 默认值：无 配置原则：1为最高优先级，100为最低优先级。                                                                                              |
| DESC     | 描述     | 可选必选说明：可选参数 参数含义：该参数是APN优先级配置的描述信息。 数据来源：整网规划 取值范围：0～32位字符串。 默认值：无                                                                                                                                                                                                    |

#### 使用实例

任务描述：

假设某运营商GU网络能力有限，不能同时支持2个及以上的PDP上下文，即当用户从LTE网络切换到GU网络后，运营商期望SGSN按优先级保留1个PDP。为确保重要业务不被中断，运营商需要对全网用户进行如下APN优先级配置：

- “IMSI前缀”为“12302”的用户有两个“APNNI”：“huawei4.com”和“huawei5.com”，运营商期望优先保留“APNNI”为“huawei4.com”所对应的PDP。
- “IMSI前缀”为“1230”的用户，运营商期望优先保留“APNNI”为“huawei3.com”的PDP。
- 对于本网用户，运营商期望优先保留“APNNI”为“huawei2.com”的PDP。
- 对于其他所有用户，运营商期望优先保留“APNNI”为“huawei1.com”的PDP。

配置脚本：

1. 开启PDP过滤功能，设置为最大支持1个PDP：

   SET PDPFILTERCTL: SWITCH=ON, PDPNUM=1;
2. 增加两条“用户范围”为“IMSI\_PREFIX(指定IMSI前缀)”、“IMSI前缀”为“12302”、“APNNI”分别为“huawei4.com”和“huawei5.com”的APN优先级记录，使得在该范围内“APNNI”为“huawei4.com”的优先级高于“huawei5.com”：

   ADD PDPFILTERAPN: SUBRANGE=IMSI\_PREFIX, IMSIPRE="12302", APNNI="huawei4.com", PRI=1;

   ADD PDPFILTERAPN: SUBRANGE=IMSI\_PREFIX, IMSIPRE="12302", APNNI="huawei5.com", PRI=2;
3. 增加一条“用户范围”为“IMSI\_PREFIX(指定IMSI前缀)”、“IMSI前缀”为“1230”、“APNNI”为“huawei3.com”、“优先级”为“1”的APN优先级记录：

   ADD PDPFILTERAPN: SUBRANGE=IMSI\_PREFIX, IMSIPRE="1230", APNNI="huawei3.com", PRI=1;
4. 增加一条“用户范围”为“LOCAL\_USER(本网用户)”、“APNNI”为“huawei2.com”、“优先级”为“1”的APN优先级记录：

   ADD PDPFILTERAPN: SUBRANGE=LOCAL\_USER, APNNI="huawei2.com", PRI=1;
5. 增加一条“用户范围”为“ALL\_USER(所有用户)”、“APNNI”为“huawei1.com”、“优先级”为“1”的APN优先级记录：

   ADD PDPFILTERAPN: SUBRANGE=ALL\_USER, APNNI="huawei1.com", PRI=1;

**任务描述：**

假设某运营商期望只对“IMSI前缀”为“12300”的用户按优先级保留1个PDP，对其他所有用户不限制最大保留的PDP个数，运营商需要进行如下APN优先级配置：

- “IMSI前缀”为“12300”的用户，运营商期望优先保留“APNNI”为“huawei7.com”的PDP。

**配置脚本：**

1. 开启PDP过滤功能，设置为最大支持1个PDP：

   `SET PDPFILTERCTL: SWITCH=ON, PDPNUM=1;`
2. 增加一条“用户范围”为“IMSI\_PREFIX(指定IMSI前缀)”、“IMSI前缀”为“12300”、“APNNI”为“huawei7.com”、“优先级”为“1”的APN优先级记录：

   `ADD PDPFILTERAPN: SUBRANGE=IMSI_PREFIX, IMSIPRE="12300", APNNI="huawei7.com", PRI=1;`