# 查询PIM接口无效报文统计（DSP PIMINVPKTCNTIF）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示PIM接口无效报文统计。

#### 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                               |
|:--------------|:--------|:-------------------------------------------------------------------------------------------------------------------|
| IFNAME        | 接口名称    | 可选必选说明：必选参数 参数含义：该参数用来表示接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：请使用LST INTERFACE命令查看可用接口。               |
| ADDRESSFAMILY | 地址族     | 可选必选说明：必选参数 参数含义：该参数用于表示地址族类型。 数据来源：本端规划 取值范围：枚举类型。 ipv4unicast：IPv4单播。 默认值：无                                      |
| VRFNAME       | VPN实例名称 | 可选必选说明：可选参数 参数含义：该参数用来表示VPN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |

#### 使用实例

显示PIM接口无效报文统计：

```
DSP PIMINVPKTCNTIF:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,IFNAME="Ethernet64/0/3";
```

```
RETCODE = 0 操作成功

结果如下
-------------------------
查询返回结果
                               VPN实例名称 = _public_
                                    地址族 = IPv4单播
                                  接口名称 = Ethernet64/0/3
              目的地址非法的Assert报文计数 = 0
            报文源地址非法的Assert报文计数 = 0
            无效组播源地址的Assert报文计数 = 0
            无效组播组地址的Assert报文计数 = 0
            无效的报文长度的Assert报文计数 = 0
                无效的Payload的BSR报文计数 = 0
               无效的报文长度的BSR报文计数 = 0
              无效的Scope掩码的BSR报文计数 = 0
               无效组播组地址的BSR报文计数 = 0
        不是CBSR却收到BSR消息的BSR报文计数 = 0
                  无效BSR地址的BSR报文计数 = 0
               无效的哈希长度的BSR报文计数 = 0
               无效报文源地址的BSR报文计数 = 0
           无效地址列表的PIM Hello报文计数 = 0
         无效的报文长度的PIM Hello报文计数 = 0
     无效的Holdtime长度的PIM Hello报文计数 = 0
无效的LanPruneDelay长度的PIM Hello报文计数 = 0
  无效的DR Priority长度的PIM Hello报文计数 = 0
 无效的GenerationID长度的PIM Hello报文计数 = 0
           无效目的地址的PIM Hello报文计数 = 0
         无效报文源地址的PIM Hello报文计数 = 0
        无效组播源地址的Join/Prune报文计数 = 0
        无效组播组地址的Join/Prune报文计数 = 0
        无效的上游邻居的Join/Prune报文计数 = 0
        无效报文源地址的Join/Prune报文计数 = 0
          无效目的地址的Join/Prune报文计数 = 0
        无效的报文长度的Join/Prune报文计数 = 0
无效目的地址的Auto-RP Announcement报文计数 = 0
  无效源地址的Auto-RP Announcement报文计数 = 0
    无效下一跳Auto-RP Announcement报文计数 = 0
    无效源接口Auto-RP Announcement报文计数 = 0
   无效错误长度的Auto-RP Discovery报文计数 = 0
     无效RP地址的Auto-RP Discovery报文计数 = 0
       无效源地址Auto-RP Discovery报文计数 = 0
       无效组播组Auto-RP Discovery报文计数 = 0
         无效TTL Auto-RP Discovery报文计数 = 0
       无效源接口Auto-RP Discovery报文计数 = 0
(结果个数 = 1)
----- END
```

#### 输出结果说明

| 输出项名称                            | 输出项解释                                 |
|:---------------------------------|:--------------------------------------|
| VPN实例名称                          | 用来表示VPN实例名称。                          |
| 地址族                              | 用于表示地址族类型。                            |
| 接口名称                             | 用来表示接口名称。                             |
| 目的地址非法的Assert报文计数                | 用来表示目的地址非法的Assert报文计数。                |
| 报文源地址非法的Assert报文计数               | 用来表示报文源地址非法的Assert报文计数。               |
| 无效组播源地址的Assert报文计数               | 用来表示无效组播源地址的Assert报文计数。               |
| 无效组播组地址的Assert报文计数               | 用来表示无效组播组地址的Assert报文计数。               |
| 无效的报文长度的Assert报文计数               | 用来表示无效的报文长度的Assert报文计数。               |
| 无效的Payload的BSR报文计数               | 用来表示无效的Payload的BSR报文计数。               |
| 无效的报文长度的BSR报文计数                  | 用来表示无效的报文长度的BSR报文计数。                  |
| 无效的Scope掩码的BSR报文计数               | 用来表示无效的Scope掩码的BSR报文计数。               |
| 无效组播组地址的BSR报文计数                  | 用来表示无效组播组地址的BSR报文计数。                  |
| 不是CBSR却收到BSR消息的BSR报文计数           | 用来表示不是CBSR却收到BSR消息的BSR报文计数。           |
| 无效BSR地址的BSR报文计数                  | 用来表示无效BSR地址的BSR报文计数。                  |
| 无效的哈希长度的BSR报文计数                  | 用来表示无效的哈希长度的BSR报文计数。                  |
| 无效报文源地址的BSR报文计数                  | 用来表示无效报文源地址的BSR报文计数。                  |
| 无效地址列表的PIM Hello报文计数             | 用来表示无效地址列表的PIM Hello报文计数。             |
| 无效的报文长度的PIM Hello报文计数            | 用来表示无效的报文长度的PIM Hello报文计数。            |
| 无效的Holdtime长度的PIM Hello报文计数      | 用来表示无效的Holdtime长度的PIM Hello报文计数。      |
| 无效的LanPruneDelay长度的PIM Hello报文计数 | 用来表示无效的LanPruneDelay长度的PIM Hello报文计数。 |
| 无效的DR Priority长度的PIM Hello报文计数   | 用来表示无效的DR Priority长度的PIM Hello报文计数。   |
| 无效的GenerationID长度的PIM Hello报文计数  | 用来表示无效的GenerationID长度的PIM Hello报文计数。  |
| 无效目的地址的PIM Hello报文计数             | 用来表示无效目的地址的PIM Hello报文计数。             |
| 无效报文源地址的PIM Hello报文计数            | 用来表示无效报文源地址的PIM Hello报文计数。            |
| 无效组播源地址的Join/Prune报文计数           | 用来表示无效组播源地址的Join/Prune报文计数。           |
| 无效组播组地址的Join/Prune报文计数           | 用来表示无效组播组地址的Join/Prune报文计数。           |
| 无效的上游邻居的Join/Prune报文计数           | 用来表示无效的上游邻居的Join/Prune报文计数。           |
| 无效报文源地址的Join/Prune报文计数           | 用来表示无效报文源地址的Join/Prune报文计数。           |
| 无效目的地址的Join/Prune报文计数            | 用来表示无效目的地址的Join/Prune报文计数。            |
| 无效的报文长度的Join/Prune报文计数           | 用来表示无效的报文长度的Join/Prune报文计数。           |
| 无效目的地址的Auto-RP Announcement报文计数  | 用来表示无效目的地址的Auto-RP Announcement报文计数。  |
| 无效源地址的Auto-RP Announcement报文计数   | 用来表示无效源地址的Auto-RP Announcement报文计数。   |
| 无效下一跳Auto-RP Announcement报文计数    | 用来表示无效下一跳Auto-RP Announcement报文计数。    |
| 无效源接口Auto-RP Announcement报文计数    | 用来表示无效源接口Auto-RP Announcement报文计数。    |
| 无效错误长度的Auto-RP Discovery报文计数     | 用来表示无效错误长度的Auto-RP Discovery报文计数。     |
| 无效RP地址的Auto-RP Discovery报文计数     | 用来表示无效RP地址的Auto-RP Discovery报文计数。     |
| 无效源地址Auto-RP Discovery报文计数       | 用来表示无效源地址Auto-RP Discovery报文计数。       |
| 无效组播组Auto-RP Discovery报文计数       | 用来表示无效组播组Auto-RP Discovery报文计数。       |
| 无效TTL Auto-RP Discovery报文计数      | 用来表示无效TTL Auto-RP Discovery报文计数。      |
| 无效源接口Auto-RP Discovery报文计数       | 用来表示无效源接口Auto-RP Discovery报文计数。       |