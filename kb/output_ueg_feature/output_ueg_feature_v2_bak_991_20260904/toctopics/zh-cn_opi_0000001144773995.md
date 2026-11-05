# 激活动态分流规则安装（UPF）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

UPF上的动态规则生效原则受本地配置控制，本地配置支持两种粒度：DNN级别通过**SET APNAPPPARA**命令配置、全局级别通过**SET GLBAPPPARA**命令配置，其中，DNN级别优先级大于全局级别。根据全局/DNN级配置控制UPF上的APP动态规则如何安装生效。

**说明** 

适用于UPF。

## 必备事项

前提条件

请仔细阅读动态分流规则安装（UPF）。

数据

| 类别             | 参数名称                      | 取值样例          | 获取方法     | 说明                                                                                                                                                                                                      |
|:---------------|:--------------------------|:--------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SET GLBAPPPARA | App规则生效条件 （APPRVALIDCOND） | N4_INDICATION | 本端规划     | “N4_INDICATION”：APP所有动态规则需要根据PDR携带的Application ID生效。“N4_UNRELATED”：APP动态规则不根据PDR携带的Application ID生效，不论N4接口是否下发Application ID，均进行APP动态规则匹配。                                                              |
| SET GLBAPPPARA | 通用应用标识（GENERALAPPID）      | huaweiapp     | 本端规划     | 全局Application ID，该参数用于和SMF下发的PDR中携带的Application ID进行匹配。 如果PDR中Application ID优先匹配上“GENERALAPPID”，则所有动态规则在后续流匹配中均生效。如果PDR中Application ID未匹配上“GENERALAPPID”，但匹配上某一动态规则中对应的Application ID，则后续流匹配仅对某一动态规则生效。 |
| SET APNAPPPARA | APN（APN）                  | apn1          | 已配置数据中获取 | 已通过ADD APN命令配置。                                                                                                                                                                                         |
| SET APNAPPPARA | App规则生效条件（APPRVALIDCOND）  | N4_INDICATION | 本端规划     | 配置APN的APP动态规则匹配条件。 “INHERIT”：继承全局配置。表明该生效条件是继承SET GLBAPPPARA命令中参数“APPRVALIDCOND”的取值范围。“N4_INDICATION”：根据N4接口下发的Application ID作为APP规则的匹配条件。“N4_UNRELATED”：不论N4接口是否下发Application ID，均进行APP规则匹配。           |

## 操作步骤

1. **可选**：配置全局的APP动态分流规则匹配条件。

   **SET GLBAPPPARA**
2. **可选**：配置DNN级的APP动态分流规则匹配条件。

   **SET APNAPPPARA**

## 任务示例

任务描述

任务一：配置全局的APP动态分流规则匹配条件，添加全局Application ID，UPF收到SMF下发的PDR，优先匹配该Application ID，所有动态规则支持后续的数据流匹配。

任务二：配置DNN级的APP动态分流规则匹配条件。

脚本

//任务一：配置全局的APP动态分流规则匹配条件，添加全局Application ID，UPF收到SMF下发的PDR，优先匹配该Application ID，所有动态规则支持后续的数据流匹配。

```
SET GLBAPPPARA: APPRVALIDCOND=N4_INDICATION,GENERALAPPID="huaweiapp";
```

//任务二：配置DNN级的APP动态分流规则匹配条件，指定DNN的用户访问APP时，根据N4接口下发的Application ID作为APP动态规则的匹配条件。

```
SET APNAPPPARA: APN="apn1",APPRVALIDCOND=N4_INDICATION;
```