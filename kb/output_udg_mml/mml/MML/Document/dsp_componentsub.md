# 显示组件订阅信息（DSP COMPONENTSUB）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示指定进程内的组件订阅信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                         |
|:----------------|:-------|:-------------------------------------------------------------------------------------------------------------|
| COMPCID         | 组件ID   | 可选必选说明：必选参数 参数含义：组件ID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                    |
| PROCID          | 进程ID   | 可选必选说明：必选参数 参数含义：该参数用于指定要查询组件所属进程的ID。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                           |
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### 使用实例

在VNFC侧显示进程1001上组件0x80CF001F的订阅信息：

```
DSP COMPONENTSUB:COMPCID="0x80CF001F",PROCID=1001,SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
订阅时间                 组件ID           对端组件ID     组件状态      通知          

11-15 11:40:43.291362    0x80CF001F       0xCB0009       NULL          SUBSCRIBE             
11-15 11:40:43.291424    0x80CF001F       0xCD0008       NULL          SUBSCRIBE                  
11-15 11:40:43.291480    0x80CF001F       0x8003001E     NULL          SUBSCRIBE             
11-15 11:40:43.291597    0x80CF001F       0x8003001E     PRIMARY       COMP-UPDATE STATE: OK 
11-15 11:40:43.291653    0x80CF001F       0x80CF001F     NULL          SUBSCRIBE             
11-15 11:40:43.291664    0x80CF001F       0x80CF001F     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:43.298049    0x80CF001F       0xCB0009       NULL          PID WAITABLE          
11-15 11:40:43.298050    0x80CF001F       0xCB0009       PRIMARY       COMP-UPDATE STATE: OK 
11-15 11:40:43.298160    0x80CF001F       0xCD0008       NULL          PID WAITABLE          
11-15 11:40:43.298161    0x80CF001F       0xCD0008       PRIMARY       COMP-UPDATE STATE: OK 
11-15 11:40:47.961245    0x80CF001F       0x80650020     NULL          SUBSCRIBE             
11-15 11:40:47.962689    0x80CF001F       0x84040021     NULL          SUBSCRIBE             
11-15 11:40:47.963011    0x80CF001F       0x82080022     NULL          SUBSCRIBE             
11-15 11:40:47.993768    0x80CF001F       0x80970027     NULL          SUBSCRIBE             
11-15 11:40:48.046106    0x80CF001F       0x81970029     NULL          SUBSCRIBE             
11-15 11:40:48.046648    0x80CF001F       0x80920032     NULL          SUBSCRIBE             
11-15 11:40:48.047589    0x80CF001F       0x80930033     NULL          SUBSCRIBE             
11-15 11:40:48.050176    0x80CF001F       0x80650020     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.051249    0x80CF001F       0x84040021     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.051569    0x80CF001F       0x82080022     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.052651    0x80CF001F       0x80970027     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.052764    0x80CF001F       0x81970029     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.053138    0x80CF001F       0x80920032     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.053696    0x80CF001F       0x80930033     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:42:41.721464    0x80CF001F       0xCB0009       NULL          COMP-UPDATE STATE: NG 
11-15 11:42:41.721494    0x80CF001F       0xCD0008       NULL          COMP-UPDATE STATE: NG 
11-15 11:42:41.784603    0x80CF001F       0xCB0009       PRIMARY       COMP-UPDATE STATE: OK 
11-15 11:42:41.784811    0x80CF001F       0xCD0008       PRIMARY       COMP-UPDATE STATE: OK 
(结果个数 = 28)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释          |
|:--------|:---------------|
| 订阅时间    | 用于说明订阅发生的时间。   |
| 组件ID    | 组件ID。          |
| 对端组件ID  | 用以说明订阅对端的组件ID。 |
| 组件状态    | 组件的主备状态。       |
| 通知      | 用于说明订阅的状态。     |