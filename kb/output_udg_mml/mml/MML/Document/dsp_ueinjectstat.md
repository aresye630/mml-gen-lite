# 查询UE灌包状态（DSP UEINJECTSTAT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询当前灌包UE的灌包状态。

#### 注意事项

该命令显示的信息在执行命令ACT UEINJECTSEND失败时不会被重置。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询UE下行灌包状态：

```
DSP UEINJECTSTAT:;
```

```
RETCODE = 0 操作成功。

UE灌包状态信息
--------------------------
UE灌包状态 =
            SENDER  =  0
          ForceEnd  =  0
      TotalSendNum  =  0
      TotalSendFLow =  0
          CurrRate  =  0
(结果个数 = 1)
--- END
```

#### 输出结果说明

| 输出项名称         | 输出项解释               |
|:--------------|:--------------------|
| SENDER        | 发包状态，0为不在灌包，1为正在灌包。 |
| ForceEnd      | 灌包过载，0为未过载，1为过载。    |
| TotalSendNum  | 灌包个数。               |
| TotalSendFlow | 灌包流量，单位为千比特。        |
| CurrRate      | 灌包速率，单位为千字节/秒。      |