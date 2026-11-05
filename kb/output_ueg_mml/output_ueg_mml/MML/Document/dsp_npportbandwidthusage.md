# 查询NP端口带宽实时利用率（DSP NPPORTBANDWIDTHUSAGE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询NP端口带宽实时利用率。

#### 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                          |
|:-------|:-------|:----------------------------------------------------------------------------------------------|
| RUID   | RU编号   | 可选必选说明：必选参数。 参数含义：RU编号。 数据来源：本端规划。 取值范围：整数类型，取值范围为0～4294967294。 默认值：无。 配置原则：使用DSP RU命令查询RU编号。 |

#### 使用实例

显示RUID为66的NP端口带宽实时利用率：

```
DSP NPPORTBANDWIDTHUSAGE: RUID=66;
RETCODE = 0  操作成功

结果如下
--------
端口编号  端口名称      附加信息            端口使能状态  物理端口状态  链路状态  端口带宽  告警上报阈值  告警清除阈值  接收方向告警状态  接收速率  接收方向带宽利用率  发送方向告警状态  发送速率  发送方向带宽利用率  从驱动获取端口速率成功次数  从驱动获取端口速率失败次数  

400       100G/NP0/12   internal interface  enabled       UP            UP        0Gbps     95%           90%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           4619                        
412       100G/NP0/142  internal interface  enabled       UP            UP        0Gbps     95%           90%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
0         100G/NP0/0    external interface  enabled       UP            UP        0Gbps     90%           80%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
4         100G/NP0/130  external interface  enabled       UP            UP        0Gbps     90%           80%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
8         100G/NP0/4    external interface  enabled       DOWN          INVALID   0Gbps     90%           80%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
12        100G/NP0/134  external interface  enabled       DOWN          INVALID   0Gbps     90%           80%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
200       25G/NP0/8     external interface  enabled       DOWN          INVALID   0Gbps     90%           80%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
201       25G/NP0/138   external interface  enabled       DOWN          INVALID   0Gbps     90%           80%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
202       25G/NP0/9     external interface  enabled       DOWN          INVALID   0Gbps     90%           80%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
203       25G/NP0/139   external interface  enabled       DOWN          INVALID   0Gbps     90%           80%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
208       25G/NP0/10    internal interface  enabled       UP            UP        0Gbps     95%           90%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
209       25G/NP0/11    internal interface  enabled       UP            UP        0Gbps     95%           90%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
210       25G/NP0/140   internal interface  enabled       UP            UP        0Gbps     95%           90%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
211       25G/NP0/141   internal interface  enabled       UP            UP        0Gbps     95%           90%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
404       25G/NP0/16    internal interface  enabled       UP            UP        0Gbps     95%           90%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
405       25G/NP0/17    internal interface  enabled       UP            UP        0Gbps     95%           90%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
406       25G/NP0/146   internal interface  enabled       UP            UP        0Gbps     95%           90%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
407       25G/NP0/147   internal interface  enabled       UP            UP        0Gbps     95%           90%           初始状态          0bps      0%                  初始状态          0bps      0%                  0                           0                           
(结果个数 = 18)

---    END
```

#### 输出结果说明

| 输出项名称         | 输出项解释                                                                     |
|:--------------|:--------------------------------------------------------------------------|
| 端口编号          | NP端口编号                                                                    |
| 端口名称          | NP端口名称                                                                    |
| 附加信息          | NP端口附加信息                                                                  |
| 端口使能状态        | 端口使能状态                                                                    |
| 物理端口状态        | NP端口的物理状态。 物理状态枚举类型： UP：端口物理UP。DOWN：端口物理DOWN。                             |
| 链路状态          | NP端口的链路状态。 链路状态枚举类型： UP：链路已链接。DOWN：链路已中断。INVALID：链路状态无效。SUBHEALTHY：链路亚健康。 |
| 端口带宽          | 端口带宽                                                                      |
| 告警上报阈值        | “ALM-89006 NP接口流量带宽利用率超过告警阈值”告警上报阈值                                       |
| 告警清除阈值        | “ALM-89006 NP接口流量带宽利用率超过告警阈值”告警清除阈值                                       |
| 接收方向告警状态      | 接收方向“ALM-89006 NP接口流量带宽利用率超过告警阈值”告警状态： 0：初始状态 1：清除 2：上报                   |
| 接收速率          | 接收速率                                                                      |
| 接收方向带宽利用率     | 接收方向带宽利用率                                                                 |
| 发送方向告警状态      | 发送方向“ALM-89006 NP接口流量带宽利用率超过告警阈值”告警状态： 0：初始状态 1：清除 2：上报                   |
| 发送速率          | 发送速率                                                                      |
| 发送方向带宽利用率     | 发送方向带宽利用率                                                                 |
| 从驱动获取端口速率成功次数 | 从驱动获取端口速率成功次数                                                             |
| 从驱动获取端口速率失败次数 | 从驱动获取端口速率失败次数                                                             |