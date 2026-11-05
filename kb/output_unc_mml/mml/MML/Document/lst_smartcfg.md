# 查询智能用户功能（LST SMARTCFG）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

该命令用于查询SMART用户功能。包括SMART用户识别功能、识别SMART用户的SERVICE REQUEST门限、SMART用户是否禁止启用DT功能和SMART用户是否禁止启用去活非活动PDP功能。

#### 注意事项

无

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询智能用户功能：

LST SMARTCFG:;

```
%%LST SMARTCFG:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                  是否启用SMART用户识别功能  =  是
识别SMART用户的SERVICE REQUEST门限(times/h)  =  60
                SMART用户是否禁止启用DT功能  =  否
     SMART用户是否禁止启用去活非活动PDP功能  =  是
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**SET SMARTCFG**的参数说明。