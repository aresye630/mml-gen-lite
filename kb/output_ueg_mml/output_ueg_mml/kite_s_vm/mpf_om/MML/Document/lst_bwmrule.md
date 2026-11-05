# 查询带宽管理规则（LST BWMRULE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：MPF**

该命令用于查询默认用户组、或具体用户组的业务带宽控制规则。当运营商希望查询带宽管理规则的类型、用户组或用户级别、业务类型和控制器等参数信息时，则执行该命令。

#### 注意事项

如果指定用户组类型，而不指定带宽管理规则名称，可以查询用户组下的所有带宽管理规则，包括默认的规则。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                                                                                                                                                                                   |
|:--------------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| USERGROUPTYPE | 用户组类型    | 可选必选说明：可选参数 参数含义：该参数用于配置带宽管理用户组的类型。 数据来源：本端规划 取值范围：枚举类型。 DEFAULT_GROUP：默认用户组。SPECIFIC_GROUP：特定用户组。 默认值：无 配置原则：无                                                                                                                                        |
| USERGROUPNAME | 用户组名称    | 可选必选说明：条件必选参数 前提条件：该参数在“USERGROUPTYPE”配置为“SPECIFIC_GROUP”时为必选参数。 参数含义：该参数用于配置具体用户组的名称，该参数由增加带宽管理用户组定义。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                     |
| BWMRULETYPE   | 带宽管理规则类型 | 可选必选说明：条件可选参数 前提条件：该参数在“USERGROUPTYPE”配置为“SPECIFIC_GROUP” 或 “DEFAULT_GROUP”时为可选参数。 参数含义：该参数用于配置带宽管理规则的类型。 数据来源：本端规划 取值范围：枚举类型。 GROUP_DEFAULT：用户组级别默认规则。SUBSCRIBER_DEFAULT：用户级别默认规则。GROUP_SPECIFIC：用户组级别特定规则。SUBSCRIBER_SPECIFIC：用户级别特定规则。 默认值：无 配置原则：无 |
| BWMRULENAME   | 带宽管理规则名称 | 可选必选说明：条件必选参数 前提条件：该参数在“BWMRULETYPE”配置为“GROUP_SPECIFIC” 或 “SUBSCRIBER_SPECIFIC”时为必选参数。 参数含义：该参数用于配置带宽管理规则的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                              |

#### 使用实例

- 假如运营商需要查询名为“testbwmusergroup”用户组下具体的带宽管理规则“testbwmrule”：

  ```
  LST BWMRULE: USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="testbwmusergroup",BWMRULETYPE=SUBSCRIBER_DEFAULT;
  ```

  ```
  RETCODE = 0  操作成功。

  带宽管理规则信息
  ----------------
                用户组类型  =  特定用户组
                用户组名称  =  testbwmusergroup
          带宽管理规则名称  =  subscriber_default
          带宽管理规则类型  =  用户级别默认
        带宽管理规则优先级  =  NULL
          带宽控制业务名称  =  NULL
                       RAT  =  未配置
                      漫游  =  未配置
  上行带宽管理控制器名称一  =  testbwmrule
  下行带宽管理控制器名称一  =  NULL
              时间段名称一  =  NULL
  上行带宽管理控制器名称二  =  NULL
  下行带宽管理控制器名称二  =  NULL
              时间段名称二  =  NULL
  上行带宽管理控制器名称三  =  NULL
  下行带宽管理控制器名称三  =  NULL
              时间段名称三  =  NULL
  上行带宽管理控制器名称四  =  NULL
  下行带宽管理控制器名称四  =  NULL
              时间段名称四  =  NULL
                  业务级别  =  1
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商需要查询具体用户组“testbwmusergroup”下所有的带宽管理规则：

  ```
  LST BWMRULE: USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="testbwmusergroup";
  ```

  ```
  RETCODE = 0  操作成功。

  带宽管理规则信息
  ----------------
  用户组类型    用户组名称          带宽管理规则名称      带宽管理规则类型    带宽管理规则优先级    带宽控制业务名称    RAT       漫游      上行带宽管理控制器名称一    下行带宽管理控制器名称一    时间段名称一    上行带宽管理控制器名称二    下行带宽管理控制器名称二    时间段名称二    上行带宽管理控制器名称三    下行带宽管理控制器名称三    时间段名称三    上行带宽管理控制器名称四    下行带宽管理控制器名称四    时间段名称四    业务级别

  特定用户组    testbwmusergroup    group_default         用户组级别默认      NULL                  NULL                未配置    未配置    testupbwmctrl               testupbwmctrl               NULL            NULL                        NULL                        NULL            NULL                        NULL                        NULL            NULL                        NULL                        NULL            1       
  特定用户组    testbwmusergroup    subscriber_default    用户级别默认        NULL                  NULL                未配置    未配置    testbwmrule                 NULL                        NULL            NULL                        NULL                        NULL            NULL                        NULL                        NULL            NULL                        NULL                        NULL            1       
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

参见ADD BWMRULE的参数说明。