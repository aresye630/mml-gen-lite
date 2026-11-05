# 查询路由前缀长度(LST PREFIXCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询路由前缀长度信息：

- 若需要查询全部路由前缀长度概要信息，请不要输入任何参数。
- 若需要查询某业务类型的路由前缀长度详细信息，请输入“SERVICETYPE”。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                |
|:------------|:-------|:------------------------------------------------------------------------------------|
| SERVICETYPE | 业务类型   | 用于指示系统需要按照哪个业务类型来查询路由前缀长度配置信息。 若输入该参数时，查询返回该业务类型对应的配置信息。 若不输入该参数时，则表示该参数不作为查询的限制条件。 |
| LENGTH      | 前缀长度   | 用于指示系统需要按照路由前缀长度查询配置信息。 若输入该参数时，查询返回该路由前缀长度对应的配置信息。 若不输入该参数时，则表示该参数不作为查询的限制条件。      |

## 使用实例

1. 查询所有路由前缀长度的配置信息：

   ```
   LST PREFIXCFG:;
   ```

   ```
   %%LST PREFIXCFG:;%%
   RETCODE = 0  Operation succeeded

   The result is as follows
   ------------------------
    Service type  Length

    SUP-FE        56       
   (Number of results = 1)

   ---    END
   ```
2. 以单一参数为条件进行查询。例如：查询“业务类型”为“SUP-FE”的路由前缀长度的配置信息。

   ```
   LST PREFIXCFG: SERVICETYPE="SUP-FE";
   ```

   ```
   %%LST PREFIXCFG: SERVICETYPE="SUP-FE";%%
   RETCODE = 0  Operation succeeded

   The result is as follows
   ------------------------
   Service type  =  SUP-FE
         Length  =  56
   (Number of results = 1)

   ---    END
   ```

## 输出结果说明

| 输出项名称        | 输出项解释              |
|:-------------|:-------------------|
| Service type | 用于返回一个业务类型标识。      |
| Length       | 用于返回一个业务类型的路由前缀长度。 |