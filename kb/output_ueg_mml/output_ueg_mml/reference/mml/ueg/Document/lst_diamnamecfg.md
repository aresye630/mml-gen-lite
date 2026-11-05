# 查询Diameter主机名域名配置(LST DIAMNAMECFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询系统配置的被割接局点用户所在MME的Diameter主机名域名关联记录。

- 若需要查询所有已配置的被割接局点用户所在MME的Diameter主机名域名关联记录，则不输入任何参数。
- 若需要查询某个被割接局点用户所在MME的Diameter主机名域名关联记录，请输入“索引”参数。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                  |
|:---------|:-------|:----------------------------------------------------------------------------------------------------------------------|
| CFGINDEX | 索引     | 可选必选说明：可选参数 参数含义：用于指示系统需要按照哪个索引标识查询已配置的被割接局点用户所在MME的Diameter主机名域名关联记录；若不输入，则表示查询所有的索引记录。 取值范围：1~10000。 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有索引对应的主机名域名关联记录信息：

   ```
   LST DIAMNAMECFG:;
   ```

   ```
   %%LST DIAMNAMECFG:;%%
   RETCODE = 0  Operation succeeded
   The result is as follows
   ------------------------
    Index   Host Name            Realm name
    2       hss2.huawei.com      huawei.com
    3       hss3.huawei.com      huawei.com
    4       hss4.huawei.com      huawei.com
    6       hss6.huawei.com      huawei.com
    7       hss7.huawei.com      huawei.com
    8       hss8.huawei.com      huawei.com
    10000   hss10000.huawei.com  huawei.com
   (Number of results = 7)
   ---    END
   ```
2. 查询“索引”为“2”的主机名域名关联记录信息：

   ```
   LST DIAMNAMECFG: CFGINDEX = 2;
   ```

   ```
   %%LST DIAMNAMECFG: CFGINDEX=2;%%
   RETCODE = 0  Operation succeeded
   The result is as follows
   ------------------------
        Index  =  2
    Host Name  =  hss2.huawei.com
   Realm name  =  huawei.com
   (Number of results = 1)
   ---    END
   ```

## 输出结果说明

参数请参见**ADD DIAMNAMECFG**命令的参数说明。