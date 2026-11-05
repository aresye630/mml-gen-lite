# 查询TCP优化策略组合优先级（LST TOPLYPRIORITY）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询TCP优化策略组合优先级。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

运营商需要查询所有的TCP优化策略组合优先级：

```
LST TOPLYPRIORITY:;
```

```
RETCODE = 0  操作成功

TCP优化策略组合优先级
----------------
配置类型           优先级
TO_MATCH_ALL       7
TO_MATCH_RAT_CELL  6
TO_MATCH_CELL_IMSI 5
TO_MATCH_RAT_IMSI  4
TO_MATCH_RAT       3
TO_MATCH_CELL      2
TO_MATCH_IMSI      1
(结果个数 = 7)

---    END
```

#### 输出结果说明

参见SET TOPLYPRIORITY的参数说明。