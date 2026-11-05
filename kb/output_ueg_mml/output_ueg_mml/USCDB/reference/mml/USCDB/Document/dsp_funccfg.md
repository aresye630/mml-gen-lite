# 查询业务配置信息(DSP FUNCCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于请求系统显示安装的产品业务配置信息。

## 注意事项

该命令只支持网元类型“HSS9860”。

## 参数说明

| 参数标识        | 参数名称   | 参数说明                   |
|:------------|:-------|:-----------------------|
| SERVICETYPE | 网元类型   | 用于请求系统显示哪个网元类型的资源配置信息。 |

## 使用实例

查询“网元类型”为“HSS9860”的资源配置信息。

```
DSP FUNCCFG: SERVICETYPE="HSS9860";
```

```
%%DSP FUNCCFG: SERVICETYPE="HSS9860";%%
RETCODE = 0  操作成功

操作结果
--------
          DevicName  =  HLR
          DevicType  =  HLR9820
      DevicHardware  =  OSTA
      DevicProvider  =  HuaWei
      HLRMaxNumImsi  =  0
    HLRMaxNumMsisdn  =  0
HLRmaxNumPdpAddress  =  0
      AUCMaxNumImsi  =  0
       ISSEPARATING  =  0
(结果个数 = 1)

---    END
```

## 输出结果说明

各输出项含义请参见**SET FUNCCFG**命令的参数说明。