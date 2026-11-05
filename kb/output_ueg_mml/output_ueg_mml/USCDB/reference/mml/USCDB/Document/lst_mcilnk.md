# 查询MCI链路（LST MCILNK）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询MCI链路信息。

- 若要查询全部MCI链路配置信息时，请不要输入任何参数。
- 若要查询指定MCI链路配置信息时，请根据实际情况输入“链路ID”、“链路集ID”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                |
|:-------|:-------|:----------------------------------------------------|
| LNKID  | 链路ID   | 可选必选说明：可选参数 参数含义：本参数用于标识一条MCI链路。 取值范围：1～50。 默认值：无。  |
| LKSID  | 链路集ID  | 可选必选说明：可选参数 参数含义：本参数用于标识一个MCI链路集。 取值范围：1～50。 默认值：无。 |

## 使用实例

1. 查询指定MCI链路的配置，该“链路ID”为“1”。

   ```
   LST MCILNK: LNKID=1;
   ```

   ```
   %%LST MCILNK: LNKID=1;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
          链路ID  =  1
        链路集ID  =  1
          FE类型  =  SUP-FE
    Location标识  =  1
        服务名称  =  PES
   Partition标识  =  2
        链路描述  =  NULL
   (结果个数 = 1)

   ---    END
   ```
2. 查询指定MCI链路集中所有链路的配置，该“链路集ID”为“1”。

   ```
   LST MCILNK: LKSID=1;
   ```

   ```
   %%LST MCILNK: LKSID=1;%%
   RETCODE = 0  Operation succeeded

   操作结果如下
   ------------
    链路ID  链路集ID  FE类型  Location标识  服务名称  Partition标识  链路描述

    1       1         SUP-FE  1             PES       2              NULL            
    2       1         SUP-FE  1             CCU       6              NULL  

   (结果个数 = 2)

   ---    END
   ```
3. 查询所有MCI链路的配置。

   ```
   LST MCILNK:;
   ```

   ```
   %%LST MCILNK:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    链路ID  链路集ID  FE类型  Location标识  服务名称  Partition标识  链路描述

    1       1         SUP-FE  1             PES       2              NULL            
    2       1         SUP-FE  1             CCU       6              NULL  
    3       2         SUP-FE  1             PES       2              NULL            
    4       2         SUP-FE  1             CCU       6              NULL 

   (结果个数 = 4)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD MCILNK**命令的参数说明。