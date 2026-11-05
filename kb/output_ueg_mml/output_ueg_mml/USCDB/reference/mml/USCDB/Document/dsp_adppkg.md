# 显示适配包(DSP ADPPKG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于请求系统按照指定“适配包类型名称”、“适配包类型”或者“显示详细模板情况”显示已加载适配包的信息。

## 注意事项

无。

## 参数说明

| 参数标识            | 参数名称     | 参数说明                                                                                                     |
|:----------------|:---------|:---------------------------------------------------------------------------------------------------------|
| ADAPTERTYPENAME | 适配包类型名称  | 用于指示系统按照哪个适配包类型名称显示适配包信息。 取值范围：长度不超过128的字符串。 默认值：无。                                                      |
| PKGTYPE         | 适配包加载类型  | 用于指示系统按照哪个适配包类型显示适配包信息；若不输入则表示显示所有适配包类型的适配包信息。 取值范围： EXPORT(EXPORT)IMPORT(IMPORT)MIGRATE(MIGRATE) 默认值：无。 |
| DETAIL          | 显示详细模板情况 | 用于指示系统是否显示导入或导出模板的详细信息。 取值范围： YES(YES)：显示详细情况。NO(NO)：不显示详细情况。 默认值：无。                                     |

## 使用实例

1. 查询“适配包类型名称”为“SUP-FE”、“适配包加载类型”为“EXPORT”、“显示详细模板情况”为“NO”的模板配置详细信息，执行如下命令：

   ```
   DSP ADPPKG: ADAPTERTYPENAME="SUP-FE", PKGTYPE=EXPORT, DETAIL=NO;
   ```

   ```
   %%DSP ADPPKG: ADAPTERTYPENAME="SUP-FE", PKGTYPE=EXPORT, DETAIL=NO;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    模块号         适配包 ID           适配包类型名称     适配包名称            适配包加载类型        版本号                 加载时间
    30             2                   SUP-FE             SUP-FE_ADPPKG.tar     EXPORT                V100R001C00SPC301B001  2017-03-06 11:24:35
    1075           2                   SUP-FE             SUP-FE_ADPPKG.tar     LDAP                  V100R001C00SPC301B001  2017-03-06 11:24:35
    1076           2                   SUP-FE             SUP-FE_ADPPKG.tar     LDAP                  V100R001C00SPC301B001  2017-03-06 11:24:35
    1079           2                   SUP-FE             SUP-FE_ADPPKG.tar     LDAP                  V100R001C00SPC301B001  2017-03-06 11:24:35
    1080           2                   SUP-FE             SUP-FE_ADPPKG.tar     LDAP                  V100R001C00SPC301B001  2017-03-06 11:24:35
    1083           2                   SUP-FE             SUP-FE_ADPPKG.tar     LDAP                  V100R001C00SPC301B001  2017-03-06 11:24:35
    1084           2                   SUP-FE             SUP-FE_ADPPKG.tar     LDAP                  V100R001C00SPC301B001  2017-03-06 11:24:35
    1099           2                   SUP-FE             SUP-FE_ADPPKG.tar     LDAP                  V100R001C00SPC301B001  2017-03-06 11:24:35
    1100           2                   SUP-FE             SUP-FE_ADPPKG.tar     LDAP                  V100R001C00SPC301B001  2017-03-06 11:24:35
    1103           2                   SUP-FE             SUP-FE_ADPPKG.tar     LDAP                  V100R001C00SPC301B001  2017-03-06 11:24:35
    1104           2                   SUP-FE             SUP-FE_ADPPKG.tar     LDAP                  V100R001C00SPC301B001  2017-03-06 11:24:35 
   (结果个数 = 11)

   ---    END
   ```
2. 查询“适配包类型名称”为“SUP\_FE\_IMPORT”，“适配包加载类型”为“IMPORT”的适配包信息：

   ```
   DSP ADPPKG: ADAPTERTYPENAME="SUP_FE_IMPORT", PKGTYPE=IMPORT;
   ```

   ```
   %%DSP ADPPKG: ADAPTERTYPENAME="SUP_FE_IMPORT", PKGTYPE=IMPORT;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------------------
    模块号         适配包ID            适配包类型名称     适配包名称                适配包加载类型        版本号                                       加载时间             全局数据加载状态
    30             1                   SUP_FE_IMPORT      SUP_FE_IMPORT_ADPPKG.tar  IMPORT                SingleSDBTOOLUSCDBToolV100R001C00SPC301B001  2018-01-31 02:07:52  NULL                   
    1075           1                   SUP_FE_IMPORT      SUP_FE_IMPORT_ADPPKG.tar  IMPORT                SingleSDBTOOLUSCDBToolV100R001C00SPC301B001  2018-01-31 02:07:52  加载成功         
    1076           1                   SUP_FE_IMPORT      SUP_FE_IMPORT_ADPPKG.tar  IMPORT                SingleSDBTOOLUSCDBToolV100R001C00SPC301B001  2018-01-31 02:07:52  加载成功         
    1079           1                   SUP_FE_IMPORT      SUP_FE_IMPORT_ADPPKG.tar  IMPORT                SingleSDBTOOLUSCDBToolV100R001C00SPC301B001  2018-01-31 02:07:52  加载成功         
    1080           1                   SUP_FE_IMPORT      SUP_FE_IMPORT_ADPPKG.tar  IMPORT                SingleSDBTOOLUSCDBToolV100R001C00SPC301B001  2018-01-31 02:07:52  加载成功         
    1083           1                   SUP_FE_IMPORT      SUP_FE_IMPORT_ADPPKG.tar  IMPORT                SingleSDBTOOLUSCDBToolV100R001C00SPC301B001  2018-01-31 02:07:52  加载成功         
    1084           1                   SUP_FE_IMPORT      SUP_FE_IMPORT_ADPPKG.tar  IMPORT                SingleSDBTOOLUSCDBToolV100R001C00SPC301B001  2018-01-31 02:07:52  加载成功         
    1099           1                   SUP_FE_IMPORT      SUP_FE_IMPORT_ADPPKG.tar  IMPORT                SingleSDBTOOLUSCDBToolV100R001C00SPC301B001  2018-01-31 02:07:52  加载成功         
    1100           1                   SUP_FE_IMPORT      SUP_FE_IMPORT_ADPPKG.tar  IMPORT                SingleSDBTOOLUSCDBToolV100R001C00SPC301B001  2018-01-31 02:07:52  加载成功         
    1103           1                   SUP_FE_IMPORT      SUP_FE_IMPORT_ADPPKG.tar  IMPORT                SingleSDBTOOLUSCDBToolV100R001C00SPC301B001  2018-01-31 02:07:52  加载成功         
    1104           1                   SUP_FE_IMPORT      SUP_FE_IMPORT_ADPPKG.tar  IMPORT                SingleSDBTOOLUSCDBToolV100R001C00SPC301B001  2018-01-31 02:07:52  加载成功         
   (结果个数 = 11)

   ---    END
   ```
3. 查询“适配包类型名称”为“SUP\_FE\_IMPORT01”，“适配包加载类型”为“IMPORT”，“显示详细模板情况”为“YES”的适配包信息：

   ```
   DSP ADPPKG: ADAPTERTYPENAME="SUP_FE_IMPORT01", PKGTYPE=IMPORT, DETAIL=YES;
   ```

   ```
   %%DSP ADPPKG: ADAPTERTYPENAME="SUP_FE_IMPORT01", PKGTYPE=IMPORT, DETAIL=YES;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------------------
   服务类型   模板名称        模板文件名称          模板描述
   SUP-FE     sup_import001   SUP_FE_IMPORT01.xml   template of mem import SUP  
   SUP-FE     sup_import002   SUP_FE_IMPORT02.xml   template of mem import SUP02
   (结果个数 = 2)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见表1。

| 输出项名称       | 输出结果解释                                                                                |
|:------------|:--------------------------------------------------------------------------------------|
| 模块号         | 用于标识一个模块，即Pod上运行的进程。                                                                  |
| 适配包ID       | 用于标识一个已加载的适配包。                                                                        |
| 适配包类型名称     | 用于标识加载的适配包类型名称。                                                                       |
| 适配包名称       | 用于标识加载的适配包名称。                                                                         |
| 适配包加载类型     | 用于标识该适配包的加载类型。                                                                        |
| 适配包版本号      | 用于标识加载的适配包版本号。                                                                        |
| 加载时间        | 用于标识适配包加载开始的时间。                                                                       |
| 全局数据加载状态    | 用于标识全局数据加载状态。 PGW模块的“全局数据加载状态”固定显示为“NULL”。 DMA模块的“全局数据加载状态”有以下五种： NULL加载成功未加载正在加载加载失败 |
| 服务类型        | 用于标识FE适配包的服务类型。                                                                       |
| 模板名称        | 用于标识模板名称。                                                                             |
| 模板文件名称      | 用于标识模板文件名称。                                                                           |
| 模板描述        | 用于标识模板的描述信息，例如对模板的功能进行描述。                                                             |
| 过滤参数1～过滤参数6 | 用于标识导出模板的过滤参数值。                                                                       |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|   错误码 | 错误码解释                             | 原因分析                             | 处理建议                                                                                                |
|------:|:----------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------|
|  1710 | 无可用的模块。                           | 系统中未添加(PGW/DRU/DSU)模块。           | 执行ADD MODULE命令添加缺少的模块（PGW/DRU/DSU），确保成功添加后，重新执行本命令。                                                 |
|  1854 | 连接数据库失败。                          | 未上传正确的适配包。                       | 须知： 如下操作需要在华为工程师的指导下处理。 请参照如下步骤执行： 登录华为技术支持网站获取正确的FE适配包。使用文件传输功能上传FE适配包至CGPLite容器的指定目录下。执行本命令加载适配包。 |
|  1855 | 执行SQL语句失败。                        | 未上传正确的适配包。                       | 须知： 如下操作需要在华为工程师的指导下处理。 请参照如下步骤执行： 登录华为技术支持网站获取正确的FE适配包。使用文件传输功能上传FE适配包至CGPLite容器的指定目录下。执行本命令加载适配包。 |
|  2033 | 该类型适配包不存在。                        | 未加载“适配包类型”。                      | 先执行LOD ADPPKG命令加载“适配包类型”，再执行本命令查询“适配包类型”，确保查询结果中“适配包类型”已存在。                                         |
|  2498 | 当前版本不支持此功能。                       | “适配包类型”类型参数选择了“EXPORT”之外的取值。     | 将“适配包类型”类型参数取值修改为“EXPORT”，再执行此命令。                                                                   |
|  2058 | 该类型适配包加载失败。                       | 该类型应用视图加载失败。                     | 根据“ALM-10001适配包加载失败”告警定位原因处理。                                                                       |
|  2570 | 指定的适配包类型名称与指定的适配包加载类型不匹配。         | 命令中输入的适配包类型名称和适配包加载类型不匹配。        | 先执行LST ADPPKG查询“适配包名称”对应的适配包类型名称，再执行此命令。                                                            |
|  2572 | 当参数“显示详细导出情况”存在时，参数“适配包加载类型”必须存在。 | 当参数“显示详细导出情况”输入时，“适配包加载类型”参数未输入。 | 当参数“显示详细导出情况”输入时，“适配包加载类型”输入后再执行此命令。                                                                |