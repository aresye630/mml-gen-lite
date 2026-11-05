# 设置TCP优化策略组合优先级（SET TOPLYPRIORITY）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于设置TCP优化策略组合优先级。当运营商希望修改当前TCP优化策略组合优先级时，则配置该命令。

#### 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为7。
- 不同配置类型的优先级建议设置为不同值。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | COMBTYPE           |   PRIORITY |
|:-------|:-------------------|-----------:|
| 初始值    | TO_MATCH_IMSI      |         10 |
| 初始值    | TO_MATCH_CELL      |         20 |
| 初始值    | TO_MATCH_RAT       |         30 |
| 初始值    | TO_MATCH_RAT_IMSI  |         40 |
| 初始值    | TO_MATCH_CELL_IMSI |         50 |
| 初始值    | TO_MATCH_RAT_CELL  |         60 |
| 初始值    | TO_MATCH_ALL       |         70 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识     | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                                                                      |
|:---------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| COMBTYPE | TCP优化策略组合类型 | 可选必选说明：可选参数 参数含义：用于指定TCP优化策略组合类型。 数据来源：本端规划 取值范围：枚举类型。 TO_MATCH_IMSI：仅匹配IMSIGroupName。TO_MATCH_CELL：仅匹配CellGroupName。TO_MATCH_RAT：仅匹配RATtype。TO_MATCH_RAT_IMSI：仅匹配RATtype和IMSIGroupName。TO_MATCH_CELL_IMSI：仅匹配CellGroupName和IMSIGroupName。TO_MATCH_RAT_CELL：仅匹配RATtype和CellGroupName。TO_MATCH_ALL：RATtype，CellGroupName和IMSIGroupName均需要匹配中。 默认值：无 配置原则：无 |
| PRIORITY | 优先级         | 可选必选说明：可选参数 参数含义：用于设置指定TCP优化策略组合优先级。 数据来源：本端规划 取值范围：整数类型，取值范围1～255，数值越大优先级越高。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                |

#### 使用实例

运营商需要设置TCP优化策略组合为RATtype和IMSIGroupName的优先级为100：

```
SET TOPLYPRIORITY: COMBTYPE=TO_MATCH_RAT_IMSI,PRIORITY =100;
```