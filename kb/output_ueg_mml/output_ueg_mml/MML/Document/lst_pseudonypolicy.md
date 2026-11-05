# 查询CHR假名化本地策略（LST PSEUDONYPOLICY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、SGSN、MME、SGW-C、PGW-C、NCG、NEF、NWDAF、SMSF、SCF**

该命令用于查询CHR假名化本地策略的属性配置信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

无

## 使用实例

如果想查询CHR假名化本地策略的属性配置，可以用如下命令：

```
%%LST PSEUDONYPOLICY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
CHR pseudony local policy switch  =  ON
   CHR pseudony local policy key  =  *****
(Number of results = 1)
```

## 输出结果说明

| 输出项名称        | 输出项解释                               |
|:-------------|:------------------------------------|
| CHR假名化本地策略开关 | 该参数用于设置CHR假名化本地策略是否开启。              |
| CHR假名化本地策略口令 | 该参数用于设置CHR假名化本地策略的口令，口令用于生成密钥并进行加密。 |