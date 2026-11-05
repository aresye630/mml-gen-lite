# 查询Bi口IPCONVERGENCE开关状态（LST IPCONVERGENCE）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：NCG**

该命令用于查询Bi口IPCONVERGENCE开关状态。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询Bi口IPCONVERGENCE开关状态：

```
LST IPCONVERGENCE:;
```

```
RETCODE = 0  操作成功

结果如下:
---------
      Bi口IPCONVERGENCE 开关  =  开启          
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见SET IPCONVERGENCE的参数说明。