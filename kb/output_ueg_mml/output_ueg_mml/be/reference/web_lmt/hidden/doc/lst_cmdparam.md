# 查询参数信息(LST CMDPARAM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询以下参数信息：

- 若需要查询系统中加载的所有FE类型参数信息，请将“参数名称”设置为“FETYPE”。
- 若需要查询系统中设置的Banner信息，请将“参数名称”设置为“BANNERINFO”。
- 若需要查询系统中加载的某个FE类型对应的模板名称或者服务器名称参数信息，请将“参数名称”设置为“TPLNAME”或者“SERVERNAME”，并且将“关联参数”设置为待查询的FE类型。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                 |
|:---------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| PARANAME | 参数名称   | 用于指定待查询的参数信息。 取值范围： FETYPE：FE类型TPLNAME：模板名称SERVERNAME：服务器名称BANNERINFO：Banner信息，是指操作员每次成功登录PGW Web LMT和DMS WebUI系统时，界面显示的Banner信息。 默认值：无。             |
| REFPARAM | 关联参数   | 仅当“参数名称”输入“TPLNAME”或“SERVERNAME”时该参数有效，用于指定系统需要按照哪个FE类型来查询模板名称或者服务器名称参数信息。 此参数必须通过“USCDB MML命令”界面的LOD FEPLUG命令加载FE插件后在此引用。 取值范围：长度不超过255的字符串。 默认值：无。 |

## 使用实例

1. 查询系统中加载的所有FE类型参数信息。

   ```
   LST CMDPARAM: PARAMNAME="FETYPE";
   ```

   ```
   %%LST CMDPARAM: PARAMNAME="FETYPE";%%
   RETCODE = 0 Operation is successful

                        PARAMNAME = FETYPE
                           RESULT = USCDB&GU-HLR&SUP-FE

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询系统中加载的FE类型为“USCDB”的模板名称参数信息。

   ```
   LST CMDPARAM: PARAMNAME="TPLNAME", REFPARAM="USCDB";
   ```

   ```
   %%LST CMDPARAM: PARAMNAME="TPLNAME", REFPARAM="USCDB";%%
   RETCODE = 0 Operation is successful

                        PARAMNAME = TPLNAME
                           RESULT = DataExp_USCDB_11001&DataExp_TaskMgt_TaskDsp_01_06

   Total count = 2

   There is together 1 report

   ---    END
   ```
3. 查询操作员每次成功登录PGW Web LMT和DMS WebUI系统时，界面显示的Banner信息。

   **说明** 

   如下查询结果以用户已通过**SET SECPOLICY**命令设置“显示Banner”为“TRUE”且“Banner信息”为“警告！本系统仅允许授权用户访问，严禁未经授权使用。”为例。

   ```
   LST CMDPARAM: PARAMNAME="BANNERINFO";
   ```

   ```
   %%LST CMDPARAM: PARAMNAME="BANNERINFO";%%
   RETCODE = 0 Operation is successful

                        PARAMNAME = BANNERINFO
                           RESULT = 警告！本系统仅允许授权用户访问，严禁未经授权使用。

   Total count = 2

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数。