# 查询号段配置信息（LST NSPREFIX）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于在配置库中查询用户的号段配置信息。

- 如果需要查询全部用户的号段配置信息，请不要输入任何参数。
- 如果需要查询某个号段配置信息，请依据参数说明输入查询条件。

## 注意事项

该命令最多支持显示999条号段前缀记录。如果要查询全部记录，可以登录OM Portal界面，在“应用管理>MML”中选择“USCDB”网元，先后执行**LST MODULE**和**GET NODEINFO**命令获取全部号段前缀记录，命令示例如下：

1. 执行**LST MODULE**命令查询模块号，设置“模块类型”为“PGW”，查询得到“模块号”为“9”。

   ```
   LST MODULE: MT=PGW;
   ```
2. 执行**GET NODEINFO**命令获取全部号段前缀记录，设置“节点信息类型”为“GLOBALDATA”，“模块号”为“9”，“全局数据表名”为“P\_NSPREFIX”。

   ```
   GET NODEINFO: TYPE=GLOBALDATA, MID=9, TABLE="P_NSPREFIX";
   ```

   执行命令之后，会经过初始化、写文件、压缩、上传、清理临时文件等过程，执行成功后可通过如下操作下载获取到的文件到本地：单击“系统 > 文件传输”打开文件传输窗口，再单击“CGPLite文件 > 网元文件 > USCDB\_NODEINFO”，选择指定网元的文件下载获取。

   下载下来的文件为.tar.gz后缀名的压缩包，解压缩后的日志文件中可以查询到所有用户的“号段前缀”、“用户类型”、“Partition标识”、“SPR Partition标识”和“描述”，分别对应文件中的“NSP”、“SUBTYPE”、“PARTITIONID”、“SPRPARTITIONID”、“DESCRIPTION”字段。

## 参数说明

| 参数标识   | 参数名称            | 参数说明                                                                                                                      |
|:-------|:----------------|:--------------------------------------------------------------------------------------------------------------------------|
| NSP    | 号段前缀            | 用于指示系统需要按照哪个号段来查询用户号段配置信息；若不输入，则表示所有的号段配置信息。 取值范围：长度不超过15的字符串，大小写敏感。 默认值：无。                                               |
| PID    | Partition标识     | 用于指示系统需要按照哪个partition标识来查询用户号段配置信息；若不输入，则表示所有的partition标识。 取值范围：1～250。 默认值：无。                                             |
| SPRPID | SPR Partition标识 | 混合组网N:1全路由组网场景添加号段前缀时会携带此参数，用于营帐操作触发的MCI订阅通知消息指定发送到对应的SPR。 在UPCF对接的多个SPR中，标识需要收到订阅通知的SPR Partition ID。 取值范围：1～250。 默认值：无。 |

## 使用实例

1. 查询全部用户的号段配置信息。

   ```
   LST NSPREFIX:;
   ```

   ```
   %%LST NSPREFIX:;%%
   RETCODE = 0 Operation succeeded

   Number Segment Prefix   Partition ID       SPR Partition ID        Description
   861382525****           5                  NULL                    NULL
   861550532****           5                  NULL                    NULL
   861895636****           15                 NULL                    NULL

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询某个用户的号段配置信息。“号段前缀”为“861234567\*\*\*\*”，“partition标识”为“5”。

   ```
   LST NSPREFIX: NSP="861234567****", PID=5;
   ```

   ```
   %%LST NSPREFIX: NSP="861234567****", PID=5;%%
   RETCODE = 0 Operation succeeded

   Number Segment Prefix   Partition ID       SPR Partition ID        Description
   861234567****           5                  NULL                    NULL

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见ADD NSPREFIX命令的参数说明

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释   | 原因分析                | 处理建议                                                  |
|------:|:--------|:--------------------|:------------------------------------------------------|
| 90527 | 号段不存在   | 输入需要查询的“号段前缀”取值不存在。 | 请确保输入的“号段前缀”参数取值在系统中已存在。已存在的“号段前缀”可以通过执行本命令不输入任何参数查询。 |