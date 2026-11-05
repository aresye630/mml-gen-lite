# 查询SGsAP协议兼容性(LST SGSAPCMPT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

该命令用于查询SGsAP接口协议兼容性开关参数。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询SGsAP协议兼容性：

LST SGSAPCMPT:;

```
%%LST SGSAPCMPT:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                     TAI  =  按协议定义携带
                   E-CGI  =  按协议定义携带
TMSI based NRI container  =  不携带
             设置特殊LAI  =  否
                     LAI  =  NULL
          UE不可达原因值  =  UE不可达
(结果个数 = 1)

---    END
```

#### 输出结果说明

请参考命令**SET SGSAPCMPT**参数说明。