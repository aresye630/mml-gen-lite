# 查询PCC动作属性（LST PCCACTIONPROP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

此命令用于查询PCC动作属性。

支持批量查询，不输入查询条件，表示查询已经配置的所有PCC动作属性。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识           | 参数名称      | 参数说明                                                                                      |
|:---------------|:----------|:------------------------------------------------------------------------------------------|
| PCCACTPROPNAME | PCC动作属性名称 | 可选必选说明：可选参数 参数含义：设置PCC动作属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 查询名称为test\_pccact\_1的PCC动作属性：

  ```
  LST PCCACTIONPROP: PCCACTPROPNAME="test_pccact_1";
  ```

  ```
  RETCODE = 0  操作成功。

  PCC动作属性信息
  ---------------
     PCC动作属性名称  =  test_pccact_1
  上行发起重定向名称  =  test_redirect
    上行发起上行门控  =  Pass
    上行发起下行门控  =  Pass
  下行发起重定向名称  =  NULL
    下行发起上行门控  =  Discard
    下行发起下行门控  =  Discard
          配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有的PCC动作属性：

  ```
  LST PCCACTIONPROP:;
  ```

  ```
  RETCODE = 0  操作成功。

  PCC动作属性信息
  ---------------
  PCC动作属性名称    上行发起重定向名称    上行发起上行门控    上行发起下行门控    下行发起重定向名称    下行发起上行门控    下行发起下行门控    配置域名称
  test_pccact_1      test_redirect         Discard             Discard             NULL                  Pass                Pass                NULL
  test_pccact_2      NULL                  Pass                Pass                test_caqos            Discard             Discard             NULL
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

参见ADD PCCACTIONPROP的参数说明。