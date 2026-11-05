# 显示APP内存信息（DSP MEMINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示APP内存信息。

#### 注意事项

该命令仅用于研发问题定位。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                                                                      |
|:----------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| DBID            | 数据库ID  | 可选必选说明：可选参数 参数含义：数据库ID。 数据来源：本端规划 取值范围：整数类型，取值范围为0～100。 默认值：无                                                                                             |
| LOCINDEX1       | 进程ID   | 可选必选说明：必选参数 参数含义：进程ID（当在VNFP服务实例上执行该命令时，该参数通过DSP RESPROCESSINFO命令获取，其他服务实例上执行该命令时，该参数通过DSP PROCESSINFO命令获取）。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967295。 默认值：无 |
| DEBUGTYPE       | 调试类型   | 可选必选说明：可选参数 参数含义：调试类型。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：46                                                                                      |
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。                                              |

#### 使用实例

显示APP内存信息：

```
DSP MEMINFO:LOCINDEX1=3,SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功

结果如下:
----------
查询结果  
     
2015-11-26 22:40:28, Memory of config-data <rundata_0>(4) is 5822352 Byte
The memory usage statistics of config-data:
   Schema size of config-data:         1791024 Byte
   Total record data size:             2939813 Byte
   Total index data size:              1045408 Byte
   Miscellaneous size of config-data:  46107 Byte
The memory allocated for common resources of config-data component:
   Memory allocated for config-data resources: 1568086 Byte
   Transaction statistics information:
      Initial transaction count:               3
      Total transactions currently allocated:  3
      Number of transactions in used state:    0
      Number of transactions in free state:    3

--------------------------------------------------------------------------------
Table_Name       Table_Id         Using(Byte)
--------------------------------------------------------------------------------
sysindexbook     0x0              34897     
sysindexmng      0x1              76093    
(结果个数 = 2)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释   |
|:--------|:--------|
| 查询结果    | 结果信息。   |