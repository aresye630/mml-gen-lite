# 增加基于IMSI的缺省NI策略(ADD DFTNIPLCYIMSI)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于基于用户范围配置MME的缺省NI（Network Identity）策略，即通过用户特征（如是否签约特定APN）决策是否向UE下发缺省NI。

应用场景为：当现网全局的缺省NI策略不适用所有用户时，通过本配置达到运营商希望针对本网用户、IMSI号段来分别配置缺省NI策略的效果。

#### 注意事项

- 该命令最大记录数为1024。
- 该命令执行后立即生效。
- 该命令与**SET DFTNIPLCY**命令均可对缺省NI策略进行配置。系统会首先匹配本命令的配置记录，若发现系统中不存在或不匹配本命令的配置记录才会匹配**SET DFTNIPLCY**命令的配置记录。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:-------------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE     | 用户范围            | 可选必选说明：必选参数 参数含义：该参数用于表示MME上配置AM策略控制参数的用户范围。 数据来源：全网规划 取值范围： “HOME_USER（本网用户）”：本网用户“IMSI_PREFIX（IMSI前缀）”：IMSI前缀“SPECIFIC_IMSI（特定IMSI）”：特定IMSI 默认值：无 配置原则： AM策略匹配的优先级从高到低依次为：“SPECIFIC_IMSI（特定IMSI）”、“IMSI_PREFIX(IMSI前缀)”、“HOME_USER(本网用户)”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| NOID         | 运营商标识           | 可选必选说明：条件必选参数 参数含义：该参数用于指定运营商标识。 前提条件：该参数在“用户范围”参数配置为“HOME_USER（本网用户）”后生效。 数据来源：整网规划 取值范围：0~64，128~254 默认值：无 配置规则： 若该参数需要配置为0或128~254之间的值时，须先在ADD MNO中配置取值相同的“MNOID”参数。 若该参数需要配置为1~64之间的值时，须先在ADD MVNO中配置取值相同的“MVNOID”参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| IMSIPRE      | IMSI前缀          | 可选必选说明：该参数在“SUBRANGE”配置为“IMSI_PREFIX”时为条件必选参数。 参数含义：该参数用于指定应用AM策略和UE策略的用户的IMSI前缀。 数据来源：全网规划 取值范围：字符串类型，输入长度范围是5~14。只允许输入十进制数字（0-9）。 默认值：无 配置原则： 不可与“IMSI”相同。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| IMSI         | IMSI            | 可选必选说明：条件必选参数 参数说明：该参数用于指定国际移动用户标识。 前提条件：此参数在“用户范围”设置为“SPECIFIC_IMSI(特定IMSI)”后生效。 取值范围：14-15位十进制数字字符串 默认值：无 配置原则： 指定单用户范围时使用该参数，不可与“IMSIPRE（IMSI前缀）”相同。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| MMEAPNSW     | 基于APN下发缺省NI功能开关 | 可选必选说明：可选参数 参数含义：该参数用于控制MME是否支持基于特定APN关键字下发缺省NI功能。当本参数设置为"ON"时，MME会根据用户签约的APN前缀是否匹配配置的特定APN关键字（ADD DFTNIAPN命令中“APN关键字”参数）来判断用户是否需要下发缺省NI；如果APN匹配成功，MME会下发缺省NI给UE。 数据来源：全网规划 取值范围： “OFF（关闭）”：关闭 “ON（开启）”：开启 默认值：“OFF（关闭）”。  说明： 本开关开启后，如果MME收到了HSS发送的 Insert Subscriber Data Request或Update Location Answer消息，且消息中携带的签约APN前缀与配置的特定APN关键字（ADD DFTNIAPN命令中“APN关键字”参数）匹配，那么会向UE发送EMM information消息。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MMEDFTNI     | 缺省NI取值策略        | 可选必选说明：条件可选参数 前提条件：“基于APN下发缺省NI功能开关”取值为“ON（开启）”时条件可选参数。 参数含义：该参数用于控制MME缺省NI下发策略。 对于勾选的缺省NI下发时，MME会根据用户签约的APN前缀是否匹配配置的特定APN关键字（ADD DFTNIAPN命令中“APN关键字”参数）来判断用户是否需要下发缺省NI；如果APN匹配成功，MME会下发缺省NI。 对于未勾选的缺省NI下发时，不考虑用户是否签约特定APN，默认下发缺省NI。 数据来源：全网规划 取值范围：如果全部不勾选，相当于“基于APN下发缺省NI功能”未开启。 “MMEPCFFUNC（MMEPCFFUNC）”：SET MMEPCFFUNC配置的缺省NI"PCRFPLCY（PCRFPLCY）"：SET PCRFPLCY配置的缺省NI“AREAMMINFO（AREAMMINFO）”：ADD AREAMMINFO配置的缺省NI“USRMMINFO（USRMMINFO）”：ADD USRMMINFO配置的缺省NI“MVNO（MVNO）”：ADD MVNO配置的缺省NI“MNO（MNO）”：ADD MNO配置的缺省NI 默认值："MNO-1&MVNO-1&USRMMINFO-1&AREAMMINFO-1&PCRFPLCY-1&MMEPCFFUNC-1"  说明： 在开启基于PCRF的动态NI功能的场景下，当PCRF取消动态NI时，网络侧下发的缺省NI取值优先级如下：SET PCRFPLCY>ADD AREAMMINFO>ADD USRMMINFO>ADD MVNO或ADD MNO; 在开启基于PCF的动态NI功能的场景下，当PCF取消动态NI时，网络侧下发的缺省NI取值优先级如下：SET MMEPCFFUNC>ADD AREAMMINFO>ADD USRMMINFO>ADD MVNO或ADD MNO; 未开启动态NI功能的场景下，网络侧下发的缺省NI取值优先级如下：ADD AREAMMINFO>ADD USRMMINFO>ADD MVNO或ADD MNO。 |
| HSSBYPASSAPN | 是否使用最小签约数据      | 可选必选说明：条件可选参数 前提条件：“基于APN下发缺省NI功能开关”取值为“ON（开启）”时条件可选参数 参数含义：该参数用于控制是否使用最小签约数据（ADD HSSBPUSRSUB、ADD HSSBPAPNGRP、ADD HSSBPAPNSUB关联的最小APN签约数据）进行APN关键字匹配。 当用户进入HSS BYPASS状态后，由于无法获取用户真实签约数据，在开启“基于APN下发缺省NI功能开关”时，APN会匹配失败，用户始终不下发缺省NI，该参数用于控制是否使用最小签约数据替代真实签约数据进行APN匹配。 数据来源：全网规划 取值范围： “YES（是）”“NO（否）” 默认值：“NO（否）” 配置原则：除非局点有特殊的诉求，否则不建议开启该开关。  说明： 本参数仅在命令SET HSSBYPASS的参数“IWKSUBEN”配置为“ON（开启）”时生效，如果“IWKSUBEN”配置为“OFF（关闭）”，MME不受本参数控制，会直接使用最小签约数据（ADD HSSBPUSRSUB、ADD HSSBPAPNGRP、ADD HSSBPAPNSUB关联的最小APN签约数据）进行APN关键字匹配。                                                                                                                                                                                                                                                                                                                                                                                       |

#### 使用实例

增加基于IMSI的缺省NI策略：“用户范围”设置为“IMSI\_PREFIX”，IMSI前缀为46009876000001，基于APN下发缺省NI功能开关打开，并且指定默认NI的范围为SET MMEPCFFUNC、SET PCRFPLCY、ADD AREAMMINFO、ADD USRMMINFO、ADD MVNO、ADD MNO配置的NI，且不使用最小签约数据。

```
ADD DFTNIPLCYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="46009876000001", MMEAPNSW=ON, MMEDFTNI=AREAMMINFO-1&MMEPCFFUNC-1&MNO-1&MVNO-1&PCRFPLCY-1&USRMMINFO-1, HSSBYPASSAPN=NO;
```