# 查询Voice Centric终端接入参数配置（LST VCFUNCPARA）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME、AMF**

查询Voice Centric终端接入参数配置。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 使用实例

查询VC的基本参数配置：

LST VCFUNCPARA:;

```
%%LST VCFUNCPARA:;%% 
RETCODE = 0  操作成功  
输出结果如下 
------------------------ 
  Mobile country code  =  123 
  Mobile network code  =  00 
Authentication Domain  =  ims.mnc000.mcc123.3gppnetwork.org 
    Encryption Policy  =  OFF 
Registration Duration  =  3600 
   IMPU in SIP format  =  sip:+1234567890123@ims.mnc000.mcc123.3gppnetwork.org 
   IMPU in TEL format  =  tel:+1234567890123 
(结果个数 = 1) 
---    END
```

#### 输出结果说明

请参考**SET VCFUNCPARA** 的参数标识。