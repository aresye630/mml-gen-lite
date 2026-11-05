# 设置CPU睿频开关（SET CPUGENTURBO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

如果配置不合理会导致权重计算产生偏差。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于设置不同CPU代际的睿频开关。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CPUGENERATION   | TURBOSWITCH   |
|:----------------|:--------------|
| Icelake         | -             |
| Skylake         | -             |
| Broadwell       | -             |
| Haswell         | -             |
| CascadeLake     | -             |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                                                                                     |
|:--------------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPUGENERATION | CPU代际类型 | 可选必选说明：必选参数  参数含义：该参数用于指定CPU代际类型。  数据来源：本端规划 取值范围： Icelake（Icelake代际）Skylake（kylake代际）Broadwell（Broadwell代际）Haswell（Haswell代际）CascadeLake（CascadeLake代际）  默认值：无。  配置原则：无 |
| TURBOSWITCH   | 睿频开关    | 可选必选说明：必选参数  参数含义：该参数用于设置睿频的开关。  数据来源：本端规划 取值范围： OFF（OFF）ON（ON）  默认值：无。  配置原则：无                                                                                          |

## 使用实例

查询CPU代际类型为Icelake的代际开关：

```
SET CPUGENTURBO:CPUGENERATION=Icelake,TURBOSWITCH=ON;
```