# 停止用户退出UDM Bypass任务（STP SMSFEXITUDMBYPASS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

当启动用户退出UDM Bypass任务时，CPU和内存使用率会升高，和周边网元交互消息量增大，待用户退出UDM Bypass任务完成后，系统会恢复正常。

**适用NF：SMSF**

该命令用于启动用户退出UDM Bypass任务。当UDM故障已恢复但用户尚未退出UDM Bypass状态时，可以执行该命令使用户退出UDM Bypass状态。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

无

## 使用实例

当运营商希望停止退出UDM Bypass任务，执行如下命令：

```
STP SMSFEXITUDMBYPASS:;
```