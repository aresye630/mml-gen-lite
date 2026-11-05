# 查询私有密钥(LST PRVTKEY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询HSS/HLR中所有的私有密钥配置信息：

- 若需要查询全部的私有密钥数据，请输入“HLR序列号”，其他参数不输入。
- 若需要查询某个私有密钥序列号的私有密钥数据的详细信息，请输入“HLR序列号”和“私有密钥序列号”。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称    | 参数说明                                                   |
|:--------|:--------|:-------------------------------------------------------|
| HLRSN   | HLR序列号  | 用于指定需要查询哪个HLR上的私有密钥数据记录，操作员可以使用LST HLRSN命令查询获得。        |
| PKEYSNO | 私有密钥序列号 | 用于指定需要查询哪个私有密钥序列号对应的私有密钥数据记录，操作员可以使用LST PRVTKEY命令查询获得。 |

## 使用实例

1. 查询“HLR序列号”为“6”的私有密钥数据：

   ```
   LST PRVTKEY: HLRSN=6;
   ```

   ```
   %%LST PRVTKEY: HLRSN=6;%%
   RETCODE = 0 SUCCESS0001:操作成功

                 PKEYSNO               KEYNAME
                 2                     keynamehlr6pkeysno2
                 1                     keynamehlr6pkeysno1
                 3                     keynamehlr6pkeysno3
                 4                     keynamehlr6pkeysno4

   Total count = 4

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“6”的私有密钥数据，其中“私有密钥序列号”为“2”：

   ```
   LST PRVTKEY: HLRSN=6,PKEYSNO=2;
   ```

   ```
   %%LST PRVTKEY: HLRSN=6,PKEYSNO=2;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 6
                          PKEYSNO = 2
                          KEYNAME = keynamehlr6pkeysno2

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD PRVTKEY**命令的参数说明。

执行该命令返回的常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                 | 处理建议                                                                                               |
|:--------|:--------|:-------------------------------------|:---------------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在   | 有两点原因：HLR序列号未定义。HLR序列号对应的私有密钥序列号未添加。 | 对于第一点原因，执行LST HLRSN命令查询出已定义的HLRSN，然后在执行LST PRVTKEY命令时输入即可。 对于第二点原因，在执行LST PRVTKEY命令时只输入“HLR序列号”即可。 |