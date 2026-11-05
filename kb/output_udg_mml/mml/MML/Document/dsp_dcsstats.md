# 显示DCS打点统计信息（DSP DCSSTATS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

显示DCS打点统计信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                        |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMDSTR | 命令字符串  | 可选必选说明：必选参数  参数含义：该参数用于表示需要查询的统计数据类型，当CMDSTR="dcs vod help"时可以查询出点播支持的统计数据类型。当CMDSTR="dcs live help"时可以查询出直播支持的统计数据类型。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~1024。  默认值：无  配置原则：无 |

## 使用实例

显示所有实例的DCS打点统计信息。

```
%%DSP DCSSTATS: CMDSTR="dcs vod help";%%
RETCODE = 0  操作成功

结果如下
------------------------
输出字符串

                                                                             
Pod Name: relay-pod-1, Dsp Help result as follows:
|--------------------------------|----------------------------------------------------------------|
|Command                         |Descript                                                        |
|--------------------------------|----------------------------------------------------------------|
|help                            |dcs vod help                                                    |
|ott                             |dcs vod ott                                                     |
|api                             |dcs vod api                                                     |
|traffic                         |dcs vod traffic                                                 |
|sdk_msg                         |dcs vod sdk_msg                                                 |
|sdk_delay                       |dcs vod sdk_delay                                               |
|cross_msg                       |dcs vod cross_msg                                               |
|cross_delay                     |dcs vod cross_delay                                             |
|buff_delay                      |dcs vod buff_delay                                              |
|disk_info                       |dcs vod disk_info                                               |
|disk_msg                        |dcs vod disk_msg                                                |
|disk_delay                      |dcs vod disk_delay                                              |
|task_delay                      |dcs vod task_delay                                              |
|mem_pool                        |dcs vod mem_pool                                                |
|pool_cache                      |dcs vod pool_cache                                              |
|heat_info                       |dcs vod heat_info                                               |
|node_info                       |dcs vod node_info                                               |
|videos_name                     |dcs vod videos_name {begin_idx}                                 |
|video_info                      |dcs vod video_info {ottname} {url}                              |
|video_bitmap                    |dcs vod video_bitmap {ottname} {url}                            |
|video_buff                      |dcs vod video_buff {ottname} {url} {buffer_idx}                 |
|--------------------------------|----------------------------------------------------------------|
  

Pod Name: relay-pod-0, Dsp Help result as follows:
|--------------------------------|----------------------------------------------------------------|
|Command                         |Descript                                                        |
|--------------------------------|----------------------------------------------------------------|
|help                            |dcs vod help                                                    |
|ott                             |dcs vod ott                                                     |
|api                             |dcs vod api                                                     |
|traffic                         |dcs vod traffic                                                 |
|sdk_msg                         |dcs vod sdk_msg                                                 |
|sdk_delay                       |dcs vod sdk_delay                                               |
|cross_msg                       |dcs vod cross_msg                                               |
|cross_delay                     |dcs vod cross_delay                                             |
|buff_delay                      |dcs vod buff_delay                                              |
|disk_info                       |dcs vod disk_info                                               |
|disk_msg                        |dcs vod disk_msg                                                |
|disk_delay                      |dcs vod disk_delay                                              |
|task_delay                      |dcs vod task_delay                                              |
|mem_pool                        |dcs vod mem_pool                                                |
|pool_cache                      |dcs vod pool_cache                                              |
|heat_info                       |dcs vod heat_info                                               |
|node_info                       |dcs vod node_info                                               |
|videos_name                     |dcs vod videos_name {begin_idx}                                 |
|video_info                      |dcs vod video_info {ottname} {url}                              |
|video_bitmap                    |dcs vod video_bitmap {ottname} {url}                            |
|video_buff                      |dcs vod video_buff {ottname} {url} {buffer_idx}                 |
|--------------------------------|----------------------------------------------------------------|
  
(结果个数 = 2)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释        |
|:--------|:-------------|
| 输出字符串   | 该参数用于表示查询结果。 |