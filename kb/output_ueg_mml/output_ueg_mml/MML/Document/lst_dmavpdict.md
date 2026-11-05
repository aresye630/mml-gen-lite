# 查询Diameter AVP表(LST DMAVPDICT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询Diameter数据字典。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询Diameter数据字典：

LST DMAVPDICT:;

```
%%LST DMAVPDICT:;%%
RETCODE = 0  执行成功。

操作结果如下
-------------------------
        字典名称  =  6
        信元名称  =  129
        信元编码  =  1032
      Vendor标识  =  10415
        信元类型  =  DIAM_AVP_TYPE_UINT32
        信元标记  =  DIAM_AVP_FLAG_V_PRESENT
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**MOD DMAVPDICT**的参数标识。