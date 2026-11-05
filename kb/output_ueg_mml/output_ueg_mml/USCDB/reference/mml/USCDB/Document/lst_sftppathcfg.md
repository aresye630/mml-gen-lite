# 查询SFTP配置信息(LST SFTPPATHCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询SFTP路径配置信息：

- 若需要查询所有的SFTP路径配置的概要信息，请不要输入任何参数。
- 若需要查询某个SFTP路径配置的详细信息，请输入“用户类型”或其它参数或这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                   |
|:------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------|
| USERTYPE    | 用户类型   | 用于指示系统需要按照哪个“用户类型”来查询SFTP路径配置；若不输入，则表示查询所有用户类型的SFTP路径配置信息。 取值范围：PROV(业务)：表示查询的SFTP路径配置信息为营帐功能。DATAMTN(维护)：表示查询的SFTP路径配置信息为导出功能。 默认值：无。 |
| SERVICETYPE | 业务类型   | 若输入，用于指示系统需要按照哪个业务类型名称来查询SFTP路径配置；若不输入，则表示查询所有业务类型的SFTP路径配置信息。 取值范围：长度不超过128的字符串。 默认值：无。                                               |
| NAME        | 配置名称   | 若输入，用于指示系统需要按照哪个配置名称来查询SFTP路径配置；若不输入，则表示查询所有配置名称的SFTP路径配置信息。 取值范围：长度不超过31的字符串。 默认值：无。                                                  |
| PATH        | 配置路径   | 若输入，用于指示系统需要按照哪个配置路径来查询SFTP路径配置；若不输入，则表示查询所有配置路径的SFTP路径配置信息。 取值范围：长度不超过127的字符串。 默认值：无。                                                 |

## 使用实例

1. 查询所有SFTP路径配置信息。

   ```
   LST SFTPPATHCFG:;
   ```

   ```
   %%LST SFTPPATHCFG:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    用户类型      业务类型       配置名称                          配置路径    
    Prov          SUP-FE         4                                 B_0cdefghi                      
    DataMtn       SUP-FE         ABC                               DEF                             
    Prov          SUP-FE         ABCDEFGADFDFDFSADFABCDEFGADFD_10  ABCDEFGADFDFDbFaSADFA_CDEFGab_77
    Prov          SUP-FE         DEF                               ABC                             
    Prov          SUP-FE         F                                 F                               
    DataMtn       SUP-FE         FFFF                              FFFF                            
    DataMtn       SUP-FE         ADD_S                             add_s                           
    Prov          SUP-FE         LACCIMA_S                         laccima_s   
   (结果个数 = 8)

   ---    END
   ```
2. 查询“配置名称”为“ADD\_S”的SFTP路径配置信息。

   ```
   LST SFTPPATHCFG: NAME="ADD_S";
   ```

   ```
   %%LST SFTPPATHCFG: NAME="HSS_ADD_S";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
        用户类型  =  DataMtn
        业务类型  =  SUP-FE
        配置名称  =  ADD_S
        配置路径  =  add_s
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数。