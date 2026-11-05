# 增加MME POOL（ADD MMEPOOL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C**

该命令用于添加MME POOL。当SGWPOOLNAME参数有输入时，表示添加MME POOL，并把该SGW POOL绑定至添加的MME POOL下。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入20条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称        | 参数说明                                                                                                                                                                                                                         |
|:-------------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MMEPOOLNAME  | MME POOL名称  | 可选必选说明：必选参数  参数含义：该参数用于指定MME POOL名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。  默认值：无  配置原则：无                                                                                                                          |
| SGWPOOLNAME  | SGW POOL名称  | 可选必选说明：可选参数  参数含义：该参数用于指定与该MME POOL绑定的SGW POOL名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~32。不区分大小写。  默认值：无  配置原则：  该参数使用ADD SGWPOOL命令配置生成。                                                                                           |
| BACKUPSWITCH | 指定备份MME功能开关 | 可选必选说明：可选参数  参数含义：配置是否开启指定备份MME的功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则： 该参数使能时，表示开启指定备份MME的功能，MME故障或者重启场景进行快速恢复时会向指定的备份MME发送DDN消息。该参数不使能时，表示不开启指定备份MME的功能，MME故障或者重启场景进行快速恢复时会从MME POOL中选择MME发送DDN消息。 |

## 使用实例

- 假设用户需要配置一个名称为“mmepool1”的MME POOL：

  ```
  ADD MMEPOOL:MMEPOOLNAME="mmepool1";
  ```
- 假设已配置了SGW POOL名为“sgwpool”,现假设用户需要配置一个名称为“mmepool1”的MME POOL同时为其绑定一个名为“sgwpool”的SGW POOL：

  ```
  ADD MMEPOOL:MMEPOOLNAME="mmepool1",SGWPOOLNAME="sgwpool";
  ```
- 假设已配置了SGW POOL名为“sgwpool”，现假设用户需要配置一个名称为“mmepool1”的MME POOL同时为其绑定一个名为“sgwpool”的SGW POOL和开启backup功能：

  ```
  ADD MMEPOOL:MMEPOOLNAME="mmepool1",SGWPOOLNAME="sgwpool",BACKUPSWITCH=ENABLE;
  ```