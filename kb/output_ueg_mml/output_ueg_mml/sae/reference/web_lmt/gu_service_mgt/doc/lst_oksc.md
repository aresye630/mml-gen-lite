# 查询业务区域限制签约数据(LST OKSC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此操作用来查询特定用户的业务区域限制签约数据。

## 注意事项

IMSI和ISDN是条件可选参数，任何一个参数出现即可，但两个参数不能同时出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                    |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                  |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                      |
| ISDNFILE    | MSISDN文件名 | ISDN文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                    |

## 使用实例

1. 查询IMSI号码为460000009123456用户的业务区域限制签约数据情况。命令如下：

   ```
   LST OKSC: IMSI="460000009123456";
   ```

   ```
   %%LST OKSC: IMSI="460000009123456";%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009123456
                             ISDN = 2013521
                        OKSCTPLID = 2

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询第一个MSISDN号码为“13310911001”的连续3个用户业务区域限制签约数据情况：

   ```
   LST OKSC: ISDN="13310911001", RECORDCOUNT=3;
   ```

   ```
   %%LST OKSC: ISDN="13310911001", RECORDCOUNT=3;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：4. 使用CHK BATSTAT指令可查看此批操作的执行情况
   There is together 1 report

   ---    END
   ```
3. 查询“IMSI文件名”为“lst\_oksc.txt”的用户业务区域限制签约数据情况：

   ```
   LST OKSC: IMSIFILE="lst_oksc.txt";
   ```

   ```
   %%LST OKSC: IMSIFILE="lst_oksc.txt";%% 
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：268435478.使用CHK BATSTAT指令可查看此批操作的执行情况  
   There is together 1 report  

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**MOD OKSC**

命令的参数说明。表1列出的是未包含在

**MOD OKSC**

命令参数说明中的输出项。

| 输出项名称     | 输出项解释                              |
|:----------|:-----------------------------------|
| OKSCTPLID | 业务区域限制模板ID。该模板需要通过命令ADD OKSCTPL定义。 |