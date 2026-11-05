# 查询操作员（LST OPR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用来查询PGW操作员数据。

- 若需要查询某个系统序列号下全部PGW操作员的概要信息，请仅输入“系统序列号”。
- 若需要查询某个PGW操作员的详细信息，请输入“系统序列号”和“操作员名称”两个参数。

## 注意事项

操作员的级别为“ADMINISTRATOR”或操作员被赋给该命令权限时，才具有查询其他操作员的权限。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                           |
|:-------|:-------|:-----------------------------------------------|
| SYSNO  | 系统序列号  | 用于指示系统需要按照哪个系统序列号来查询PGW操作员数据。                  |
| OPNAME | 操作员名称  | 用于指示系统需要按照哪个操作员名称来查询PGW操作员数据；若不输入，则表示所有的操作员名称。 |

## 使用实例

查询“系统序列号”为“1”的局点中“操作员名称”为“test”的用户，命令如下：

```
LST OPR: SYSNO=1, OPNAME="test";
```

输出结果如下：

```
%%LST OPR: SYSNO=1, OPNAME="test";%%
RETCODE = 0 操作成功

                         SYSNO = 1
                        OPNAME = test
                          DESC = NULL
                            UG = ADMINISTRATOR
          LAST_LOGIN_IPADDRESS = NULL
               LAST_LOGIN_TIME = 0000-00-00 00:00:00
              LAST_LOGOUT_TIME = 0000-00-00 00:00:00
       PRESENT_LOGIN_IPADDRESS = NULL
            PRESENT_LOGIN_TIME = 0000-00-00 00:00:00
                           G_0 = TRUE
                           G_1 = TRUE
                           G_2 = TRUE
                           G_3 = TRUE
                           G_4 = TRUE
                           G_5 = TRUE
                           G_6 = TRUE
                           G_7 = TRUE
                        ISLOCK = 0
                          DATE = LIMIT
                     STARTDATE = 2013&10&26
                       ENDDATE = 2013&10&26
                          TIME = LIMIT
                     STARTTIME = 11&54&31
                       ENDTIME = 11&54&32
                          WEEK = LIMIT
                           SUN = TRUE
                           MON = TRUE
                           TUE = TRUE
                           WED = TRUE
                           THU = TRUE
                           FRI = TRUE
                           SAT = TRUE
                        STATUS = ACTIVE
                       TIMEMOD = TRUE
                      VALIDDAY = 90
                     PROMPTDAY = 5
                           TPS = 0
                      LOGAUDIT = FALSE
                         RELGI = NOLIMIT
                        LGIDMS = FALSE
                           ATP = MAN-MACHINE

Total count = 41

There is together 1 report

---    END
```

## 输出结果说明

| 输出项名称                   | 输出项解释                                                                             |
|:------------------------|:----------------------------------------------------------------------------------|
| SYSNO                   | 系统序列号。                                                                            |
| OPNAME                  | 操作员登录的名称。                                                                         |
| DESC                    | 操作员的其他信息。                                                                         |
| UG                      | 操作员级别。                                                                            |
| LAST_LOGIN_IPADDRESS    | 上次登录的IP地址。                                                                        |
| LAST_LOGIN_TIME         | 上次登录的时间。                                                                          |
| LAST_LOGOUT_TIME        | 上次登出的时间。                                                                          |
| PRESENT_LOGIN_IPADDRESS | 本次登录的IP地址。                                                                        |
| PRESENT_LOGIN_TIME      | 本次登录的时间。                                                                          |
| G_0~G_127               | 命令组G_0~G_127是否有效。                                                                 |
| ISLOCK                  | 操作员是否被锁定。                                                                         |
| DATE                    | 是否对用户操作的日期进行限制。                                                                   |
| STARTDATE               | 权限生效的开始日期。                                                                        |
| ENDDATE                 | 权限生效的结束日期。                                                                        |
| TIME                    | 是否对用户操作的时间进行限制。                                                                   |
| STARTTIME               | 权限生效的开始时间。                                                                        |
| ENDTIME                 | 权限生效的结束时间。                                                                        |
| WEEK                    | 是否对用户操作的星期进行限制。                                                                   |
| SUN                     | 星期日是否有效。                                                                          |
| MON                     | 星期一是否有效。                                                                          |
| TUE                     | 星期二是否有效。                                                                          |
| WED                     | 星期三是否有效。                                                                          |
| THU                     | 星期四是否有效。                                                                          |
| FRI                     | 星期五是否有效。                                                                          |
| SAT                     | 星期六是否有效。                                                                          |
| STATUS                  | 是否激活操作员，即是否允许操作员登录PGW系统。                                                          |
| TIMEMOD                 | 是否对密码的有效期进行限制。                                                                    |
| VALIDDAY                | 密码的有效期天数。                                                                         |
| PROMPTDAY               | 系统提示用户密码过期前的天数。                                                                   |
| TPS                     | 每秒钟执行的命令数。                                                                        |
| LOGAUDIT                | 操作员是否有权限查看其他操作员的操作日志。                                                             |
| RELGI                   | 是否限制操作员重复登录。                                                                      |
| LGIDMS                  | 操作员是否可以登录DMS WebUI或者PGW Web LMT。                                                  |
| ATP                     | 操作员的账号类型。  说明： 当环境是由低版本升级到高版本且低版本环境上ADD OPR命令没有“账号类型”参数时，执行本命令，该输出项的返回结果取值为“ALL”。 |