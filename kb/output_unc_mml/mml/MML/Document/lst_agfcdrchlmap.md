# 查询话单通道一级目录映射表配置（LST AGFCDRCHLMAP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NCG**

该命令用于查询OCS NFINSTANCEID与话单通道一级目录映射关系。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识         | 参数名称              | 参数说明                                                                                                                                                                                     |
|:-------------|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSTANCEID | OCS的NFINSTANCEID值 | 可选必选说明：可选参数  参数含义：该参数用于指定OCS的NFINSTANCEID值。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~40。NFINSTANCEID必须来源于PNFPROFILE命令中NFINSTANCEID参数。  默认值：无  配置原则：无                                              |
| FIELDTYPE    | 决定话单通道分拣的字段       | 可选必选说明：可选参数  参数含义：该参数用于指定决定话单分拣的字段。  数据来源：本端规划 取值范围： SUPI_GPSI（SUPI或GPSI）APN（APN）  默认值：无  配置原则：无                                                                                         |
| CDRFIRSTDIR  | 话单通道一级目录名         | 可选必选说明：可选参数  参数含义：该参数用于指定话单一级目录名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~30。当FIELDTYPE取值为SUPI_GPSI时，CDRFIRSTDIR只能填00~31通道名。当FIELDTYPE取值为APN时，CDRFIRSTDIR只能填JASPER、IOT、DEFAULT通道。  默认值：无  配置原则：无 |

## 使用实例

查询FIELDTYPE为SUPI\_GPSI的话单通道一级目录映射关系：

```
%%LST AGFCDRCHLMAP:;%%
RETCODE = 0  Operation succeeded
The result is as follows
------------------------
                                 OCS NFINSTANCEID  =  00000000-0000-0000-c000-000000000046
Fields that determine CDR channel sorting  =  SUPI or GPSI
                         CDR First Directory  =  01
(Number of results = 1)

---    END
```

## 输出结果说明

| 输出项名称             | 输出项解释                     |
|:------------------|:--------------------------|
| OCS的NFINSTANCEID值 | 该参数用于指定OCS的NFINSTANCEID值。 |
| 决定话单通道分拣的字段       | 该参数用于指定决定话单分拣的字段。         |
| 话单通道一级目录名         | 该参数用于指定话单一级目录名。           |