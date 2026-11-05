# 查询Diameter链路集(LST DMLKS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询Diameter链路集的配置信息。

- 若需要查询全部Diameter链路集记录的概要信息，请不要输入任何参数。
- 若需要查询某些Diameter链路集记录的详细信息，请输入“链路集名称”或其他参数或这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称           | 参数说明                                                                |
|:---------|:---------------|:--------------------------------------------------------------------|
| LINKSNAM | 链路集名称          | 用于指示系统按照哪个链路集名称来查询Diameter链路集信息；若不输入，则表示所有的链路集名称。                   |
| LOCALNAM | Diameter本端实体名称 | 用于指示系统按照哪个Diameter本端实体名称来查询Diameter链路集信息；若不输入，则表示所有的Diameter本端实体名称。 |
| PEERNAM  | Diameter对端实体名称 | 用于指示系统按照哪个Diameter对端实体名称来查询Diameter链路集信息；若不输入，则表示所有的Diameter对端实体名称。 |
| LNKMOD   | 链路选择模式         | 用于指示系统按照哪种链路选择模式来查询Diameter链路集信息；若不输入，则表示所有的链路选择模式。                 |

## 使用实例

1. 查询所有Diameter链路集的配置信息：

   ```
   LST DMLKS:;
   ```

   ```
   %%LST DMLKS:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    链路集名称  Diameter本端实体名称  Diameter对端实体名称  链路选择模式  Diameter链路集标识  Diameter本端实体标识  Diameter对端实体标识

    HSS_BSF     HSS9860               BSF                   激活方式      0                   0                     3                   
    HSS_AS      HSS9860               AS                    基于会话ID    1                   0                     2                   
   (结果个数 = 2)

   ---    END
   ```
2. 查询某个Diameter链路的配置信息，“链路集名称”为“HSS\_AS”。

   ```
   LST DMLKS: LINKSNAM="HSS_AS";
   ```

   ```
   %%LST DMLKS: LINKSNAM="HSS_AS";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
             链路集名称  =  HSS_AS
   Diameter本端实体名称  =  HSS9860
   Diameter对端实体名称  =  AS
           链路选择模式  =  基于会话ID
     Diameter链路集标识  =  1
   Diameter本端实体标识  =  0
   Diameter对端实体标识  =  2
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**ADD DMLKS**

命令的参数说明，表1列出的是未包含在

**ADD DMLKS**

命令参数说明中的输出项。

| 输出项名称          | 输出项解释                   |
|:---------------|:------------------------|
| Diameter链路集标识  | 用于返回Diameter链路集索引。      |
| Diameter本端实体标识 | 用于返回Diameter本端实体数据记录索引。 |
| Diameter对端实体标识 | 用于返回Diameter对端实体数据记录索引。 |