# 查询TCP全局配置（LST TCPGLOBALCFG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询TCP全局配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询TCP全局配置：

```
LST TCPGLOBALCFG:;
```

```
        RETCODE = 0  操作成功

        结果如下
        -------------------------
        TCP FIN-Wait超时时间（s）  =  675
        TCP SYN-Wait超时时间（s）  =  75
                  TCP窗口值（KB）  =  8
                     PMTU功能开关  =  打开
              PMTU老化时间（min）  =  100
   IPv6 TCP FIN-Wait超时时间（s）  =  675
   IPv6 TCP SYN-Wait超时时间（s）  =  75
             IPv6 TCP窗口值（KB）  =  8
                最大MSS值（byte）  =  65535
            IPv6最大MSS值（byte）  =  65535
        (结果个数 = 1)
        ---   END
```

#### 输出结果说明

参见SET TCPGLOBALCFG的参数说明。