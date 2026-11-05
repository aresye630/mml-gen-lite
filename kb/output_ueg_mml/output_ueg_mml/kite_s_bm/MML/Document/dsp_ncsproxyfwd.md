# 显示NETCONF代理转发策略（DSP NCSPROXYFWD）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示NETCONF代理转发策略。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

无。

#### 使用实例

显示NETCONF代理转发策略：

```
DSP NCSPROXYFWD:;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------

目标          VNFC标识    VNFC类型      模块              命名空间     

SirpAgent=0   1           VNFP          LogSirp           http://www.huawei.com/netconf/wireless-sirp/1.0                                                
SirpAgent=0   0           VNFP          netconf           http://www.huawei.com/netconf/vrp                               
SirpAgent=0   0           VNFP          AlarmSirp         http://www.huawei.com/netconf/wireless-sirp/1.0      
(结果个数 = 4)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释        |
|:--------|:-------------|
| 目标      | 代理转发的目的地。    |
| VNFC标识  | VNFC标识。      |
| VNFC类型  | VNFC类型。      |
| 模块      | 转发目标模块。      |
| 命名空间    | 转发目标模块的名字空间。 |