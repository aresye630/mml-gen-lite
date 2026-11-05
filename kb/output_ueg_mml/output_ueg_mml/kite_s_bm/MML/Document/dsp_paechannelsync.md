# 显示同步到业务进程的通道信息（DSP PAECHANNELSYNC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示同步到业务进程的通道信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                          |
|:-------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CELLTYPE     | 微服务类型  | 可选必选说明：必选参数 参数含义：该参数用于指定微服务类型。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看微服务类型。                          |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数 参数含义：该参数用于指定微服务实例号。本参数可通过DSP PAENODE命令获取。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看微服务实例号。 |
| LOGICPID     | 逻辑进程号  | 可选必选说明：必选参数 参数含义：逻辑进程号。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295 默认值：无 配置原则：使用DSP MSSFMMPROCESS查看逻辑进程号。                                                                                          |

#### 使用实例

显示类型为aa的微服务aa中根据逻辑进程ID，查询对应的队列信息：

```
DSP PAECHANNELSYNC: CELLTYPE="aa", CELLINSTANCE="aa", LOGICPID=1;
```

```
RETCODE = 0  操作成功。

结果如下
--------
通道ID      通道名称      通道类型      TP          优先级为0的队列ID    优先级为1的队列ID    优先级为2的队列ID    优先级为3的队列ID    优先级为4的队列ID    优先级为5的队列ID    优先级为6的队列ID    优先级为7的队列ID 

0           sdr0110-000   服务          0x83701f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           
1           ext0110-000   服务          0x83711f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           
2           1000012705    服务          0x83301f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           
3           1001012705    服务          0x83311f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           
4           1000012673    服务          0x83281f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           
5           1001012673    服务          0x83291f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           
6           1000012801    服务          0x83481f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           
7           1001012801    服务          0x83491f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           
8           1000013089    服务          0x83901f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           
9           1001013089    服务          0x83911f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           
10          1000018241    服务          0x84381f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           
11          1001018241    服务          0x84391f00  0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff           0xffffffff  
(结果个数 = 12)
---    END
```

#### 输出结果说明

| 输出项名称      | 输出项解释                                |
|:-----------|:-------------------------------------|
| 通道ID       | 全局通道ID。                              |
| 通道名称       | 通道名称。                                |
| 通道类型       | 通道类型分为：NULL、默认、透传、转发链、硬件加速、直连、服务和低速。 |
| TP         | 目标端口。                                |
| 优先级为0的队列ID | 优先级为0的队列ID。                          |
| 优先级为1的队列ID | 优先级为1的队列ID。                          |
| 优先级为2的队列ID | 优先级为2的队列ID。                          |
| 优先级为3的队列ID | 优先级为3的队列ID。                          |
| 优先级为4的队列ID | 优先级为4的队列ID。                          |
| 优先级为5的队列ID | 优先级为5的队列ID。                          |
| 优先级为6的队列ID | 优先级为6的队列ID。                          |
| 优先级为7的队列ID | 优先级为7的队列ID。                          |