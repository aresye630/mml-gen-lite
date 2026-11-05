# 查询IMPI的HTTP Digest鉴权信息(LST HHDAINF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于从HSS的业务数据库中查询指定IMPI或用户名称的HTTP Digest鉴权信息，需要输入唯一标识该数据记录的关键参数IMPI或HUSERNAME参数。

## 注意事项

IMPI参数和HUSERNAME参数必须存在且仅能存在一个。

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                 |
|:----------|:-------|:-------------------------------------------------------------------------------------|
| IMPI      | IMPI   | 用于指示系统需要按照哪个IMPI来查询Http Digest数据；若不输入，则表示按用户名称来查询。 取值范围：长度不超过127的字符串 默认值：无。 说明：可选参数。 |
| HUSERNAME | 用户名称   | 用于指示系统需要按照哪个用户名称来查询Http Digest数据；若不输入，则表示按IMPI来查询。 取值范围：长度不超过127的字符串 默认值：无。 说明：可选参数。 |

## 使用实例

查询IMPI的HTTP Digest鉴权信息，“IMPI”为“impiinfo”：

```
LST HHDAINF: IMPI="impiinfo";
```

```
%%LST HHDAINF: IMPI="impiinfo";%%
RETCODE = 0 Operation is successful

IMPI                                 HUSERNAME                                   PWD                                   HA1
impiinfo                                                                                                               ******

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，参数含义请参见表1的参数说明，其他输出项的详细说明请参见参数说明。

| 输出项名称    | 输出项解释                                 |
|:---------|:--------------------------------------|
| PWD      | 用于显示HTTP Digest鉴权的密码，出于安全原因，仅显示“*”。   |
| HA1      | 用于显示HTTP Digest鉴权的HA1值，出于安全原因，仅显示“*”。 |
| PWDK2SNO | 用于显示PWD K2索引号。                        |
| HA1K2SNO | 用于显示HA1 K2索引号。                        |