# 删除ISDNPRE/GT号码模板(RMV ISDNPREGT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于删除ISDNPRE/GT号码模板。通过参数“HLR序列号”和“模板ID”来唯一标识一个ISDNPRE/GT号码模板。

## 注意事项

当执行该命令删除用户已签约的ISDNPRE/GT号码模板时，系统会提示“ERR3005:模板已经被使用”的错误信息，该ISDNPRE/GT号码模板不能被删除。如果要删除该ISDNPRE/GT号码模板，必须先执行**MOD USSDDAT**命令取消由“ISDNPRE/GT号码模板ID”关联的ISDNPRE/GT号码模板。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                  |
|:-------|:-------|:--------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 标识ISDNPRE/GT号码模板数据记录的关键字段之一，用于指定在哪个HLR上删除ISDNPRE/GT号码模板的数据记录，操作员可以使用LST HLRSN命令查询获得。  |
| TPLID  | 模板ID   | 标识ISDNPRE/GT号码模板数据记录的关键字段之一，用于指定需要删除哪个ISDNPRE/GT号码模板的数据记录，操作员可以使用LST ISDNPREGT命令查询获得。 |

## 使用实例

删除“HLR序列号”为“1”的HLR上的ISDNPRE/GT号码模板数据记录。其中“模板ID”为“1”：

```
RMV ISDNPREGT: HLRSN=1, TPLID=1;
```