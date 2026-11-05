# 查询本地APNNI组(LST LOCALAPNNIGP)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

该命令用于查询本地APNNI组信息。定制APN纠正功能会引用该配置参数APNNIGRPID，可参考**ADD SMACTCTRL**命令的APNNIGRPID参数说明。

#### 注意事项

- 该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询LOCALAPNNI组信息。

LST LOCALAPNNIGP:;

```
%%LST LOCALAPNNIGP:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
本地APNNI组号  =  1
        APNNI  =  HUAWEI1.COM
  APNNI优先级  =  1
(结果个数 = 1)

---    END
```

#### 输出结果说明

请参考**ADD LOCALAPNNIGP**命令的参数说明。