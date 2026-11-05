# 查询Rule IMSI/MSISDN号段组绑定（LST RULESEGBIND）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询IMSI/MSISDN号段组与Rule的绑定关系。

#### 注意事项

如果不输入IMSI/MSISDN号段组名称，表示查询所有IMSI/MSISDN号段组与规则的绑定关系。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称             | 参数说明                                                                                                    |
|:-----------|:-----------------|:--------------------------------------------------------------------------------------------------------|
| IMSIMSSEGG | IMSI/MSISDN号段组名称 | 可选必选说明：可选参数 参数含义：该参数用于指定要绑定的IMSI/MSISDN号段组。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 假如运营商需要查询名为testseg号段组绑定的规则：

  ```
  LST RULESEGBIND: IMSIMSSEGG="testseg";
  ```

  ```
  RETCODE = 0  操作成功。

  规则IMSI/MSISDN号段组绑定
  -------------------------
  IMSI/MSISDN号段组名称  =  testseg
               Rule名称  =  testrule
               策略类型  =  IP Redirect
             配置域名称  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商需要查询所有号段组绑定的规则：

  ```
  LST RULESEGBIND:;
  ```

  ```
  RETCODE = 0  操作成功。

  规则IMSI/MSISDN号段组绑定
  -------------------------
  IMSI/MSISDN号段组名称  Rule名称   策略类型     配置域名称  

  testseg                testrule   IP Redirect  NULL           
  testseg1               testrule1  IP Redirect  NULL           
  (结果个数 = 2)

  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释     |
|:--------|:----------|
| 策略类型    | 用于显示策略类型。 |

其余输出项请参见ADD RULESEGBIND的参数说明。