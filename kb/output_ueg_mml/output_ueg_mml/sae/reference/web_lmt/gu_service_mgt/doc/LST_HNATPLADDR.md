# 查询游牧地址(LST HNATPLADDR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在HSS的业务数据库中查询指定游牧模板关联的所有游牧地址。

## 注意事项

“NASS游牧模板ID”参数和“NASS游牧模板名称”参数必须存在且仅能存在一个。

## 参数说明

| 参数标识    | 参数名称       | 参数说明                                                                                                            |
|:--------|:-----------|:----------------------------------------------------------------------------------------------------------------|
| NATPLID | NASS游牧模板ID | 用于指示系统需要按照哪个游牧模板ID来查询游牧地址数据，操作员可以使用LST HTPLINF命令查询获得。 取值范围：0～67108863 默认值：无。 说明：可选参数。该参数为255表示无效值。              |
| TPLNAME | NASS游牧模板名称 | 用于指示系统需要按照哪个游牧模板名称来查询游牧地址数据，操作员可以使用LST HTPLINF命令查询获得。 取值范围：长度不超过64的字符串，字符串由数字、字母、“.”、“-”或“_”组成。 默认值：无。 说明：可选参数。 |

## 使用实例

1. 查询游牧地址，NASS游牧模板ID为“10”：

   ```
   LST HNATPLADDR: NATPLID=10;
   ```

   ```
   %%LST HNATPLADDR: NATPLID=10;%%
   RETCODE = 0 操作成功

   NATPLID          TPLNAME          NA                    BEGINIP                     ENDIP                        NATYPE
   10               Templet2         10.huawei.com                                                                  0

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询游牧地址，NASS游牧模板名称为“07550011”：

   ```
   LST HNATPLADDR: TPLNAME="07550011";
   ```

   ```
   %%LST HNATPLADDR: TPLNAME="07550011";%%
   RETCODE = 0 操作成功

   NATPLID          TPLNAME          NA                    BEGINIP                     ENDIP                        NATYPE
   10               07550011                               10.2.2.70                   10.2.2.90                    1

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

| 输出项名称   | 输出项解释                                                       |
|:--------|:------------------------------------------------------------|
| NATPLID | 用于显示NASS游牧模板的ID。                                            |
| TPLNAME | 用于显示NASS游牧模板的名称。                                            |
| nan     | 用于显示NASS游牧模板的游牧地址名称。                                        |
| BEGINIP | 用于显示在游牧模板中增加的IP地址段的起始地址。                                    |
| ENDIP   | 用于显示在游牧模板中增加的IP地址段的结束地址。                                    |
| NATYPE  | 用于显示NASS游牧模板的游牧地址类型。 “0”：表示IMS系统将允许用户注册。“1”：表示IMS系统将限制用户注册。 |