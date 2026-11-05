# 查询Radius服务器组（LST RDSSVRGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用来查询RADIUS SERVER GROUP配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称                  | 参数说明                                                                                 |
|:--------------|:----------------------|:-------------------------------------------------------------------------------------|
| RDSSVRGRPNAME | Radius Server Group名称 | 可选必选说明：可选参数 参数含义：该参数用于指定RADIUS服务器组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无 |

#### 使用实例

查询Radius服务器组：

```
LST RDSSVRGRP:RDSSVRGRPNAME="rsg";
```

```
RETCODE = 0  操作成功。

Radius Server Group
-------------------
                        Radius Server Group名称  =  rsg
                                           模式  =  主备模式
      Accounting Request ON应答之前是否激活用户  =  禁止
                             利用鉴权服务器计费  =  禁止
                                         DSCP值  =  255
                               支持可选计费消息  =  禁止
Accounting Request On/Off消息间的时间间隔（秒）  =  9
                  Accounting Request On重发次数  =  3
             Accounting Request On超时时间 (秒)  =  3
                 Accounting Request Off重发次数  =  3
             Accounting Request Off超时时间(秒)  =  3
              Radius Accounting Request重发次数  =  3
         Radius Accounting Request超时时间 (秒)  =  3
          Radius Authentication Request重发次数  =  3
     Radius Authentication Request超时时间 (秒)  =  3
                 Radius Accounting超时时长 (秒)  =  12
          Radius计费服务器Down状态保持时长 (秒)  =  180
                  Radius鉴权服务器超时时长 (秒)  =  12
          Radius鉴权服务器Down状态保持时长 (秒)  =  180
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见ADD RDSSVRGRP的参数说明。