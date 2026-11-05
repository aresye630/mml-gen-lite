# 查询CCO策略（LST CCOPOLICY）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询CCO策略。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

显示CCO策略：

```
LST CCOPOLICY:;
```

```
RETCODE = 0  操作成功

CCO策略:
------------
    BWMCAR策略开关  = ENABLE
 BWMSHAPING策略开关 = ENABLE
 大象流抑制策略开关 = ENABLE
     TO分流策略开关 = ENABLE
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET CCOPOLICY的参数说明。