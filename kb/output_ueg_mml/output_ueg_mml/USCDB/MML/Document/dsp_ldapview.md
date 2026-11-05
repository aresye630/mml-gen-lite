# 显示LDAP视图(DSP LDAPVIEW)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于请求系统显示LAS服务中已加载的LDAP视图信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询LDAP视图信息。

```
DSP LDAPVIEW:;
```

```
%%DSP LDAPVIEW:;%%
RETCODE = 0  操作成功

操作结果如下
------------

模块号         LDAP视图名称   LDAP视图包名称                     加载时间              操作结果

539025156      XX_SESSIONDB   XX_SESSIONDB_VIEW_V200R025C02.tar  2021-03-25 21:45:39   Operation succeeded
539020054      XX_SESSIONDB   XX_SESSIONDB_VIEW_V200R025C02.tar  2021-03-25 21:45:38   Operation succeeded
539020714      XX_SESSIONDB   XX_SESSIONDB_VIEW_V200R025C02.tar  2021-03-25 21:45:39   Operation succeeded
539024673      XX_SESSIONDB   XX_SESSIONDB_VIEW_V200R025C02.tar  2021-03-25 21:45:42   Operation succeeded
539024303      XX_SESSIONDB   XX_SESSIONDB_VIEW_V200R025C02.tar  2021-03-25 21:45:42   Operation succeeded
539021753      XX_SESSIONDB   XX_SESSIONDB_VIEW_V200R025C02.tar  2021-03-25 21:45:45   Operation succeeded
(结果个数 = 6)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见表1的参数说明。

| 输出项名称     | 输出项解释               |
|:----------|:--------------------|
| 模块号       | 用于返回LDAP视图所在的服务模块号。 |
| LDAP视图名称  | 用于返回LDAP视图名称。       |
| LDAP视图包名称 | 用于返回LDAP视图包名称。      |
| 加载时间      | 用于标识加载开始的时间。        |
| 操作结果      | 用于标识操作结果。           |