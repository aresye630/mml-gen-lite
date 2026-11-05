# 增加APN下用户和UPF的绑定关系配置（ADD IMSIAPNBINDUP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于增加APN下用户和UPF的绑定关系，在拨测场景下需要增加APN下用户IMSI和UPF的绑定关系，同一个APN下系统支持添加一个用户和UPF的绑定关系，同时也支持添加连续IMSI号段用户和UPF的绑定关系。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 本配置会优先于ADD IMSIBINDUP生效。
- 使用该命令时，如果用户在SGW-C、PGW-C、I-SMF、N16aSMF、V-SMF、N16SMF形态下想要选中特定UPF，建议将参数PAUPNFINSTNAME和参数IMUPNFINSTNAME配置为同一个UPF。
- 2G/3G/4G场景不支持绑定辅锚点。
- 不支持智能分流专用会话。

- 最多可输入500条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                  |
|:----------------|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI            | 起始IMSI          | 可选必选说明：必选参数  参数含义：该参数用于指定IMSI号段的起始IMSI，当ENDIMSI没有值时，起始IMSI和终止IMSI相同。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是14~15。该参数每一位只能是数字0-9。  默认值：无  配置原则：无                                                                                                                                                               |
| ENDIMSI         | 终止IMSI          | 可选必选说明：可选参数  参数含义：该参数用于标识IMSI号段的最后一个IMSI，包含在号段内。当ENDIMSI没有值时，起始IMSI和终止IMSI相同。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是14~15。该参数每一位只能是数字0-9。  默认值：无  配置原则：无                                                                                                                                                      |
| ACCESSTYPE      | 接入类型            | 可选必选说明：必选参数  参数含义：该参数用于指定用户的接入类型。  数据来源：本端规划 取值范围： GUL（2/3/4G接入）NG（5G接入）  默认值：无  配置原则：无                                                                                                                                                                                                               |
| APN             | APN名称           | 可选必选说明：必选参数  参数含义：该参数用于指定APN实例名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。  默认值：无  配置原则：  输入APN需要在ADD CPAPN命令中配置。  输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”。 |
| PAUPNFINSTNAME  | 主锚点UPF实例名称      | 可选必选说明：可选参数  参数含义：该参数用于指定主锚点UPF实例名称。主锚点UPF为用户接入数据网络使用到的中心UPF锚点。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：  主锚点UPF实例名称可通过LST PNFPROFILE查询。                                                                                                                                                    |
| IMUPNFINSTNAME  | N3/S1-U口UPF实例名称 | 可选必选说明：可选参数  参数含义：该参数用于指定N3/S1-U口UPF实例名称。N3/S1-U口UPF是用户与锚点UPF之间的I-UPF。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：  若通过IMSIAPNBINDUP选择插入I-UPF，请针对该I-UPF增加服务区域信息（ADD PNFSMFSERAREA），服务区域需要绑定到TAI或LAI。                                                                                           |
| AUXUPNFINSTNAME | 辅锚点UPF实例名称      | 可选必选说明：可选参数  参数含义：该参数用于指定辅锚点UPF实例名称。辅锚点UPF为用户接入数据网络使用到的边缘UPF锚点。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：  辅锚点UPF实例名称可通过LST PNFPROFILE查询。                                                                                                                                                    |
| ULCLDEPLOYMODE  | UL CL部署模式       | 可选必选说明：该参数在"ACCESSTYPE"配置为"NG"时为条件可选参数。  参数含义：该参数用于表示UL CL部署模式。  数据来源：本端规划 取值范围： “AUXSHUNTPREFER（优先使用辅锚点分流）”：优先辅锚点分流。如果没有与辅锚点合设的ULCL，则使用分离的ULCL。“PSASHUNTMUST（只使用主锚点分流）”：只使用主锚点分流。  默认值：AUXSHUNTPREFER  配置原则：无                                                                                        |

## 使用实例

- 增加IMSI为“11111111111111”，APN为“huawei.com”的用户在5G的UP绑定关系：N11形态下激活时主锚点为UP1，N3锚点为UP1；N16a形态下激活时主锚点为UP1；I-SMF形态下激活时N3锚点为UP1：

  ```
  ADD IMSIAPNBINDUP: IMSI="11111111111111", ACCESSTYPE=NG, APN="huawei.com", PAUPNFINSTNAME="UP1", IMUPNFINSTNAME="UP1";
  ```
- 增加IMSI为“11111111111111”，APN为“huawei.com”的用户在234G的UP绑定关系：SPGWC形态下激活时主锚点为UP1，N3锚点为UP2；PGW-C形态下激活时主锚点为UP1；SGW形态下激活时N3锚点为UP2：

  ```
  ADD IMSIAPNBINDUP: IMSI="11111111111111", ACCESSTYPE=GUL, APN="huawei.com", PAUPNFINSTNAME="UP1", IMUPNFINSTNAME="UP2";
  ```
- 增加IMSI为“11111111111111”，APN为“huawei.com”的用户在5G的UP绑定关系：N11形态下激活时主锚点为UP1，辅锚点为UP2，N3锚点为UP2；N16a形态下激活时主锚点为UP1；I-SMF形态下激活时辅锚点为UP2，N3锚点为UP2；UL CL部署模式为优先使用辅锚点分流：

  ```
  ADD IMSIAPNBINDUP: IMSI="11111111111111", ACCESSTYPE=NG, APN="huawei.com", PAUPNFINSTNAME="UP1",  AUXUPNFINSTNAME="UP2", IMUPNFINSTNAME="UP2", ULCLDEPLOYMODE=AUXSHUNTPREFER;
  ```
- 增加IMSI为“11111111111111”，APN为“huawei1.com”的用户在5G的UP绑定关系：N11形态下激活时主锚点为UP1，辅锚点为UP1，N3锚点为UP1；N16a形态下激活时主锚点为UP1；I-SMF形态下激活时辅锚点为UP1，N3锚点为UP1；UL CL部署模式为只使用主锚点分流：

  ```
  ADD IMSIAPNBINDUP: IMSI="11111111111111", ACCESSTYPE=NG, APN="huawei1.com", PAUPNFINSTNAME="UP1",  AUXUPNFINSTNAME="UP1", IMUPNFINSTNAME="UP1", ULCLDEPLOYMODE=PSASHUNTMUST;
  ```