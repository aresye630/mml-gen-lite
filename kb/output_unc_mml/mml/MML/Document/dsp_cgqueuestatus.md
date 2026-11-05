# 显示NCG队列状态（DSP CGQUEUESTATUS）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：NCG**

该命令用于查询NCG内部队列的状态。

#### 注意事项

无

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                     |
|:----------|:-------|:-------------------------------------------------------------------------------------------------------------------------|
| RUID      | RU的ID  | 可选必选说明：可选参数 参数含义：RU的ID。 数据来源：本端规划 取值范围：整数类型，取值范围为64～4294967294。 默认值：无 配置原则：该值需要执行LST SERVICERUSTATE命令，查询出存在的“RU的ID”进行填写。 |
| QUEUETYPE | 队列类型   | 可选必选说明：可选参数 参数含义：该参数用于指定查询的队列类型。 数据来源：本端规划。 取值范围：枚举类型。 GA_QUEUE：GA接口的相关队列。COMP_QUEUE：组件消息队列。 默认值：无 配置原则：无                |

#### 使用实例

查询当前NCG内部队列状态，示例如下：

```
DSP CGQUEUESTATUS:;
```

```
RETCODE = 0  操作成功  
结果如下: 
--------- 
RU的ID  进程名  队列类型      队列名称          队列容量  当前使用量  队列超限次数  关键字1                                                                      关键字2  关键字3  关键字4  关键字5
2       QBM     组件消息队列  MSG_QUEUE         524288    0           0             QBM                                                                          NULL     NULL     NULL     NULL
64      AP64_1  组件消息队列  MSG_QUEUE         524288    0           0             CCL                                                                          NULL     NULL     NULL     NULL      
64      AP64_1  组件消息队列  MSG_QUEUE         524288    0           0             GACM                                                                         NULL     NULL     NULL     NULL      
64      AP64_1  组件消息队列  MSG_QUEUE         524288    0           0             CDW                                                                          NULL     NULL     NULL     NULL      
64      AP64_1  组件消息队列  MSG_QUEUE         524288    0           0             BILLSAVE                                                                     NULL     NULL     NULL     NULL      
64      AP64_1  组件消息队列  MSG_QUEUE         524288    0           0             FAM                                                                          NULL     NULL     NULL     NULL      
64      AP64_1  GA接口队列    DATA_QUEUE        480000    0           0             Normal:0,MayDup:0,Release:0,Cancel:0,Empty:0,Other:0                         NULL     NULL     NULL     NULL    
64      AP64_1  GA接口队列    NEW_FRAMES_QUEUE  4500      0           0             SRC:10.31.14.7:7112 DST:10.31.14.3:3386                                      NULL     NULL     NULL     NULL
64      AP64_1  GA接口队列    DUP_FRAMES_QUEUE  65535     0           0             SRC:10.31.14.7:7112 DST:10.31.14.3:3386                                      NULL     NULL     NULL     NULL
64      AP64_1  GA接口队列    REL_FRAMES_QUEUE  65535     0           0             SRC:10.31.14.7:7112 DST:10.31.14.3:3386                                      NULL     NULL     NULL     NULL
64      CBK     组件消息队列  MSG_QUEUE         524288    0           0             CBK                                                                          NULL     NULL     NULL     NULL      
64      CDM     组件消息队列  MSG_QUEUE         524288    0           0             CDM                                                                          NULL     NULL     NULL     NULL      
64      CQB     组件消息队列  MSG_QUEUE         524288    0           0             CQB                                                                          NULL     NULL     NULL     NULL      
64      RCM     组件消息队列  MSG_QUEUE         524288    0           0             RCM                                                                          NULL     NULL     NULL     NULL     
(结果个数 = 14)  
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释                                                                                                                                                                                                                    |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RU的ID   | 表示当前队列所在的RU ID。                                                                                                                                                                                                          |
| 进程名     | 表示当前队列所在的业务进程名称。                                                                                                                                                                                                         |
| 队列类型    | 表示当前队列的类型。 组件消息队列GA接口队列                                                                                                                                                                                                  |
| 队列名称    | 表示当前队列的名称。 MSG_QUEUE：消息队列。DATA_QUEUE：GA接入全局流控队列。NEW_FRAMES_QUEUE：新收数据帧队列。DUP_FRAMES_QUEUE：可能重复帧待确认队列。REL_FRAMES_QUEUE：已确认待落盘的可能重复帧队列。                                                                                    |
| 队列容量    | 表示当前队列定义的最大容量。                                                                                                                                                                                                           |
| 当前使用量   | 表示当前队列的使用量。                                                                                                                                                                                                              |
| 队列超限次数  | 表示当前队列的超限次数。 当队列名称为DUP_FRAMES_QUEUE时，需执行SET SRVSTH命令开启“GA链路可能重复帧剔重异常校验”开关 ，表示统计重复帧不一致数量而导致的丢帧数。当队列名称不为DUP_FRAMES_QUEUE时，表示因当前队列满无法进队列的次数。                                                                                |
| 关键字1    | 表示队列相关的关键字1，与队列强相关。 当队列名称为MSG_QUEUE时，表示当前队列所在的组件名称。当队列名称为DATA_QUEUE时，表示当前GA接入全局流控队列中各种消息帧的帧数。当队列名称为NEW_FRAMES_QUEUE时，表示当前队列所在链路的五元组信息。当队列名称为DUP_FRAMES_QUEUE时，表示当前队列所在链路的五元组信息。当队列名称为REL_FRAMES_QUEUE时，表示当前队列所在链路的五元组信息。 |
| 关键字2    | 表示队列相关的关键字2，与队列强相关。                                                                                                                                                                                                      |
| 关键字3    | 表示队列相关的关键字3，与队列强相关。                                                                                                                                                                                                      |
| 关键字4    | 表示队列相关的关键字4，与队列强相关。                                                                                                                                                                                                      |
| 关键字5    | 表示队列相关的关键字5，与队列强相关。                                                                                                                                                                                                      |