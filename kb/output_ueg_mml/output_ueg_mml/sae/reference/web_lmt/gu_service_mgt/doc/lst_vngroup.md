# 查询5G虚拟网络组 (LST VNGROUP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询已配置的5G虚拟网络组配置信息。

## 注意事项

“内部组ID”、“外部组ID”和“共享ID”三个参数必须且只能输入一个。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                    |
|:-----------|:-------|:------------------------------------------------------------------------------------------------------------------------|
| INGROUPID  | 内部组ID  | 可选必选说明：条件必选参数 参数含义：用于指定系统按照哪个内部组ID查询5G虚拟网络组配置信息。 取值范围：10～38个十进制数字、十六进制数字或“-”组成的字符串。 默认值：无。 配置原则：该参数输入的字母不区分大小写。         |
| EXTGROUPID | 外部组ID  | 可选必选说明：条件必选参数 参数含义：用于指定系统按照哪个外部组ID查询5G虚拟网络组配置信息。 取值范围：3～128个字母、十进制数字、“@”、“.”、“-”或“_”组成的字符串。 默认值：无。 配置原则：该参数输入的字母不区分大小写。 |
| SHAREDID   | 共享数据ID | 可选必选说明：条件必选参数 参数含义：用于指定系统按照哪个共享数据ID查询5G虚拟网络组配置信息。 取值范围：长度不超过64位的字符串。 默认值：无。 配置原则：该参数输入的字母不区分大小写。                        |

## 使用实例

1. 查询“内部组ID”为“1-46001-2D”的5G虚拟网络组数据记录。

   ```
   LST VNGROUP:INGROUPID="1-46001-2D";
   ```

   ```
   %%LST VNGROUP: INGROUPID="1-46001-2D";%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                        INGROUPID = 1-46001-2d
                       EXTGROUPID = group1@huawei.com
                         SHAREDID = 46001-shared1
                        GROUPNAME = Huawei
                           SNSSAI = 1-123456
                              DNN = cmnet
                         PDUTYPES = IPV6
                    SECONDARYAUTH = FALSE
                      AAAIPV4ADDR = 10.20.30.100
                      AAAIPV6ADDR = 2001:db8::1234
                         SIMPLFIN = TRUE

   Total count = 12

   There is together 1 report

   ---    END
   ```
2. 查询“外部组ID”为“group1@huawei.com”的5G虚拟网络组数据记录。

   ```
   LST VNGROUP: EXTGROUPID="group1@huawei.com";
   ```

   ```
   %%LST VNGROUP: EXTGROUPID="group1@huawei.com";%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                        INGROUPID = 1-46001-2d
                       EXTGROUPID = group1@huawei.com
                         SHAREDID = 46001-shared1
                        GROUPNAME = Huawei
                           SNSSAI = 1-123456
                              DNN = cmnet
                         PDUTYPES = IPV6
                    SECONDARYAUTH = FALSE
                      AAAIPV4ADDR = 10.20.30.100
                      AAAIPV6ADDR = 2001:db8::1234
                         SIMPLFIN = TRUE

   Total count = 12

   There is together 1 report

   ---    END
   ```
3. 查询“共享数据ID”为“46001-shared1”的5G虚拟网络组数据记录。

   ```
   LST VNGROUP: SHAREDID="46001-shared1";
   ```

   ```
   %%LST VNGROUP: SHAREDID="46001-shared1";%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                        INGROUPID = 1-46001-2d
                       EXTGROUPID = group1@huawei.com
                         SHAREDID = 46001-shared1
                        GROUPNAME = Huawei
                           SNSSAI = 1-123456
                              DNN = cmnet
                         PDUTYPES = IPV6
                    SECONDARYAUTH = FALSE
                      AAAIPV4ADDR = 10.20.30.100
                      AAAIPV6ADDR = 2001:db8::1234
                         SIMPLFIN = TRUE

   Total count = 12

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD VNGROUP**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                         | 处理建议                                                                          |
|:--------|:--------|:---------------------------------------------|:------------------------------------------------------------------------------|
| ERR1009 | 参数丢失    | 执行命令时未输入“内部组ID”、“外部组ID”或“共享数据ID”三个参数任何一个。    | “内部组ID”、“外部组ID”和“共享ID”三个参数必须且只能输入一个。                                          |
| ERR1010 | 参数冲突    | 执行命令时同时输入“内部组ID”、“外部组ID”或“共享数据ID”参数。         | “内部组ID”、“外部组ID”和“共享ID”三个参数必须且只能输入一个。                                          |
| ERR3007 | 记录不存在   | “内部组ID”、“外部组ID”或“共享数据ID”参数对应的5G虚拟网络组数据记录不存在。 | “内部组ID”、“外部组ID”或“共享数据ID”对应的5G虚拟网络组数据记录不存在。可以根据实际情况执行ADD VNGROUP命令增加5G虚拟网络组数据。 |