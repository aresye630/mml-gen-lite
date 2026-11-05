# 查询IMPU或PUSI的标准优先级(LST HSTDPRIOR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中查询指定的IMPU或PUSI的3GPP协议规定的优先级数据。

## 注意事项

参数“IMPU”和参数“PUSI”必须存在且仅能存在一个。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                           |
|:-------|:-------|:-----------------------------------------------------------------------------------------------|
| IMPU   | IMPU   | 用于指定一个需要查询优先级数据的IMPU，要求输入的IMPU值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串。 默认值：无。 说明：可选参数。 |
| PUSI   | PUSI   | 用于指定一个需要查询优先级数据的PUSI，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串。 默认值：无。 说明：可选参数。 |

## 使用实例

查询IMPU或PUSI的优先级。“IMPU”为“sip:impuinfo@huawei.com”：

```
LST HSTDPRIOR: IMPU="sip:impuinfo@huawei.com";
```

```
%%LST HSTDPRIOR: IMPU="sip:impuinfo@huawei.com";%%
RETCODE = 0 SUCCESS0001:操作成功

STDPRIOR

NAMESPACE                       EXTPRIOR  CNAMESP

There is together 1 report

---    END
```

## 输出结果说明

| 参数标识      | 参数说明                                                                                                                                                     |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| STDPRIOR  | 用于显示IMPU或PUSI的标准优先级。 “0”：指标准优先级为HIGHEST-PRIORITY。“1”：指标准优先级为HIGH-PRIORITY。“2”：指标准优先级为MIDDLE-PRIORITY。“3”：指标准优先级为LOW-PRIORITY。“4”：指标准优先级为LOWEST-PRIORITY。 |
| NAMESPACE | 用于显示IMPU或PUSI的扩展优先级域名空间。 “0”：指扩展优先级域名空间为WPS。                                                                                                             |
| EXTPRIOR  | 用于显示IMPU或PUSI的扩展优先级，由0～4之间的整数表示，优先级的高低随数值的增加而降低。                                                                                                         |