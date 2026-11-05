# 查询隔离状态(LST SEGSTATE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于在配置数据库中查询DRU或DSU业务进程的隔离状态。

- 若需要查询全部DRU和DSU业务模块的隔离状态，请不要输入任何参数。
- 若需要查询所有模块中符合某一参数条件的模块时，请在对应参数中输入对应的参数值。
- 若需要查询所有模块中符合多个参数条件的模块时，请在对应的多个参数中输入对应的参数值。如：需要查询模块类型为DRU且属于Pod“USCDB\_LHS\_101\_HSSRSU\_VDU1\_0”的模块时，请在参数“模块类型”中选择对应的参数值“DRU(DRU)”，参数“Pod名称”中选择对应值“USCDB\_LHS\_101\_HSSRSU\_VDU1\_0”。

  **说明** 

  USCDB\_LHS\_101\_HSSRSU\_VDU1\_0为一个举例的名称，请根据实际的查询情况选择对应的Pod名称。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称      | 参数说明                                                  |
|:-------|:----------|:------------------------------------------------------|
| CID    | Cluster标识 | 用于指示系统需要按照哪个Cluster标识来查询模块的隔离信息；若不输入，则表示所有的Cluster标识。 |
| MID    | 模块号       | 用于指示系统需要按照哪个模块号来查询模块的隔离信息；若不输入，则表示所有的模块号。             |
| MDTYPE | 模块类型      | 用于指示系统需要按照哪个模块类型来查询模块的隔离信息；若不输入，则表示所有的模块类型。           |
| VMNAME | Pod名称     | 用于指示系统需要按照哪个Pod名称来查询模块的隔离信息；若不输入，则表示所有的Pod名称。         |

## 使用实例

1. 以单一参数为条件进行查询。例如：查询“Cluster标识”为“1027”的模块隔离信息。命令执行如下：

   ```
   LST SEGSTATE: CID=1027;
   ```

   ```
   %%LST SEGSTATE: CID=1027;%%
   RETCODE = 0  操作成功

   查询结果如下
   ----------

    Cluster标识  模块号  模块类型  隔离类型  隔离状态  隔离启动时间  Pod名称                 

    1027         1027    DRU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0
    1027         1028    DRU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0

   (结果个数 = 2)

   ---    END
   ```
2. 以多个参数为条件进行组合查询。例如：查询“模块类型”为“DSU”，且“Pod名称”为“USCDB\_LHS\_101\_HSSRSU\_VDU1\_0”的模块隔离信息。

   ```
   LST SEGSTATE: MDTYPE=DSU, VMNAME="USCDB_LHS_101_HSSRSU_VDU1_0";
   ```

   ```
   %%LST SEGSTATE: MDTYPE=DSU, VMNAME="USCDB_LHS_101_HSSRSU_VDU1_0";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    Cluster标识  模块号  模块类型  隔离类型  隔离状态  隔离启动时间  Pod名称                 

    1033         1033    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0
    1035         1035    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0
    1037         1037    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0
    1039         1039    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0
    1041         1041    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0
    1043         1043    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0
    1045         1045    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0
   (结果个数 = 7)

   ---    END
   ```
3. 显示所有业务模块的隔离状态，命令执行如下：

   ```
   LST SEGSTATE;
   ```

   ```
   %%LST SEGSTATE;%%
   RETCODE = 0  操作成功

   操作结果如下 
   ------------  
   Cluster标识  模块号  模块类型  隔离类型  隔离状态  隔离启动时间  Pod名称                    
   1            1025    DRU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0  
   1            1026    DRU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0  
   1027         1027    DRU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0  
   1027         1028    DRU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0  
   1029         1029    DRU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0  
   1029         1030    DRU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0  
   1031         1031    DRU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0  
   1031         1032    DRU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0  
   1033         1033    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0  
   1033         1034    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0  
   1035         1035    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0  
   1035         1036    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0  
   1037         1037    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0  
   1037         1038    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0  
   1039         1039    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0  
   1039         1040    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0  
   1041         1041    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0  
   1041         1042    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0  
   1043         1043    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0  
   1043         1044    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0  
   1045         1045    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU1_0  
   1045         1046    DSU       故障隔离  非隔离    NULL          USCDB_LHS_101_HSSRSU_VDU2_0 
   (结果个数 = 22) 

    ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释   | 原因分析             | 处理建议                                    |
|-------:|:--------|:-----------------|:----------------------------------------|
| 260046 | 该模块不存在。 | “模块号”参数指定的模块不存在。 | 使用LST MODULE命令查询后，重新输入类型为DRU或DSU的“模块号”。 |