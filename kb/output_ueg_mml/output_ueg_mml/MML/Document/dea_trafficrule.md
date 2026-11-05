# 去激活流规则（DEA TRAFFICRULE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：MPF**

该命令用于去激活流规则配置。

#### 注意事项

该命令执行后60s生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                                                         |
|:--------------|:-------|:-------------------------------------------------------------------------------------------------------------|
| APPNAME       | 应用名称   | 可选必选说明：必选参数 参数含义：指定应用名称，可以通过DSP APPLICATIONINFO查出所有的应用名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：无     |
| APPINSTANCEID | APP实例号 | 可选必选说明：可选参数 参数含义：指定app实例号，可以通过DSP APPLICATIONINFO查出所有的app实例号。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～32。 默认值：无 配置原则：无 |
| TRAFFICRULEID | 流规则ID  | 可选必选说明：可选参数 参数含义：指定流规则ID。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～95。 默认值：无 配置原则：无                                     |

#### 使用实例

- 根据指定app名称去激活流规则配置，app名称为“appName\_0”。命令执行后，app名称为“appName\_0”下所有规则的state将置为INACTIVE：

  ```
  DEA TRAFFICRULE: APPNAME="appName_0";
  ```
- 根据指定app名称和app实例号去激活流规则配置，app名称为“appName\_1”、app实例号为“appInstanceId\_1”。命令执行后，app名称为“appName\_1”、app实例号为“appInstanceId\_1”下所有规则的state将置为INACTIVE：

  ```
  DEA TRAFFICRULE: APPNAME="appName_1", APPINSTANCEID="appInstanceId_1";
  ```
- 根据指定app名称和流规则ID去激活流规则配置，app名称为“appName\_2”、流规则ID为“trafficRuleId\_2”。命令执行后，app名称为“appName\_2”下的所有流规则ID为“trafficRuleId\_2”的规则的state将置为INACTIVE：

  ```
  DEA TRAFFICRULE: APPNAME="appName_2", TRAFFICRULEID="trafficRuleId_2";
  ```
- 根据指定app名称、app实例号和流规则ID去激活流规则配置，app名称为“appName\_1”、app实例号为“appInstanceId\_1”、流规则ID为“trafficRuleId\_0”。命令执行后，该规则的state将置为INACTIVE：

  ```
  DEA TRAFFICRULE: APPNAME="appName_1", APPINSTANCEID="appInstanceId_1", TRAFFICRULEID="trafficRuleId_0";
  ```