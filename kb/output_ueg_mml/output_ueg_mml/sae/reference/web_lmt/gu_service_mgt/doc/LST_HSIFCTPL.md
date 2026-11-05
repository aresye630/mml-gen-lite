# 查询共享iFC模板(LST HSIFCTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在HSS的业务数据库中查询一个共享iFC模板的数据记录。在该命令中，系统通过“共享iFC模板ID”参数来唯一标识一条共享iFC模板信息。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称      | 参数说明                                                                      |
|:-------|:----------|:--------------------------------------------------------------------------|
| HLRSN  | HLR序列号    | 用于指示系统需要按照哪个HLR序列号来查询共享iFC模板信息。如果不输入，则查询“HLR序列号”为“0”的所有共享iFC模板信息。 说明：可选参数 |
| TPLID  | 共享iFC模板ID | 用于指示系统需要按照哪个共享iFC模板ID来查询共享iFC模板信息，操作员可以使用LST HTPLINF命令查询获得。 说明：必选参数。      |

## 使用实例

查询共享iFC模板信息，“共享iFC模板ID”为“10”：

```
LST HSIFCTPL: TPLID=10;
```

```
%%LST HSIFCTPL: TPLID=10;%%
RETCODE = 0 操作成功

TPLNAME                                                                         COMMENT
SIFCTPL                                                                         Share IFC Template

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

请参见**ADD HSIFCTPL**命令的参数说明。