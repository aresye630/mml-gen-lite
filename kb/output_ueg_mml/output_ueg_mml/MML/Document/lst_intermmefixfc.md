# 查询Inter-MME接入固定速率流控功能相关参数(LST INTERMMEFIXFC)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

该命令用于查询Inter-MME接入固定速率流控功能的相关参数。

#### 注意事项

无。

#### 本地用户权限

manage-ug;system-ug;monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无

#### 使用实例

查询Inter-MME接入固定速率流控功能的相关参数：

```
LST INTERMMEFIXFC:;
```

```
查询结果如下
-------------------------
                      流控粒度   =  单进程
         Attach接入流控功能开关  =  关闭
 Attach Request流控阈值作用范围  =  单进程
  Attach Request速率门限(个/秒)  =  4080
             SR接入流控功能开关  =  关闭
Service Request流控阈值作用范围  =  单进程
 Service Request速率门限(个/秒)  =  4080
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET INTERMMEFIXFC的参数说明。