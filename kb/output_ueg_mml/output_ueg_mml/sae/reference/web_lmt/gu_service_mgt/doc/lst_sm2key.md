# 查询SM2密钥（LST SM2KEY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询已生成的国密SM2密钥记录。

- 执行本命令仅携带“HLR序列号”时，查询结果显示“密钥序列号”和“密钥名”。
- 执行本命令同时携带“HLR序列号”和“密钥序列号”时，查询结果显示该密钥的公钥信息。

## 注意事项

本命令为局点定制命令，非定制局点使用前请务必先联系华为技术支持。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                              |
|:-------|:-------|:--------------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 可选必选说明：必选参数 参数含义：用于标识系统按照哪个HLR序列号来查询国密SM2密钥记录。 取值范围：1~255 默认值：无。 配置原则：无。                          |
| KEYSNO | 密钥序列号  | 可选必选说明：可选参数 参数含义：用于标识系统按照哪个密钥序列号来查询国密SM2密钥记录。如果不输入，表示查询所有国密SM2密钥公钥记录。 取值范围：1～65535 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询“HLR序列号”为“1”、“密钥序列号”为“2”的国密SM2密钥的公钥信息：

   ```
   LST SM2KEY: HLRSN=1, KEYSNO=2;
   ```

   ```
   %%LST SM2KEY: HLRSN=1, KEYSNO=2;%%
   RETCODE = 0 SUCCESS0001:操作成功

                          KEYNAME = etast
                                C = CN
                        PUBLICKEY = 04b137b63167be89987b5bf73e6321564e19e6c7750c6516069b577fdbc0c1eae08931d3e0ef8d5f7f4dc7c43451a5043ef44bcae03723dfdc9726174bf2999fed

   -----BEGIN CERTIFICATE REQUEST-----
   MIHaMIGAAgEAMB0xDjAMBgNVBAMMBWV0YXN0MQswCQYDVQQGEwJDTjBaMBQGCCqB
   HM9VAYItBggqgRzPVQGCLQNCAASxN7YxZ76JmHtb9z5jIVZOGebHdQxlFgabV3/b
   wMHq4Ikx0+DvjV9/TcfENFGlBD70S8rgNyPf3JcmF0vymZ/toAAwCgYIKoEcz1UB
   g3UDSQAwRgIhALqKCn8pfA0w5xNMc1byMaWyd8RNqWiIfM/QjW79DKx/AiEAzPQj
   3WX7mgRtjzflTp3RM9EY17Nh7+4eak5E4p/f5rk=
   -----END CERTIFICATE REQUEST-----

   Total count = 4

   There is together 1 report

   ---    END
   ```
2. 查询所有“HLR序列号”为“1”的国密SM2密钥记录：

   ```
   LST SM2KEY: HLRSN=1;
   ```

   ```
   %%LST SM2KEY: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  KEYSNO       KEYNAME
                  66           VERIFIER
                  2            etast
                  3            etast
                  4            etast
                  5            etast
                  6            etast
                  7            etast

   Total count = 7

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。