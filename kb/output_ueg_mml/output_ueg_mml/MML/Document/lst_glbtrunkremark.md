# 查询整机Trunk Remark配置（LST GLBTRUNKREMARK）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U**

该命令用于查询整机所有的Trunk Remark配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询整机的Trunk Remark配置：

```
LST GLBTRUNKREMARK:;
```

```
RETCODE = 0  操作成功

宽带集群重标记配置信息
----------------------
QCI  ARP的优先级别  标记类型  DSCP  AF级别  AF丢弃优先级  TOS值  DSCP值  

1    1              TOS       EF    0       0             3      0       
1    2              TOS       EF    0       0             5      0       
(结果个数 = 2)

---    END
```

#### 输出结果说明

参见ADD GLBTRUNKREMARK的参数说明。