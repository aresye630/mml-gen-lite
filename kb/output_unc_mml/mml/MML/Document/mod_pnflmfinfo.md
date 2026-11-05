# 修改对端LMF信息（MOD PNFLMFINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、CBC、CBCF**

该命令用于修改本地配置的对端LMF的信息。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:-------------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSTANCEID | NF实例标识  | 可选必选说明：必选参数  参数含义：该参数用于指定NF实例标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~64。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）建议为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度建议不超过18且不输入只包含0-9和“.”的字符串，例如：1.2.3.4、不建议输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。  默认值：无  配置原则：无                                                                                                                                                      |
| LMFID        | LMF标识   | 可选必选说明：可选参数  参数含义：该参数用于标识该LMF的LMFINFO信息。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。该参数大小写不敏感。  默认值：无  配置原则： 本参数的构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"组成的字符串。 一个LMF仅能配置一个LMFID。 一个LMFID仅能配置一个LMF。                                                                                                                                                                                                                                                                                            |
| CLIENTTYPES  | 外部客户端类型 | 可选必选说明：可选参数  参数含义：此参数用于表示该LMF用于服务的外部客户端类型。此参数为空并且通过ADD PNFWILDCARD命令打开了CLIENTTYPE通配开关意味着LMF可以用于所有客户端类型。  数据来源：本端规划 取值范围： EMERGENCY_SERVICES（紧急服务的外部客户端）VALUE_ADDED_SERVICES（增值业务外部客户端）PLMN_OPERATOR_SERVICES（PLMN运营商业务外部客户端）LAWFUL_INTERCEPT_SERVICES（合法拦截服务的外部客户端）PLMN_OPERATOR_BROADCAST_SERVICES（PLMN运营商广播业务外部客户端）PLMN_OPERATOR_OM（PLMN运营商运维外部客户端）PLMN_OPERATOR_ANONYMOUS_STATISTI（PLMN操作员匿名统计外部客户端）PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT（PLMN运营商目标MS服务支持的外部客户端）  默认值：无  配置原则：无 |

## 使用实例

修改对端LMF信息，NF实例标识为LMF\_Instance\_0，外部客户端类型为EMERGENCY\_SERVICES。

```
MOD PNFLMFINFO: NFINSTANCEID="LMF_Instance_0", LMFID="0001", CLIENTTYPES=EMERGENCY_SERVICES-1&VALUE_ADDED_SERVICES-0&PLMN_OPERATOR_SERVICES-0&LAWFUL_INTERCEPT_SERVICES-0&PLMN_OPERATOR_BROADCAST_SERVICES-0&PLMN_OPERATOR_OM-0&PLMN_OPERATOR_ANONYMOUS_STATISTI-0&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT-0;
```