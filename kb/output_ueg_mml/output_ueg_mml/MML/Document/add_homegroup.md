# 增加Home Group（ADD HOMEGROUP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、GGSN**

该命令用于增加一个Home Group，把能够匹配IMSI/MSISDN号码段组中号段或者计费属性组中计费特征值的用户激活请求消息转发到Home GGSN/PGW去处理。

## 注意事项

- 该命令执行后立即生效。

- 配置Home Group后，需要继续对Home IP进行配置，否则该Proxy功能无法生效。
- Home Group配置的各个组之间有优先级的关系。收到激活消息后按照IMSI，MSISDN和计费特征值同整机配置的号段或计费属性组进行匹配，如果匹配到多个Home Group，则选择优先级较高的Home Group。Home Group优先级相同时，根据基于Home Group记录的Proxy用户数，定时对优先级相同的Home Group进行重新排序，时长为1分钟。
- 当MULTIDNNSW参数为DISABLE时，需要保证IMSIMSISDNGRPNUM和CCGROUPNAME两个参数中至少有一个有效。
- 当MULTIDNNSW参数为ENABLE时，IMSIMSISDNGRPNUM和CCGROUPNAME两个参数不生效。

- 最多可输入128条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                 | 参数说明                                                                                                                                     |
|:----------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| HOMEGROUPINDX   | Home Group编号         | 可选必选说明：必选参数  参数含义：该参数用于设置Home Group的编号。  数据来源：本端规划  取值范围：整数类型，取值范围是1~128。  默认值：无  配置原则：无                                                 |
| HOMEGROUPPRI    | Home Group优先级        | 可选必选说明：可选参数  参数含义：该参数用于设置Home Group的优先级。  数据来源：本端规划  取值范围：整数类型，取值范围是1~65535。值越小优先级越高。  默认值：65535  配置原则：无                                 |
| IMSIMSISDNGRPNM | Home Group绑定的用户号码段组名 | 可选必选说明：可选参数  参数含义：该参数用于设置Home Group绑定的IMSI/MSISDN号码段组名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。  默认值：无  配置原则：  该参数使用ADD PRIMSIMSISDNG命令配置生成。 |
| CCGROUPNAME     | 计费特征组名称              | 可选必选说明：可选参数  参数含义：该参数用于设置Home Group绑定的计费特征组名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。  默认值：无  配置原则：  该参数使用ADD CCGROUP命令配置生成。                |
| MULTIDNNSW      | 2B2C漫游双DNN特性功能开关     | 可选必选说明：可选参数  参数含义：该参数用于HOMEGROUP支持2B2C漫游双DNN特性功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无  配置原则：无                                 |

## 使用实例

- 增加“Home Group编号”为“1”，“Home Group优先级”为“65535”，“Home Group绑定的用户号码段组名”为“grp1”，“计费特征组名称”为“c1”，“2B2C漫游双DNN特性功能开关”为“DISABLE”的Home Group配置：

  ```
  ADD HOMEGROUP: HOMEGROUPINDX=1, IMSIMSISDNGRPNM="grp1", CCGROUPNAME="c1", MULTIDNNSW=DISABLE;
  ```
- 增加“Home Group编号”为“2”，“Home Group优先级”为“65535”的Home Group配置：

  ```
  ADD HOMEGROUP: HOMEGROUPINDX=2;
  ```