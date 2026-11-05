# 查询CP Data流控参数(LST CPDATAFLOWCTRL)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

此命令用于查询当前配置的CP Data流控参数。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug。

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组。

#### 参数说明

无。

#### 使用实例

查询CP Data流控参数：

`LST CPDATAFLOWCTRL:;`

```
%%LST CPDATAFLOWCTRL:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------

CP Data CPU 过载流控功能开关 = 打开
           T3448最小值（秒） = 500
           T3448最大值（秒） = 800
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**SET CPDATAFLOWCTRL**的参数说明。