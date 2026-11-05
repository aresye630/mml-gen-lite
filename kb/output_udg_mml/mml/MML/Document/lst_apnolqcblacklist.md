# 查询过载限速APN黑名单（LST APNOLQCBLACKLIST）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询过载限速APN黑名单。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询过载限速APN黑名单：

```
LST APNOLQCBLACKLIST:;
```

```
RETCODE = 0  操作成功

结果如下
-----------------------
APN

testapn   
testapn1  
(结果个数 = 2)

---    END
```

#### 输出结果说明

参见ADD APNOLQCBLACKLIST的参数说明。