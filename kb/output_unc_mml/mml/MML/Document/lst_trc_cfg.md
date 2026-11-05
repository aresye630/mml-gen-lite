# 查询跟踪参数(LST TRC\_CFG)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查看Gb、Gb NS接口跟踪、随机用户跟踪和用户跟踪参数。用户跟踪表示查看以IMSI（International Mobile Subscriber Identity）或MSISDN（Mobile Station International ISDN Number）为标识的特定用户消息；随机用户跟踪表示基于设置的条件，随机性的选择满足触发条件的任何用户并上报其用户跟踪；接口跟踪表示查看接口的消息。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

无。

#### 使用实例

查询跟踪参数：

LST TRC\_CFG:;

```
%%LST TRC_CFG:;%%
RETCODE = 0  操作成功。

查询跟踪任务(LST TRC_CFG)
-------------------------
  允许的用户跟踪消息类型  =  Gn/Gp接口GTPU消息 & Gb接口SNDCP消息 & Gb接口PTP消息 & Gb接口LLC消息 & Iu接口SCCP消息 & Iu接口RANAP消息 & LCS消息 & Ge接口CAP消息 & Gs/Gd/Gr接口MAP消息 & Gs/Gd/Gr接口BSSAP+消息 & Iu/Gb接口SMS消息 & S1/Iu/Gb/Gn/Gp接口SM消息 & S1/Iu/Gb/Gn/Gp接口MM消息 & Iu/Gb接口SS消息 & S1AP消息 & DIAMETER消息
不允许的用户跟踪消息类型  =  NULL
  允许的用户跟踪消息方向  =  入口 & 出口
不允许的用户跟踪消息方向  =  NULL
      是否允许GB接口跟踪  =  NULL
   是否允许GB NS接口跟踪  =  NULL
            GTPU消息长度  =  0
    是否允许随机用户跟踪  =  是
(结果个数 = 1)
---    END
```

**说明** 

“是否允许GB接口跟踪”、“是否允许GB NS接口跟踪”的取值为“NULL”时，等同于取值为“Yes”。

#### 输出结果说明

参考**SET TRC\_CFG**命令的参数说明。