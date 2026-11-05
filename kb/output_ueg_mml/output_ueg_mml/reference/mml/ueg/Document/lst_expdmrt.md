# 查询显式Diameter路由 (LST EXPDMRT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询设置的显式Diameter路由详细信息：

- 若需要查询全部已经设置的显式Diameter路由信息则不需要输入任何参数。
- 若按照路由组名称来查询已经设置的显式Diameter路由信息，请输入“路由组名称”，其他参数不输入。
- 若按照目的对端名称来查询已经设置的显式Diameter路由信息，请输入“目的对端名称”，其他参数不输入。
- 若按照路由选择模式来查询已经设置的显式Diameter路由信息，请输入“路由选择模式”，其他参数不输入。
- 若按照路由对端名称来查询已经设置的显式Diameter路由信息，请输入“路由对端名称”，其他参数不输入。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称     | 参数说明                                             |
|:------------|:---------|:-------------------------------------------------|
| RTNAME      | 路由组名称    | 用于指示系统按照哪个Diameter路由组来查询显式Diameter路由信息。          |
| DPEERNAME   | 目的对端名称   | 用于指示系统按照哪个Diameter路由目的对端实体来查询显式Diameter路由信息。     |
| SMODE       | 路由选择模式   | 用于指示系统按照哪种Diameter消息所对应的路由选择模式来查询显式Diameter路由信息。 |
| RPEERNAME1  | 路由对端名称1  | 用于指示系统按照哪个Diameter路由对端设备来查询显式Diameter路由信息。       |
| RPEERNAME2  | 路由对端名称2  | 用于指示系统按照哪个Diameter路由对端设备来查询显式Diameter路由信息。       |
| RPEERNAME3  | 路由对端名称3  | 用于指示系统按照哪个Diameter路由对端设备来查询显式Diameter路由信息。       |
| RPEERNAME4  | 路由对端名称4  | 用于指示系统按照哪个Diameter路由对端设备来查询显式Diameter路由信息。       |
| RPEERNAME5  | 路由对端名称5  | 用于指示系统按照哪个Diameter路由对端设备来查询显式Diameter路由信息。       |
| RPEERNAME6  | 路由对端名称6  | 用于指示系统按照哪个Diameter路由对端设备来查询显式Diameter路由信息。       |
| RPEERNAME7  | 路由对端名称7  | 用于指示系统按照哪个Diameter路由对端设备来查询显式Diameter路由信息。       |
| RPEERNAME8  | 路由对端名称8  | 用于指示系统按照哪个Diameter路由对端设备来查询显式Diameter路由信息。       |
| RPEERNAME9  | 路由对端名称9  | 用于指示系统按照哪个Diameter路由对端设备来查询显式Diameter路由信息。       |
| RPEERNAME10 | 路由对端名称10 | 用于指示系统按照哪个Diameter路由对端设备来查询显式Diameter路由信息。       |

## 使用实例

查询“路由组名称”为“S6A/S6D”的显式Diameter路由详细信息：

`LST EXPDMRT: RTNAME="S6A/S6D";`

```
%%LST EXPDMRT: RTNAME="S6A/S6D";%%
RETCODE = 0  操作成功

操作结果如下
------------
    路由组名称  =  S6A/S6D
  目的对端名称  =  AS13
  路由选择模式  =  轮询方式
 路由对端名称1  =  AS13
 路由对端名称2  =  NULL
 路由对端名称3  =  NULL
 路由对端名称4  =  NULL
 路由对端名称5  =  NULL
 路由对端名称6  =  NULL
 路由对端名称7  =  NULL
 路由对端名称8  =  NULL
 路由对端名称9  =  NULL
路由对端名称10  =  NULL

(结果个数 = 1)

---    END
```

## 输出结果说明

请参见**SET EXPDMRT**命令的参数说明。