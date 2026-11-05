# 查询Cluster的状态(DSP CLUSTER)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询Cluster的状态信息。

- 若需要查询所有Cluster的状态信息，请不要输入任何参数。
- 若需要查询某个Cluster的状态信息，请输入“Cluster标识”或其他参数或这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                                                           |
|:------------|:-----------|:---------------------------------------------------------------------------------------------------------------|
| CID         | Cluster标识  | 用于指示系统需要按照哪个Cluster标识来查询Cluster的状态信息，该参数是通过ADD CLUSTER定义后在此引用；若不输入，则表示查询所有Cluster标识的接管状态信息。 取值范围：1～4096 默认值：无。 |
| CT          | Cluster类型  | 用于指示系统需要按照哪个Cluster类型来查询Cluster的状态信息；若不输入，则表示查询所有Cluster类型所对应的Cluster的状态信息。 取值范围： DRU(DRU)DSU(DSU) 默认值：无。      |
| ROLE        | 主备标识       | 用于指示系统需要按照哪个主备标识来查询Cluster的状态信息；若不输入，则表示查询所有主备标识所对应的Cluster的状态信息。 取值范围： ACTIVE：主用REDUNDANCY：容灾 默认值：无。          |
| SERVICETYPE | 业务类型       | 用于指示系统需要按照哪个业务类型来查询Cluster的状态信息，此参数在USCDB下通过LOD FEPLUG命令加载FE插件后在此引用；若不输入，则表示查询所有业务类型所对应的Cluster的状态信息。          |
| LID         | Location标识 | 用于指示系统需要按照哪个Location标识来查询Cluster的状态信息；若不输入，则表示查询所有Location标识所对应的Cluster的状态信息。 取值范围：1～512 默认值：无。                |
| STATE       | 状态         | 用于指示系统需要查询哪种状态的Cluster信息；若不输入，则表示所有的状态。 取值范围： Abnormal：未知状态。Normal：非接管状态。Takeover：接管状态。 默认值：无。                 |

## 使用实例

1. 查询所有Cluster在所有Location中的状态信息：

   ```
   DSP CLUSTER:;
   ```

   ```
   %%DSP CLUSTER:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   Cluster标识       Cluster类型        主备标识         业务类型       Location 标识     状态
   1                 DRU                主用             SUP-FE         5                 Normal
   1                 DRU                容灾             SUP-FE         8                 Takeover
   1                 DRU                容灾             SUP-FE         12                Abnormal
   2                 DSU                容灾             SUP-FE         5                 Takeover
   2                 DSU                主用             SUP-FE         8                 Normal
   2                 DSU                容灾             SUP-FE         12                Normal

   (结果个数 = 6)

   ---    END
   ```
2. 以单一参数为条件进行查询。例如：查询“Cluster标识”为“1”的Cluster的状态信息。

   ```
   DSP CLUSTER: CID=1;
   ```

   ```
   %%DSP CLUSTER: CID=1;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   Cluster标识       Cluster类型        主备标识         业务类型       Location 标识     状态
   1                 DRU                主用             SUP-FE         5                 Normal
   1                 DRU                容灾             SUP-FE         8                 Takeover
   1                 DRU                容灾             SUP-FE         12                Abnormal

   (结果个数 = 1)

   ---    END
   ```
3. 以多个参数为条件进行组合查询。例如：查询“Cluster类型”为“DSU”，且“业务类型”为“SUP-FE”的Cluster的状态信息。

   ```
   DSP CLUSTER: CT=DSU, SERVICETYPE="SUP-FE";
   ```

   ```
   %%DSP CLUSTER: CT=DSU, SERVICETYPE="SUP-FE";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   Cluster标识       Cluster类型        主备标识         业务类型       Location 标识     状态
   2                 DSU                容灾             SUP-FE         5                 Takeover
   2                 DSU                主用             SUP-FE         8                 Normal
   2                 DSU                容灾             SUP-FE         12                Normal

   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令操作成功的提示信息和相关参数，各参数含义请参见本命令的参数说明。