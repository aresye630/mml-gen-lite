# 增加用户和UPF的绑定关系（ADD IMSIBINDUP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于增加用户和UPF的绑定关系，在拨测场景下需要增加用户IMSI和UPF的绑定关系，系统支持添加一个用户和UPF的绑定关系，同时也支持添加连续IMSI号段用户和UPF的绑定关系。

## 注意事项

- 如果REDIRECT属性为DISABLE，则只在会话建立流程有效；如果REDIRECT属性为ENABLE，则在会话建立和切换流程同时有效。

- 使用该命令时，如果用户在SGW-C、PGW-C、I-SMF、N16aSMF、V-SMF、N16SMF形态下想要选中特定UPF，建议将参数PAUPNFINSTNAME和参数IMUPNFINSTNAME配置为同一个UPF。
- 4G UL CL激活场景，通过设置REDIRECT为ENABLE以及RAUXUPINSTNAME信息，绑定辅锚点UPF。

- 最多可输入100条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称              | 参数说明                                                                                                                                                                                                                                                      |
|:----------------|:------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI            | 起始IMSI            | 可选必选说明：必选参数  参数含义：该参数用于指定IMSI号段的起始IMSI，当只有一个IMSI时，起始IMSI和末位IMSI相同。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~15。IMSI参数每一位只能是数字0-9；当IMSI长度不足15位时，会自动低位补0直到15位。  默认值：无  配置原则：无                                                                                        |
| ENDIMSI         | 终止IMSI            | 可选必选说明：可选参数  参数含义：该参数用于标识IMSI号段的最后一个IMSI，包含在号段内。当只有一个IMSI时，起始IMSI和末位IMSI相同。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~15。ENDIMSI参数每一位只能是数字0-9；当ENDIMSI长度不足15位时，会自动低位补9直到15位。  默认值：无  配置原则：无                                                                         |
| ACCESSTYPE      | 接入类型              | 可选必选说明：必选参数  参数含义：该参数用于指定用户的接入类型。  数据来源：本端规划 取值范围： GUL（2/3/4G接入）NG（5G接入）  默认值：无  配置原则：无                                                                                                                                                                   |
| PAUPNFINSTNAME  | 主锚点UPF实例名称        | 可选必选说明：可选参数  参数含义：该参数用于指定主锚点UPF实例名称。 主锚点UPF为用户接入数据网络使用到的中心UPF锚点。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则：无                                                                                                                               |
| AUXUPNFINSTNAME | 辅锚点UPF实例名称        | 可选必选说明：可选参数  参数含义：该参数用于指定辅锚点UPF实例名称。 辅锚点UPF为用户接入数据网络使用到的边缘UPF锚点。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则：无                                                                                                                               |
| IMUPNFINSTNAME  | N3/S1-U口UPF实例名称   | 可选必选说明：可选参数  参数含义：该参数用于指定N3/S1-U口UPF实例名称。 N3/S1U口UPF是用户与锚点UPF之间的IUPF。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则：  若通过IMSIBINDUP选择插入I-UPF，请针对该I-UPF增加服务区域信息（ADD PNFSMFSERAREA），服务区域需要绑定到TAI或LAI。                                            |
| ULCLDEPLOYMODE  | ULCL部署模式          | 可选必选说明：该参数在"ACCESSTYPE"配置为"NG"时为条件可选参数。  参数含义：该参数用于表示ULCL部署模式。  数据来源：本端规划  取值范围：当ACCESSTYPE为GUL时，自动修改此值为PSASHUNTMUST。 “AUXSHUNTPREFER（优先使用辅锚点分流）”：优先辅锚点分流。如果没有与辅锚点合设的ULCL，则使用分离的ULCL。“PSASHUNTMUST（只使用主锚点分流）”：只使用主锚点分流。  默认值：AUXSHUNTPREFER  配置原则：无       |
| REDIRECT        | 重选到绑定UPF          | 可选必选说明：可选参数  参数含义：该参数用于表示是否允许用户在UP重选的场景下，选择IMSI绑定的UPF。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：DISABLE  配置原则：无                                                                                                                                          |
| RAUXUPINSTNAME  | 重选指向的辅锚点UPF实例名称   | 可选必选说明：该参数在"REDIRECT"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于重选指向的辅锚点UPF实例名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则：无                                                                                                                          |
| RIMUPINSTNAME   | 重选指向的接入UPF实例名称    | 可选必选说明：该参数在"REDIRECT"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于重选指向的接入UPF实例名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则：无                                                                                                                           |
| RULCLDEPLOYMODE | 重选后的ULCL部署模式      | 可选必选说明：该参数在"REDIRECT"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于表示重选后的ULCL部署模式。  数据来源：本端规划  取值范围：当ACCESSTYPE为GUL时，自动修改此值为PSASHUNTMUST。 “AUXSHUNTPREFER（优先使用辅锚点分流）”：优先辅锚点分流。如果没有与辅锚点合设的ULCL，则使用分离的ULCL。“PSASHUNTMUST（只使用主锚点分流）”：只使用主锚点分流。  默认值：AUXSHUNTPREFER  配置原则：无 |
| MDNUPNFINSTNAME | 智能分流专用会话锚点UPF实例名称 | 可选必选说明：该参数在"ACCESSTYPE"配置为"NG"时为条件可选参数。  参数含义：该参数用于指定智能分流专用会话的锚点UPF。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。不区分大小写。  默认值：无  配置原则：无                                                                                                                           |

## 使用实例

- 增加IMSI前缀为“111111”的用户在5G的UP绑定关系：N11形态下激活时主锚点为UP1，N3锚点为UP1；N16a形态下激活时主锚点为UP1；I-SMF形态下激活时N3锚点为UP1：

  ```
  ADD IMSIBINDUP: IMSI="111111", ACCESSTYPE=NG, PAUPNFINSTNAME="UP1", IMUPNFINSTNAME="UP1";
  ```
- 增加IMSI前缀为“111111”的用户在234G的UP绑定关系：SPGWC形态下激活时主锚点为UP1，N3锚点为UP2；PGWC形态下激活时主锚点为UP1；SGW形态下激活时N3锚点为UP2：

  ```
  ADD IMSIBINDUP: IMSI="111111", ACCESSTYPE=GUL, PAUPNFINSTNAME="UP1", IMUPNFINSTNAME="UP2";
  ```
- 增加IMSI前缀为“111111”的用户在5G的UP绑定关系：N11形态下激活时主锚点为UP1，辅锚点为UP2，N3锚点为UP2；N16a形态下激活时主锚点为UP1；I-SMF形态下激活时辅锚点为UP2，N3锚点为UP2；ULCL部署模式为优先使用辅锚点分流：

  ```
  ADD IMSIBINDUP: IMSI="111111", ACCESSTYPE=NG, PAUPNFINSTNAME="UP1",  AUXUPNFINSTNAME="UP2", IMUPNFINSTNAME="UP2", ULCLDEPLOYMODE=AUXSHUNTPREFER;
  ```
- 增加IMSI前缀为“111111”的用户在5G的UP绑定关系：N11形态下激活时主锚点为UP1，辅锚点为UP1，N3锚点为UP1；N16a形态下激活时主锚点为UP1；I-SMF形态下激活时辅锚点为UP1，N3锚点为UP1；ULCL部署模式为只使用主锚点分流：

  ```
  ADD IMSIBINDUP: IMSI="111111", ACCESSTYPE=NG, PAUPNFINSTNAME="UP1",  AUXUPNFINSTNAME="UP1", IMUPNFINSTNAME="UP1", ULCLDEPLOYMODE=PSASHUNTMUST;
  ```
- 增加IMSI前缀为“111111”的用户在5G的UP绑定关系：N11形态下激活时主锚点为UP1，N3锚点为UP1；触发切换UP重选后插入辅锚点UP2，N3锚点为UP2；重选后的ULCL部署模式为优先使用辅锚点分流：

  ```
  ADD IMSIBINDUP: IMSI="111111", ACCESSTYPE=NG, PAUPNFINSTNAME="UP1", IMUPNFINSTNAME="UP1", REDIRECT= ENABLE, RAUXUPINSTNAME = "UP2", RIMUPINSTNAME="UP2", RULCLDEPLOYMODE=AUXSHUNTPREFER;
  ```
- 增加IMSI前缀为“111111”的用户在5G的UP绑定关系：N11形态下激活时主锚点为UP1，辅锚点为UP2，N3锚点为UP3；ULCL部署模式为优先使用辅锚点分流；触发切换UP重选后辅锚点为UP4，N3锚点为UP5；重选后的ULCL部署模式为只使用主锚点分流：

  ```
  ADD IMSIBINDUP: IMSI="111111", ACCESSTYPE=NG, PAUPNFINSTNAME="UP1",  AUXUPNFINSTNAME="UP2", IMUPNFINSTNAME="UP3", ULCLDEPLOYMODE=AUXSHUNTPREFER, REDIRECT= ENABLE, RAUXUPINSTNAME = "UP4", RIMUPINSTNAME="UP5", RULCLDEPLOYMODE=PSASHUNTMUST;
  ```
- 增加用户识别码号段前缀为“111111”到“111119”在5G的UP绑定关系：智能分流专用会话锚点UPF绑定UP3：

  ```
  ADD IMSIBINDUP: IMSI="111111", ENDIMSI="111119",ACCESSTYPE=NG, MDNUPNFINSTNAME="UP3";
  ```