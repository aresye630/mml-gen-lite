# 停止IMSI分离4G用户任务(STP VLROFFLOADBYLAI)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

用户通过启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)**STR VLROFFLOADBYLAI**启动扫描任务后，如果发现系统负荷过载或者LAI列表配置错误，可以执行本命令停止扫描任务，终止对于4G用户的IMSI分离操作。

#### 注意事项

- 此命令执行后立即生效。
- LAI列表配置可以通过命令**LST VLROFFLOADLAILST**查询。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

无。

#### 使用实例

停止由启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)**STR VLROFFLOADBYLAI**启动的扫描任务，终止对于4G用户的IMSI分离操作：

`STP VLROFFLOADBYLAI:;`