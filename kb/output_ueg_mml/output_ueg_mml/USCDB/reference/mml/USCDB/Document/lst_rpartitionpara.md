# 查询远端Partition的配置信息(LST RPARTITIONPARA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询远端分区参数的配置。

- 若需要查询所有远端分区的参数信息，请不要输入任何参数。
- 若需要查询某个远端分区的详细参数信息，请输入对应的参数。

## 注意事项

无。

## 参数说明

| 参数标识         | 参数名称          | 参数说明                                                                  |
|:-------------|:--------------|:----------------------------------------------------------------------|
| PARANAME     | 参数名称          | 用于指示系统需要按照哪个参数名称来查询远端分区参数配置信息。                                        |
| PARAVALUE    | 参数值           | 用于指示系统需要按照哪个参数值来查询远端分区参数配置信息。                                         |
| RPARTITIONID | 远端Partition标识 | 用于指示系统需要按照哪个远端Partition标识来查询远端分区参数配置信息。若不输入则查询所有远端Partition的远端分区参数信息。 |
| SERVICETYPE  | 业务类型          | 用于指示系统需要按照哪种应用类型来查询远端分区参数配置信息。若不输入则查询所有业务类型的远端分区参数信息。                 |

## 使用实例

1. 查询所有远端分区参数。

   ```
   LST RPARTITIONPARA:;
   ```

   ```
   %%LST RPARTITIONPARA:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    参数名称        参数值  远端Partition标识  业务类型  

    分区间状态开关  1        8                  SUP-FE     
    分区间状态开关  1        8                  USCDB 
    分区间校验模式  0        8                  SUP-FE     
    分区间校验模式  0        8                  USCDB

   (结果个数 = 4)

   ---    END
   ```
2. 查询指定Partition“业务类型”为“SUP-FE”的分区间状态开关状态。

   ```
   LST RPARTITIONPARA: PARANAME=INTERPARTSTATUS, RPARTITIONID=8, SERVICETYPE="SUP-FE";
   ```

   ```
   %%LST RPARTITIONPARA: PARANAME=INTERPARTSTATUS, RPARTITIONID=8, SERVICETYPE="SUP-FE";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
            参数名称  =  分区间状态开关
              参数值  =  0
   远端Partition标识  =  8
            业务类型  =  SUP-FE
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

各输出项含义请参见**SET RPARTITIONPARA**的参数说明。