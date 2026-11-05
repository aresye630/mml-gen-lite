# 查询规则匹配测试结果（DSP TESTRULEMATCH）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用来获取匹配结果。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

显示规则匹配结果：

```
DSP TESTRULEMATCH:;
```

```
RETCODE = 0  Operation succeeded

Rule Match Result Information
-----------------------------
Match Result  =  
                      PCC Policy:
                       Rule Name = rule01
                     Filter Name = filter1l34
                Flow Filter Name = flowfilter1
               PccPolicyGrp Name = pccgp1
                   upUrr(ONLINE) = cbbid-34000
                 upUrrID(ONLINE) = 234000
                   dnUrr(ONLINE) = cbbid-34000
                 dnUrrID(ONLINE) = 234000
                  upUrr(OFFLINE) = cbbid-34000off
                upUrrID(OFFLINE) = 134000
                  dnUrr(OFFLINE) = cbbid-34000off
                dnUrrID(OFFLINE) = 134000

(Number of results = 1)

---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释     |
|:--------|:----------|
| 匹配结果    | 用于存放匹配结果。 |