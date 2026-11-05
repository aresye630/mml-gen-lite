# 查询所有基于APN的CHR本地存盘策略（LST CHRRPTAPN）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于显示所有基于APN的CHR本地存盘策略。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

- 显示一个基于APN的CHR本地存盘策略信息：

  ```
  LST CHRRPTAPN:;
  ```

  ```
  %%
  RETCODE = 0 操作成功。

  基于APN的CHR本地存盘策略
  -------------------
       APN = apn1.com
  CHR 类型 = 信令CHR
   会话数量 = 3
  (结果个数 = 1)
  --- END
  ```
- 显示多个基于APN的CHR本地存盘策略信息：

  ```
  LST CHRRPTAPN:;
  ```

  ```
  RETCODE = 0 操作成功。

  基于APN的CHR本地存盘策略
  -------------------
  APN              CHR 类型    会话数量
  apn1.com     Signal CHR      1
  apn2.com     Signal CHR      1
  (结果个数 = 2)
  ```

#### 输出结果说明

参见ADD CHRRPTAPN的参数说明。