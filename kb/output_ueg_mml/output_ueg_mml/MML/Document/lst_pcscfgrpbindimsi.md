# 查询P-CSCF组和IMSI/MSISDN号段的绑定关系（LST PCSCFGRPBINDIMSI）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF、GGSN、PGW-C**

该命令用于查询p-cscf组和IMSI/MSISDN号段的绑定关系信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识          | 参数名称            | 参数说明                                                                                                                                                                      |
|:--------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：可选参数  参数含义：该参数用于号段名称。指定某号段绑定到p-cscf组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数使用ADD PCSCFIMSISDNSEG命令配置生成。 |

## 使用实例

- 查询p-cscf组绑定号段记录，没有配置，查询记录为零：

  ```
  LST PCSCFGRPBINDIMSI: IMSIMSISDNSEG="myseg";
  RETCODE = 0  操作成功。

  P-CSCF组绑定IMSI配置信息:
  -------------------------
  IMSI/MSISDN 号段名称  =  myseg
                优先级  =  1
          P-CSCF组类型  =  IPv4
       主IPv4 P-CSCF组  =  mastergrp1
       备IPv4 P-CSCF组  =  slavegrp1
       主IPv6 P-CSCF组  =  NULL
       备IPv6 P-CSCF组  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询整机p-cscf组绑定号段记录，没有配置，查询记录为零：

  ```
  LST PCSCFGRPBINDIMSI:;
  RETCODE = 0  操作成功。

  P-CSCF组绑定IMSI配置信息:
  -------------------------
  IMSI/MSISDN 号段名称    优先级    P-CSCF组类型    主IPv4 P-CSCF组    备IPv4 P-CSCF组    主IPv6 P-CSCF组    备IPv6 P-CSCF组

  myseg                   1         IPv4            mastergrp1         slavegrp1          NULL               NULL           
  seg                     2         IPv4            mygroup            NULL               NULL               NULL           
  (结果个数 = 2)
  ---    END
  ```

## 输出结果说明

| 输出项名称           | 输出项解释                                              |
|:----------------|:---------------------------------------------------|
| IMSI/MSISDN号段名称 | 该参数用于号段名称。指定某号段绑定到p-cscf组。                         |
| 优先级             | 该参数用于表示该配置的执行优先级。                                  |
| P-CSCF组类型       | 该参数用于指定P-CSCF组类型。                                  |
| 主IPv4 P-CSCF组   | 该参数用于绑定主IPv4 P-CSCF组名称。当指定该参数时，表示绑定了主IPv4 P-CSCF组。 |
| 备IPv4 P-CSCF组   | 该参数用于绑定备IPv4 P-CSCF组名称。当指定该参数时，表示绑定了备IPv4 P-CSCF组。 |
| 主IPv6 P-CSCF组   | 该参数用于绑定主IPv6 P-CSCF组名称。当指定该参数时，表示绑定了主IPv6 P-CSCF组。 |
| 备IPv6 P-CSCF组   | 该参数用于绑定备IPv6 P-CSCF组名称。当指定该参数时，表示绑定了备IPv6 P-CSCF组。 |