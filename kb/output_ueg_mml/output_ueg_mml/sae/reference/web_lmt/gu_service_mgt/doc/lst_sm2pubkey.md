# 查询SM2公钥（LST SM2PUBKEY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询已配置的SM2公钥记录。

## 注意事项

本命令为局点定制命令，非定制局点使用前请务必先联系华为技术支持。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                            |
|:-------|:-------|:------------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 可选必选说明：必选参数 参数含义：用于标识系统按照哪个HLR序列号来查询国密SM2公钥记录。 取值范围：1~255 默认值：无。 配置原则：无。                        |
| KEYSNO | 密钥序列号  | 可选必选说明：必选参数 参数含义：用于标识系统按照哪个密钥序列号来查询国密SM2公钥记录。如果不输入，表示查询所有国密SM2公钥记录。 取值范围：1～65535 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询“HLR序列号”为“1”、“密钥序列号”为“7”的国密SM2密钥公钥记录：

   ```
   LST SM2PUBKEY: HLRSN=1, KEYSNO=7;
   ```

   ```
   %%LST SM2PUBKEY: HLRSN=1, KEYSNO=7;%%
   RETCODE = 0 SUCCESS0001:操作成功

         KEYNAME = 1
          PUBKEY = 04DC406DDC9A75D8DFBC50E258F5B2DB6C71F1CF1AFDC1EA4615233603EFBCC3C0A24130C5579843DAB47119EC1D1BF3C5ED595B7C9C3AEE97D00146A23872A0B0

   Total count = 1

   There is together 1 report
   ```
2. 查询所有“HLR序列号”为“1”的国密SM2密钥公钥记录：

   ```
   LST SM2PUBKEY: HLRSN=1;
   ```

   ```
   %%LST SM2PUBKEY: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  KEYSNO       KEYNAME
                  7            1

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。