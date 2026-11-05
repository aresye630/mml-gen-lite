# 查询Cluster的配置信息(LST CLUSTER)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

用于查询Pod上Cluster的配置信息。

- 若需要查询所有Cluster的概要配置信息，请不要输入任何参数。
- 若需要查询某个Cluster的详细配置信息，请输入“Cluster标识”或其他参数或这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                      |
|:------------|:----------|:----------------------------------------------------------|
| CID         | Cluster标识 | 用于指示系统需要按照哪个Cluster标识来查询Cluster配置信息；若不输入，则表示所有的Cluster标识。 |
| CT          | Cluster类型 | 用于指示系统需要按照哪个Cluster类型来查询Cluster配置信息；若不输入，则表示所有的Cluster类型。 |
| ROLE        | 主备标识      | 用于指示系统需要按照哪个主备标识来查询Cluster配置信息；若不输入，则表示所有的主备标识。           |
| SERVICETYPE | 业务类型      | 用于指示系统需要按照哪个业务类型来查询Cluster配置信息；若不输入，则表示所有的业务类型。           |

## 使用实例

1. 查询所有Cluster的配置数据：

   ```
   LST CLUSTER:;
   ```

   ```
   %%LST CLUSTER:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    Cluster标识  Cluster类型  数据类型            主备标识  业务类型

    1            DRU          全局数据            主用      USCDB   
    200          DSU          用户数据            主用      SUP-FE  
   (结果个数 = 3)

   ---    END
   ```
2. 以单一参数为条件进行查询。例如：查询“Cluster标识”为“1”的Cluster的配置信息。

   ```
   LST CLUSTER: CID=1;
   ```

   ```
   %%LST CLUSTER: CID=1;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   Cluster标识  =  1
   Cluster类型  =  DRU
      数据类型  =  全局数据
      主备标识  =  主用
      业务类型  =  USCDB
   (结果个数 = 1)

   ---    END
   ```
3. 以多个参数为条件进行组合查询。例如：查询“Cluster类型”为DSU，且“业务类型”为“SUP-FE”的Cluster的配置信息。

   ```
   LST CLUSTER: CT=DSU, SERVICETYPE="SUP-FE";
   ```

   ```
   %%LST CLUSTER: CT=DSU, SERVICETYPE="SUP-FE";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   Cluster标识  =  200
   Cluster类型  =  DSU
      数据类型  =  用户数据
      主备标识  =  主用
      业务类型  =  SUP-FE
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令操作成功的提示信息和相关参数，各参数含义请参见**ADD CLUSTER**命令的参数说明。