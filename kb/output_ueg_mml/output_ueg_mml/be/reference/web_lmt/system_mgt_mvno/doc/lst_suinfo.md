# 查询超级管理员信息（LST SUINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询超级管理员的信息。

## 注意事项

此命令只有超级管理员才能执行。

## 参数说明

无。

## 使用实例

查询超级管理员信息，执行命令如下：

```
LST SUINFO:;
```

输出结果如下：

```
%%LST SUINFO:;%%
RETCODE = 0 操作成功

                        OPNAME = admin
          LAST_LOGIN_IPADDRESS = NULL
               LAST_LOGIN_TIME = 0000-00-00 00:00:00
              LAST_LOGOUT_TIME = 0000-00-00 00:00:00
       PRESENT_LOGIN_IPADDRESS = NULL
            PRESENT_LOGIN_TIME = 0000-00-00 00:00:00
                         RELGI = NOLIMIT
                           ATP = MAN-MACHINE

Total count = 8

There is together 1 report

---    END
```

## 输出结果说明

| 输出项名称                   | 输出项解释                                            |
|:------------------------|:-------------------------------------------------|
| OPNAME                  | 超级管理员的名称。                                        |
| LAST_LOGIN_IPADDRESS    | 上次登录的IP地址。                                       |
| LAST_LOGIN_TIME         | 上次登录的时间。                                         |
| LAST_LOGOUT_TIME        | 上次登出的时间。                                         |
| PRESENT_LOGIN_IPADDRESS | 本次登录的IP地址。                                       |
| PRESENT_LOGIN_TIME      | 本次登录的时间。                                         |
| RELGI                   | 是否限制超级管理员重复登录，具体请参见MOD SUINFO命令中的参数“重复登录限制开关”解释。 |
| ATP                     | 超级管理员的账号类型，具体请参见MOD SUINFO命令中的参数“账号类型”解释。        |