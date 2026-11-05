# 查询Diameter路由下一跳（LST UPDIAMRTNEXTHOP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查看已配置的Diameter路由下一跳信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称         | 参数说明                                                                                                                                                          |
|:------------|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REALMNAME   | Diameter域名名称 | 可选必选说明：可选参数 参数含义：该参数用于指定Diameter路由的realm名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 2670控制是否区分大小写。 默认值：无 配置原则：该参数使用ADD UPDIAMRTREALM命令配置生成。 |
| APPLICATION | Diameter应用   | 可选必选说明：可选参数 参数含义：该参数用于指定Diameter路由的Diameter应用。 数据来源：本端规划 取值范围：枚举类型。 SWM：SWM接口应用。 默认值：无 配置原则：无                                                                 |

#### 使用实例

- 显示指定realm名的Diameter路由下一跳信息，realm名为“example.com”：

  ```
  LST UPDIAMRTNEXTHOP:REALMNAME="example.com";
  ```

  ```
  RETCODE = 0  操作成功。
  Diameter路由下一跳信息
  ----------------
  Diameter域名名称             Diameter应用    下一跳               序号
  example.com                  SWM             host1                1  
  example.com                  SWM             host2                2
    (结果个数 = 2)
  ---    END
  ```
- 显示所有Diameter路由下一跳信息：

  ```
  LST UPDIAMRTNEXTHOP:;
  ```

  ```
  RETCODE = 0  操作成功。
  Diameter路由下一跳信息
  ----------------
  Diameter域名名称             Diameter应用    下一跳               序号
  example.com                  SWM             host1                1
  example.com                  SWM             host2                2      
  example1.com                 SWM             host3                1     
  (结果个数 = 3)
  ---    END
  ```

#### 输出结果说明

参见ADD UPDIAMRTNEXTHOP的参数说明。