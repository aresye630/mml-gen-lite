# 查询服务号码(LST OSNNUM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询服务号码。

## 注意事项

如果没有指定OSNNUM，显示所有的服务号码相关数据。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                |
|:-------|:-------|:----------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询服务号码。                            |
| OSNNUM | 服务号码   | 用于标识SRI消息中需要进行特殊处理的MSISDN号码。 取值范围：1～15位十进制数字组成的字符串。 |

## 使用实例

1. 要查询服务号码，“HLR序列号”为“1”，“服务号码”为“12334567890”：

   ```
   LST OSNNUM: HLRSN=1, OSNNUM="12334567890";
   ```

   ```
   %%LST OSNNUM: HLRSN=1, OSNNUM="12334567890";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

           "OSNNUM"            "OSNNAME"
           12334567890         service1

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 要查询全部服务号码，“HLR序列号”为“1”：

   ```
   LST OSNNUM: HLRSN=1;
   ```

   ```
   %%LST OSNNUM: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

           "OSNNUM"            "OSNNAME"
           12334567890         service1
           12334567891         service2

   Total count = 2

   There is together 1 report

   ---    END
   ```