# 修改升级补丁定时器（SET UPGPATTIMER）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于修改升级/补丁对应定时器的时长值。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

**说明** 

此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| NAME                    |   VALUE |
|:------------------------|--------:|
| UpgradeStackUpdateTimer |      40 |
| PatchStackUpdateTimer   |      20 |
| PodDeleteTimer          |      10 |
| OSPatchPushTimer        |      15 |
| UpgradeCommonTimer1     |       5 |
| UpgradeCommonTimer2     |       5 |
| UpgradeCommonTimer3     |       5 |
| UpgradeCommonTimer4     |       5 |
| UpgradeCommonTimer5     |       5 |
| UpgradeCommonTimer6     |       5 |
| UpgradeCommonTimer7     |       5 |
| UpgradeCommonTimer8     |       5 |
| UpgradeCommonTimer9     |       5 |
| UpgradeCommonTimer10    |       5 |
| UpgradeCommonTimer11    |      10 |
| UpgradeCommonTimer12    |      10 |
| UpgradeCommonTimer13    |      10 |
| UpgradeCommonTimer14    |      10 |
| UpgradeCommonTimer15    |      10 |
| UpgradeCommonTimer16    |      10 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识   | 参数名称     | 参数说明                                                                                                                                                                                                                                                                  |
|:-------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME   | 定时器名称参数  | 可选必选说明：必选参数  参数含义：该参数用于指示定时器名称。UpgradeStackUpdateTimer：升级堆栈更新时长。PatchStackUpdateTimer：补丁堆栈更新时长。PodDeleteTimer：POD删除时长。OSPatchPushTimer：OS补丁推送时长。UpgradeCommonTimer1~10：升级通用定时配置1。PatchCommonTimer1~10：补丁通用定时配置1。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~255。  默认值：无。  配置原则：无 |
| VALUE  | 定时器配置时长值 | 可选必选说明：必选参数  参数含义：该参数用于设置指定定时器的配置时长。  数据来源：本端规划  取值范围：整数类型，取值范围是0~1000，单位是分钟。定时器参数修改必须大于等于系统默认值。  默认值：无。  配置原则：无                                                                                                                                                      |

## 使用实例

设置堆栈更新时长定时器为45分钟

```
SET UPGPATTIMER:NAME="UpgradeStackUpdateTimer" ,VALUE=45;
```