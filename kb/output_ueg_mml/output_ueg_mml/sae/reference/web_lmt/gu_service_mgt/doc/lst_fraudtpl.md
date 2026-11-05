# 查询防欺诈模板(LST FRAUDTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此命令用来查询已存在的防欺诈模板数据。

若需要查询所有防欺诈模板，请不要输入模板ID。若需要查询某一模板信息时，请输入对应模板ID。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                             |
|:-------|:-------|:-------------------------------------------------|
| HLRSN  | HLR序列号 | HLR序列号，在PGW支持容灾功能或虚拟HLR功能时设置。 取值范围：1～255 说明：必选参数 |
| TPLID  | 模板ID   | 用于在模板ID列表框中选择模板的ID。 取值范围：0～65534 说明：可选参数         |

## 使用实例

查询1号防欺诈模板中的数据。例如：

```
LST FRAUDTPL: HLRSN=1, TPLID=1;
```

```
%%LST FRAUDTPL: HLRSN=1, TPLID=1;%%
RETCODE = 0 SUCCESS0001:操作成功

                         HLRSN = 1
                         TPLID = 1
                       TPLNAME = FRAUD-01
               MO_CONTROL_MODE = MOTIME
                        MOTIME = 5
                         MOACT = REJECT
               CF_CONTROL_MODE = NONE
                         CFACT = NE
                        CFRMAX = 0

Total count = 9

There is together 1 report

---    END
```

## 输出结果说明

输出项的详细说明请参见参数说明。