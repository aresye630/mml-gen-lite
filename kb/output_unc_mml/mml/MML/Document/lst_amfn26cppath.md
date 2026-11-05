# 查询AMF N26消息抄送路径（LST AMFN26CPPATH）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME、AMF**

该命令用于查询AMF N26消息抄送路径相关的参数。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug。

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组。

#### 参数说明

无。

#### 使用实例

查询AMF N26消息抄送路径：

LST AMFN26CPPATH:;

```
%%LST AMFN26CPPATH:;%%
RETCODE = 0  操作成功

输出结果如下
------------------------
        抄送路径开关  =  打开
          IP地址类型  =  IPV4类型
       MME侧IPv4地址  =  192.168.1.1
       MME侧IPv6地址  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
       AMF侧IPv4地址  =  192.168.2.2
       AMF侧IPv6地址  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
             VPN名称  =  _abc_
            抄送增强  =  关闭
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET AMFN26CPPATH的参数说明。