# 查询ADSU鉴权算法配置(LST ALGTAG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用于查询ADSU鉴权算法配置。

## 注意事项

如果ADSUALG没有出现，查询所有ADSU鉴权算法配置。

## 参数说明

| 参数标识    | 参数名称      | 参数说明                 |
|:--------|:----------|:---------------------|
| ADSUALG | ADSU鉴权算法值 | ADSU鉴权算法值，取值范围1-127。 |

## 使用实例

在［ADSU鉴权算法配置表］中查询一条记录，ADSU鉴权算法值为1。命令如下：

LST ALGTAG: ADSUALG=1;

```
%%LST ALGTAG: ADSUALG=1;%%
RETCODE = 0 SUCCESS0001:操作成功

        "ADSU ALG"  "AUC ALG"
        1           COMP128_1

Total count = 1

There is together 1 report
```