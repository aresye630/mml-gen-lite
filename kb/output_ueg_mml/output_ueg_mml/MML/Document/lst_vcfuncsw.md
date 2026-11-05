# 查询Voice Centric终端接入功能开关（LST VCFUNCSW）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME、AMF**

该命令用于查询Voice Centric终端接入功能开关。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 使用实例

查询Voice Centric终端接入功能开关，执行命令：

LST VCFUNCSW:;

```
%%LST VCFUNCSW:;%% 
RETCODE = 0  操作成功
输出结果如下 
------------------------ 
Function Switch  =  ENABLE 
(结果个数 = 1)  

---    END
```

#### 输出结果说明

请参考**SET VCFUNCSW** 的参数标识。