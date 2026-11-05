# 显示SSH服务器的错误日志（DSP SSHSERRORLOG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询SSH服务器的错误日志。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                         |
|:----------------|:-------|:-------------------------------------------------------------------------------------------------------------|
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### 使用实例

查询SSH服务器的错误日志：

```
DSP SSHSERRORLOG:SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
    时间  =  2024-02-23, 08:27:24:432
日志信息  =  LogOff. TCP disconnect from client(FD=133, ErrorCode=0x201d), User=HAFG, IP=192.168.0.1, SockId=133, ChId=135339, Trace=StartTime:2024-02-23:08-05-26. snd sshver(0)->rev sshver(0)->snd keyinit(0)->rev keyinit(0)->rev curveinit(0)->snd curv... new glbreq(418)->rev new glbreq(538)->rev new glbreq(658)->rev new glbreq(778)->rev new glbreq(898)->rev new glbreq(1018)->rev new glbreq(1138)->rev new glbreq(1258)->rev chnlclose(1318)->snd discnt(1318)->snd camldiscntreq(1318)->END
(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释   |
|:--------|:--------|
| 时间      | 日志时间。   |
| 日志信息    | 日志信息。   |