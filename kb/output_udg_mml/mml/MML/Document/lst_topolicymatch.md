# 查询TCP优化策略匹配规则（LST TOPOLICYMATCH）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询TCP优化策略匹配规则。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

运营商需要查询所有的TCP优化策略匹配规则：

```
LST TOPOLICYMATCH:;
```

```
RETCODE = 0  操作成功

TCP优化策略匹配规则
----------------
小区组名称          IMSI组名称        RAT类型    策略ID
TestCellGroupName   TestIMSIGroupName  NR         1
TestCellGroupName   TestIMSIGroupName  EUTRAN     2
(结果个数 = 2)

---    END
```

#### 输出结果说明

参见ADD TOPOLICYMATCH的参数说明。