# 查询TOKEN请求配置（LST TOKENREQ）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

该命令用于查询UPCF与CHF/BSF/UDR/NWDAF/HPCF对接的TOKEN请求配置信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询所有Token请求配置信息。

```
LST TOKENREQ:;
```

```
%%LST TOKENREQ:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------
  CHF开关  =  Off
  BSF开关  =  Off
  UDR开关  =  Off
NWDAF开关  =  Off
 HPCF开关  =  Off
(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见SET TOKENREQ。

## 参考信息

无。