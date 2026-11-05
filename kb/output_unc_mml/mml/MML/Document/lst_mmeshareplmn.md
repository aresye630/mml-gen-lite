# 查询MME的共享PLMN(LST MMESHAREPLMN)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

此命令用于查看MME的共享PLMN。

#### 注意事项

此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查看MME的共享PLMN：

LST MMESHAREPLMN:;

```
%%LST MMESHAREPLMN:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
移动国家码  =  123
  移动网号  =  01
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**ADD MMESHAREPLMN**的参数说明。