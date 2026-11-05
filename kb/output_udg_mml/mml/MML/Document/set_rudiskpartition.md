# 设置RU磁盘过载配置（SET RUDISKPARTITION）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用来设置不同RU类型的磁盘分区过载阈值。

当RU磁盘分区使用率超过阈值时，会触发“ALM-221257761 资源单元磁盘分区使用率超阈值”。

#### 注意事项

- 该命令执行后立即生效。
- 系统中支持的磁盘分区以网元部署的实际情况为准。
- “ALM-221257761 资源单元磁盘分区使用率超阈值”告警上报阈值缺省值为50，空间不足告警恢复阈值缺省值为100。
- root分区使用率过载重要级别告警上报阈值缺省值为95，告警恢复阈值缺省值为85。
- 该命令存在系统初始记录，参数的初始设置值如下表：

|   PARTITIONUNOVLIMITMIN |   PARTITIONOVLIMITMIN |   PARTITIONUNOVLIMIT |   PARTITIONOVLIMIT |   PARTITIONUNOVLIMITCRI |   PARTITIONOVLIMITCRI |   PARTITIONDETWINDOW |   PARTITIONCAPOVLIMIT |   PARTITIONCAPUNOVLIMIT |
|------------------------:|----------------------:|---------------------:|-------------------:|------------------------:|----------------------:|---------------------:|----------------------:|------------------------:|
|                       0 |                     0 |                   85 |                 95 |                       0 |                     0 |                   12 |                    50 |                     100 |

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识                  | 参数名称                 | 参数说明                                                                                                                                                                                                                                                                                                                                                         |
|:----------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RUTYPE                | RU类型                 | 可选必选说明：必选参数 参数含义：该参数用于指定RU类型。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则：请使用LST RESINSTANCETYPE命令查询存在的资源单元类型。                                                                                                                                                                                                                                  |
| PARTITIONNAME         | 磁盘分区名称               | 可选必选说明：必选参数 参数含义：该参数用于设置要配置的磁盘分区。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则：请使用LST RUDISKPARTITION命令查询存在的磁盘分区名称。                                                                                                                                                                                                                              |
| PARTITIONUNOVLIMITMIN | 分区使用率过载次要级别告警恢复阈值（%） | 可选必选说明：可选参数 参数含义：该参数用于设置分区使用率过载次要级别告警恢复阈值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～100。 默认值：无 配置原则： 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。参数非0时，要满足PARTITIONUNOVLIMITMIN < PARTITIONOVLIMITMIN < PARTITIONUNOVLIMIT< PARTITIONOVLIMIT < PARTITIONUNOVLIMITCRI < PARTITIONOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。        |
| PARTITIONOVLIMITMIN   | 分区使用率过载次要级别告警上报阈值（%） | 可选必选说明：可选参数 参数含义：该参数用于设置分区使用率过载次要级别告警上报阈值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～100。 默认值：无 配置原则： 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。参数非0时，要满足PARTITIONUNOVLIMITMIN < PARTITIONOVLIMITMIN < PARTITIONUNOVLIMIT< PARTITIONOVLIMIT < PARTITIONUNOVLIMITCRI < PARTITIONOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。        |
| PARTITIONUNOVLIMIT    | 分区使用率过载重要级别告警恢复阈值（%） | 可选必选说明：可选参数 参数含义：该参数用于设置分区使用率过载重要级别告警恢复阈值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～100。 默认值：无 配置原则： 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。参数非0时，要满足PARTITIONUNOVLIMITMIN < PARTITIONOVLIMITMIN < PARTITIONUNOVLIMIT< PARTITIONOVLIMIT < PARTITIONUNOVLIMITCRI < PARTITIONOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。        |
| PARTITIONOVLIMIT      | 分区使用率过载重要级别告警上报阈值（%） | 可选必选说明：可选参数 参数含义：该参数用于设置分区使用率过载重要级别告警上报阈值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～100，单位是百分比。 默认值：无 配置原则： 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。参数非0时，要满足PARTITIONUNOVLIMITMIN < PARTITIONOVLIMITMIN < PARTITIONUNOVLIMIT< PARTITIONOVLIMIT < PARTITIONUNOVLIMITCRI < PARTITIONOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。 |
| PARTITIONUNOVLIMITCRI | 分区使用率过载紧急级别告警恢复阈值（%） | 可选必选说明：可选参数 参数含义：该参数用于设置分区使用率过载紧急级别告警恢复阈值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～100。 默认值：无 配置原则： 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。参数非0时，要满足PARTITIONUNOVLIMITMIN < PARTITIONOVLIMITMIN < PARTITIONUNOVLIMIT< PARTITIONOVLIMIT < PARTITIONUNOVLIMITCRI < PARTITIONOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。        |
| PARTITIONOVLIMITCRI   | 分区使用率过载紧急级别告警上报阈值（%） | 可选必选说明：可选参数 参数含义：该参数用于设置分区使用率过载紧急级别告警上报阈值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～100。 默认值：无 配置原则： 参数配置为0时，表示不支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为0。参数配置为非0时，表示支持该级别的告警，同一级别的过载恢复阈值和过载上报阈值需要同时配置为非0。参数非0时，要满足PARTITIONUNOVLIMITMIN < PARTITIONOVLIMITMIN < PARTITIONUNOVLIMIT< PARTITIONOVLIMIT < PARTITIONUNOVLIMITCRI < PARTITIONOVLIMITCRI，当字段的阈值为零时，则该字段将不参与比较。        |
| PARTITIONDETWINDOW    | 分区使用率过载告警的采样窗口       | 可选必选说明：可选参数 参数含义：该参数用于设置分区使用率过载告警的采样窗口。当使用率大于过载阈值的连续次数不小于该采样窗口，将上报相应等级的告警。 数据来源：本端规划 取值范围：整数类型，取值范围为1～36。 默认值：无                                                                                                                                                                                                                                              |
| PARTITIONCAPOVLIMIT   | 分区空间不足告警上报阈值（MB）     | 可选必选说明：可选参数 参数含义：该参数用于设置分区空间不足告警上报阈值。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967295。 默认值：无 配置原则：参数需满足PARTITIONCAPOVLIMIT<PARTITIONCAPUNOVLIMIT。                                                                                                                                                                                                                      |
| PARTITIONCAPUNOVLIMIT | 分区空间不足告警恢复阈值（MB）     | 可选必选说明：可选参数 参数含义：该参数用于设置分区空间不足告警恢复阈值。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967295。 默认值：无 配置原则：参数需满足PARTITIONCAPOVLIMIT<PARTITIONCAPUNOVLIMIT。                                                                                                                                                                                                                      |
| SERVICEINSTANCE       | 服务实例                 | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。                                                                                                                                                                                                                                  |

#### 使用实例

- 将VNODE\_CSLB\_VNFC\_OMU类型的root分区的分区使用率过载次要级别告警恢复阈值设置为70，分区使用率过载次要级别告警上报阈值设置为75，分区使用率过载重要级别告警恢复阈值设置为80，分区使用率过载重要级别告警上报阈值设置为85，分区使用率过载紧急级别告警恢复阈值设置为90，分区使用率过载紧急级别告警上报阈值设置为95：

  ```
  SET RUDISKPARTITION:RUTYPE="VNODE_CSLB_VNFC_OMU",PARTITIONNAME="root",PARTITIONUNOVLIMITMIN=70,PARTITIONOVLIMITMIN=75,PARTITIONUNOVLIMIT=80,PARTITIONOVLIMIT=85,PARTITIONUNOVLIMITCRI=90,PARTITIONOVLIMITCRI=95,SERVICEINSTANCE="vnfc";
  ```
- 将VNODE\_CSLB\_VNFC\_OMU类型的root分区的分区使用率过载告警的采样窗口设置为12：

  ```
  SET RUDISKPARTITION:RUTYPE="VNODE_CSLB_VNFC_OMU",PARTITIONNAME="root",PARTITIONDETWINDOW=12,SERVICEINSTANCE="vnfc";
  ```
- 将VNODE\_CSLB\_VNFC\_OMU类型的root分区的分区空间不足上报阈值设置为60，分区空间不足恢复阈值设置为120：

  ```
  SET RUDISKPARTITION:RUTYPE="VNODE_CSLB_VNFC_OMU",PARTITIONNAME="root",PARTITIONCAPOVLIMIT=60,PARTITIONCAPUNOVLIMIT=120,SERVICEINSTANCE="vnfc";
  ```