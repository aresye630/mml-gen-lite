# 查询缺省NI策略(LST DFTNIPLCY)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

该命令用于查询缺省NI策略。

#### 注意事项

- 此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询MME的缺省NI(Network Identity)策略。

LST DFTNIPLCY:;

```
%%LST DFTNIPLCY:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
基于APN下发缺省NI功能开关  =  开启
           缺省NI取值策略  =  ADD AREAMMINFO配置的缺省NI&SET MMEPCFFUNC配置的缺省NI&ADD MNO配置的缺省NI&ADD MVNO配置的缺省NI&SET PCRFPLCY配置的缺省NI&ADD USRMMINFO配置的缺省NI
     是否使用最小签约数据  =  NO
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见**SET DFTNIPLCY**的参数说明。