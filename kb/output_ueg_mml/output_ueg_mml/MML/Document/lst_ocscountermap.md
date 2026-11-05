# 查询OCS Counter映射(LST OCSCOUNTERMAP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询UPCF配置数据库中配额名称与配额状态的OCS Counter映射记录配置信息。

- 如果需要查询全部的OCS Counter映射配置记录，请不要输入任何参数。
- 如果需要查询指定的OCS Counter映射配置记录，请输入“配额名称”参数。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称   | 参数描述                                                                           |
|:----------|:-------|:-------------------------------------------------------------------------------|
| QUOTANAME | 配额名称   | 可选必选说明：可选参数 参数含义：用于指定要查询OCS Counter映射关系的配额名称。 取值范围：长度不超过32的字符串。 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有OCS Counter映射记录配置信息。

   ```
   LST OCSCOUNTERMAP:;
   ```

   ```
   %%LST OCSCOUNTERMAP:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
    配额名称   配额状态  

    PackName   PackUsage 
    PackName1  PackUsage1
   (结果个数 = 2)

   ---    END
   ```
2. 查询指定OCS Counter映射记录配置信息，“配额名称”为“PackName”。

   ```
   LST OCSCOUNTERMAP: QUOTANAME="PackName";
   ```

   ```
   %%LST OCSCOUNTERMAP: QUOTANAME="PackName";%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   配额名称  =  PackName
   配额状态  =  PackUsage
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD OCSCOUNTERMAP**命令的参数说明。