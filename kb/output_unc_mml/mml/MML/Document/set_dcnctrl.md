# 设置DCN控制参数(SET DCNCTRL)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于配置MME对专用核心网重选的控制方式。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识             | 参数名称                 | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:-----------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RESELECTPLCY     | 重选策略                 | 可选必选说明：可选参数 参数含义：该参数用于指定MME触发专用核心网重选时的执行策略。 数据来源：本端规划 取值范围：“IMMEDIATE(立即)”“DELAY(延缓)” 系统初始设置值：“IMMEDIATE(立即)” 配置原则：当需要快速完成重选流程时，可以将此参数配置为“IMMEDIATE(立即)”。此方式可能会导致用户正在进行的业务流程中断。当不希望业务流程中断，并且避免同一时刻大量用户执行重选流程时对网络产生波动，可以将此参数配置为“DELAY(延缓)”。此方式可能导致需要重选到其他专网的用户长时间驻留在本专网中。  说明： 当MME通过DCN迁移或者HSS通过签约数据变更需要触发专用核心网重选时，此参数的控制流程如下：IMMEDIATE：系统通过主动触发业务流程，让用户在空闲态发送TAU Request消息。MME在TAU流程中进行专用核心网重选处理。DELAY：系统等待用户在空闲态发送Attach Request或者TAU Request（不包括周期性TAU）消息时，通过给eNodeB发送Reroute NAS Request消息进行专用核心网重选。用户在空闲态发送周期性TAU消息时，通过GUTI重分配流程进行专用核心网重选。 |
| CONTAINUEUSGTYPE | 携带UE Usage Type      | 可选必选说明：可选参数 参数含义：该参数用于指定是否向新侧MME携带UE Usage Type。 数据来源：全网规划 取值范围：“NO(否)”“YES(是)” 系统初始设置值：“NO(否)” 配置原则：当对端网元不支持UE Usage Type时，配置该参数为“NO(否)”。  说明： 当该参数设置为“YES(是)”时，如果源侧存在UE USAGE TYPE，MME会在Attach流程的Identification Response消息、TAU流程的Context Response消息或者Handover流程Forward Relocation Request消息中携带UE USAGE TYPE到新侧MME，否则不携带。                                                                                                                                                                                                                      |
| UEUSGTYPECONPLCY | UE USAGE TYPE携带策略    | 可选必选说明：条件可选参数 参数含义：该参数用于指定向新侧MME携带的UE USAGE TYPE类型。 前提条件: 该参数在“携带UE Usage Type”参数配置为“YES(是)”后生效。 数据来源：全网规划 取值范围：“USED(正在使用的UE USAGE TYPE)”“SUBSCRIBE(签约的UE USAGE TYPE)” 系统初始设置值： “USED(正在使用的UE USAGE TYPE)”  说明： 当此参数配置为“SUBSCRIBE(签约的UE USAGE TYPE)”时，只填充从HSS获取的UE USAGE TYPE。当系统中没有有效的签约UE USAGE TYPE时，若特性相关license项“81202740 LKV2DECOR00 DECOR基础功能”和“82207914 LKV2DECOR01 DECOR”都开启，则向新侧MME携带长度字段为0的UE USAGE TYPE信元，否则不携带。                                                                                                                   |
| NONTAI           | 非广播TAI               | 可选必选说明：可选参数 参数含义：该参数用于指定非广播TAI，用于在GUTI重分配流程中下发给UE，触发UE主动发起TAU流程。 数据来源：全网规划 取值范围：9~10位字符串 系统初始设置值：0000000000 配置原则：TAI由MCC，MNC，TAC组成。MCC为3个BCD码字符，MNC为2个或者3个BCD码字符，填写时请遵循实际长度。TAC编码为16进制数，固定为4位，不足前面补0。非广播TAI需要与系统中的所有TAI不相同，系统中已有的TAI可以通过LST S1PAGING查看。  说明： 系统对已接入的用户进行专用核心网重选时会触发GUTI重分配流程。GUTI重分配消息中TA List信元会携带非广播TAI，终端收到之后会触发TAU流程。                                                                                                                                                                                                       |
| MMEGIQUERYPLCY   | MMEGI查询策略            | 可选必选说明：可选参数 参数含义：该参数用于指定用户所归属MMEGI（用户所属DCN的覆盖范围）的查询策略。 数据来源：全网规划 取值范围：枚举类型。“LOCAL(使用本地配置查询MMEGI)”“DNS(使用DNS查询MMEGI)” 系统初始设置值：“LOCAL(使用本地配置查询MMEGI)” 配置原则：如果希望以TAI粒度进行划分DCN的覆盖范围时，可以在DNS服务器使用对应TAI和UE USAGE TYPE完成DNS记录配置，此时参数选择“DNS(使用DNS查询MMEGI)”方式；如果希望以MME粒度划分DCN的覆盖范围时，通过ADD DCNMEMBER命令在UNC完成本地配置部署，此时参数选择“LOCAL(使用本地配置查询MMEGI)”方式。                                                                                                                                                                                                        |
| DNSROLLBACK      | 域名回退查询               | 可选必选说明：可选参数 参数含义：该参数用于控制在DNS查询网元IP地址时是否使用域名回退查询方式。如果选中对应网元参数，系统首次使用UE USAGE TYPE查询对应网元的DNS记录失败之后，将会不使用UE USAGE TYPE再进行一次DNS查询。 数据来源：全网规划 取值范围：位域类型。“MME（MME）”“SGW（SGW）”“PGW（PGW）” 系统初始设置值：“NULL” 配置原则：希望最大可能成功地完成某些网元选择时，可以将这些网元的控制开关选中。希望用户只能接入到UE USAGE TYPE对应的专用网络中某些网元时，可以取消勾选这些网元。 说明： SGW和PGW参数暂不支持。                                                                                                                                                                                                                                      |
| BACKOFFSW        | Backoff Timer分配开关    | 可选必选说明：可选参数 参数含义：该参数用于指定在附着流程或者TAU流程中，如果系统判断用户不能在本专网接入时向终端下发的拒绝消息中是否携带Backoff Timer信元。 数据来源：全网规划 取值范围：枚举类型。“OFF(关闭)”：当该开关关闭时，如果系统判断用户不能在本专网接入时，在附着/TAU流程的拒绝消息中不携带Backoff Timer。“ON(开启)：当该开关开启时，如果系统判断用户不能在本专网接入时，在附着/TAU流程的拒绝消息中携带Backoff Timer。” 系统初始设置值：“OFF(关闭)” 配置原则：当系统判断用户不能在本专网中服务而拒绝用户的NAS请求之后，期望用户不立即发起附着/TAU流程，可将此参数配置为“ON(开启)”。  说明： Backoff Timer为UE和网络启动的定时器，在该定时器时间内，UE不允许发起附着/TAU流程。                                                                                                                                             |
| MINBOT           | Back off timer最小值（秒） | 可选必选说明：条件可选参数 参数含义：本参数用于设置Back off timer的最小值，用于计算发给终端的附着拒绝消息或者TAU拒绝消息中的Back off timer时长。 前提条件：该参数在“Backoff Timer分配开关”配置为“ON(开启)”后生效。 数据来源：本端规划 取值范围：1～11160。 系统初始设置值：300                                                                                                                                                                                                                                                                                                                                                                        |
| MAXBOT           | Back off timer最大值（秒） | 可选必选说明：条件可选参数 参数含义：本参数用于设置Back off timer的最大值，用于计算发给终端的附着拒绝消息或者TAU拒绝消息中的Back off timer时长。 前提条件：该参数在“Backoff Timer分配开关”配置为“ON(开启)”后生效。 数据来源：本端规划 取值范围：1～11160。 系统初始设置值：1800 配置原则：该参数的取值必须大于等于“Back off timer最小值”的取值。                                                                                                                                                                                                                                                                                                                              |

#### 使用实例

用户签约数据修改时，希望已接入的用户立即重选至所属专用核心网，并向新侧MME携带正在使用的UE Usage Type，采用本地配置查询，携带Backoff Timer信元，Back off timer最小值为300秒，Back off timer最大值为1800秒：

SET DCNCTRL: RESELECTPLCY=IMMEDIATE, CONTAINUEUSGTYPE=YES, UEUSGTYPECONPLCY=USED, MMEGIQUERYPLCY=LOCAL, BACKOFFSW=ON, MINBOT=300, MAXBOT=1800;