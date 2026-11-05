# 显示网元生命周期子任务的相关信息（DSP ACTIONINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于显示网元内生命周期任务的子任务（Action）重试次数和超时时间。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

显示某网元内生命周期任务的子任务（Action）重试次数和超时时间。

```
%%DSP ACTIONINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
Action名称                                              Action超时时间（秒）         Action重试次数    

ActionAddVNode                                          30                           20                  
ActionCheckRu                                           30                           20                  
ActionGetServiceDepData                                 30                           90                  
ActionGetServiceSpec                                    30                           90                  
ActionGetSrvoDepData                                    5                            540                 
ActionNotifyServiceDepData                              30                           20                  
ActionWaitContainerNormalForInstantWithDynamicWorkload  30                           60                  
ActionWaitScaleOutManager                               1800                         0                   
ActionWaitSrvo                                          60                           30                  
(结果个数 = 9)

---    END
```

## 输出结果说明

| 输出项名称         | 输出项解释                      |
|:--------------|:---------------------------|
| Action名称      | 网元内生命周期任务的子任务（Action）名称。   |
| Action超时时间（秒） | 网元内生命周期任务的子任务（Action）超时时间。 |
| Action重试次数    | 网元内生命周期任务的子任务（Action）重试次数。 |