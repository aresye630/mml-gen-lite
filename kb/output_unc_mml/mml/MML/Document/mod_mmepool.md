# 修改MME POOL（MOD MMEPOOL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C**

该命令用于修改绑定MME POOL的SGW POOL和设置备份开关。假设运营商需要重新规划网络时，使用该命令。

## 注意事项

- 该命令执行后立即生效。

- SGWPOOLNAME字段为单空格时，表示清空SGWPOOLNAME。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称        | 参数说明                                                                                                                                                                                                                   |
|:-------------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MMEPOOLNAME  | MME POOL名称  | 可选必选说明：必选参数  参数含义：该参数用于指定MME POOL名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。  默认值：无  配置原则：无                                                                                                                    |
| SGWPOOLNAME  | SGW POOL名称  | 可选必选说明：可选参数  参数含义：该参数用于指定与该MME POOL绑定的SGW POOL名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~32。不区分大小写。  默认值：无  配置原则：  该参数使用ADD SGWPOOL命令配置生成。                                                                                     |
| BACKUPSWITCH | 指定备份MME功能开关 | 可选必选说明：可选参数  参数含义：配置是否开启指定备份MME的功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无  配置原则： 该参数使能时，表示开启指定备份MME的功能，MME故障或者重启场景进行快速恢复时会向指定的备份MME发送DDN消息。该参数不使能时，表示不开启指定备份MME的功能，MME故障或者重启场景进行快速恢复时会从MME POOL中选择MME发送DDN消息。 |

## 使用实例

- 假设已经与名为“mmepool1”的MME POOL绑定的名为“sgwpool1”的SGW POOL，需要改为绑定名为“sgwpool2”的SGW POOL：

  ```
  MOD MMEPOOL:MMEPOOLNAME="mmepool1",SGWPOOLNAME="sgwpool2";
  ```
- 假设已配置的名为“mmepool2”的MME POOL还未绑定SGW POOL，现需绑定一个名为“sgwpool3”：

  ```
  MOD MMEPOOL:MMEPOOLNAME="mmepool2",SGWPOOLNAME="sgwpool3";
  ```
- 假设已配置的名为“mmepool3”的MME POOL还未绑定SGW POOL，现需绑定一个名为“sgwpool4”，且备份开关设置为打开：

  ```
  MOD MMEPOOL:MMEPOOLNAME="mmepool3",SGWPOOLNAME="sgwpool4",BACKUPSWITCH=ENABLE;
  ```