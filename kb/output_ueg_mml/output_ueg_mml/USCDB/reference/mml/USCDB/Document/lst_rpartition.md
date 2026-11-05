# 查询远端Partition信息(LST RPARTITION)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询USCDB网元内配置的远端Partition信息。

- 若需要查询全部的远端Partition概要信息，请不要输入任何参数值。
- 若需要查询某条远端Partition的详细信息，请输入“远端Partition标识”参数或者其他参数或者这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识         | 参数名称          | 参数说明                                          |
|:-------------|:--------------|:----------------------------------------------|
| RPARTITIONID | 远端Partition标识 | 用于指示系统需要按照哪个远端Partition标识来查询远端Partition的配置信息。 |
| RLOCID       | 远端Location标识  | 用于指示系统需要按照哪个远端Location标识来查询远端Partition的配置信息。  |
| RROLE        | 远端Partition角色 | 用于指示系统需要按照哪个远端Partition角色来查询远端Partition的配置信息。 |
| DESCRIPTION  | 描述            | 用于指示系统需要按照哪个远端Partition描述来查询远端Partition的配置信息。 |

## 使用实例

1. 查询USCDB网元内配置的所有远端Partition信息：

   ```
   LST RPARTITION:;
   ```

   ```
   %%LST RPARTITION:;%% 
   RETCODE = 0  操作成功  

   操作结果如下 
   ------------  
   远端Partition标识  远端Location标识  远端Partition角色 远端BE网元类型  描述     
   5                  83                服务              UDB            NULL    
   101                82                云版本服务        UDR            NULL   
   (结果个数 = 2)  
   ---    END
   ```
2. 查询USCDB网元内，配置的Partition角色为vService的远端Partition信息：

   ```
   LST RPARTITION: RROLE=vService;
   ```

   ```
   %%LST RPARTITION: RROLE=vService;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   远端Partition标识  =  101
    远端Location标识  =  82
   远端Partition角色  =  云版本服务
       远端BE网元类型 =  UDR
                描述  =  NULL
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD RPARTITION**命令的参数说明。