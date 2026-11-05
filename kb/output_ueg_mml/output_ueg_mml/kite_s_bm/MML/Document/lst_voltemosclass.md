# 查询MOS分类区间值（LST VOLTEMOSCLASS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U**

该命令用于查询MOS分类区间值。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询MOS分类信息：

```
LST VOLTEMOSCLASS:;
```

```
RETCODE = 0  操作成功

MOS分类配置
-----------
MOS值为excellent和good之间的边界值  =  40
   MOS值为good和accept之间的边界值  =  36
   MOS值为accept和poor之间的边界值  =  31
      MOS值为poor和bad之间的边界值  =  26
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET VOLTEMOSCLASS的参数说明。