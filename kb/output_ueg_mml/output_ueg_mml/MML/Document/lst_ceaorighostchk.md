# 查询对Gy接口的cea消息中的Origin-Host检查开关（LST CEAORIGHOSTCHK）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询Diameter对Gy接口的cea消息中的Origin-Host检查开关。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询Diameter对Gy接口的cea消息中的Origin-Host检查开关，则可按如下配置：

```
LST CEAORIGHOSTCHK:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
检查Gy的CEA消息中的Origin-Host  =  禁止
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见SET CEAORIGHOSTCHK的参数说明。