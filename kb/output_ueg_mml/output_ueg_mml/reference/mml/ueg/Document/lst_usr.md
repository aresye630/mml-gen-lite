# 查询用户标识关联关系(LST USR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于查询用户标识间的关联关系。当操作员使用IMPU、MSISDN或IMSI创建一个跟踪任务后，网管自动调用该命令获取其它用户标识，并创建相应跟踪任务。

## 注意事项

“IMSI”、“IMPI”、“MSISDN”和“IMPU”四个参数必须有且只能有一个参数出现。

## 参数说明

| 参数ID    | 参数名称      | 参数描述                                                                                                                                                   |
|:--------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI    | IMSI      | 用于标识查询用户标识关联关系的IMSI。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                                                                                                     |
| MSISDN  | MSISDN    | 用于标识查询用户标识关联关系的MSISDN。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                                                                                                   |
| IMPU    | IMPU      | 用于标识查询用户标识关联关系的IMPU。 取值范围：1～128位十进制数字组成的字符串。 默认值：无。                                                                                                    |
| IMPI    | IMPI      | 用于标识查询用户标识关联关系的IMPI。 取值范围：1～128位十进制数字组成的字符串。 默认值：无。                                                                                                    |
| DEFAULT | 只查询默认IMPU | 仅当指定本命令参数“IMSI”、“IMPI”或“MSISDN”的值时该参数有效。用于标识查询用户标识关联关系时是否只查询默认IMPU。 取值范围：0～1 0：查询IMSI或MSISDN所属IMPI对应的所有IMPU。1：查询IMSI或MSISDN所属IMPI的隐式注册集中的默认IMPU。 默认值：0 |

## 使用实例

1. 查询IMSI“460001234567891”所属IMPI的隐式注册集中的默认IMPU：

   ```
   LST USR: IMSI="460001234567891", DEFAULT=1;
   ```

   ```
   %%LST USR: IMSI="460001234567891", DEFAULT=1;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------------------
    IMSI             MSISDN         IMPU                                                IMPI                                          
    460001234567891  8613988888881  sip:ST_OM_VoLTE_LSTUSR_001_001_impu_1_1@huawei.com  ST_OM_VoLTE_LSTUSR_001_001_impu_1_1@huawei.com
    460001234567891  8613988888881  sip:ST_OM_VoLTE_LSTUSR_001_001_impu_1_2@huawei.com  ST_OM_VoLTE_LSTUSR_001_001_impu_1_1@huawei.com
   (结果个数 = 2)

   ---    END
   ```
2. 查询IMSI“460001234567891”所属IMPI对应的所有IMPU：

   ```
   LST USR: IMSI="460001234567891", DEFAULT=0;
   ```

   ```
   %%LST USR: IMSI="460001234567891", DEFAULT=0;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------------------
    IMSI             MSISDN         IMPU                                                IMPI                                          
    460001234567891  8613988888881  sip:ST_OM_VoLTE_LSTUSR_001_001_impu_1_1@huawei.com  ST_OM_VoLTE_LSTUSR_001_001_impu_1_1@huawei.com
    460001234567891  8613988888881  sip:ST_OM_VoLTE_LSTUSR_001_001_impu_1_2@huawei.com  ST_OM_VoLTE_LSTUSR_001_001_impu_1_1@huawei.com
   (操作个数 = 2)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数请参见本命令的参数说明。