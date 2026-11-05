# 查询检测用户信息（DSP SESSIONDETECT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询检测会话信息。

#### 注意事项

- 该命令执行后立即生效。
- 使用该命令查询前，需要通过SET SESSIONDETECT命令配置检测用户功能开关为开启。
- 每次执行DSP命令，每POD最多回显50个用户信息，下一次查询显示下一批次的用户信息。
- 检测用户被检测时间小于一个周期无法显示带宽信息，界面回显NULL。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识   | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                     |
|:-------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI   | 用户IMSI号 | 可选必选说明：可选参数 参数含义：用户的IMSI信息。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。 默认值：无 配置原则：无 |

#### 使用实例

查询检测用户信息：

```
DSP SESSIONDETECT:;
```

```
RETCODE = 0 操作成功

Session detect info
--------------
Session Detect Info

No   IMSI    APN   IPv4Addr   IPv6Addr   UpLinkBw(bps)  DnLinkBw(bps)  IdleTime (min)    PodName     Round
1    imsi1   apn1  xxx        xxx        xxx            xxx            xxx               xxx         xxx
2    imsi2   apn2  xxx        xxx        xxx            xxx            xxx               xxx         xxx
3    imsi3   apn3  xxx        xxx        xxx            xxx            xxx               xxx         xxx
All sessions have been displayed. 
 
(结果个数 = 1)
--- END
```

#### 输出结果说明

| 输出项名称                            | 输出项解释                                 |
|:---------------------------------|:--------------------------------------|
| IMSI                             | 国际移动用户标识。                             |
| APN                              | APN名称。                                |
| IPv4Addr                         | 用户IPv4地址。                             |
| IPv6Addr                         | 用户IPv6地址。                             |
| UpLinkBw(bps)                    | 上行数据报文真实可达到速率，如果被检测用户处于第一个周期显示为NULL。  |
| DnLinkBw(bps)                    | 下行数据报文真实可达到速率, 如果被检测用户处于第一个周期显示为NULL。 |
| IdleDuration (min)               | 用户真实空闲时长。                             |
| All sessions have been displayed | 该输出表示所有检测会话都已经显示。                     |