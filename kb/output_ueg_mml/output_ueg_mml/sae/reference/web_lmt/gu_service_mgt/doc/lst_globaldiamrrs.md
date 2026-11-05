# 查询全局Diameter漫游限制(LST GLOBALDIAMRRS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询全局Diameter漫游限制数据信息：

- 若需要查询全局Diameter缺省漫游限制数据信息，则输入“HLR序列号”参数，“操作类型”参数设为“DEFRULE”。
- 若需要查询所有全局Diameter漫游限制数据信息，则输入“HLR序列号”参数，“操作类型”参数设为“ALL”。
- 若需要查询基于指定Diameter服务节点的全局Diameter漫游限制数据信息，则输入“HLR序列号”参数，“操作类型”参数设为“ONE”，并且输入指定的“Diameter身份标识”参数。

## 注意事项

- 当“操作类型”参数为“DEFRULE”或“ALL”时，不能输入“Diameter身份标识”参数的值。
- 当“操作类型”参数为“ONE”时，必须输入“Diameter身份标识”参数的值。

## 参数说明

| 参数标识         | 参数名称         | 参数说明                                                                                                                                                     |
|:-------------|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN        | HLR序列号       | 用于指示系统按照哪个HLR序列号来查询用户的漫游限制数据信息，该参数必须输入。                                                                                                                  |
| OPTYPE       | 操作类型         | 用于指示系统按照哪种操作类型来查询用户的漫游限制数据信息，该参数必须输入。 取值范围：DEFRULE：查询全局Diameter缺省漫游限制数据信息。 ALL：查询所有全局Diameter漫游限制数据信息。 ONE：查询基于某个Diameter服务节点的全局Diameter漫游限制数据信息。 默认值：无。 |
| DIAMIDENTITY | Diameter身份标识 | 仅当“操作类型”参数取值为“ONE”时，该参数有效。用于指示系统按照哪个Diameter服务节点来查询用户的漫游限制数据信息。                                                                                          |

## 使用实例

1. 查询“HLR序列号”为“1”的HLR中用户的全局Diameter缺省漫游限制数据信息：

   ```
   LST GLOBALDIAMRRS: HLRSN=1, OPTYPE=DEFRULE;
   ```

   ```
   %%LST GLOBALDIAMRRS: HLRSN=1, OPTYPE=DEFRULE;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                      DEFAULTRULE = RESTRICT
                   DEFAULTERRCODE = ROAMNTALD

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的HLR中用户的所有全局Diameter漫游限制数据信息：

   ```
   LST GLOBALDIAMRRS: HLRSN=1, OPTYPE=ALL;
   ```

   ```
   %%LST GLOBALDIAMRRS: HLRSN=1, OPTYPE=ALL;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

         "RULE"         "ERRCODE"         "DIAMIDENTITYTYPE"  "DIAMIDENTITY"
         RESTRICT       ROAMNTALDODBV     HOSTNAME            test.huawei.com
         RESTRICT       UNEPSSUB          HOSTNAME            b.com

   Total count = 2

   There is together 1 report

   ---    END
   ```
3. 查询“HLR序列号”为“1”的HLR中用户基于“Diameter身份标识”为“test.huawei.com”的全局Diameter漫游限制数据信息：

   ```
   LST GLOBALDIAMRRS: HLRSN=1, OPTYPE=ONE, DIAMIDENTITY="test.huawei.com";
   ```

   ```
   %%LST GLOBALDIAMRRS: HLRSN=1, OPTYPE=ONE, DIAMIDENTITY="test.huawei.com";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

         "RULE"         "ERRCODE"         "DIAMIDENTITYTYPE"  "DIAMIDENTITY"
         RESTRICT       ROAMNTALDODBV     HOSTNAME            test.huawei.com

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                              | 处理建议                                                               |
|:--------|:--------|:--------------------------------------------------|:-------------------------------------------------------------------|
| ERR1009 | 参数丢失    | 当“操作类型”参数为“ONE”时，没有输入“Diameter身份标识”参数的值。          | 根据实际情况，重新输入参数。确保当“操作类型”参数为“ONE”时，必须输入“Diameter身份标识”参数的值。           |
| ERR1010 | 参数冲突    | 当“操作类型”参数为“DEFRULE”或“ALL”时，输入了“Diameter身份标识”参数的值。 | 根据实际情况，重新输入参数。确保当“操作类型”参数为“DEFRULE”或“ALL”时，不能输入“Diameter身份标识”参数的值。 |