# 删除APN配置（RMV CPAPN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

执行不当会导致系统异常。

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用来删除指定的APN实例。

## 注意事项

- 该命令执行后立即生效。

- APN实例下有用户存在时不允许删除该APN实例。执行该命令将失败。仅在该APN下无用户时，删除操作才能成功。
- 将APN上激活用户数降至0的方法有两个，可以通过LCK CPAPN修改APN的Locked参数为ENABLE，使新用户无法接入该APN，随着已激活用户逐渐去激活，该APN上的激活用户数也将逐渐减至0；也可以通过将Locked参数和LockDeactive参数置为ENABLE直接去激活该APN所有的用户，但这样将会中断已经激活的用户业务，请谨慎使用此方法。
- 执行RMV CPAPN时会同步删除的配置清单：UEDNSBINDAPN，APNAUTHATTR，APNRADIUSATTR，APNACCESSCTRL，APNADDRESSATTR，APNMBRFUNC(APNPCRFEMEREATTACH)，APNIDLETIME，DftGBRBearer，ApnPccFunc，APNCharge，ApnRdsAcctCtrl，APNRdsSvrGrp，APNL2TPCTRL，ApnQosAttr，APNREPORTATTR，APNIMSATTR，BACKOFFTIME，SgwApnChgMeth，APNPCSCFSRVPRI，SPECIFICAPNVAL，RadiusNasIp，ApnRdsClientIp，APNACCESSWAL，ApnUsrProfG，PcrfGrpBndApn，RealmBindAPN，APNALIAS，APNNONIPFUNC，APNProfSpace，POOLBINDAPN，APNPLMNRATECTRL，APNRATECTRL，PERFREGAPN，SMFAPNSOFTPARA，APNIPV6INFID，APNDHCPATTR，APNIPALLOCRULE，APNDIAMAAAGRP，APNUPSELPLY，APNPTTFUNC，LOCUPDQOS，APNCHRFUNC，APNPGWCHGPAUSE，APNREVERSESHUNT，APNTRAFFICDIST，APNAMBRCTRL，GBRBWCTRL，ROAMCHGMODE，APNGA5GREUSEAVP，APNGY5GREUSEAVP，L2RULEGRPBIND，APNUPRECOVER，APNTOHCTRL。
- 如果APN已经绑定在SMFAPNDLBUFTIME，APNEDRXATTR，APNQOSBYPASS，PCSCFGRPBNDAPN，APNGWPROXYFUNC，APNINTELSHUNT，APNMULTIDNNCTRL，VIRTUALAPNRULE，POOLGRPMAP，M2MSVRGRPBIND或IMSIAPNBINDUP中，则不允许删除，需要执行命令RMV SMFAPNDLBUFTIME，RMV APNEDRXATTR，RMV APNQOSBYPASS，RMV PCSCFGRPBNDAPN，RMV APNGWPROXYFUNC，RMV APNINTELSHUNT，RMV APNMULTIDNNCTRL，RMV VIRTUALAPNRULE，RMV CPPOOLGRPMAP，RMV M2MSVRGRPBIND或RMV IMSIAPNBINDUP解除绑定关系后再删除。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                         |
|:-------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN    | APN名称  | 可选必选说明：必选参数  参数含义：该参数用于指定APN实例名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。  默认值：无  配置原则：  输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”。 |

## 使用实例

假设运营商需要删除指定的APN实例，“APN”为“huawei.com”：

```
RMV CPAPN:APN="huawei.com";
```