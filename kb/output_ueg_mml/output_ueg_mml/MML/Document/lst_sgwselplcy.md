# 查询S-GW选择策略(LST SGWSELPLCY)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询S-GW选择策略。

#### 注意事项

- 无

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称           | 参数说明                                                                                                                                                                                                                                                                            |
|:----------|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE  | 用户范围           | 可选必选说明：可选参数 参数含义：该参数用于指定用户范围。 数据来源：整网规划 取值范围：“IMSI_PREFIX(指定IMSI前缀)”“MSISDN_PREFIX(指定MSISDN前缀)”“SPECIFIC_IMSI(特定IMSI)”“SPECIFIC_MSISDN(特定MSISDN)” 默认值：无                                                                                                                         |
| IMSIPRE   | IMSI前缀         | 可选必选说明：条件可选参数 参数含义：该参数用于指定IMSI前缀。 前提条件：只有“SUBRANGE（用户范围）”为“IMSI_PREFIX（指定IMSI前缀）”时，该参数才有效。 数据来源：整网规划 取值范围：1～15位十进制数字字符串 默认值：无                                                                                                                                                   |
| MSISDNPRE | MSISDN前缀       | 可选必选说明：条件可选参数 参数含义：该参数用于指定MSISDN前缀。 前提条件：只有“SUBRANGE（用户范围）”为“MSISDN_PREFIX(指定MSISDN前缀)”时，该参数才有效。 数据来源：整网规划 取值范围：1～15位十进制数字字符串 默认值：无                                                                                                                                             |
| IMSI      | IMSI           | 可选必选说明：条件可选参数 参数说明：该参数用于指定国际移动用户标识。 前提条件：此参数在“用户范围”设置为“SPECIFIC_IMSI(特定IMSI)”后生效。 取值范围：15位十进制数字字符串 默认值：无                                                                                                                                                                        |
| MSISDN    | MSISDN         | 可选必选说明：条件可选参数 参数说明：该参数用于指定移动台国际ISDN号码。 前提条件：此参数在“用户范围”设置为“SPECIFIC_MSISDN (特定MSISDN)”后生效。 取值范围：13位十进制数字字符串 默认值：无                                                                                                                                                                |
| SLCTM     | 选择方法           | 可选必选说明：可选参数 参数含义：该参数用于指定选择方法。 数据来源：整网规划 取值范围：“S-GW_QNAME(指定S-GW的查询域名)”“S-GW_IP (指定S-GW的IP地址)” 默认值：无                                                                                                                                                                             |
| QNAME     | 查询域名           | 可选必选说明：条件可选参数 参数含义：该参数用于指定查询域名。 前提条件：只有“SLCTM（选择方法）”为“S-GW_QNAME(指定S-GW的查询域名)”时，该参数才有效。 数据来源：整网规划 取值范围：1~255位字符串 默认值：无 配置原则：该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，字母不区分大小写。按照协议RFC1035规定，Hostname最大有效字符数为253，并且每个Label最大长度为63个字节。                                            |
| IPV4      | S-GW的信令面IPv4地址 | 可选必选说明：条件可选参数 参数含义：该参数用于指定S-GW的信令面IPv4地址。 前提条件：该参数在“SLCTM（选择方法）”参数设置为“S-GW_IP（指定S-GW IP的地址）”值后生效。 数据来源：整网规划 取值范围：0.0.0.0～255.255.255.255 默认值：无 配置原则：IPV4地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。IPV4地址必须是A、B或者C类地址。                                                      |
| IPV6      | S-GW的信令面IPv6地址 | 可选必选说明：条件可选参数 参数含义：该参数用于指定S-GW的信令面IPv6地址。 前提条件：该参数在“SLCTM（选择方法）”参数设置为“S-GW_IP（指定S-GW IP地址）”值后生效。 数据来源：整网规划 取值范围：::～FFFF：FFFF：FFFF：FFFF：FFFF：FFFF：FFFF：FFFF 默认值：无 配置原则：IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

#### 使用实例

1. 查询所有记录

   LST SGWSELPLCY:;

   ```
   %%LST SGWSELPLCY:;%%
   RETCODE = 0  操作成功。

   输出结果如下
   --------------
    用户范围        IMSI前缀  MSISDN前缀  IMSI  MSISDN  选择方法            查询域名                                                      S-GW的信令面IPv4地址  S-GW的信令面IPv6地址
    指定IMSI前缀    134       NULL        NULL  NULL    指定S-GW的查询域名                       TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
    指定MSISDN前缀  NULL      134         NULL  NULL    指定S-GW的查询域名  TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
   (结果个数 = 2)

   ---    END
   ```
2. 通过“用户范围”为“MSISDN\_PREFIX(指定MSISDN前缀)”查询记录

   LST SGWSELPLCY: SUBRANGE=MSISDN\_PREFIX, MSISDNPRE="134";

   ```
   %%LST SGWSELPLCY: SUBRANGE=MSISDN_PREFIX, MSISDNPRE="134";%%
   RETCODE = 0  操作成功。

   输出结果如下
   --------------
               用户范围  =  指定MSISDN前缀
               IMSI前缀  =  NULL
             MSISDN前缀  =  134
                   IMSI  =  NULL
                 MSISDN  =  NULL 
               选择方法  =  指定S-GW的查询域名
               查询域名  =  TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG
   S-GW的信令面IPv4地址  =  NULL
   S-GW的信令面IPv6地址  =  NULL
   (结果个数 = 1)

   ---    END
   ```
3. 通过“用户范围”为“IMSI\_PREFIX(指定IMSI前缀)”查询记录

   LST SGWSELPLCY: SUBRANGE=IMSI\_PREFIX, IMSIPRE="134";

   ```
   %%LST SGWSELPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="134";%%
   RETCODE = 0  操作成功。

   输出结果如下
   --------------
   用户范围  =  指定MSISDN前缀
               IMSI前缀  =  134
             MSISDN前缀  =  NULL
                   IMSI  =  NULL
                 MSISDN  =  NULL 
               选择方法  =  指定S-GW的查询域名
               查询域名  =  TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG
   S-GW的信令面IPv4地址  =  NULL
   S-GW的信令面IPv6地址  =  NULL
   (结果个数 = 1)

   ---    END
   ```
4. 通过“选择方法”为“S-GW\_QNAME(指定S-GW的查询域名)”查询记录

   LST SGWSELPLCY: SLCTM=S-GW\_QNAME;

   ```
   %%LST SGWSELPLCY: SLCTM=S-GW_QNAME;%%
   RETCODE = 0  操作成功。

   输出结果如下
   --------------
    用户范围        IMSI前缀  MSISDN前缀  IMSI  MSISDN  选择方法            查询域名                                                      S-GW的信令面IPv4地址  S-GW的信令面IPv6地址
    指定IMSI前缀    134       NULL        NULL  NULL    指定S-GW的查询域名                       TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
    指定MSISDN前缀  NULL      134         NULL  NULL    指定S-GW的查询域名  TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
   (结果个数 = 2)

   ---    END
   ```
5. 通过“选择方法”为“S-GW\_QNAME(指定S-GW的查询域名)”，“查询域名”为指定域名方式查询记录

   LST SGWSELPLCY: SLCTM=S-GW\_QNAME, QNAME="TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG";

   ```
   %%LST SGWSELPLCY: SLCTM=S-GW_QNAME, QNAME="TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG";%%
   RETCODE = 0  操作成功。

   输出结果如下
   --------------
    用户范围        IMSI前缀  MSISDN前缀  IMSI  MSISDN  选择方法            查询域名                                                      S-GW的信令面IPv4地址  S-GW的信令面IPv6地址
    指定IMSI前缀    134       NULL        NULL  NULL    指定S-GW的查询域名                       TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
    指定MSISDN前缀  NULL      134         NULL  NULL    指定S-GW的查询域名  TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
   (结果个数 = 2)

   ---    END
   ```

#### 输出结果说明

参见**ADD SGWSELPLCY**的参数说明。