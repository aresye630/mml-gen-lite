# 查询选择SCP的方式(LST SCPSELINFO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询选择SCP的方式。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询所有选择SCP的方式信息。

```
LST SCPSELINFO:;
```

```
%%LST SCPSELINFO:;%%
RETCODE = 0  操作成功

操作结果如下 
------------------------ 
  SCP选择模式  =  LOCALFIRST
         方案  =  http
  SCP选择方法  =  PRIORITY
(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET SCPSELINFO**。