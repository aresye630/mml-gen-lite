# 停止迁移任务(STP OFFLOAD)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

此命令用于停止当前正在进行的迁移任务。

#### 注意事项

- 当由**STR OFFLOADBYMME**命令启动的迁移任务结束后，如果需要MME继续接入新用户，则需通过**SET SYS**命令将MME的“设备能力”设置成对应的值。
- 当由**STR OFFLOADBYSGSN**、
  **STR OFFLOADBYRNC**、**STR OFFLOADBYBSC**命令启动的迁移任务结束后，如果需要本SGSN通过指定RNC/BSC继续接入新用户，则需在相应RNC/BSC上将本SGSN的状态恢复为“Normal”。
- 此命令对类型为“IMSI(IMSI)”的迁移任务不生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

无。

#### 使用实例

停止迁移任务：

STP OFFLOAD:;