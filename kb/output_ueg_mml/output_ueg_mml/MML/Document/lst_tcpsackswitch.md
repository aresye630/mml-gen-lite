# 查询TCP SACK开关配置（LST TCPSACKSWITCH）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-C、PGW-C、SMF**

LST TCPSACKSWITCH命令用来查询Gx，Gy支持SACK选项情况。

#### 注意事项

该命令执行后对新数据流生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询Gx，Gy接口TCP支持SACK情况命令为：

```
LST TCPSACKSWITCH:;
```

```
RETCODE = 0  操作成功

TCP SACK 开关
-------------
Gx接口TCP协议支持SACK选项开关  =  允许
Gy接口TCP协议支持SACK选项开关  =  允许
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET TCPSACKSWITCH的参数说明。