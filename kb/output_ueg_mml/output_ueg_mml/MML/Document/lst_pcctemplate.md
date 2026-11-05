# 查询PCC模板（LST PCCTEMPLATE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询PCC模板配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                                                                        |
|:------------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCCTEMPNAME | PCC模板名称 | 可选必选说明：可选参数 参数含义：该参数用于指定PCC模板的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写，不允许命名为“global”。 默认值：无 配置原则： 如果查询指定的PCC模板请输入PCC模板的名称。如果不输入PCC模板名称则查询全部PCC模板。 |

#### 使用实例

- 查询某个PCC模板确认参数是否配置正确：

  ```
  LST PCCTEMPLATE: PCCTEMPNAME="new_pcc_template";
  ```

  ```
  RETCODE = 0  操作成功

  PCC模板信息
  -----------
                               PCC模板名称  =  new_pcc_template
                              缺省上报级别  =  Rating Group
                      缺省离线计费统计方式  =  流量
     基于CCA-I Origin-Host AVP触发PCRF重选  =  禁止
     基于CCA-U Origin-Host AVP触发PCRF重选  =  禁止
       基于RAR Origin-Host AVP触发PCRF重选  =  禁止
                      选择PCF/PCRF失败动作  =  继承
   选择PCF/PCRF失败回滚为Local PCC用户类型  =  回滚为本地PCC用户
                   Initial流程故障处理动作  =  继承
    Initial流程故障回滚为Local PCC用户类型  =  回滚为本地PCC用户
                    Update流程故障处理动作  =  继承
            用户回滚后在线保持时长（分钟）  =  65535
                      随机延迟范围（分钟）  =  0
                        本端主机名选择模式  =  继承全局配置
                                本端主机名  =  NULL
   Initial流程故障回滚为RADIUS PCC用户类型  =  回滚为本地PCC用户
  选择PCF/PCRF失败回滚为RADIUS PCC用户类型  =  回滚为本地PCC用户
     Update流程故障回滚为Local PCC用户类型  =  回滚为本地PCC用户
      基于Notify消息ResourceURI触发PCF重选  =  继承
                       N7 Failover功能开关  =  继承全局配置
                           PCF负荷分担参数  =  继承全局配置
                       优先使用N15 PCF开关  =  继承全局配置
  (结果个数 = 1)

  ---    END
  ```
- 查询所有PCC模板配置：

  ```
  LST PCCTEMPLATE:;
  ```

  ```
  RETCODE = 0  操作成功。

  PCC模板信息
  -----------
  PCC模板名称         缺省上报级别          缺省离线计费统计方式    基于CCA-I Origin-Host AVP触发PCRF重选    基于CCA-U Origin-Host AVP触发PCRF重选    基于RAR Origin-Host AVP触发PCRF重选    激活号段匹配失败动作    激活号段匹配失败回滚为Local PCC用户类型    激活号段匹配失败回滚为RADIUS PCC用户类型    Initial流程故障处理动作    Initial流程故障回滚为Local PCC用户类型    Initial流程故障回滚为RADIUS PCC用户类型    Update流程故障处理动作    Update流程故障回滚为Local PCC用户类型    用户回滚后在线保持时长（分钟）    随机延迟范围（分钟）   本端主机名选择模式    本端主机名   基于Notify消息ResourceURI触发PCF重选   N7 Failover功能开关   PCF负荷分担参数   优先使用N15 PCF开关
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
  new_pcc_template    Service-Identifier    流量                    允许                                     禁止                                     禁止                                   回滚                    回滚为本地PCC用户              回滚为本地PCC用户                             激活失败                   回滚为本地PCC用户             回滚为本地PCC用户                            缺省                      回滚为本地PCC用户                          65535                             0                      继承全局配置          NULL               NULL        继承全局配置                           继承全局配置          继承全局配置      继承全局配置
  pcctemplate_1       Rating-Group          流量                    禁止                                     禁止                                     禁止                                   继承                    回滚为本地PCC用户              回滚为本地PCC用户                             继承                       回滚为本地PCC用户             回滚为本地PCC用户                            继承                      回滚为本地PCC用户                          65535                             0                      继承全局配置          NULL               NULL        继承全局配置                           继承全局配置          继承全局配置      继承全局配置
  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

参见ADD PCCTEMPLATE的参数说明。