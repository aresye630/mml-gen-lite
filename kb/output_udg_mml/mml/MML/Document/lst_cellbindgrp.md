# 查询小区和小区组绑定关系（LST CELLBINDGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询小区组和小区的绑定关系。

#### 注意事项

- 如果不输入小区组名称，表示查询系统中所有小区组和小区的绑定关系。
- 如果输入小区组名称，表示查询指定的小区组和小区的绑定关系。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                                                                 |
|:--------------|:-------|:---------------------------------------------------------------------------------------------------------------------|
| CELLGROUPNAME | 小区组名称  | 可选必选说明：可选参数 参数含义：该参数用于设置小区组名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD CELLBINDGRP命令配置生成。 |

#### 使用实例

- 假如运营商需要查询名称为TestCellGroupName的小区组下绑定的小区信息：

  ```
  LST CELLBINDGRP: CELLGROUPNAME="TestCellGroupName";
  ```

  ```
  RETCODE = 0  操作成功

  小区和小区组绑定关系
  ----------------
  小区组名称     小区名称
  TestCellGroupName  TestCellName
  TestCellGroupName  TestCellName2  
  (结果个数 = 2)

  ---    END
  ```
- 假如运营商需要查询所有的小区组下绑定的小区信息：

  ```
  LST CELLBINDGRP:;
  ```

  ```
  RETCODE = 0  操作成功

  小区和小区组绑定关系
  ----------------
  小区组名称     小区名称
  TestCellGroupName  TestCellName
  TestCellGroupName  TestCellName2 
  TestCellGroupName1 TestCellName3
  TestCellGroupName1 TestCellName4
  (结果个数 = 4)

  ---    END
  ```

#### 输出结果说明

参见ADD CELLBINDGRP的参数说明。