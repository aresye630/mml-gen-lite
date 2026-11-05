# 查询本地LMF信息配置（LST GMLCLOCLMFINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询本地LMF Identification信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询本地LMF Identification信息：

```
LST GMLCLOCLMFINFO:;
```

```
RETCODE = 0  操作成功

本地LMF信息
---------------------
 NF实例标识  =  1465150f-32dc-496f-9e51-b204b0a44275
      LMF标识  =  lmf_identification_0
(结果条数 = 1)

---    END
```

#### 输出结果说明

参见ADD GMLCLOCLMFINFO的参数说明。