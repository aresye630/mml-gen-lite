# 查询PCC组业务属性绑定（LST SRVPBINDPCCPG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

此命令用于查询PCC策略组业务属性绑定组合。

#### 注意事项

- 不输入查询条件，表示查询已经配置的所有PCC策略组业务属性绑定组合。
- 只输入PCCPOLICYGRPNM，表示查询指定名称的PCC策略组业务属性绑定组合。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识           | 参数名称     | 参数说明                                                                                     |
|:---------------|:---------|:-----------------------------------------------------------------------------------------|
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：必选参数 参数含义：设置PCC策略组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无 |
| SRVPROPNAME    | 业务属性名称   | 可选必选说明：可选参数 参数含义：设置业务属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无   |

#### 使用实例

- 查询PCC策略组名称为test\_pccgrp\_1，业务属性名称为test\_srvp\_1的PCC策略组业务属性绑定组合：

  ```
  LST SRVPBINDPCCPG: PCCPOLICYGRPNM="test_pccgrp_1",SRVPROPNAME="test_srvp_1";
  ```

  ```
  RETCODE = 0  操作成功。

  业务属性绑定PCC策略组信息
  -------------------------
         PCC策略组名称  =  test_pccgrp_1
          业务属性名称  =  test_srvp_1
          计费属性名称  =  NULL
       PCC动作属性名称  =  NULL
          扩展属性名称  =  NULL
            监控属性值  =  NULL
  Session级FUP累计标识  =  不使能
  (结果个数 = 1)
  ---    END
  ```
- 查询PCC策略组名称为test\_pccgrp\_1的PCC策略组业务属性绑定组合：

  ```
  LST SRVPBINDPCCPG: PCCPOLICYGRPNM="test_pccgrp_1";
  ```

  ```
  RETCODE = 0  操作成功。

  业务属性绑定PCC策略组信息
  -------------------------
  PCC策略组名称    业务属性名称    计费属性名称    PCC动作属性名称    扩展属性名称    监控属性值    Session级FUP累计标识

  test_pccgrp_1    test_srvp_1     NULL            NULL               NULL            NULL          不使能              
  test_pccgrp_1    test_srvp_2     NULL            NULL               NULL            NULL          不使能              
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

参见ADD SRVPBINDPCCPG的参数说明。