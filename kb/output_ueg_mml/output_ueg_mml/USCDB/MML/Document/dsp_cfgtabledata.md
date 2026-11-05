# 显示满足条件的CFG表数据（DSP CFGTABLEDATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示满足条件的CFG表数据。

#### 注意事项

该命令仅用于研发问题定位。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                                                                                        |
|:----------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OMUTYPE         | OMU类型  | 可选必选说明：必选参数 参数含义：主备OMU类型。 数据来源：本端规划 取值范围：枚举类型。 master：主主控。slave：备主控。 默认值：无                                                                                                  |
| DBTYPE          | 数据库类型  | 可选必选说明：必选参数 参数含义：数据库类型，包括master，candidate，running等。 数据来源：本端规划 取值范围：枚举类型。 master：master数据。candidate：预提交的数据。running：运行的数据。cfg：CFG数据。paf：PAF数据。base：base数据。dynamic：动态数据。 默认值：无 |
| QUERYTYPE       | 查询类型   | 可选必选说明：必选参数 参数含义：查询类型，可以查询Table内容，或者查询Table清单等。 数据来源：本端规划 取值范围：枚举类型。 table-data：表的数据。table-list：数据表列表。table-field：表的字段。table-index：表的索引。mem-info：数据表内存信息。 默认值：table-data    |
| TABLENAME       | 表名称    | 可选必选说明：条件必选参数，该参数在“QUERYTYPE”配置为“table-data”、“table-field” 或 “table-index”时为必选参数。 参数含义：数据库表名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。 默认值：无                                       |
| INDEX           | 起始索引   | 可选必选说明：条件可选参数，该参数在“QUERYTYPE”配置为“table-data”时为可选参数。 参数含义：起始索引值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                                                                |
| NUM             | 查询记录数  | 可选必选说明：条件可选参数，该参数在“QUERYTYPE”配置为“table-data”时为可选参数。 参数含义：查询得到的记录数。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967295。 默认值：无                                                             |
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。                                                                |

#### 使用实例

显示满足条件的CFG表数据：

```
DSP CFGTABLEDATA:OMUTYPE=master,DBTYPE=cfg,QUERYTYPE=table-list,SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功

结果如下:
---------
查询结果    
Field(0)        Field(1)        Field(2)        Field(3)        Field(4)        Field(5)        Field(6)        
Table_Name      Table_Id        MaxRecNum       ActRecNum       RecLength       FieldNum        IndexNum
        
StpTBL          0x0             0x1000          0x2             0x94            0x6             0x1             

(结果个数 = 2)

---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释   |
|:--------|:--------|
| 查询结果    | 结果信息。   |