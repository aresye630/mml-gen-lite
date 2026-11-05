# 增加对鉴权信元用户名和密码的控制（ADD AUTHNAMEPWDCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加对鉴权信元用户名和密码的控制。

## 注意事项

- 该命令执行后立即生效。

- 该命令最大记录数为20000。
- ADD命令可以把UNLIMITED的参数看做通配符，这样新增记录可能与已有记录在通配条件下冲突。这种情况RETCODE = 65558，可不添加此记录，或者识别到已有的冲突记录删除后，再添加。
- 最后两个属性NAMESOURCE、PWDSOURCE是配置的目标值，当业务中获取不到对应的用户名或密码时，不再根据配置进行鉴权信元的重刷。
- 业务在读取配置时，如果同时匹配到EFFECTIVESCOPE等于GLOBAL和SINGLE\_APN两种模式的配置记录，则优先取用SINGLE\_APN模式的结果。
- 配置生效后，业务中会对除了NAMESOURCE、PWDSOURCE之外的属性进行匹配，其中属性APN、ACCESSMODE、AUTHMODE、PCOPRIORITY、PWDUSEPCO会与LST APNAUTHATTR查询出的配置对应字段进行匹配。在EFFECTIVESCOPE等于GLOBAL模式下，业务使用会话对应apn获取APNAUTHATTR配置。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                |
|:---------------|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EFFECTIVESCOPE | 生效范围       | 可选必选说明：必选参数  参数含义：该参数用于指定单APN生效或全局生效。  数据来源：本端规划 取值范围： “GLOBAL（全局生效）”：全局生效“SINGLE_APN（单个APN生效）”：单个APN生效  默认值：无  配置原则：无                                                                                                                                                                                                                                              |
| APN            | APN名称      | 可选必选说明：该参数在"EFFECTIVESCOPE"配置为"SINGLE_APN"时为条件必选参数。  参数含义：该参数用于指定APN实例名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。  默认值：无  配置原则：  该参数使用ADD APN命令配置生成。                                                                                                |
| PCONAME        | PCO是否携带用户名 | 可选必选说明：必选参数  参数含义：该参数表示PCO是否携带用户名。  数据来源：本端规划 取值范围： “PCO_NAME_FALSE（PCO未携带用户名）”：PCO未携带用户名。“PCO_NAME_TRUE（PCO携带用户名）”：PCO携带用户名。“PCO_NAME_UNLIMITED（不限制PCO是否携带用户名）”：不限制PCO是否携带用户名。  默认值：无  配置原则：无                                                                                                                                                                      |
| PCOPWD         | PCO是否携带密码  | 可选必选说明：必选参数  参数含义：该参数表示PCO是否携带密码。  数据来源：本端规划 取值范围： “PCO_PWD_FALSE（PCO未携带密码）”：PCO未携带密码。“PCO_PWD_TRUE（PCO携带密码）”：PCO携带密码。“PCO_PWD_UNLIMITED（不限制PCO是否携带密码）”：不限制PCO是否携带密码。  默认值：无  配置原则：无                                                                                                                                                                                |
| ACCESSMODE     | 接入模式       | 可选必选说明：必选参数  参数含义：该参数表示接入模式。  数据来源：本端规划 取值范围： “TRANS_AUTH（透明鉴权）”：指定为透明并需要鉴权。这种鉴权方式对用户是透明的，不需要用户感知，鉴权使用的用户名和密码一般由PGW/GGSN配置。“TRANS_NON_AUTH（透明不鉴权）”：指定为透明不需要鉴权。这种接入方式不需要去RADIUS服务器鉴权。“NON_TRANS（不透明）”：指定为不透明接入，需要鉴权。这种鉴权方式可以继续配置鉴权使用的用户名和密码。“LOC_AUTH（本地鉴权）”：指定为本地鉴权。这种接入方式不需要去RADIUS服务器鉴权，通过PGW/GGSN完成鉴权功能。“ACCESS_MODE_UNLIMITED（接入模式无限制）”：接入模式无限制。  默认值：无  配置原则：无 |
| AUTHMODE       | 鉴权模式       | 可选必选说明：必选参数  参数含义：该参数表示鉴权模式。  数据来源：本端规划 取值范围： “PCO（使用PCO）”：表示鉴权和计费消息使用PCO中携带的用户名和密码。“APN（使用APN）”：表示鉴权和计费消息使用APN作为用户名，密码由参数PASSWORD配置。“MSISDN（使用MSISDN）”：表示鉴权和计费消息使用MSISDN作为用户名，密码由PASSWORD配置。“AUTH_MODE_UNLIMITED（鉴权模式无限制）”：鉴权模式无限制。  默认值：无  配置原则：无                                                                                                                 |
| PCOPRIORITY    | PCO优先级     | 可选必选说明：必选参数  参数含义：该参数用于指定当鉴权方式选择为APN或者MSISDN的时候，如果PCO携带了用户名、密码，是否优先采用PCO中的携带的用户名密码。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：不使能“ENABLE（使能）”：使能“UNLIMITED（无限制）”：无限制  默认值：无  配置原则：无                                                                                                                                                                                           |
| PWDUSEPCO      | 使用PCO中的密码  | 可选必选说明：必选参数  参数含义：该参数用于指定当鉴权方式选择为APN或者MSISDN的时候，密码是否优先采用PCO中携带的密码。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：不使能“ENABLE（使能）”：使能“UNLIMITED（无限制）”：无限制  默认值：无  配置原则：无                                                                                                                                                                                                            |
| NAMESOURCE     | 用户名来源      | 可选必选说明：必选参数  参数含义：该参数用于指定用户名来源。  数据来源：本端规划 取值范围： “FROM_CFG（取自配置）”：取自配置“FROM_PCO（取自PCO）”：取自PCO“FROM_APN（取自APN）”：取自APN“FROM_IMSI（取自IMSI）”：取自IMSI“FROM_MSISDN（取自MSISDN）”：取自MSISDN  默认值：无  配置原则：无                                                                                                                                                                       |
| PWDSOURCE      | 密码来源       | 可选必选说明：必选参数  参数含义：该参数用于指定密码来源。  数据来源：本端规划 取值范围： “FROM_CFG_PASSWORD（取自配置Password值）”：取自配置Password值“FROM_CFG_COMMONUSERPASS（取自配置CommonUserPass值）”：取自配置CommonUserPass值“FROM_PCO（取自PCO中密码）”：取自PCO中密码  默认值：无  配置原则：无                                                                                                                                                      |

## 使用实例

如果需要通过配置来决定鉴权信元内用户名和密码的填写方式，如透明鉴权，所有APN下，通过读取配置填入鉴权的用户名，通过配置中的CommonUserPass填充密码信元，可以使用该实例：

```
ADD AUTHNAMEPWDCTRL: EFFECTIVESCOPE=GLOBAL, PCONAME=PCO_NAME_UNLIMITED, PCOPWD=PCO_PWD_UNLIMITED, ACCESSMODE=TRANS_AUTH, AUTHMODE=AUTH_MODE_UNLIMITED, PCOPRIORITY=UNLIMITED, PWDUSEPCO=UNLIMITED, NAMESOURCE=FROM_CFG, PWDSOURCE=FROM_CFG_COMMONUSERPASS;
```