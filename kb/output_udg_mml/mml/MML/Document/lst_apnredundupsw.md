# 查询指定APN静态地址路由冗余上行报文隧道转发功能开关（LST APNREDUNDUPSW）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询指定APN静态地址路由冗余上行报文隧道转发功能开关。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                           |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------|
| APN    | APN名称  | 可选必选说明：可选参数 参数含义：指定APN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

- 假设用户要查询所有APN下配置的静态地址路由冗余上报隧道转发功能相关信息：

  ```
  LST APNREDUNDUPSW:;
  ```

  ```
  %%LST APNREDUNDUPSW:;%%
  RETCODE = 20111  There is no data in the table.

  No matching result is found
  ---    END
  ```
- 假设用户要查询APN “huawei.com”下配置的静态地址路由冗余上报隧道转发功能相关信息：

  ```
  LST APNREDUNDUPSW:APN="huawei.com";
  ```

  ```
  %%LST APNREDUNDUPSW: APN="huawei.com";%%
  RETCODE = 0  Operation succeeded

  APN Routing Redundancy Uplink Packet Tunnel Forwarding Switch Information
  -------------------------------------------------------------------------
                                 APN  =  huawei.com
  APN-specific IPV4 Redund up Switch  =  DISABLE
  APN-specific IPV6 Redund up Switch  =  DISABLE
  (Number of results = 1)

  ---    END
  ```

#### 输出结果说明

参见SET APNREDUNDUPSW的参数说明。