# 查询APN PPP配置（LST APNPPPACCESS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询APN的PPP配置信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                           |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------|
| APN    | APN名称  | 可选必选说明：可选参数 参数含义：指定APN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 假设用户要查询所有APN下配置的PPP配置信息：

  ```
  LST APNPPPACCESS:;
  ```

  ```
  RETCODE = 0  Operation Success.

  APN PPP Configuration Information
  ---------------------------------
  APN           Authentication switch    Maximum Receive Unit

  huawei.com    ENABLE                   NULL                   
  example.com    DISABLE                  1500                
  (Number of results = 2)
  ---    END
  ```
- 假设用户要查询APN “huawei.com”下配置的PPP相关信息：

  ```
  LST APNPPPACCESS:;
  ```

  ```
  RETCODE = 0  Operation Success.

  APN PPP Configuration Information
  ---------------------------------
                    APN  =  huawei.com
  Authentication switch  =  ENABLE
   Maximum Receive Unit  =  NULL
  (Number of results = 1)
  ---    END
  ```

#### 输出结果说明

参见SET APNPPPACCESS的参数说明。