# 查询冲突检测结果（DSP COLLISIONCHECK）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于显示对配置的Filter、Rule、UserProfile进行冲突检测的结果信息。仅支持检测简单IPv4的Filter中的协议、IP地址和Port是否存在冲突。如果Filter中有IPLIST或者IPv6的Filter，不参与冲突检测，并提示存在不参与冲突检测的Filter信息。

#### 注意事项

冲突的Flow Filter的定义是指：定义为外置定义属性的Flow Filter名称在外置OTT数据库里没有定义；或者定义为非外置定义属性的Flow Filter名称在外置OTT数据库里有定义。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                                                                                                                                                                 |
|:----------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CHECKTYPE       | 冲突检测类型 | 可选必选说明：必选参数 参数含义：该参数用于指定冲突检测类型。 数据来源：本端规划 取值范围：枚举类型。 COLL_FILTER_CHECK：过滤器冲突检测。COLL_ACL_CHECK：ACL冲突检测。COLL_RULE_CHECK：规则冲突检测。COLL_USRP_CHECK：用户模板冲突检测。COLL_FLOWFILTER_CHECK：Flow filter冲突检测。 默认值：无 配置原则：如果运营商想要检查Filter冲突检测，设置此参数为COLL_FILTER_CHECK。 |
| FILTERNAME      | 过滤器名字  | 可选必选说明：条件可选参数 前提条件：该参数在“CHECKTYPE”配置为“COLL_FILTER_CHECK”时为可选参数。 参数含义：该参数用于指定过滤器名字。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD FILTER命令配置生成。                                                                                  |
| ACLNAME         | ACL名称  | 可选必选说明：条件可选参数 前提条件：该参数在“CHECKTYPE”配置为“COLL_ACL_CHECK”时为可选参数。 参数含义：该参数用于指定ACL名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：该参数使用ADD ACL命令配置生成。                                                                                                     |
| RULENAME        | 规则名称   | 可选必选说明：条件必选参数 前提条件：该参数在“CHECKTYPE”配置为“COLL_RULE_CHECK”时为必选参数。 参数含义：该参数用于设置规则名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD RULE命令配置生成。                                                                                       |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：条件必选参数 前提条件：该参数在“CHECKTYPE”配置为“COLL_USRP_CHECK”时为必选参数。 参数含义：该参数用于设置用户模板名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD USERPROFILE命令配置生成。                                                                              |

#### 使用实例

- 假设运营商想要查询所有Filter的冲突检测：

  ```
  DSP COLLISIONCHECK: CHECKTYPE=COLL_FILTER_CHECK;
  ```

  ```
  RETCODE = 0 Operation Success.

  Collision Check Result Information
  ----------------------------------
  Collision Check Type Query Result
  Filter Collision Check Filter-overlap happens, please check the whole filter configuration
  Filter Collision Check 1. Filter [TestFilter1] and existing filter [TestFilter2] totally overlap
  Filter Collision Check 2. Filter [TestFilter3] and existing filter [TestFilter4] partially overlap
  (Number of results = 2)
  --- END
  ```
- 假设运营商想要查询名称为TestFilter1的冲突检测：

  ```
  DSP COLLISIONCHECK:CHECKTYPE=COLL_FILTER_CHECK,FILTERNAME="TestFilter1";
  ```

  ```
  RETCODE = 0 Operation Success.

  Collision Check Result Information
  ----------------------------------
  Collision Check Type Query Result
  Filter Collision Check Filter-overlap happens, please check the whole filter configuration
  Filter Collision Check 1. Filter [TestFilter1] and existing filter [TestFilter2] totally overlap

  (Number of results = 1)
  --- END
  ```
- 假设运营商想要查询名称为TestRule1的冲突检测：

  ```
  DSP COLLISIONCHECK: CHECKTYPE=COLL_RULE_CHECK, RULENAME="TestRule1";
  ```

  ```
  RETCODE = 0  Operation succeeded

  Collision Check Result Information
  ----------------------------------
  Collision Check Type  =  Rule Collision Check
          Query Result  =     1. Rule [TestRule1] is contained by Rule [TestRule2] (RuleType = PCC)
  (Number of results = 1)

  ---    END
  ```
- 假设运营商想要查询名称为TestUserProfile1的冲突检测：

  ```
  DSP COLLISIONCHECK: CHECKTYPE=COLL_USRP_CHECK, USERPROFILENAME="TestUserProfile1";
  ```

  ```
  RETCODE = 0  Operation succeeded

  Collision Check Result Information
  ----------------------------------
  Collision Check Type  =  User Profile Collision Check
          Query Result  =     1. Rule [TestRule1] belongs to UserProfile [TestUserProfile1] is overlapped with Rule [TestRule2] (RuleType = 0) GLOBLE
  (Number of results = 1)

  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 冲突检测类型  | 用于指定冲突检测类型。 |
| 查询结果    | 用于存放查询结果。   |