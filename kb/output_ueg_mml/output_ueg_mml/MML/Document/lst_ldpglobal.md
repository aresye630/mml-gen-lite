# 查询LDP全局配置（LST LDPGLOBAL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询LDP全局配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询LDP全局配置：

```
LST LDPGLOBAL:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
           MTU私有信令能力  =  ENABLE
           MTU标准信令能力  =  DISABLE
                  触发策略  =  主机
            IP地址前缀名称  =  NULL
                    GR能力  =  DISABLE
       会话重链接时间（s）  =  300
          LSP恢复时间（s）  =  300
   对端存活定时器时间（s）  =  600
      BackOff初始时间（s）  =  15
      BackOff最大时间（s）  =  120
          动态通告能力使能  =  DISABLE
禁止建立代理Egress LDP LSP  =  FALSE
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见SET LDPGLOBAL的参数说明。