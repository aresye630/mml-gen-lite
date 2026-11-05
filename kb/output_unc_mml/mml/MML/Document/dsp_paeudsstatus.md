# 显示UDS链路状态（DSP PAEUDSSTATUS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于显示UDS链路状态。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识   | 参数名称    | 参数说明                                                                                                       |
|:-------|:--------|:-----------------------------------------------------------------------------------------------------------|
| CELLID | Cell ID | 可选必选说明：必选参数  参数含义：该参数用于指定CELLID，可以通过使用命令DSP PAENODE获取。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无 |

## 使用实例

显示UDS链路状态：

```
%%DSP PAEUDSSTATUS: CELLID="sfpod-0__103__0";%%
RETCODE = 0  操作成功

结果如下
--------
    Cell ID  =  sfpod-0__103__0
UDS链路状态  =
UDS INFORMATION
ENDPOINT TYPE: Server
UDS FILE:/dev/shm/pae_perf_mode_s0.sock
ENDPOINT ID:2
PEER[0]
    ENDPOINT ID:3
    CONNECT FD:459
    CONNECT TIME:2024-05-20 11:28:30
    SEND COUNTER:6
    RECV COUNTER:6
PEER[1]
    ENDPOINT ID:4
    CONNECT FD:464
    CONNECT TIME:2024-05-20 11:28:30
    SEND COUNTER:7
    RECV COUNTER:7

UDS INFORMATION
ENDPOINT TYPE: Client
UDS FILE:/dev/shm/pae_perf_mode_s0.sock
ENDPOINT ID:3
PEER[0]
    ENDPOINT ID:0
    CONNECT FD:458
    CONNECT TIME:2024-05-20 11:28:30
    SEND COUNTER:6
    RECV COUNTER:6

(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                                |
|:--------|:-------------------------------------|
| Cell ID | 该参数用于指定CELLID，可以通过使用命令DSP PAENODE获取。 |
| UDS链路状态 | UDS链路状态信息。                           |