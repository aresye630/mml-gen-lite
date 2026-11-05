# 查询共享iFC模板信息(LST HSIFCINF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在HSS的业务数据库中查询指定共享iFC模板中的共享iFC信息。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称      | 参数说明                                                                                       |
|:----------|:----------|:-------------------------------------------------------------------------------------------|
| HLRSN     | HLR序列号    | 用于指示系统需要按照哪个HLR序列号来查询共享iFC模板数据。如果不输入，则表示查询“HLR序列号”为“0”的所有共享iFC模板数据。 可选必选说明：可选参数            |
| SIFCTPLID | 共享iFC模板ID | 用于指示系统需要按照哪个共享iFC模板ID来查询共享iFC模板数据，一次只能查询一个共享iFC模板的数据，操作员可以使用LST HTPLINF命令查询获得。 可选必选说明：必选参数 |

## 使用实例

查询共享iFC模板中的iFC信息，“共享iFC模板ID”为“1”：

```
LST HSIFCINF: SIFCTPLID=1;
```

```
%%LST HSIFCINF: SIFCTPLID=1;%%
RETCODE = 0 SUCCESS0001:Operation is successful

IFCNAME                                                                         PRIORITY            PARTIND                       SERVER                                                                                                                                                DEFHND                        SERVINFO                                                                                                                                              INCLUDEREGREQ                 INCLUDEREGRSP                 TRIGPT
                                                                                1                   2                             sip:as.huawei.com                                                                                                                                     2                                                                                                                                                                                   0                             1                             

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**ADD HSIFCINF**

命令的参数说明。表1列出的是未包含在

**ADD HSIFCINF**

命令参数含义中的输出项。

| 输出项名称         | 输出项解释                                                                                                             |
|:--------------|:------------------------------------------------------------------------------------------------------------------|
| PARTIND       | 用于显示共享iFC业务相关性。 取值范围： “0”：与注册业务相关，即当用户当前注册状态为注册时，触发该共享iFC。“1”：与未注册业务相关，即当用户当前注册状态为未注册时，触发该共享iFC。“2”：以上两种状态都会触发业务。 |
| DEFHND        | 用于显示共享iFC的默认处理方式。 取值范围： “0”：会话继续。“1”：会话中止。“2”：由AS决定如何处理该会话。                                                       |
| INCLUDEREGREQ | 用于显示S-CSCF发起第三方注册时，是否携带第一方注册的请求消息内容：“0”：不携带。“1”：携带。                                                               |
| INCLUDEREGRSP | 用于显示S-CSCF发起第三方注册时，iFC是否携带IncludeRegisterResponse标志位：“0”：不携带。“1”：携带。                                              |