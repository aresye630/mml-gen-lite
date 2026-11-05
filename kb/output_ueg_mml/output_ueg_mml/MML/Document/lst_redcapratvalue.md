# 查询RedCap接入用户的RAT填写值（LST REDCAPRATVALUE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

该命令用于查询RedCap终端接入时UNC给周边网元UPF，PCF，CHF，N16SMF，N16aSMF，AAAACCT，AAAAUTH发送消息时RatType信元中填写的值。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

显示RedCap终端接入与CHF交互时Rat值为NR\_REDCAP，PCF交互时Rat值为NR\_REDCAP，UPF交互时Rat值为NR\_REDCAP，与AAAACCT交互时Rat值为NR\_REDCAP，与AAAAUTH交互时Rat值为NR\_REDCAP，与N16SMF交互时Rat值为NR\_REDCAP，与N16aSMF交互时Rat值为NR\_REDCAP：

```
LST REDCAPRATVALUE:;
RETCODE = 0  操作成功

结果如下
------------------------
                  和CHF交互使用的RAT值          =  NR_REDCAP
		  和PCF交互使用的RAT值          =  NR_REDCAP
	          和UPF交互使用的RAT值          =  NR_REDCAP
		  和AAAACCT交互使用的RAT值      =  NR_REDCAP
		  和AAAAUTH交互使用的RAT值      =  NR_REDCAP
		  和N16SMF交互使用的RAT值       =  NR_REDCAP
		  和N16ASMF交互使用的RAT值      =  NR_REDCAP
(结果个数 = 1)
```

## 输出结果说明

| 输出项名称             | 输出项解释                     |
|:------------------|:--------------------------|
| 和CHF交互使用的RAT值     | 该参数用于设置和CHF交互使用的RAT值。     |
| 和PCF交互使用的RAT值     | 该参数用于设置和PCF交互使用的RAT值。     |
| 和UPF交互使用的RAT值     | 该参数用于设置和UPF交互使用的RAT值。     |
| 和AAA计费交互使用的RAT值   | 该参数用于设置和ACCT交互使用的RAT值。    |
| 和AAA鉴权交互使用的RAT值   | 该参数用于设置和AUTH交互使用的RAT值。    |
| 和N16SMF交互使用的RAT值  | 该参数用于设置和N16SMF交互使用的RAT值。  |
| 和N16aSMF交互使用的RAT值 | 该参数用于设置和N16aSMF交互使用的RAT值。 |