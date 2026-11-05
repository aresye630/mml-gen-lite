# 查询SKTYPE(LST SKTYPE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

操作员可以通过此命令查询智能业务类型。

## 注意事项

- 当参数中只有HLRSN时，查询HLRSN的所有SK记录。
- 若参数索引号存在，不管参数智能业务类型是否存在，都以索引号来查询。
- 当参数为HLRSN、SKINDEX时，查询HLRSN、SKINDEX对应的这一条记录。
- 当参数为HLRSN、SKTYPE时，查询HLRSN的类型为SKTYPE的所有记录。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                        |
|:--------|:-------|:------------------------------------------------------------|
| HLRSN   | HLR序列号 | HLR序列号，有效值域为1～255，在PGW支持容灾功能或虚拟HLR功能时设置。                    |
| SKINDEX | 索引号    | 用来标识智能业务编码号段的记录，两条智能业务编码号段记录不能使用同一个SKINDEX。 值域：0～999。 可选参数。 |
| SKTYPE  | 智能业务类型 | 智能业务的类型。 值域： PrePaid：预付费 缺省值：PrePaid。 可选参数。                 |

## 使用实例

查询预付费业务所对应的所有智能业务编码起始值和结束值。

LST SKTYPE: HLRSN=1, SKTYPE=PrePaid;

```
%%LST SKTYPE: HLRSN=1, SKTYPE=PrePaid;%%
RETCODE = 0 SUCCESS0001:操作成功

        SKINDEX       SKTYPE        SKBEGIN       SKEND
        3             PrePaid       123456        1234567

Total count = 1

There is together 1 report

---    END
```