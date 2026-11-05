# 查询SMF的非Default QoS Flow配置（LST SMFNONDFTQOSCTL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

该命令用来查询SMF的非Default QoS Flow配置。

## 注意事项

MFBRUL、MFBRDL、GFBRUL、GFBRDL结果如果为0，说明未对该参数进行配置，不进行限速或控制。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                      |
|:---------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------|
| MCC      | 移动国家码  | 可选必选说明：可选参数  参数含义：该参数用于表示组成QoS控制的用户归属地网络的移动国家码信息。  数据来源：本端规划  取值范围：字符串类型，输入长度是3。  默认值：无  配置原则：无                                           |
| MNC      | 移动网号   | 可选必选说明：可选参数  参数含义：该参数用于表示组成QoS控制的用户归属地网络的移动网号信息。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是2~3。  默认值：无  配置原则：无                                        |
| CTRLTYPE | 控制类型   | 可选必选说明：可选参数  参数含义：该参数用于表示组成QoS控制的缺省QoS类型。  数据来源：全网规划 取值范围： DNN_LEVEL（DNN级别）GLOBAL_LEVEL（整系统级别）  默认值：无  配置原则：无                             |
| DNN      | DNN    | 可选必选说明：该参数在"CTRLTYPE"配置为"DNN_LEVEL"时为条件必选参数。  参数含义：该参数用于指定组成QoS控制的DNN，即用户请求的DNN。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~63。区分大小写。  默认值：无  配置原则：无 |

## 使用实例

查询I-SMF/V-SMF上所有PLMN的Non Default QoS Flow配置，执行如下命令:

```
%%LST SMFNONDFTQOSCTL:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
Mobile Country Code  Mobile Network Code  Control Type  DNN   Maximum Uplink Rate (kbit/s)  Maximum Downlink Rate (kbit/s)  Uplink Guaranteed Rate (kbit/s)  Downlink Guaranteed Rate (kbit/s)  Bandwidth Action  Allowed 5QI List Index  Bind Allowed 5QI List  Allowed ARP List  Bind Allowed ARP List  

460                  00                   GLOBAL_LEVEL  null  0                             0                               0                                0                                  reject            65535                   DISABLE                65535             DISABLE                
460                  01                   GLOBAL_LEVEL  null  1                             0                               0                                0                                  reject            1                       ENABLE                 65535             DISABLE                
460                  09                   GLOBAL_LEVEL  null  0                             0                               0                                0                                  reject            1                       ENABLE                 65535             DISABLE                
470                  00                   DNN_LEVEL     aaa   0                             3                               0                                0                                  reject            65535                   DISABLE                3                 ENABLE                 
501                  00                   GLOBAL_LEVEL  null  0                             0                               0                                0                                  reject            65535                   DISABLE                1                 DISABLE                
(Number of results = 5)

---    END
```

## 输出结果说明

| 输出项名称          | 输出项解释                           |
|:---------------|:--------------------------------|
| 移动国家码          | 该参数用于表示组成QoS控制的用户归属地网络的移动国家码信息。 |
| 移动网号           | 该参数用于表示组成QoS控制的用户归属地网络的移动网号信息。  |
| 控制类型           | 该参数用于表示组成QoS控制的缺省QoS类型。         |
| DNN            | 该参数用于指定组成QoS控制的DNN，即用户请求的DNN。   |
| 上行最大速率 (千比特/秒) | 该参数用于指定组成QoS控制的上行最大速率 (千比特/秒)。  |
| 下行最大速率 (千比特/秒) | 该参数用于指定组成QoS控制的下行最大速率 (千比特/秒)。  |
| 上行保证速率 (千比特/秒) | 该参数用于指定组成QoS控制的上行保证大速率 (千比特/秒)。 |
| 下行保证速率 (千比特/秒) | 该参数用于指定组成QoS控制的下行保证大速率 (千比特/秒)。 |
| 超过带宽的处理        | 该参数用于表示超过带宽的处理行为。               |
| 允许的5QI列表索引     | 该参数用于指定允许的5QI列表索引，用来绑定允许的5QI列表。 |
| 绑定允许的5QI列表     | 该参数用于指定是否绑定允许的5QI列表。            |
| 允许的ARP列表       | 该参数用于指定允许的ARP列表索引，用来绑定允许的ARP列表。 |
| 绑定允许的ARP列表     | 该参数用于指定是否绑定允许的ARP列表。            |