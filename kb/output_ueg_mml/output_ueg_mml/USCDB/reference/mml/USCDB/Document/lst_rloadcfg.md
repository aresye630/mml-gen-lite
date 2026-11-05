# 查询远端加载开关(LST RLOADCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询已配置的远端加载信息，若不输入任何参数，则查询所有已配置的远端加载开关信息。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称         | 参数说明                                                       |
|:------------|:-------------|:-----------------------------------------------------------|
| SERVICETYPE | 业务类型         | 用于指示系统需要按照哪个业务类型查询已配置的远端加载信息，若不输入，表示查询所有业务类型下的远端加载信息。      |
| RLOCID      | 远端Location标识 | 用于指示系统需要按照哪个远端Location标识查询远端加载信息；若不输入，则表示查询当前类型下所有的远端加载信息。 |

## 使用实例

1. 查询所有已配置的远端加载信息：

   ```
   LST RLOADCFG:;
   ```

   ```
   +++    USCDB/*MEID:5 MENAME:UDR_FS102_db10_LCBB231_5*/        2022-03-04 17:17:27+7:00
   O&M    #9762
   %%LST RLOADCFG:;%%
   RETCODE = 0  Operation succeeded

   The result is as follows
   ------------------------
    Service type  Remote location ID  Remote loading switch

    SUP-FE        8                   ON                   
    USCDB         8                   ON                   
   (Number of results = 2)

   ---    END
   ```
2. 查询“SUP-FE”类型下已配置的远端加载信息：

   ```
   LST RLOADCFG: SERVICETYPE="SUP-FE";
   ```

   ```
   %%LST RLOADCFG: SERVICETYPE="SUP-FE";%%
   RETCODE = 0  Operation succeeded

   The result is as follows
   ------------------------
            Service type  =  SUP-FE
      Remote location ID  =  8
   Remote loading switch  =  ON
   (Number of results = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令操作成功的提示信息和相关参数，各参数含义请参见**SET RLOADCFG**命令的参数说明。