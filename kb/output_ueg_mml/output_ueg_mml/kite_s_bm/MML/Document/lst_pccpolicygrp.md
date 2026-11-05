# 查询PCC策略组（LST PCCPOLICYGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

此命令用于查询PCC策略组。

支持批量查询，不输入查询条件，表示查询已经配置的所有PCC策略组。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识           | 参数名称     | 参数说明                                                                                     |
|:---------------|:---------|:-----------------------------------------------------------------------------------------|
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：可选参数 参数含义：设置PCC策略组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 查询名称为test\_pccgrp\_1的PCC策略组：

  ```
  LST PCCPOLICYGRP: PCCPOLICYGRPNM="test_pccgrp_1";
  ```

  ```
  RETCODE = 0  操作成功。

  PCC策略组信息
  -------------
         PCC策略组名称  =  test_pccgrp_1
       PCC动作属性名称  =  NULL
          扩展属性名称  =  NULL
  Session级FUP累计标识  =  不使能
             Token密钥  =  *****
      信令关联计费标识  =  使能
       ADC静默通知标识  =  使能
           Qos属性名称  =  NULL
   HTTP2.0协议回落开关  =  继承
     Token检测功能标识  =  不使能
             URR组名称  =  NULL
         信令URR组名称  =  NULL
          事件计费标识  =  不使能
            事件计费点  =  响应
          彩信计费类型  =  单条计费
            配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有的PCC策略组：

  ```
  LST PCCPOLICYGRP:;
  ```

  ```
  RETCODE = 0  操作成功。

  PCC策略组信息
  -------------
  PCC策略组名称    PCC动作属性名称    扩展属性名称    Session级FUP累计标识    Token密钥    信令关联计费标识    ADC静默通知标识    Qos属性名称    HTTP2.0协议回落开关    Token检测功能标识    URR组名称    信令URR组名称    事件计费标识    事件计费点    彩信计费类型    CfgDomainName

  test_pccgrp_1    NULL               NULL            不使能                  *****        使能                使能               NULL           继承                   不使能               NULL         NULL             不使能          响应          单条计费        NULL
  test_pccgrp_2    NULL               NULL            不使能                  *****        使能                使能               NULL           继承                   不使能               NULL         NULL             不使能          响应          单条计费        NULL
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

参见ADD PCCPOLICYGRP的参数说明。