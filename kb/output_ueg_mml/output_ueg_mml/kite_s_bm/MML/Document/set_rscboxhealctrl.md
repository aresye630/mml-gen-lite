# 设置ResourceBox自愈策略控制参数（SET RSCBOXHEALCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于设置ResourceBox自愈策略控制参数。

## 注意事项

- 该命令执行后立即生效。

- 该命令只适用于裸机容器云场景。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RSCALFTNODFTSW   | RSCALFTNODNLSW   | RSCPTFTNODNLSW   |
|:-----------------|:-----------------|:-----------------|
| ENABLE           | ENABLE           | DISABLE          |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                        | 参数说明                                                                                                                                                                                                                                                                                                                                  |
|:---------------|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RSCALFTNODFTSW | ResourceBox全故障Node故障升级自愈控制  | 可选必选说明：可选参数  参数含义：该参数用于表示ResourceBox全部Pod故障、Node故障时，且进行Pod重建无法修复时，是否需要将自愈升级到ResourceBox进行复位、重建处理。  数据来源：本端规划 取值范围： “DISABLE（去使能）”：Resourcebox中所有Pod故障时，并且Node故障时，不作处理。“ENABLE（使能）”：Resourcebox中所有Pod故障时，并且Node故障时，将自愈升级到Resourcebox进行自愈处理。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RSCBOXHEALCTRL查询当前参数配置值。  配置原则：无                  |
| RSCALFTNODNLSW | ResourceBox全故障Node正常升级自愈控制  | 可选必选说明：可选参数  参数含义：该参数用于表示ResourceBox全部Pod故障、Node正常时，且进行Pod重建无法修复时，是否需要将自愈升级到ResourceBox进行复位、重建处理。  数据来源：本端规划 取值范围： “DISABLE（去使能）”：Resource中所有Pod故障，并且Node正常时，不作处理。“ENABLE（使能）”：Resourcebox中所有Pod故障，并且Node正常时，将自愈升级到Resourcebox进行自愈处理。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RSCBOXHEALCTRL查询当前参数配置值。  配置原则：无                       |
| RSCPTFTNODNLSW | ResourceBox部分故障Node正常升级自愈控制 | 可选必选说明：可选参数  参数含义：该参数用于表示ResourceBox中单个Pod或部分Pod故障、Node正常时，且进行Pod重建无法修复时，是否需要将自愈升级到ResourceBox进行复位、重建处理。  数据来源：本端规划 取值范围： “DISABLE（去使能）”：Resourcebox中单个Pod或部分Pod故障，并且Node正常时，不作处理。“ENABLE（使能）”：Resourcebox中单个Pod或部分Pod故障，并且Node正常时，将自愈升级到Resourcebox进行自愈处理。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RSCBOXHEALCTRL查询当前参数配置值。  配置原则：无 |

## 使用实例

去使能ResourceBox全故障NOD故障自愈功能:

```
SET RSCBOXHEALCTRL:RSCALFTNODFTSW=DISABLE;
```