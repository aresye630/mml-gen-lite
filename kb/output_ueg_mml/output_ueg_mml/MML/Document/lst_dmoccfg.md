# 查询Diameter流控控制参数(LST DMOCCFG)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询Diameter流控控制参数。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无

#### 使用实例

查询普通计费属性的配置信息：

LST DMOCCFG:;

```
%%LST DMOCCFG:;%%
RETCODE = 0  执行成功

操作结果如下:
-------------------------
 Diameter流控Sequence Number有效变化门限值  =  367778
             Diameter流控导致ULR拒绝原因值  =  53
             Diameter流控导致AIR拒绝原因值  =  45
(结果个数 = 1)

---    END
```

#### 输出结果说明

请参考**SET DMOCCFG**的参数标识。