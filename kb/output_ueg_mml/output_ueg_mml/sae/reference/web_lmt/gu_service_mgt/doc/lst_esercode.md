# 查询私有业务的业务码（LST ESERCODE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询私有业务的业务码。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询私有业务的业务码，命令如下：

`LST ESERCODE:;`

如果操作成功，返回的结果如下：

```
%%LST ESERCODE:;%%
RETCODE = 0 SUCCESS0001:操作成功

                       MAP2OSK = 243
                       MAP2TSK = 244
                     MAP2STYPE = 247
                       MAP2EMA = 252
                      MAP2PRBT = 253
                      MAP2VMCC = 254
                        MAP2DT = 255
                  MAP2RESERVE1 = 241
                  MAP2RESERVE2 = 242
                  MAP2RESERVE3 = 245
                  MAP2RESERVE4 = 246
                    MSCCPPFLAG = NONE
                  CLOPPCPPFLAG = NONE
                       MAP3EMA = 11
                      ICIPCODE = 245
                      ICISCODE = 176

Total count = 16

There is together 1 report

---    END
```

## 输出结果说明

请参见**SET ESERCODE**的参数说明。