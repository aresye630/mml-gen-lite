# 显示LMF会话数（DSP LMFSESSNUM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于显示LMF当前会话数，即所显示的LMF上的当前用户数。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

假如运营商想要显示LMF当前会话数：

```
DSP LMFSESSNUM:;
```

```
RETCODE = 0  操作成功

LMF会话数信息
-------------
Result  =  
                           Pod Name = lcs-e-pod-66644b8459-t2z4h
         LMF User Session Number(s) = 0

     All LMF User Session Number(s) = 0
(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称                          | 输出项解释        |
|:-------------------------------|:-------------|
| Pod Name                       | pod的名称。      |
| LMF User Session Number(s)     | LMF当前接入的会话数。 |
| All LMF User Session Number(s) | LMF接入的所有会话数。 |