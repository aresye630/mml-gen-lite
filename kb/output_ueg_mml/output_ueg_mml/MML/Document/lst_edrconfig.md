# 查询EDR配置（LST EDRCONFIG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于查询EDR文件名的前缀以及校验文件的输出格式。

## 注意事项

执行本命令查询出的“天控制文件上传时间”的值仅在“EDR文件校验”为“EDRDailyControlFile”或“ENABLEDailyWithSmartFormat”时有效，其他情况下即使有值也无效。

## 参数说明

无。

## 使用实例

查询EDR文件配置。

```
LST EDRCONFIG:;
```

```
%%LST EDRCONFIG:;%%
RETCODE = 0  操作成功

操作结果如下:
-------------

     EDR文件名前缀  =  TestFileName
       EDR文件校验  =  使能并统计行数
天控制文件上传时间  =  0
        匿名化开关  =  ON

(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET EDRCONFIG**命令的参数说明。