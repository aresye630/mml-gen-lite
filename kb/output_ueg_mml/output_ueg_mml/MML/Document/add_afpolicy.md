# 增加防欺诈策略配置（ADD AFPOLICY）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于增加判断出欺诈行为后的处理策略。如果AFPolicy没有配置参数，无法匹配选择到欺诈策略，则欺诈业务流会使用正常配置的处理策略，不会做策略切换。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为3。
- 由于AFPolicy不参与静态配置中serviceProp的选择和阻塞处理，不建议配置绑定了serviceProp的PCCPOLICYGRP作为DNS防欺诈策略。
- 如果PCCPOLICYGRPNM参数对应的URRGROUP配置仅绑定FUP类型的URR，则欺诈场景下计费会按照Common Policy和SpecTrafURRGrp的顺序选择OFFLINE/ONLINE类型的URR。
- 如果PCCPOLICYGRPNM参数对应的URRGROUP配置仅绑定计费类型的URR，则欺诈场景下FUP会按照Common Policy和SpecTrafURRGrp的顺序选择Monitoring-Key类型的URR。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称     | 参数说明                                                                                                                                               |
|:---------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| AFPOLICYTYPE   | 防欺诈策略类型  | 可选必选说明：必选参数 参数含义：该参数用于指定防欺诈策略类型。 数据来源：本端规划 取值范围：枚举类型。 DNS：指定DNS防欺诈。HTTP：指定HTTP防欺诈。HTTPS：指定HTTPS防欺诈。 默认值：无 配置原则：无                                   |
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：可选参数 参数含义：该参数用于指定PCC策略组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD PCCPOLICYGRP命令配置生成。                           |
| AFAPPID        | 防欺诈应用标识  | 可选必选说明：可选参数 参数含义：该参数用于指定上报给PCRF的AFAPPID名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。不区分大小写。 默认值：无 配置原则： 若ADD PCCPOLICYGRP命令中的ADCMUTEFLAG参数为DISABLE时，本参数有效。 |
| CATEPROPNAME   | 分类属性名称   | 可选必选说明：可选参数 参数含义：该参数用于指定分类属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD CATEGORYPROP命令配置生成。                             |

#### 使用实例

- 如果运营商需要增加判断出DNS欺诈行为后的PCC处理策略和带宽处理策略，则配置命令如下：

  ```
  ADD AFPOLICY:AFPOLICYTYPE=DNS,PCCPOLICYGRPNM="pccpolicygroup",CATEPROPNAME="cateprop";
  ```
- 如果运营商需要增加判断出DNS欺诈行为后的PCC处理策略，并且进行ADC上报，则配置命令如下：

  ```
  ADD AFPOLICY:AFPOLICYTYPE=DNS,PCCPOLICYGRPNM="pccpolicygroup",AFAPPID="applicationidname";
  ```