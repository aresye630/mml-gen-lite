# 显示MEC会话数（DSP MECSESSNUM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：MPF**

该命令用于查询MEC当前会话数，即所查询的MPF上的当前用户数。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

假如运营商想要查询MEC当前会话数：

```
DSP MECSESSNUM;
```

```
RETCODE = 0  操作成功

Mec会话数信息
-------------
Result  =  
                           Pod Name = mpfisu-pod-0
        Nxua User Session Number(s) = 1
                           Pod Name = mpfisu-pod-1
        Nxua User Session Number(s) = 3

    All Nxua User Session Number(s) = 4
(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称                           | 输出项解释            |
|:--------------------------------|:-----------------|
| Pod Name                        | pod的名称。          |
| Nxua User Session Number(s)     | Nxua当前接入的MEC会话数。 |
| All Nxua User Session Number(s) | Nxua接入的所有MEC会话数。 |