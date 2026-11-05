# 查询IMPI的SIP Digest鉴权信息(LST HSDAINF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于从HSS的业务数据库中查询指定“IMPI”或“用户名称”的SIP Digest鉴权信息，需要输入唯一标识该数据记录的关键参数“IMPI”或“用户名称”参数。

## 注意事项

“IMPI”参数和“用户名称”参数必须存在且仅能存在一个。如果用户签约HA1信息，则使用“用户名称”查询时，返回用户名不存在。

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                |
|:----------|:-------|:------------------------------------------------------------------------------------|
| IMPI      | IMPI   | 用于指示系统需要按照哪个IMPI来查询SIP Digest数据；若不输入，则表示按用户名称来查询。 取值范围：长度不超过127的字符串 默认值：无。 说明：可选参数。 |
| HUSERNAME | 用户名称   | 用于指示系统需要按照哪个用户名称来查询SIP Digest数据；若不输入，则表示按IMPI来查询。 取值范围：长度不超过127的字符串 默认值：无。 说明：可选参数。 |

## 使用实例

1. 查询IMPI的SIP Digest鉴权信息，“IMPI”为“impiinfo”：

   ```
   LST HSDAINF: IMPI="impiinfo";
   ```

   ```
   %%LST HSDAINF: IMPI="impiinfo";%%
   RETCODE = 0 操作成功

   IMPI                        HUSERNAME                        PWD                        REALM                        HA1
   impiinfo                                                                                huawei.com                   ******

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询IMPI的SIP Digest鉴权信息，“用户名称”为“IMPIINFO”：

   ```
   LST HSDAINF: HUSERNAME="IMPIINFO";
   ```

   ```
   %%LST HSDAINF: HUSERNAME="IMPIINFO";%%
   RETCODE = 0 操作成功

   IMPI                        HUSERNAME                        PWD                        REALM                        HA1
   impiinfo                    IMPIINFO                         ***                        huawei.com                   

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

以下列出的是未包含在本命令输入参数中的输出项，其他输出项的详细说明请参见参数说明。

| 输出项名称    | 输出项解释                                                                                                 |
|:---------|:------------------------------------------------------------------------------------------------------|
| PWD      | 用于显示SIP Digest鉴权的密码，出于安全原因，仅显示“*”。                                                                    |
| REALM    | 用于显示SIP Digest鉴权的域名。                                                                                  |
| HA1      | 用于显示SIP Digest鉴权的HA1值。 说明：当参数“AUTHENCRYMODEDISP”为“0”时，该参数显示为明文。当参数“AUTHENCRYMODEDISP”为“1”时，该参数仅显示“*”。 |
| PWDK2SNO | 用于显示PWD K2索引号。                                                                                        |
| HA1K2SNO | 用于显示HA1 K2索引号。                                                                                        |