# 查询闭锁短消息业务(LST PREMSMS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户的短消息闭锁业务：

- 若需要查询单个用户的短消息闭锁业务，请输入“IMSI”或“MSISDN”。
- 若需要查询多个连续用户的短消息闭锁业务，请输入“IMSI”或“MSISDN”与“用户个数”的组合。
- 若需要查询多个不连续用户的短消息闭锁业务，请输入“IMSI文件名”或“MSISDN文件名”。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                   |
|:------------|:----------|:---------------------------------------|
| IMSI        | IMSI      | 用于指示系统需要查询哪个IMSI号码的用户的短消息闭锁业务。         |
| ISDN        | ISDN      | 用于指示系统需要查询哪个MSISDN号码的用户的短消息闭锁业务。       |
| RECORDCOUNT | 用户个数      | 用于指示系统需要查询连续多少个用户的短消息闭锁业务。             |
| IMSIFILE    | IMSI文件名   | 用于指示系统需要查询哪个IMSI批操作文件中包含的用户的短消息闭锁业务。   |
| ISDNFILE    | MSISDN文件名 | 用于指示系统需要查询哪个MSISDN批操作文件中包含的用户的短消息闭锁业务。 |

## 使用实例

1. 查询IMSI号码为“460030913121001”的用户的短消息闭锁业务：

   ```
   LST PREMSMS: IMSI="460030913121001";
   ```

   ```
   %%LST PREMSMS: IMSI="460030913121001";%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460030913121001
                             ISDN = 460030913121001
                       ODBPREMSMS = TRUE
                      ODBADULTSMS = FALSE

   Total count = 4

   There is together 1 report

   ---    END
   ```
2. 查询第一个MSISDN号码为“13310911001”的连续3个用户的短消息闭锁业务：

   ```
   LST PREMSMS: ISDN="13310911001", RECORDCOUNT=3;
   ```

   ```
   %%LST PREMSMS: ISDN="13310911001", RECORDCOUNT=3;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：8. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```
3. 查询“MSISDN文件名”为“lstpremsms.txt”的用户的短消息闭锁业务：

   ```
   LST PREMSMS: ISDNFILE="lstpremsms.txt";
   ```

   ```
   %%LST PREMSMS: ISDNFILE="lstpremsms.txt";%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：268435463. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```

## 输出结果说明

请参见

**MOD PREMSMS**

命令的参数说明，表1列出的是未包含在

**MOD PREMSMS**

命令参数说明中的输出项。

| 输出项名称   | 输出项解释                                      |
|:--------|:-------------------------------------------|
| 批操作ID   | 用于返回批操作的任务号。通过执行CHK BATSTAT命令可以查询该任务的详细信息。 |