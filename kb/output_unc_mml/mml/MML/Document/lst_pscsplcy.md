# 查询联合接入策略(LST PSCSPLCY)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于查询联合接入策略。

#### 注意事项

无

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询联合接入策略：

```
+++    UNC/*MEID:0 MENAME:unc*/        2023-08-15 10:57:34 
O&M    #1018 
%%LST PSCSPLCY:;%% RETCODE = 0  操作成功  
查询结果如下 
------------           
            是否开启联合接入限制功能  =  否               
                联合接入限制通用条件  =  IMS APN&IMSCAP&STNSR                       
                        预设STN-SR值  =  NULL
                  预设STN-SR生效模式  =  与预设STN-SR不同时进行联合接入限制
                          白名单策略  =  HSS标识           
            是否开启联合附着限制功能  =  否            
             是否开启联合TAU限制功能  =  否     
      无IMS PDN连接时是否限制联合TAU  =  否               
                联合接入是否响应成功  =  是           
            UE发起CS业务时是否驻留4G  =  否     
      手动HSS Bypass时用户是否驻留4G  =  否                 
                  联合接入限制原因值  =  CS_DOMAIN_NOT_AVAILABLE(#18 CS domain not available)               
                是否开启无CS控制策略  =  否                   
                    无CS规划识别条件  =  TAILAI                       
                        用户识别条件  =  IMS APN&IMSCAP 
  无CS规划用户是否响应联合接入假成功  =  否 
  无CS规划的UE发起CS业务时是否驻留4G  =  是       
        无CS规划的联合接入限制原因值  =  CS_DOMAIN_NOT_AVAILABLE(#18 CS domain not available)    
     联合接入响应假成功时LAI填写策略  =  TAI映射                      
                       LAI固定填充值  =  NULL 
(结果个数 = 1)  

---    END
```