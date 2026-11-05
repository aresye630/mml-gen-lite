# 修改短消息Short-Code类型(MOD SCTYPE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于对一条短消息Short-Code类型数据记录的某些参数进行修改或调整。在该命令中，系统通过以下关键参数的组合来唯一标识一条短消息Short-Code类型数据记录：

- “HLR序列号”
- “Short-Code前缀”

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称         | 参数说明                                                                                                      |
|:-----------|:-------------|:----------------------------------------------------------------------------------------------------------|
| HLRSN      | HLR序列号       | 标识一条短消息Short-Code类型数据记录的关键字段之一（其取值不能被修改），用于标识需要对哪一条短消息Short-Code类型数据记录的参数进行修改或调整，操作员可以使用LST HLRSN命令查询获得。  |
| CODEPREFIX | Short-Code前缀 | 标识一条短消息Short-Code类型数据记录的关键字段之一（其取值不能被修改），用于标识需要对哪一条短消息Short-Code类型数据记录的参数进行修改或调整，操作员可以使用LST SCTYPE命令查询获得。 |
| PREMSMS    | 是否为付费短消息     | 用于标识Short-Code前缀对应的短消息是否为付费短消息。 取值范围： TRUE：是。FALSE：否。 默认值：无                                               |
| ADULTSMS   | 是否为成人短消息     | 用于标识Short-Code前缀对应的短消息是否为成人短消息。 取值范围： TRUE：是。FALSE：否。 默认值：无                                               |

## 使用实例

1. 在HLR中修改Short-Code前缀对应的类型。“HLR序列号”为“1”，“Short-Code前缀”为“800”，“是否为付费短消息”为“FALSE”：

   ```
   MOD SCTYPE: HLRSN=1, CODEPREFIX="800", PREMSMS=FALSE;
   ```
2. 在HLR中修改Short-Code前缀对应的类型。“HLR序列号”为“1”，“Short-Code前缀”为“800”，“是否为成人短消息”为“FALSE”：

   ```
   MOD SCTYPE: HLRSN=1, CODEPREFIX="800", ADULTSMS=FALSE;
   ```