# 查询微服务迁移过程（LST L3SERVICEDUALUPG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

灰度升级中，执行此命令，用于查询微服务迁移过程。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询服务名为AM的微服务迁移流程信息：

```
%%LST L3SERVICEDUALUPG:;%%
RETCODE = 0  操作成功

结果如下
--------
 L3Service  =  AM
OldVersion  =  21.1
NewVersion  =  21.5
 OldPODNum  =  5
 NewPODNum  =  7
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称      | 输出项解释            |
|:-----------|:-----------------|
| L3Service  | 该参数用于标识一个微服务。    |
| OldVersion | 该参数用于标识一个老版本。    |
| NewVersion | 该参数用于标识新版本。      |
| OldPODNum  | 该参数用于标识老pod数量。   |
| NewPODNum  | 该参数用于标识新版本pod数量。 |