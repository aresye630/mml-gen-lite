# 增加S-GW DNS域名策略（ADD SGWDNS）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

该命令用于在多PLMN共享跟踪区域或者位置区域场景时，定制S-GW域名中的PLMN组装策略，从而可以简化**ADD DNSN**的配置信息。

在E-UTRAN网络查询S-GW时使用的是TAI FQDN，在UTRAN网络查询S-GW时使用的是RAI FQDN。被多个PLMN共享的一组跟踪区域或者位置区域其对应的S-GW一般都是一样的，为了S-GW查询，则需要针对每一个PLMN配置一条DNSN记录。为了减少DNSN配置，UNC系统提供该命令，指定一个特定的PLMN代替所有的PLMN来组装FQDN，进行S-GW查询。

场景举例：

以E-UTRAN网络为例，如果RAN侧的跟踪区域码为0x1234，分别被五个PLMN共享，PLMN1（111222）、PLMN2（111333）、PLMN3（111444）、PLMN4（111555）和PLMN（111666）。 该跟踪区对应如下S-GW：

```
ADD IPV4DNSH: HSINDEX=1, HOSTNAME="TOPON.S11.SGW1.PUDONG.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.10.10";
```

- 当无此配置时，则需要配置如下五条查询DNSN记录，才可以满足在该跟踪区下选择不同PLMN的用户正常附着：

  ```
  ADD IPV4DNSH: HSINDEX=1, HOSTNAME="TOPON.S11.SGW1.PUDONG.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1="10.10.10.10";
  ```

  ```
  ADD DNSN: FQDN="TAC-LB34.TAC-HB12.TAC.EPC.MNC222.MCC111.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
  ```

  ```
  ADD DNSN: FQDN="TAC-LB34.TAC-HB12.TAC.EPC.MNC333.MCC111.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
  ```

  ```
  ADD DNSN: FQDN="TAC-LB34.TAC-HB12.TAC.EPC.MNC444.MCC111.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
  ```

  ```
  ADD DNSN: FQDN="TAC-LB34.TAC-HB12.TAC.EPC.MNC555.MCC111.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
  ```

  ```
  ADD DNSN: FQDN="TAC-LB34.TAC-HB12.TAC.EPC.MNC666.MCC111.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
  ```
- 当有如下配置（指定TAC 0x1234在组装FQDN选择S-GW时使用特定的PLMN：555666，该PLMN可以为任意PLMN）存在时：

  ```
  ADD SGWDNS: DNTYPE=TAI, TAC="0x1234", TACRANGE="0x1234", MCC="555", MNC="666";
  ```

  则只需要配置如下一条DNSN来代替上面五条：

  ```
  ADD DNSN: FQDN="TAC-LB34.TAC-HB12.TAC.EPC.MNC666.MCC555.3GPPNETWORK.ORG", HSINDEX=1, ENTITY=SGW, INTYPE=S11;
  ```

#### 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为1024。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识     | 参数名称    | 参数说明                                                                                                                                                                                                                                |
|:---------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DNTYPE   | 域名类型    | 可选必选说明：必选参数 参数含义：该参数用于指定DNS域名类型。 数据来源：整网规划 取值范围： “RAI(RAI)”“TAI(TAI)” 默认值：无                                                                                                                                                         |
| LAC      | 位置区域码   | 可选必选说明：条件必选参数 参数含义：该参数用于指定位置区域码。 前提条件：该参数在“DNTYPE(域名类型)”设置为“RAI(RAI)”时生效。 数据来源：整网规划 取值范围：0x0000～0xFFFF 默认值：无                                                                                                                        |
| RAC      | 路由区域码   | 可选必选说明：条件必选参数 参数含义：该参数用于指定路由区域码。 前提条件：该参数在“DNTYPE(域名类型)”设置为“RAI(RAI)”时生效。 数据来源：整网规划 取值范围：0x00～0xFF 默认值：无                                                                                                                            |
| RACRANGE | 路由区域码范围 | 可选必选说明：可选参数 参数含义：该参数用于指定路由区域码范围。 前提条件：该参数在“DNTYPE(域名类型)”设置为“RAI(RAI)”时生效。 数据来源：整网规划 取值范围：0x00～0xFF 默认值：无 配置原则：该参数的取值需要大于或等于“RAC”。  说明： 该参数与“RAC”参数构成一个RAC区段，方便客户配置连续的路由区域。如果不输入，表示配置单个RAC。相同“DNTYPE（域名类型）”和“LAC（位置区域码）”的RAC范围不允许交叉。 |
| TAC      | 跟踪区域码   | 可选必选说明：条件必选参数 参数含义：该参数用于指定跟踪区域码。 前提条件：该参数在“DNTYPE(域名类型)”设置为“TAI(TAI)”时生效。 数据来源：整网规划 取值范围：0x0000～0xFFFF 默认值 ：无                                                                                                                       |
| TACRANGE | 跟踪区域码范围 | 可选必选说明：可选参数 参数含义：该参数用于指定跟踪区域码范围。 前提条件：该参数在“DNTYPE(域名类型)”设置为“TAI(TAI)”时生效。 数据来源：整网规划 取值范围：0x0000～0xFFFF 默认值：无  说明： 该参数与“TAC”参数构成一个TAC区段，方便客户配置连续的跟踪区域。如果不输入，表示配置单个TAC。相同域名类型配置的TAC区段的范围不允许交叉。                                        |
| MCC      | 移动国家码   | 可选必选说明：必选参数 参数含义：该参数用于指定PLMN或HPLMN的移动国家号码。 数据来源：整网规划 取值范围：3位十进制数 默认值：无                                                                                                                                                              |
| MNC      | 移动网号    | 可选必选说明：必选参数 参数含义：该参数用于指定PLMN或HPLMN的移动网号码。 数据来源：整网规划 取值范围：2位或3位的十进制数 默认值：无                                                                                                                                                           |
| DESC     | 描述      | 可选必选说明：可选参数 参数含义：该参数用于增加配置命令的描述信息。 数据来源：整网规划 取值范围：0~32位字符串 默认值：无                                                                                                                                                                    |

#### 使用实例

增加一条S-GW DNS域名策略记录，跟踪区域码为“1”，跟踪区域码范围为“9”，移动国家代码为“123”，移动网号为“120”。

ADD SGWDNS: DNTYPE=TAI, TAC="1", TACRANGE="9", MCC="123", MNC="120";