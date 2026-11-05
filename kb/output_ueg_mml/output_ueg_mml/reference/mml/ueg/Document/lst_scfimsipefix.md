# 查询IMSI号段信息(LST SCFIMSIPEFIX)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在IMSI号段组中查询已配置的IMSI号段信息：

- 若需要查询全部IMSI号段的配置信息，请不要输入任何参数。
- 若需要查询某些IMSI号段的配置信息，请输入“IMSI号段组名称”参数或“IMSI号段”参数或这两个参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称      | 参数说明                                                 |
|:----------|:----------|:-----------------------------------------------------|
| GRPNAME   | IMSI号段组名称 | 用于指示系统按照哪个IMSI号段组名称来查询IMSI号段信息；若不输入，则表示所有的IMSI号段组名称。 |
| IMSIPEFIX | IMSI号段    | 用于指示系统查询哪个IMSI号段信息；若不输入，则表示所有的IMSI号段。                |

## 使用实例

1. 查询所有IMSI号段的配置信息。

   ```
   LST SCFIMSIPEFIX:;
   ```

   ```
   %%LST SCFIMSIPEFIX:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    IMSI号段组名称  IMSI号段

    TEST            138741     
    GRPNAME1        1318527    
    GRPNAME2        2589       
   (结果个数 = 3)

   ---    END
   ```
2. 查询IMSI号段组中一个指定的IMSI号段组相关IMSI号段配置信息，“IMSI号段组名称”为“GRPNAME1”，“IMSI号段”为“1318527”。

   ```
   LST SCFIMSIPEFIX: GRPNAME="GRPNAME1", IMSIPEFIX="1318527";
   ```

   ```
   %%LST SCFIMSIPEFIX: GRPNAME="GRPNAME1", IMSIPEFIX="1318527";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   IMSI号段组名称  =  GRPNAME1
         IMSI号段  =  1318527
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD SCFIMSIPEFIX**命令的参数说明。