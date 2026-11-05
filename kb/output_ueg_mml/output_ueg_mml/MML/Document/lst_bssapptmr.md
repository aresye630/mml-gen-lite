# 查询BSSAPP协议定时器表(LST BSSAPPTMR)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

此命令用于查询BSSAPP定时器长度配置。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询BSSAPP定时器长度配置：

LST BSSAPPTMR:;

```
%%LST BSSAPPTMR:;%%
RETCODE = 0  操作成功。

查询BSSAPP定时器表
------------------
  等待SPP启动定时器(min)  =  3
    等待VLR可达定时器(s)  =  45
       位置更新定时器(s)  =  15
       GPRS分离定时器(s)  =  4
        GPRS分离重发次数  =  2
   显式IMSI分离定时器(s)  =  4
    显式IMSI分离重发次数  =  2
   隐式IMSI分离定时器(s)  =  4
    隐式IMSI分离重发次数  =  2
   SGSN复位标志定时器(s)  =  8
SGSN复位VLR响应定时器(s)  =  4
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见命令**SET BSSAPPTMR**的参数说明。