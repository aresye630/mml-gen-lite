# 查询iFC信息模板(LST HIFCTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中查询一个iFC基本信息模板记录，一次只能查询一个iFC基本信息模板记录，需要输入唯一标识该数据记录的关键参数iFC模板ID。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称    | 参数说明                                                                           |
|:-------|:--------|:-------------------------------------------------------------------------------|
| HLRSN  | HLR序列号  | 用于指示系统需要按照哪个HLR序列号来查询iFC信息模板数据，如果不输入，则表示查询“HLR序列号”为“0”的所有iFC信息模板数据。            |
| TPLID  | iFC模板ID | 用于指示系统需要按照哪个iFC模板ID来查询iFC信息模板数据，一次只能查询一个iFC基本信息模板的数据，操作员可以使用LST HTPLINF命令查询获得。 |

## 使用实例

查询iFC信息模板。iFC模板ID：1。

```
LST HIFCTPL: TPLID=1;
```

```
%%LST HIFCTPL: TPLID=1;%%
RETCODE = 0 SUCCESS0001:Operation is successful

TPLNAME                                                                         PRIORITY            PARTIND                       SERVER                                                                                                                                                DEFHND                        SERVINFO                                                                                                                                              INCLUDEREGREQ                 INCLUDEREGRSP                 TRIGPT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      COMMENT
aa                                                                              1                   1                             sip:as.huawei.com                                                                                                                                     2                                                                                                                                                                                   1                             1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         iFC Template

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

| 参数标识          | 参数说明                                                                 |
|:--------------|:---------------------------------------------------------------------|
| TPLNAME       | 显示iFC模板的名称。                                                          |
| PRIORITY      | 显示iFC模板的优先级。                                                         |
| PARTIND       | 显示iFC模板的业务相关性。                                                       |
| SERVER        | 显示iFC模板的AS地址。                                                        |
| DEFHND        | 显示iFC模板的默认处理方式。                                                      |
| SERVINFO      | 显示iFC模板的业务信息。                                                        |
| INCLUDEREGREQ | 显示S-CSCF发起第三方注册时，是否携带第一方注册的请求消息内容：“0”：不携带。“1”：携带。                    |
| INCLUDEREGRSP | 用于显示S-CSCF发起第三方注册时，iFC是否携带IncludeRegisterResponse标志位：“0”：不携带。“1”：携带。 |
| TRIGPT        | 显示iFC模板的触发点。                                                         |
| COMMENT       | 显示iFC模板的注释说明。                                                        |