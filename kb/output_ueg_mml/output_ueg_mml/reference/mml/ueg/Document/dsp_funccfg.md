# 显示HLR配置信息(DSP FUNCCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

查询安装的产品形态配置管理资源信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询安装的产品形态配置管理资源信息。

```
DSP FUNCCFG:;
```

```
%%DSP FUNCCFG:;%%
RETCODE = 0  操作成功
操作结果如下
------------
                            设备名称  =  0
                            设备型号  =  HLR9820
                        设备硬件平台  =  OSTA
                          设备供应商  =  HuaWei
                      已配置2M端口数  =  0
                     已配置64k端口数  =  2
                最大可存储的IMSI个数  =  1
              最大可存储的MSISDN个数  =  1
               最大可存储的PDP地址数  =  0
                       备份的HLR编号  =  FFFFFFFFFFFFFFF
最大可存储的外网之间携转的MSISDN个数  =  0
                     MAP消息处理能力  =  0
                      最大M3ua链路数  =  0
                        网元功能类型  =  HLR
                  FE和BE是否分离部署  =  否
                           VNF实例ID  =  NULL
                       UDR VNF实例ID  =  NULL
                         UDR全量域名  =  NULL
                             UDR标签  =  NULL
                      网元IP获取方式  =  1
                           预留参数1  =  NULL
                           预留参数2  =  NULL
                        5G最大用户数  =  1
                    5G最大活动用户数  =  1
                        4G最大用户数  =  1
                    4G最大活动用户数  =  1
                    自动上报北向开关  =  否
(结果个数 = 1)
---    END
```