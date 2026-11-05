# 查询DNS NAPTR记录(LST DNSN)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询“FQDN”（全称标准规范域名）与网元接口的对应关系。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug；visit-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组；G\_4，来宾级别命令组

#### 参数说明

| 参数标识          | 参数名称            | 参数说明                                                                                                                                                                                                                                                                  |
|:--------------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FQDN          | FQDN            | 可选必选说明：可选参数 参数含义：该参数用于标识由RAI、TAI、APN、MME等构建的域名，用来进行网元查询。详见命令ADD DNSN。 数据来源：整网规划 取值范围：0~255位字符串 默认值：无  说明： FQDN不能以“.”开始，也不能以“.”结束。                                                                                                                                     |
| HSINDEX       | 主机名索引           | 可选必选说明：可选参数 参数含义：该参数用于指定FQDN对应网元的索引。 数据来源：整网规划 取值范围：1~2048 默认值：无                                                                                                                                                                                                      |
| ENTITY        | 网元类型            | 可选必选说明：可选参数 参数含义：该参数用于指定接口网元的类型。 数据来源：整网规划 取值范围：“Gn(Gn)”“SGSN(SGSN)”“GGSN(GGSN)”“MME(MME)”“SGW(SGW)”“PGW(PGW)”“MSC(MSC)”“IWS(IWS)”“AMF(AMF)” 默认值：无                                                                                                                    |
| INTYPE        | 接口类型            | 可选必选说明：可选参数 参数含义：该参数用来指定接口对应的类型。 数据来源：整网规划 取值范围：“Gn(Gn)”“Gp(Gp)”“S3(S3)”“S4(S4)”“S5(S5)”“S8(S8)”“S10(S10)”“S11(S11)”“S16(S16)”“Sv(Sv)”“S102(S102)”“Sdup(Sdup)”“Sdup(Sdup)”“N26(N26)” 默认值：无  说明： 当该配置数据用于链式备份网元寻址时，需要选Sdup枚举，Sdup接口华为私有接口，是MME和MME之间的接口，用于实现MME间的数据备份。 |
| UEUSGTYPEPLCY | UE USAGE TYPE策略 | 可选必选说明：可选参数 参数含义：该参数用来指定是否携带UE USAGE TYPE。 数据来源：全网规划 取值范围：“NO（否）”“YES（是）” 默认值：无                                                                                                                                                                                       |
| DCNR          | 支持DCNR          | 可选必选说明：可选参数 参数含义：该参数用于控制是否支持DCNR接入。 数据来源：全网规划 取值范围：“NO(否)”“YES(是)” 默认值：无                                                                                                                                                                                              |
| SMF           | 融合PGW-C/SMF     | 可选必选说明：可选参数 参数含义：该参数用于控制是否支持融合的PGW-C/SMF。 数据来源：整网规划 取值范围：“NO（否）”“YES（是）” 默认值：无                                                                                                                                                                                        |

#### 使用实例

查询FQDN为“TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG”的记录结果：

LST DNSN: FQDN="TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG";

```
%%LST DNSN: FQDN="TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG";%%
RETCODE = 0  操作成功

操作结果如下
--------------
 FQDN                                                      主机名索引  网元类型  接口类型  S5接口协议类型  S8接口协议类型  UE USAGE TYPE策略  UE USAGE TYPE群组标识  支持DCNR  融合PGW-C/SMF  优先级  权重    描述  

 TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG   1           SGW       S11       GTP             GTP             是                 1                      否        否             0       100     To huawei SGW01  
 TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG   2           SGW       S11       GTP             GTP             是                 1                      否        否             0       100     To huawei SGW01  
 TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG   3           SGW       S11       GTP             GTP             是                 1                      否        否             0       100     To huawei SGW01  
(结果个数 = 3)

---    END
```

#### 输出结果说明

参考**ADD DNSN**命令的参数标识。