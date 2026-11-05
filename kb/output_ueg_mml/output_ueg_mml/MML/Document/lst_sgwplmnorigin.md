# 查询S-GW PLMN ID来源（LST SGWPLMNORIGIN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、SGW-C**

该命令用于查询SGW-C和PGW-C合一形态时SGW-C PLMN的获取方式。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询S-GW和P-GW合一形态时S-GW PLMN的获取方式：

```
%%LST SGWPLMNORIGIN:;%%
RETCODE = 0  操作成功

结果如下
--------
S-GW PLMN ID来源  =  P-GW PLMN
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称          | 输出项解释                                   |
|:---------------|:----------------------------------------|
| S-GW PLMN ID来源 | 用于控制SGW-C和PGW-C合一形态时SGW-C PLMN ID的获取方式。 |