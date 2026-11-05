# 停止用户退出HSS BYPASS状态(STP HSSBPEXIT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于停止用户手动退出HSS BYPASS状态的任务。当系统中执行了用户退出HSS BYPASS状态(**STR HSSBPEXIT**)命令时，希望中途停止手动退出HSS BYPASS状态任务，可以执行该命令。

#### 注意事项

- 该命令执行后立即生效。
- 相关license授权并开启后，此命令配置才能执行（License部件编码：LKV2HSSBP01）。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

无

#### 使用实例

停止用户退出HSS BYPASS状态任务，可用如下命令。

```
STP HSSBPEXIT:;
```