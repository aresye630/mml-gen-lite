# 查询共享iFC(LST HSIFC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在HSS的业务数据库中查询指定“IMPU”或者“PUSI”相关的Service Profile中的共享iFC信息：

- 若需要查询指定“IMPU”或“PUSI”的全部共享iFC，请输入“IMPU”或“PUSI”。
- 若需要查询指定“IMPU”或“PUSI”的某条共享iFC，请输入“IMPU”或“PUSI”与“共享iFC模板ID”的组合。

## 注意事项

“IMPU”和“PUSI”必须存在且只能存在一个。

## 参数说明

| 参数标识   | 参数名称      | 参数说明                                                                                            |
|:-------|:----------|:------------------------------------------------------------------------------------------------|
| IMPU   | IMPU      | 用于指定一个需要查询共享iFC的“IMPU”，要求输入的IMPU值符合SIP URI或TEL URI格式，字母区分大小写。 取值范围：长度不超过127的字符串 默认值：无。 说明：可选参数。 |
| PUSI   | PUSI      | 用于指定一个需要查询共享iFC的“PUSI”，要求输入的PUSI值符合SIP URI或TEL URI格式。字母区分大小写。 取值范围：长度不超过127的字符串 默认值：无。 说明：可选参数。 |
| SIFCID | 共享iFC模板ID | 用于指定一个共享iFC信息模板的序号，以方便对共享iFC信息模板进行查询和引用，操作员可以使用LST HTPLINF命令查询获得。 说明：可选参数。                      |

## 使用实例

1. 查询IMPU的全部共享iFC，“IMPU”为“sip:impuinfo@huawei.com”：

   ```
   LST HSIFC: IMPU="sip:impuinfo@huawei.com";
   ```

   ```
   %%LST HSIFC: IMPU="sip:impuinfo@huawei.com";%%
   RETCODE = 0 操作成功

   SIFCID
   11
   10

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询IMPU的指定共享iFC，“IMPU”为“sip:impuinfo@huawei.com”，“共享iFC模板ID”为“11”：

   ```
   LST HSIFC: IMPU="sip:impuinfo@huawei.com", SIFCID=11;
   ```

   ```
   %%LST HSIFC: IMPU="sip:impuinfo@huawei.com";%%
   RETCODE = 0 操作成功

   SIFCID
   11

   Total count = 2

   There is together 1 report

   ---    END
   ```

## 输出结果说明

本命令输出结果中的输出项与输入参数相同，详细说明请参见参数说明。