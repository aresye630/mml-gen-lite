# 显示LCS UE无关信息（DSP LCSNONUEINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于显示对应基站ID的LCS UE无关信息。

#### 注意事项

- 该命令执行后立即生效。
- 该命令只显示TRP流程中获取到的TRP信息，不显示ADD PRRUNODE配置的。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                |
|:---------|:-------|:------------------------------------------------------------------------------------|
| GNODEBID | 基站ID   | 可选必选说明：必选参数 参数含义：该参数用于指定基站ID。 数据来源：全网规划 取值范围：整型数字类型，取值范围为0~4294967295。 默认值：无 配置原则：无 |

#### 使用实例

查询显示对应基站ID的LCS UE无关信息：

```
DSP LCSNONUEINFO: GNODEBID=190041;
```

```
RETCODE = 0  操作成功

LCS UE无关信息
--------------
LCS NG-RAN信息  =    
 Pod Name = lcs-e-pod-7d6fb8f855-spv7k
-------------------------------

                                gNodeB ID = 190041
                              Update Time = 20   
                        TRP Exchange Flag = 1    
                TRP Exchange Success Flag = 1    
                     TRP Re-Exchange Flag = 0    
          Number of TRP Exchange Failures = 0    
          TRP Exchange Failure Alarm Flag = 0    
                   CHOICE Reference Point = 1    
     Reference Point Coordinate Longitude = 0.000000
      Reference Point Coordinate Latitude = 0.000000
      Reference Point Coordinate Altitude = 0.000000

 TrpInfo Num : 10

TRP ID         NR Cell Identity    TRP Position Latitude    TRP Position Longitude   TRP Position Altitude    Coordinate ID  
1              0x02E65929A0        26.500000                38.520000                2.670000                 1              
2              0x02E65929A0        26.410000                28.920000                2.630000                 2              
3              0x02E65929A0        26.640000                15.570000                2.570000                 3              
4              0x02E65929A0        26.540000                3.350000                 2.780000                 4              
5              0x02E65929A0        2.960000                 3.350000                 2.800000                 5              
6              0x02E65929A0        16.560000                27.620000                2.820000                 6              
7              0x02E65929A0        16.010000                14.490000                3.070000                 7              
8              0x02E65929A0        15.740000                2.600000                 3.100000                 8              
9              0x02E65929A0        15.740000                2.600000                 3.100000                 9              
10             0x02E65929A0        15.740000                2.600000                 3.100000                 10             

AMF Instance ID                         AMF Information Update Time        Number of NonueN2 Subscription Failures   NonueN2 Subscription Failure Alarm Flag   
AMF_Instance_0                          27                                 0                                         0
 Pod Name = lcs-e-pod-7d6fb8f855-tncht
-------------------------------

There is no LcsNonueInfo!

(结果个数 = 2)

---    END
```

#### 输出结果说明

| 输出项名称                                   | 输出项解释                                                              |
|:----------------------------------------|:-------------------------------------------------------------------|
| gNodeB ID                               | 基站ID，表示发起过TRP流程的基站ID。                                              |
| Update Time                             | 当前时间距离基站更新时间的时间间隔，单位：秒。                                            |
| TRP Exchange Flag                       | TRP开关，决策是否要发起TRP流程，0代表不发起，1代表发起。                                   |
| TRP Exchange Success Flag               | 标记TRP是否执行成功，0代表不成功，1代表成功。                                          |
| TRP Re-Exchange Flag                    | 标记是否需要再次获取TRP，0表示不需要，1表示需要。                                        |
| Number of TRP Exchange Failures         | 表示获取失败的数量。                                                         |
| TRP Exchange Failure Alarm Flag         | 标记是否达到上报gNodeB的TRP信息获取失败告警阈值。                                      |
| CHOICE Reference Point                  | 代表参考点坐标类型，可以取值为0，1，2，3。0代表不可用的类型，1代表MAPID，2代表低精度参考点坐标，3代表高精度参考点坐标。 |
| Coordinate ID                           | MAPID值，取值为65535时，代表无效MAPID值。                                       |
| Reference Point Coordinate Longitude    | 参考点坐标经度。                                                           |
| Reference Point Coordinate Latitude     | 参考点坐标纬度。                                                           |
| Reference Point Coordinate Altitude     | 参考点坐标海拔。                                                           |
| TrpInfo Num                             | 当前基站获取到的TRP数量。                                                     |
| TRP ID                                  | 当前基站获取到的TRP ID。                                                    |
| NR Cell Identity                        | TRP所在小区的标识。                                                        |
| TRP Position Latitude                   | TRP参考点坐标纬度。                                                        |
| TRP Position Longitude                  | TRP参考点坐标经度。                                                        |
| TRP Position Altitude                   | TRP参考点坐标海拔。                                                        |
| AMF Instance ID                         | 基站对接的AMF标识。                                                        |
| AMF Information Update Time             | 当前时间距离AMF更新时间的时间间隔，单位：秒。                                           |
| Number of NonueN2 Subscription Failures | 表示NonueN2订阅失败的次数。                                                  |
| NonueN2 Subscription Failure Alarm Flag | 标记是否上报LCS UE无关的N2信息订阅失败告警。                                         |