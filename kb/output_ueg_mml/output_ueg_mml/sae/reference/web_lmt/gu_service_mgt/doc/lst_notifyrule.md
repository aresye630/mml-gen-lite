# 查询数据变更通知分发的规则(LST NOTIFYRULE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在UDM中查询数据变更通知分发规则的数据记录信息：

- 若需要查询某个分发类型全部分发规则数据记录的信息，请输入“分发类型”参数。
- 若需要查询第一优先级Location标识对应的分发规则数据记录信息，请在输入“分发类型”参数的同时输入“第一优先级Location标识”参数。

## 注意事项

无。

## 参数说明

| 参数标识               | 参数名称                | 参数说明                                                                                                                                    |
|:-------------------|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| RULE_TYPE          | 分发类型                | 用于指示系统按照哪种分发类型来查询数据变更通知分发规则的数据记录信息。                                                                                                     |
| LOCATION_ID        | 第一优先级Location标识     | 用于指示系统按照第一优先级Location标识来查询数据变更通知分发规则的数据记录信息；若不输入，则表示所有的Location标识。                                                                      |
| IS_ILLEGAL_SUCCESS | Location取值非法时是否下发成功 | 仅当“分发类型”参数取值为“IMSI_PREFIX”，“MSISDN_PREFIX”，“PI_PREFIX”，“PU_PREFIX”或“SUBID_PREFIX”时该参数有效。 用于标识Location取值为非法值（0）时MCI通知消息是否按照不下发处理，直接返回成功。 |

## 使用实例

1. 查询“分发类型”为“HLRSN”的所有数据变更通知分发规则的数据记录信息，命令如下：

```
LST NOTIFYRULE: RULE_TYPE=HLRSN;
```

```
%%LST NOTIFYRULE: RULE_TYPE=HLRSN;%%
RETCODE = 0 SUCCESS0001:Operation is successful

HLRSN LOCATION_ID SECOND_LOCATION_ID THIRD_LOCATION_ID   IS_ILLEGAL_SUCCESS
1     12          13                 14                  TRUE
2     23          <NULL>             <NULL>              TRUE
3     1           <NULL>             <NULL>              TRUE
4     1           2                  3                   TRUE

Total count = 4

There is together 1 report

---    END
```

2. 查询“分发类型”为“HLRSN”，“第一优先级Location标识”为“1”的数据变更通知分发规则的数据记录信息，命令如下：

```
LST NOTIFYRULE: RULE_TYPE=HLRSN, LOCATION_ID=1;
```

```
%%LST NOTIFYRULE: RULE_TYPE=HLRSN, LOCATION_ID=1;%%
RETCODE = 0 SUCCESS0001:Operation is successful

HLRSN LOCATION_ID SECOND_LOCATION_ID THIRD_LOCATION_ID
3     1           <NULL>             <NULL>
4     1           2                  3

Total count = 2

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数请参见**ADD NOTIFYRULE**命令的输出结果说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                   | 处理建议                           |
|:--------|:--------|:-----------------------------------------------------------------------|:-------------------------------|
| ERR3007 | 记录不存在   | 原因可能有以下两种： 需要查询的“分发类型”参数未添加过任何数据信息记录。需要查询的“分发类型”对应的某个“Location标识”未添加过。 | 执行ADD NOTIFYRULE命令增加需要配置的数据记录。 |