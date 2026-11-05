# 显示Diameter Route状态（DSP UPDIAMRTSTATUS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

此命令用来查询Diameter路由的状态。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                                                                          |
|:------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------|
| REALM       | Diameter域名 | 可选必选说明：可选参数 参数含义：该参数用于指定Diameter应用的域名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 2670控制是否区分大小写。 默认值：无 配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：可选参数 参数含义：该参数用于指定Diameter协议中的应用类型。 数据来源：本端规划 取值范围：枚举类型。 SWM：SWM接口应用。 默认值：无 配置原则：无                                      |

#### 使用实例

- 查询Diameter realm为"swm-realm"的Diameter Route信息：

  ```
  DSP UPDIAMRTSTATUS: REALM="swm-realm-realm",APPLICATION=SWM;
  ```

  ```
  RETCODE = 0  操作成功。
  Diameter路由状态
  ----------------
  Diameter域名    Diameter应用    POD名称       状态    
  swm-realm       Swm             updiam-pod-0  Normal  
  swm-realm       Swm             updiam-pod-0  Abnormal
  (结果个数 = 2)
  ```
- 查询全部Diameter Route信息：

  ```
  DSP UPDIAMRTSTATUS:;
  ```

  ```
  RETCODE = 0  操作成功。
  Diameter路由状态
  ----------------
  Diameter域名    Diameter应用    POD名称       状态    
  swm-realm       Swm             updiam-pod-0  Normal  
  swm-realm       Swm             updiam-pod-0  Abnormal
  (结果个数 = 2)
  ```

#### 输出结果说明

| 输出项名称      | 输出项解释                               |
|:-----------|:------------------------------------|
| Diameter域名 | 用于指定Diameter应用的域名。                  |
| Diameter应用 | 用于指定Diameter协议中的应用类型。               |
| POD名称      | 用户指定查询到的Diameter Route所在的POD资源单元名称。 |
| 状态         | 用于指定查询到的Diameter Route的状态。          |