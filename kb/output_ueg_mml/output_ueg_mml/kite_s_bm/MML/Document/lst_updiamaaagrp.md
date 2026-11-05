# 查询Diameter AAA服务器组（LST UPDIAMAAAGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询Diameter AAA组配置信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

- 当存在一条Diameter AAA组配置时，查询Diameter AAA组配置信息：

  ```
  %%LST UPDIAMAAAGRP:;
  ```

  ```
  %%
  RETCODE = 0  操作成功
  Diameter AAA组
  --------------
         Diameter AAA组名  =  diametergroup
  (结果个数 = 1)
  ---    END
  ```
- 当存在多条Diameter AAA组配置时，查询Diameter AAA组配置信息：

  ```
  %%LST UPDIAMAAAGRP:;
  ```

  ```
  %%
  RETCODE = 0  操作成功
  Diameter AAA组
  --------------
  Diameter AAA组名
  diametergroup
  diametergroup1
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

参见ADD UPDIAMAAAGRP的参数说明。