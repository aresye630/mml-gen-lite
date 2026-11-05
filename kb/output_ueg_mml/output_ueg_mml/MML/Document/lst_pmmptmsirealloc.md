# 查询Iu模式PTMSI重分配控制参数(LST PMMPTMSIREALLOC)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

此命令用于查询Iu模式PTMSI重分配控制参数。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询Iu模式PTMSI重分配控制参数所有信息：

LST PMMPTMSIREALLOC:;

```
%%LST PMMPTMSIREALLOC:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                 伴随RAU流程分配  =  否
P-TMSI重分配流程间隔时长（小时）  =  1
        P-TMSI重分配流程发起条件  =  PTMSI分配后
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**SET PMMPTMSIREALLOC**的参数说明。