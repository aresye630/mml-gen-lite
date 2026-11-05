# 查询N26 RFSP老化时长(LST N26RFSPPLCY)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

该命令用于查询新侧MME从N26/S10接口收到老侧AMF/MME传递的RFSP的老化时长。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询N26RFSPPLCY参数：

LST N26RFSPPLCY:;

```
%%LST N26RFSPPLCY:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------
RFSP老化时长  =  60
    默认RFSP  =  0
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**SET N26RFSPPLCY**的参数说明。