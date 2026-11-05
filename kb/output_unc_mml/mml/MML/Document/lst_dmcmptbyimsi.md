# 查询IMSI对应的Diameter兼容性(LST DMCMPTBYIMSI)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询Diameter兼容性参数策略。

#### 注意事项

无

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                                 |
|:---------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE | 用户范围   | 可选必选说明：可选参数 参数含义：该参数用于指定Diameter兼容性参数策略的用户范围。 数据来源：全网规划 取值范围：“FOREIGN_USER(外网用户)”“HOME_USER(本网用户)”“IMSI_PREFIX(指定IMSI前缀)” 默认值：无                                                                                      |
| NOID     | 运营商标识  | 可选必选说明：可选参数 参数含义：该参数用于指定运营商标识。 前提条件：该参数在“用户范围”参数配置为“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”后生效。 数据来源：全网规划 取值范围：0～64，128～254 默认值：无  说明： 对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO/MVNO运营商标识。对于本网用户，该参数是为该用户归属的MNO/MVNO运营商标识。 |
| IMSIPRE  | IMSI前缀 | 可选必选说明：可选参数 参数含义：该参数用于指定IMSI前缀。 前提条件: 该参数在“用户范围”参数配置为“IMSI_PREFIX(指定IMSI前缀)”后生效。 数据来源：全网规划 取值范围：0～15位十进制数字字符串。 默认值：无  说明： IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。                                 |

#### 使用实例

1. 查询IMSI前缀为12303的用户的配置策略。

   LST DMCMPTBYIMSI: SUBRANGE=IMSI\_PREFIX, IMSIPRE="12303";

   ```
   %%LST DMCMPTBYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303";%%
   RETCODE = 0  操作成功。

   输出结果如下
   -------------------------
                              用户范围  =  指定IMSI前缀
                            运营商标识  =  NULL
                              IMSI前缀  =  12303
       是否支持UE-SRVCC-Capability信元  =  支持
                              特性列表  =  NULL
                             特性列表2  =  NULL
                           P-GW ID类型  =  MIP-Home-Agent-Host
                 切换后P-GW ID更新策略  =  不更新
                       NOR消息更新参数  =  NULL
                     S6a/S6d-Indicator  =  融合SGSN/MME支持
   Homogeneous Support of IMS VoPS信元  =  按照设备能力携带
                      用户能力匹配模式  =  快速匹配
              不允许IMS VoPS的用户处理  =  携带NOT SUPPORT
    T-ADS查询结果与IMS PDN连接状态相关  =  否
                     是否支持NBIoT RAT  =  不支持
                    支持上报的状态列表  =  NULL
                        T6接口特性列表  =  NULL
                未签约DCNR是否允许DCNR  =  否
           是否支持NOR消息上报RAT TYPE  =  不支持
           是否支持LTE-M类型的RAT TYPE  =  NULL
               EPS FB后P-GW ID更新策略  =  不更新
        是否支持UE-DCNR-Capability信元  =  不支持
           是否支持AMF Instance ID信元  =  不支持
   (结果个数 = 1)

   ---    END
   ```
2. 查询所有配置策略

   LST DMCMPTBYIMSI:;

   ```
   %%LST DMCMPTBYIMSI:;%%
   RETCODE = 0  操作成功。

   输出结果如下
   -------------------------
   用户范围      运营商标识  IMSI前缀  是否支持UE-SRVCC-Capability信元  特性列表  特性列表2  P-GW ID类型                切换后P-GW ID更新策略  NOR消息更新参数  S6a/S6d-Indicator  Homogeneous Support of IMS VoPS信元  用户能力匹配模式  不允许IMS VoPS的用户处理  T-ADS查询结果与IMS PDN连接状态相关  是否支持NBIoT RAT   支持上报的状态列表  T6接口特性列表  未签约DCNR是否允许DCNR  是否支持NOR消息上报RAT TYPE  是否支持LTE-M类型的RAT TYPE  EPS FB后P-GW ID更新策略  是否支持UE-DCNR-Capability信元  是否支持AMF Instance ID信元 

   外网用户      0           NULL      支持                             NULL      NULL       MIP-Home-Agent-Host        不更新                 NULL             融合SGSN/MME支持   按照设备能力携带                     快速匹配          携带NOT SUPPORT           否                                  不支持              NULL                NULL            否                      不支持                       NULL                         不更新                   不支持                          不支持
   本网用户      1           NULL      支持                             NULL      NULL       MIP-Home-Agent-Host        不更新                 NULL             融合SGSN/MME支持   按照设备能力携带                     快速匹配          携带NOT SUPPORT           否                                  不支持              NULL                NULL            否                      不支持                       NULL                         不更新                   不支持                          不支持
   指定IMSI前缀  NULL        12303     支持                             NULL      NULL       MIP-Home-Agent-Host        不更新                 NULL             融合SGSN/MME支持   按照设备能力携带                     快速匹配          携带NOT SUPPORT           否                                  不支持              NULL                NULL            否                      不支持                       NULL                         不更新                   不支持                          不支持
   (结果个数 = 3)

   ---    END
   ```

#### 输出结果说明

参见**ADD DMCMPTBYIMSI**的参数说明。