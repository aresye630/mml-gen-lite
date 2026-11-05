# 查询前转号段限制(LST BWFTN)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用于查询前转号段限制表， 查询缺省的前转规则和呼叫前转业务。

## 注意事项

如果OPTYPE=ONE，参数FTN要出现，否则FTN不能出现。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                           |
|:-------|:-------|:-----------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | HLR序列号，有效值域为1～255，在PGW支持容灾功能或虚拟HLR功能时设置。                                                       |
| OPTYPE | 操作类型   | 操作类型。取值如下： ONE: 查询指定范围的前转号 ALL: 查询全部前转号段限制表 DEFRULE: 查询前转号段限制表的缺省的前转规则 SERVICE:查询前转号段限制表呼叫前转业务 |
| FTN    | 前转号码   | 前转号，16位以内的十进制数，采用国际格式。                                                                         |

## 使用实例

查询前转号为 12345的前转号段和前转号段限制表呼叫前转业务，命令如下：

LST BWFTN: HLRSN=1, OPTYPE=ONE, FTN="12345";

```
%%LST BWFTN: HLRSN=1, OPTYPE=ONE, FTN="12345";%%
RETCODE = 0 SUCCESS0001:操作成功

        "BEGIN FTN"                    "END FTN"                      "RULE"     "MAXMATCH"
        12345                          12356                          FORBIDDEN  FALSE

Total count = 1

There is together 1 report

---    END
```

LST BWFTN: HLRSN=1, OPTYPE=SERVICE;

```
%%LST BWFTN: HLRSN=1, OPTYPE=SERVICE;%%
RETCODE = 0 SUCCESS0001:操作成功

                       SERVICE = CFU
                       SERVICE = CFB
                       SERVICE = CFNRY
                       SERVICE = CFNRC
                       SERVICE = CFD

Total count = 5

There is together 1 report

---    END
```