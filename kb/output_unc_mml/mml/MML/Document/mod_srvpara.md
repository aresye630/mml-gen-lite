# 修改业务参数配置（MOD SRVPARA）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**须知** 

如果业务参数类型选择PASSIVE模式参数，此操作会重启FTP服务，导致计费中心客户端会中断1~2秒；如果业务参数类型选择BI收敛参数，则需要执行RST VNFC重启服务才能生效。

**适用NF：NCG**

用于修改NCG相关参数。

执行命令之前，可执行**LST SRVPARA**命令查询当前配置的参数。

#### 注意事项

- 该命令执行后立即生效；如果业务参数类型选择BI收敛参数，则需要执行RST VNFC重启服务才能生效。
- 该命令最大记录数为32。
- 起始端口与结束端口中间不能包含20048、2049、32769、2020端口。
- 该命令存在系统初始设置记录，参数的初始设置值见参数说明。
- 若配置业务RU约束为ON，统一序列号功能对234G格式引擎包不生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识                | 参数名称                  | 参数说明                                                                                                                                                                                                                                                                                                                                                |
|:--------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRVPARATYPE         | 业务参数类型                | 可选必选说明：必选参数 参数含义：用于指定对哪一类业务参数进行修改。 数据来源：本端规划 取值范围：枚举类型。 GATRACEMSGPARA：Ga跟踪消息长度。PASSIVEPARA：PASSIVE模式参数。ANOTHERNODEDOWNPARA：另一节点发生故障。CDMPULLMODEPARA：PULL分发模式参数。GALICCTRLALM：GA License控制告警阈值。GALICPARA：GA License参数。BICONVERGENCE：BI收敛参数。PORTCONSTR：端口约束。 默认值：无 配置原则：如果使用ANOTHERNODEDOWNPARA功能，请确保配置监控任务或者上报ALM-82000长时间未取话单告警之前，开启SRVPARAVALUE开关。 |
| GATRACEMSGLEN       | Ga跟踪消息长度              | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“GATRACEMSGPARA”时为条件可选参数。 参数含义：用于设置Ga跟踪消息并且消息类型是DataTransferRequest时的上报长度控制。 数据来源：本端规划 取值范围：枚举类型。 SHORT：Ga跟踪消息，且消息类型为DataTransferRequest时候，只上报24个字节的GTP’消息。LONG：Ga跟踪消息，且消息类型为DataTransferRequest时候，上报完整的GTP’报文。 初始值：SHORT 默认值：无 配置原则：无                                                                       |
| STARTPORT           | 起始端口                  | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“PASSIVEPARA”时为条件可选参数。 参数含义：PULL模式下FTP PASSIVE和PORT模式的起始端口。 数据来源：本端规划 取值范围：整数类型，取值范围为1024～65535。 初始值：20050 默认值：无 配置原则：起始端口必须小于结束端口，不同类型端口范围不能重叠。                                                                                                                                                             |
| ENDPORT             | 结束端口                  | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“PASSIVEPARA”时为条件可选参数。 参数含义：PULL模式下FTP PASSIVE和PORT模式的结束端口。 数据来源：本端规划 取值范围：整数类型，取值范围为1024～65535。 初始值：20100 默认值：无 配置原则：结束端口必须大于起始端口，不同类型端口范围不能重叠。                                                                                                                                                             |
| SRVPARAVALUE        | 业务控制参数                | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“ANOTHERNODEDOWNPARA”时为条件可选参数。 参数含义：软参值的开关状态。 数据来源：本端规划 取值范围：枚举类型。 OFF：关闭。ON：开启。 初始值：OFF 默认值：无 配置原则：无                                                                                                                                                                                                        |
| CLIENTALIVECOUNTMAX | SFTP最大超时次数            | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“CDMPULLMODEPARA”时为条件可选参数。 参数含义：PULL模式下SFTP服务端的ClientAliveCountMax参数。 数据来源：本端规划 取值范围：整数类型，取值范围为0～100。 初始值：0 默认值：0 配置原则：无                                                                                                                                                                                     |
| CLIENTALIVEINTERVAL | SFTP服务器端向客户端请求消息的时间间隔 | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“CDMPULLMODEPARA”时为条件可选参数。 参数含义：PULL模式下SFTP服务端的ClientAliveInterval参数。 数据来源：本端规划 取值范围：整数类型，取值范围为0～86400。 初始值：300 默认值：300 配置原则：无                                                                                                                                                                               |
| SFTPMAXCPULIMIT     | SFTP CPU最高占比（%）       | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“CDMPULLMODEPARA”时为条件可选参数。 参数含义：PULL模式下SFTP服务端的CPU最高占比。 数据来源：本端规划 取值范围：整数类型，取值范围为0~280。 初始值：0 默认值：0 配置原则：无                                                                                                                                                                                                   |
| FTPMAXCPULIMIT      | FTP CPU最高占比（%）        | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“CDMPULLMODEPARA”时为条件可选参数。 参数含义：PULL模式下FTP服务端的CPU最高占比。 数据来源：本端规划 取值范围：整数类型，取值范围为0~280。 初始值：0 默认值：0 配置原则：无                                                                                                                                                                                                    |
| GALICVOLALMPCT      | 容量告警百分比（%）            | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“GALICCTRLALM”时为条件可选参数。 参数含义：该参数用于指定容量告警百分比。当系统中已使用的资源控制项数目在“持续时间”内的平均值与License允许的数目比值大于该参数设定的值时，系统将产生ALM-82015告警。 数据来源：本端规划 取值范围：整数类型，取值范围为80～99。 初始值：80 默认值：80 配置原则：容量告警百分比必须大于容量告警恢复百分比。                                                                                                                  |
| GALICVOLALMRST      | 容量告警恢复百分比（%）          | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“GALICCTRLALM”时为条件可选参数。 参数含义：该参数用于指定容量告警恢复百分比。系统已经产生该资源控制项的容量告警后，当已使用的资源控制项数目在“持续时间”内的平均值与License允许的数目比值小于该参数设定的值时，系统将恢复ALM-82015告警。 数据来源：本端规划 取值范围：整数类型，取值范围为1～99。 初始值：70 默认值：70 配置原则：容量告警百分比必须大于容量告警恢复百分比。                                                                                                 |
| GALICALMDEPRD       | 告警检测周期（分钟）            | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“GALICCTRLALM”时为条件可选参数。 参数含义：告警ALM-82015的检测周期。 数据来源：本端规划 取值范围：整数类型，取值范围为1～480。 初始值：20 默认值：20 配置原则：无                                                                                                                                                                                                          |
| LRRMBST             | 会话结束及时释放License       | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“GALICPARA”时为条件可选参数。 参数含义：会话结束及时释放License的开关状态。 数据来源：本端规划 取值范围：枚举类型。 OFF：关闭。ON：开启。 初始值：OFF 默认值：OFF 配置原则：无                                                                                                                                                                                                    |
| DLRATS              | 会话结束后License延迟释放时间    | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“GALICPARA”时为条件可选参数。 参数含义：会话结束后License延迟释放时间，单位为分钟。 数据来源：本端规划 取值范围：整数类型，取值范围为0～35790。 初始值：3 默认值：3 配置原则：无                                                                                                                                                                                                     |
| LRRMBCS             | 切换场景及时释放License       | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“GALICPARA”时为条件可选参数。 参数含义：切换场景及时释放License的开关状态。 数据来源：本端规划 取值范围：枚举类型。 OFF：关闭。ON：开启。 初始值：OFF 默认值：OFF 配置原则：无                                                                                                                                                                                                    |
| GAWEIGHTSWITCH      | Ga业务权重调整              | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“BICONVERGENCE”时为条件可选参数。 参数含义：控制234G业务是否用于调整5G权重的开关。 数据来源：本端规划 取值范围：枚举类型。 OFF：关闭。ON：开启。 初始值：OFF 默认值：OFF 配置原则：无                                                                                                                                                                                               |
| SERVICERUCONSTR     | 业务RU约束                | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“BICONVERGENCE”时为条件可选参数。 参数含义：控制业务RU是否禁止配置234G业务的开关。 数据来源：本端规划 取值范围：枚举类型。 OFF：关闭。ON：开启。 初始值：OFF 默认值：OFF 配置原则：业务RU未配置234G格式引擎包才可以开启。                                                                                                                                                                          |
| PORTPROCTYPE        | 进程类型                  | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“PORTCONSTR”时为条件可选参数。 参数含义：用于选择需设置的PUSH模式CG侧端口范围的进程类型。 数据来源：本端规划 取值范围：枚举类型。 CDM：CDM进程。CBK：CBK进程。 初始值：CDM 默认值：无 配置原则：不能为空。                                                                                                                                                                                    |
| PORTTYPE            | 端口类型                  | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“PORTCONSTR”时为条件可选参数。 参数含义：用于选择需设置的PUSH模式CG侧端口范围的端口类型。 数据来源：本端规划 取值范围：枚举类型。 SFTP：PUSH SFTP模式的CG侧端口。PASSIVE：PUSH FTP的Passive模式的CG侧数据端口。PORT：PUSH FTP的Port模式的CG侧数据端口。CTRL：PUSH FTP模式CG侧的控制端口。 初始值：SFTP 默认值：无 配置原则：不能为空。                                                                                        |
| PORTMAX             | 最大端口                  | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“PORTCONSTR”时为条件可选参数。 参数含义：用于设置选择的PUSH模式CG侧端口范围的最大值。 数据来源：本端规划 取值范围：整数类型，取值范围为1024～65535。 初始值：65535 默认值：无 配置原则：不能为空，且不小于最小端口，不同类型端口范围不能重叠。                                                                                                                                                                   |
| PORTMIN             | 最小端口                  | 可选必选说明：条件可选参数 前提条件：该参数在“SRVPARATYPE”配置为“PORTCONSTR”时为条件可选参数。 参数含义：用于设置选择的PUSH模式CG侧端口范围的最小值。 数据来源：本端规划 取值范围：整数类型，取值范围为1024～65535。 初始值：1024 默认值：无 配置原则：不能为空，且不大于最大端口，不同类型端口范围不能重叠。                                                                                                                                                                    |

#### 使用实例

- 业务参数类型设置为“Ga跟踪消息长度”，Ga跟踪消息长度设置为“LONG”：

  ```
  MOD SRVPARA: SRVPARATYPE=GATRACEMSGPARA, GATRACEMSGLEN=LONG;
  ```
- 业务参数类型设置为“PASSIVE模式参数”，起始端口设置为20060，结束端口设置为20090：

  ```
  MOD SRVPARA: SRVPARATYPE=PASSIVEPARA, STARTPORT=20060, ENDPORT=20090;
  ```
- 业务参数类型设置为“另一节点发生故障”，软参值的开关状态设置为“开启”：

  ```
  MOD SRVPARA: SRVPARATYPE=ANOTHERNODEDOWNPARA, SRVPARAVALUE=ON;
  ```
- 业务参数类型设置为“PULL分发模式参数”，SFTP最大超时次数设置为5，SFTP服务器端向客户端请求消息的时间间隔设置为60，SFTP CPU最高占比（%）设置为90，FTP CPU最高占比（%）设置为90：

  ```
  MOD SRVPARA: SRVPARATYPE=CDMPULLMODEPARA, CLIENTALIVECOUNTMAX=5, CLIENTALIVEINTERVAL=60, SFTPMAXCPULIMIT=90, FTPMAXCPULIMIT=90;
  ```
- 业务参数类型设置为“GA License控制告警阈值”，容量告警百分比设置为85，容量告警恢复百分比设置为75，告警检测周期设置为30：

  ```
  MOD SRVPARA: SRVPARATYPE=GALICCTRLALM, GALICVOLALMPCT=85, GALICVOLALMRST=75, GALICALMDEPRD=30;
  ```
- 业务参数类型设置为“GA License参数”，会话结束及时释放License设置为“开启”，会话结束后License延迟释放时间设置为5，切换场景及时释放License设置为“开启”：

  ```
  MOD SRVPARA: SRVPARATYPE=GALICPARA, LRRMBST=ON, DLRATS=5, LRRMBCS=ON;
  ```
- 业务参数类型设置为“BI收敛参数”，Ga业务权重调整设置为“开启”，业务RU约束设置为“开启”：

  ```
  MOD SRVPARA: SRVPARATYPE=BICONVERGENCE, GAWEIGHTSWITCH=ON, SERVICERUCONSTR=ON;
  ```
- 业务参数类型设置为“端口约束”，选择进程类型为“CDM”，选择端口类型为“SFTP”，最大端口设置为25000，最小端口设置为24000：

  ```
  MOD SRVPARA: SRVPARATYPE=PORTCONSTR, PORTPROCTYPE=CDM, PORTTYPE=SFTP, PORTMAX=25000, PORTMIN=24000;
  ```