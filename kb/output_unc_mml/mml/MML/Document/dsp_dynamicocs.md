# 查询动态OCS（DSP DYNAMICOCS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询动态OCS主机列表项。

DRA部署场景下，DRA进行OCS寻址，如果寻址到的OCS主机名并未在网关本地配置，则网关会将寻址结果存至动态OCS主机列表。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                          |
|:------------|:--------|:------------------------------------------------------------------------------|
| OCSHOSTNAME | OCS主机名称 | 可选必选说明：可选参数 参数含义：主机的名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格。 默认值：无 配置原则：无 |

#### 使用实例

- 查询指定主机名称的动态OCS信息：

  ```
  DSP DYNAMICOCS:OCSHOSTNAME="ocs-host-name";
  ```

  ```
  Dynamic OCS Information
  -------------------------
  OCS Host Name  =  ocs-host-name
     Realm Name  =  realm
  (Number of results = 1)
  ---    END
  ```
- 查询所有动态OCS信息：

  ```
  DSP DYNAMICOCS:;
  ```

  ```
  Dynamic OCS Information
  -------------------------
  OCS Host Name    Realm Name
  ocs-host-name    realm    
  ocs-name         realm    
  (Number of results = 2)
  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释    |
|:--------|:---------|
| OCS主机名称 | 主机的名称。   |
| 域名      | 动态OCS域名。 |