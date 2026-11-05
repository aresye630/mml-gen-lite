# 查询服务端点组（LST SERVICEENDPOINTGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、MPF**

该命令用于查询服务端点组。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称    | 参数说明                                                                                                             |
|:----------|:--------|:-----------------------------------------------------------------------------------------------------------------|
| GROUPNAME | 服务端点组名称 | 可选必选说明：可选参数 参数含义：该参数用于指定服务端点组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。由大小写字母，数字，“-”，“.”组成，且只能以字母或者数字开头。 默认值：无 配置原则：无 |

#### 使用实例

- 查询全部的SERVICEENDPOINTGRP对象：

  ```
  LST SERVICEENDPOINTGRP:;
  ```

  ```
  RETCODE = 0  操作成功

  服务端点组
  ----------
  服务端点组名称  =  service_endpoint_grp
  (结果个数 = 1)

  ---    END
  ```
- 查询SERVICEENDPOINTGRP对象，查询的SERVICEENDPOINTGRP对象名称为"service\_endpoint\_grp"：

  ```
  LST SERVICEENDPOINTGRP: GROUPNAME="service_endpoint_grp";
  ```

  ```
  RETCODE = 0  操作成功

  服务端点组
  ----------
  服务端点组名称  =  service_endpoint_grp
  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

参见ADD SERVICEENDPOINTGRP的参数说明。