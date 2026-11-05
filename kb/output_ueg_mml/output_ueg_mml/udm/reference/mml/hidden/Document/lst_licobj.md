# 查询License统计对象(LST LICOBJ)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询当前系统中的License控制项测量对象。License控制项测量对象是指将每一个License控制项作为一个测量对象来统计该license控制项授权的用户数量。

主要用于网管获取License控制项测量对象。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询当前系统中的License统计对象：

```
LST LICOBJ:;
```

```
%%LST LICOBJ:;%%
RETCODE = 0  操作成功

查询结果如下
------------
 License统计对象ID  License统计对象名称                            

 1                  用户区域漫游限制                               
 2                  漫游Local Breakout功能                         
 3                  通配APN功能                                    
 4                  基于MME列表的EPC漫游限制                       
 5                  基于PLMN列表的EPS漫游限制                      
 6                  多HPLMN                                        
 7                  SRVCC                                          
 8                  IP短消息互通                                   
 9                  CSFB                                                                              
 18                 防双活功能                                     
 19                 移动终呼漫游前转(MTRF)                         
 20                 最小化路测(MDT)                                
 21                 多媒体优先级业务(MPS)                                                     
 23                 Non-3GPP接入                                   
 31                 支持S-CSCF网络容灾用户数量-每用户                
 32                 共享IMPU用户数量-每用户                        
 33                 支持Sh接口Noti-Eff功能用户数量-每用户          
 34                 支持漫游感知业务用户数-每用户                                     
 36                 支持VoLTE基础特性-每用户                       
 38                 VoLTE Multi-SIM                                
 0                  HSS支持与HLR互操作                       
 12                 多方通话(MPTY)                       
 10                 OCSI合同用户数                       
 11                 TCSI合同用户数                       
 13                 LCS位置定位业务                       
 14                 显式呼叫转移业务(ECT)                       
 16                 语音彩铃业务                       
 37                 增强多级优先和抢占业务(eMLPP)                       
 39                 DIC合同用户数                       
 40                 PLMNSS合同用户数                       
 41                 CCBS合同用户数                       
 15                 最大Multi-SIM合同用户数                       
 17                 SIM卡关联                       
 42                 短消息地址重定向                       
 22                 LTE/VoLTE自动开户                       
 24                 增强的鉴权,采用EIA鉴权的IMPI数量-每用户                       
 25                 增强的鉴权,采用EAA鉴权的IMPI数量-每用户                       
 26                 增强的鉴权,采用NBA鉴权的IMPI数量-每用户                       
 27                 增强的鉴权,采用AKA鉴权的IMPI数量-每用户                       
 28                 HSS BE基本软件,采用HDA鉴权的IMPI数量-每用户                       
 29                 增强的鉴权,采用TAA鉴权的IMPI数量-每用户                       
 30                 HSS BE基本软件,HSS BE 的Subscription数量-每用户                       
 35                 HSS FE 用户数量-每用户                       
(结果个数 = 43)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。表1列出的是该命令的输出项解释。

| 输出项名称         | 输出项解释                  |
|:--------------|:-----------------------|
| License统计对象ID | 用于标识一个License统计对象的对象ID |
| License统计对象名称 | 用于标识一个License统计对象的对象名称 |