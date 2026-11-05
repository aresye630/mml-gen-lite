# 显示指定DB表数据（DSP CFGCERTAINDB）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示指定DB表数据。

#### 注意事项

该命令仅用于研发问题定位。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                                                                      |
|:----------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| DBID            | 数据库ID  | 可选必选说明：必选参数 参数含义：数据库ID。 数据来源：本端规划 取值范围：整数类型，取值范围为0～100。 默认值：无                                                                                             |
| LOCINDEX1       | 进程ID   | 可选必选说明：必选参数 参数含义：进程ID（当在VNFP服务实例上执行该命令时，该参数通过DSP RESPROCESSINFO命令获取，其他服务实例上执行该命令时，该参数通过DSP PROCESSINFO命令获取）。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967295。 默认值：无 |
| QUERYTYPE       | 查询类型   | 可选必选说明：必选参数 参数含义：查询类型，可以查询Table内容，或者查询Table清单等。 数据来源：本端规划 取值范围：枚举类型。 table-data：表的数据。table-list：数据表列表。table-field：表的字段。table-index：表的索引。 默认值：无            |
| TABLENAME       | 表名称    | 可选必选说明：条件必选参数，该参数在“QUERYTYPE”配置为“table-data”、“table-index” 或 “table-field”时为必选参数。 参数含义：数据库表名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。 默认值：无                     |
| INDEX           | 起始索引   | 可选必选说明：条件可选参数，该参数在“QUERYTYPE”配置为“table-data”时为可选参数。 参数含义：起始索引值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                                              |
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。                                              |

#### 使用实例

显示指定DB表数据：

```
DSP CFGCERTAINDB:DBID=4,LOCINDEX1=3,QUERYTYPE=table-list,SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功

结果如下:
----------
查询结果
Field(0)        Field(1)        Field(2)        Field(3)        Field(4)        Field(5)        Field(6)        
Table_Name      Table_Id        MaxRecNum       ActRecNum       RecLength       FieldNum        IndexNum        
sysindexbook    0x0             0x780000        0x0             0x1c            0xa             0x1             
sysindexmng     0x1             0xffffff        0x87f           0x16            0x8             0x1             
indexsection    0x2             0xffffff        0x9ce           0x15            0x7             0x2             
_CountingTable_ 0x5             0x300000        0x53            0x10            0x5             0x1             
ByteOrder       0xf             0x20000         0xbf            0x28            0xb             0x3             
TrillSite       0x10            0x107f          0x0             0x10c           0x23            0x2             
TrillNickname   0x12            0x100f          0x0             0x21            0xb             0x2             

(结果个数 = 1)

--- END
```

#### 输出结果说明

| 输出项名称   | 输出项解释   |
|:--------|:--------|
| 查询结果    | 结果信息。   |