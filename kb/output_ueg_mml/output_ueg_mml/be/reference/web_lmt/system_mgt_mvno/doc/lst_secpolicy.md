# 查询系统安全策略（LST SECPOLICY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询PGW Web LMT和DMS WebUI系统的帐号锁定策略和密码安全策略配置信息。

具有该命令权限的操作员包括：

- ADMINISTRATOR管理员。
- 通过**ADD OPR**命令添加为ADMINISTRATOR级别的操作员。
- 通过**ADD CCG**命令添加具有本命令权限的命令组，然后通过**ADD OPR**命令将已具有本命令权限的命令组添加给CUSTOM级别的操作员。

## 注意事项

ADMINISTRATOR级别的操作员或被赋给该命令权限的操作员具有本命令的操作权限。

## 参数说明

无。

## 使用实例

查询系统安全策略。

```
LST SECPOLICY:;
```

```
%%LST SECPOLICY:;%%
RETCODE = 0 操作成功

                         OPLCK = TRUE
                       TRYTIME = 5
                         CLEAR = TRUE
                      INTERVAL = 10
                     AUTOUNLCK = TRUE
                       LCKTIME = 30
                      SECURITY = TRUE
                        FSTLOG = FALSE
                     HISRECORD = 5
                        MINLEN = 10
                      MMMINLEN = 16
                  PWD_CHARTYPE = TRUE
                 PWD_NO_OPR_ID = TRUE
                  PWD_NO_ORDER = TRUE
                         CNUMS = 3
                     PWD_UPPER = TRUE
                     PWD_LOWER = TRUE
                    PWD_NUMBER = TRUE
                   PWD_SPECIAL = TRUE
                       TIMEMOD = FALSE
               CONTSAMECHARNUM = 3
                    SHOWBANNER = TRUE

Total count = 22

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各输出项含义请参见**SET SECPOLICY**命令的参数说明。