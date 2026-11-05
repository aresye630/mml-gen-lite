# 查询短消息Short-Code类型(LST SCTYPE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询短消息Short-Code类型配置信息。

- 若需要查询某个虚拟HLR中所有短消息Short-Code类型的配置信息，请只输入“HLR序列号”参数。
- 若需要查询某个虚拟HLR中某条短消息Short-Code类型的详细配置信息，请同时输入“HLR序列号”和“Short-Code前缀”参数。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称         | 参数说明                                                                       |
|:-----------|:-------------|:---------------------------------------------------------------------------|
| HLRSN      | HLR序列号       | 用于标识系统按照哪个HLR序列号来查询短消息Short-Code类型数据。                                      |
| CODEPREFIX | Short-Code前缀 | 用于指示系统按照哪个Short-Code前缀来查询短消息Short-Code类型数据；若不输入，则表示查询所有的短消息Short-Code类型数据。 |

## 使用实例

1. 查询短消息Short-Code类型数据，“HLR序列号”为“1”：

   ```
   LST SCTYPE: HLRSN=1;
   ```

   ```
   %%LST SCTYPE: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

           "SMS Short-code Prefix"   "PREMSMS"     "ADULTSMS"
           12345                     TRUE          FALSE
           123                       FALSE         FALSE
           12                        TRUE          TRUE

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询短消息Short-Code类型数据，“HLR序列号”为“1”，“Short-Code前缀”为“800”：

   ```
   LST SCTYPE: HLRSN=1, CODEPREFIX="800";
   ```

   ```
   %%LST SCTYPE: HLRSN=1, CODEPREFIX="800";%%
   RETCODE = 0 SUCCESS0001:操作成功

           "SMS Short-code Prefix"   "PREMSMS"     "ADULTSMS"
           800                       FALSE         FALSE

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

请参见**ADD SCTYPE**命令的参数说明。