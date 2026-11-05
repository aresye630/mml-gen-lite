# 查询EDR上报特性列表(LST EDRREPORT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询EDR上报特性列表。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询EDR上报特性列表。

```
LST EDRREPORT:;
```

```
%%LST EDRREPORT:;%%
RETCODE = 0  操作成功

操作结果如下:
-------------
EDR上报特性列表  =  信令EDR&业务发放系统EDR&动态用户组EDR&Rx信令EDR&Sy信令EDR&N7信令EDR&N28信令EDR&N23信令EDR&N15信令EDR&N24信令EDR
强制EDR记录开关  =  NULL
(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见 **SET EDRREPORT**命令的参数说明。