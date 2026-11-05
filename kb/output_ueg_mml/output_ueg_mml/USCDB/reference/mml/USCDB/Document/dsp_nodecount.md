# 查看节点的主表记录数(DSP NODECOUNT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

该命令用于查询各模块主键表记录数：

- 若要查询全部模块的主键表记录数，请不要输入任何参数。
- 若要查询某个模块的主键表记录数，请输入“节点标识”或其他参数，或者“节点标识”和其他参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                              |
|:------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------|
| CID         | Cluster标识 | 可选必选说明：可选参数。 参数含义：用于指示系统是按照哪个Cluster标识来查询主键表记录数；若不输入，则表示所有的Cluster标识。 取值范围：1～4096 默认值：无。 配置原则：无。                                  |
| NID         | 节点标识      | 可选必选说明：可选参数。 参数含义：用于指示系统是按照哪个节点标识来查询主键表记录数；若不输入，则表示所有的节点标识。 取值范围：1～32768 默认值：无。 配置原则：无。                                           |
| SERVICETYPE | 业务类型      | 可选必选说明：可选参数。 参数含义：用于指示系统是按照哪个业务类型来查询主键表记录数；若不输入，则表示所有的业务类型。 取值范围：长度不超过128的字符串。 默认值：无。 配置原则：无。                                     |
| DATATYPE    | 数据类型      | 可选必选说明：可选参数。 参数含义：用于指示系统是按照哪个数据类型来查询主键表记录数；若不输入，则表示所有的数据类型。 取值范围： GLOBAL_DATA(全局数据)ROUTE_DATA(路由数据)USER_DATA(用户数据) 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有模块的主键表记录数：

   ```
   DSP NODECOUNT:;
   ```

   ```
   %%DSP NODECOUNT:;%%
   RETCODE = 0  操作成功
   操作结果如下
   ------------
   业务类型  Cluster标识  节点标识  主表表名                     记录数
   USCDB     1            1060      TRAFFICPOLICY_OVERLOAD_STAT  7                  
   USCDB     1            1060      PGW_SYSTEM_HLR               2                  
   USCDB     1            1060      PGW_OPR_USER                 1                  
   USCDB     1            1060      PGW_OPR_PWDHISTORY           0                  
   USCDB     1            1060      PGW_OPR_CMDGROUP             8                  
   USCDB     1            1060      PGW_VHLR_RANGE_IMSI          1                  
   USCDB     1            1060      PGW_VHLR_RANGE_ISDN          1                  
   USCDB     1            1060      PGW_OPR_SECPOLICY            1                  
   USCDB     1            1060      PGW_OPR_VHLR                 0                  
   USCDB     1            1060      PGW_BATCHJOB_SUMMARY         5                  
   USCDB     1            1060      PGW_BATCH_JOB_ON_SCHEDULE    0                  
   USCDB     1            1060      PGW_HLR_DATA                 1                  
   USCDB     1            1060      PGW_OPR_APPTYPE_CMDGROUP     8                  
   USCDB     1            1060      PGW_GLOBALDATA_STATUSINFO    23                 
   USCDB     1            1060      PGW_VHLR_RANGE_IMEI          0                  
   USCDB     1            1060      PGW_CONBATCHJOB_SUMMARY      1                  
   USCDB     1            1060      DSMETASUBCAPCTRL             0                  
   USCDB     1            1060      PGW_EQUIPMENT_LICENCE_DATA   0                  
   USCDB     1            1060      PGW_RUNTIME                  0                  
   USCDB     1            1060      PGW_EXPTASK_SUMMARY          1                  
   USCDB     1            1060      PGW_EXPLOGTASK_SUMMARY       0                  
   USCDB     1            1060      PGW_SOAP_REPORT_PARA         0                  
   USCDB     1            1060      PGW_EXPTASK_TEMPLATE         0                  
   USCDB     1            1060      PGW_BKPDB_SUMMARY            10                 
   USCDB     1            1060      PGW_INVALID_USER             0 
   (结果个数 = 25)

   共有20个报告
   ---    END
   ```
2. 查询“Cluster标识”为“1101”、“节点标识”为“1101”、“业务类型”为“SUP-FE”、“数据类型”为“USER\_DATA”的主键表记录数：

   ```
   DSP NODECOUNT: CID=1101, NID=1101, SERVICETYPE="SUP-FE", DATATYPE=USER_DATA;
   ```

   ```
   %%DSP NODECOUNT: CID=1101, NID=1101, SERVICETYPE="SUP-FE", DATATYPE=USER_DATA;%%
   RETCODE = 0  操作成功
   操作结果如下
   ------------
   业务类型  Cluster标识  节点标识  主表表名             记录数
   SUP-FE    1101         1101      SUID_DATA            0
   SUP-FE    1101         1101      INT4SUID2_DATA       0
   SUP-FE    1101         1101      STRSUID_DATA         0                  
   SUP-FE    1101         1101      INT8SUID_DATA        0
   SUP-FE    1101         1101      INT4SUID_DATA        0                  
   SUP-FE    1101         1101      PREFIX_STRSUID_DATA  0                  
   SUP-FE    1101         1101      SUID_CUTTYPE_DATA    0                  
   SUP-FE    1101         1101      TBL_IMSI             0   
   (结果个数 = 8)
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见表1中的参数说明。

| 输出项名称     | 输出项解释                        |
|:----------|:-----------------------------|
| 业务类型      | 用于表示节点的业务类型。                 |
| Cluster标识 | 用于表示节点所属的Cluster标识。          |
| 节点标识      | 用于表示节点的节点标识，此参数在Location内唯一。 |
| 主表表名      | 用于表示节点中主键数据表的名称。             |
| 记录数       | 用于表示节点中主键数据表的记录数。            |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|   错误码 | 错误码解释                           | 原因分析                                 | 处理建议                                                      |
|------:|:--------------------------------|:-------------------------------------|:----------------------------------------------------------|
|  1788 | 参数NID指定的节点在参数CID指定的cluster中不存在。 | 输入的“节点标识”在“Cluster标识”指定的Cluster中不存在。 | 执行LST NODE命令查询与该Cluster标识对应的“节点标识”并正确设置，然后重新执行本命令。        |
|  1789 | 参数NID指定的节点不存在。                  | 输入的“节点标识”在系统中不存在。                    | 执行LST NODE命令查询系统中存在的“节点标识”并正确设置，然后重新执行本命令                 |
|  2037 | 参数业务类型和Cluster标识指定的Cluster不存在。  | 输入的“Cluster标识”与输入的“业务类型”不匹配。         | 执行LST CLUSTER命令查询与该Cluster标识对应的“业务类型”并正确设置，然后重新执行本命令。     |
|  2039 | 参数业务类型和节点标识指定的节点不存在。            | 输入的“节点标识”与输入的“业务类型”中不匹配。             | 执行LST NODE命令查询与该节点标识对应的“业务类型”并正确设置，然后重新执行本命令。             |
|  2059 | 指定的业务类型不存在。                     | 输入的“业务类型”在系统中不存在。                    | 执行LST FEPLUG命令查询已加载的“FE类型名称”并正确设置“业务类型”，然后重新执行本命令。        |
|  2134 | 指定Cluster不存在。                   | 输入的“Cluster标识”在系统中不存在。               | 执行LST CLUSTER命令查询系统中存在的“Cluster标识”并正确设置，然后重新执行本命令。        |
|  2744 | 参数数据类型和Cluster标识指定的Cluster不存在。  | 输入的“数据类型”与输入的“Cluster标识”不匹配。         | 执行LST CLUSTER命令查询与该数据类型对应的“Cluster标识”并正确设置，然后重新执行本命令。     |
|  2745 | 参数数据类型和节点标识指定的节点不存在。            | 输入的“数据类型”与输入的“节点标识”不匹配。              | 执行LST CLUSTER和LST NODE命令查询与该数据类型对应的“节点标识”并正确设置，然后重新执行本命令。 |

## 参考信息

无。