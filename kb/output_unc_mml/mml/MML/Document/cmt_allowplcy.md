# 提交允许访问策略配置（CMT ALLOWPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

该命令会将之前通过ADD ALLOWEDPLMNS/RMV ALLOWEDPLMNS/ADD ALLOWEDNSSAIS/RMV ALLOWEDNSSAIS/ADD ALLOWEDNFTYPES/RMV ALLOWEDNFTYPES/ADD ALLOWEDDOMAINS/RMV ALLOWEDDOMAINS配置的所有访问授权控制策略提交并生效。

**适用NF：NRF**

该命令用于提交配置的访问授权控制策略。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                             |
|:--------|:-------|:---------------------------------------------------------------------------------|
| CMTTYPE | 提交类型   | 可选必选说明：可选参数  参数含义：该参数表示访问授权控制策略提交的范围。  数据来源：本端规划 取值范围： ALL（ALL）  默认值：ALL  配置原则：无 |

## 使用实例

提交所有访问授权控制策略配置信息。

```
CMT ALLOWPLCY: CMTTYPE=ALL;
```