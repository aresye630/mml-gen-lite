# 显示PAE告警信息（DSP PAEALARMINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示PAE告警信息。

PAE告警信息是指本端资源的链路故障数。通过此命令可查看本端资源到所有对端资源的链路故障数。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                    |
|:-------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CELLTYPE     | 微服务类型  | 可选必选说明：可选参数 参数含义：该参数用于指定微服务类型。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看微服务类型。    |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数 参数含义：该参数用于指定微服务实例号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看微服务实例号。 |

#### 使用实例

- 显示微服务类型为“104”微服务实例为“sfm-pod-7b4bc4fd54-6tcbb172-16-0-45\_\_103\_\_0”的PAE告警信息：

  ```
  %%DSP PAEALARMINFO: CELLTYPE="104", CELLINSTANCE="sfm-pod-7b4bc4fd54-6tcbb172-16-0-45__103__0";%%
  RETCODE = 0  操作成功

  结果如下:
  ---------
    微服务类型  =  104
  微服务实例号  =  sfm-pod-7b4bc4fd54-6tcbb172-16-0-45__103__0
        平面ID  =  0
      事件名称  =  PAE_ALERT_FABRIC_PLANE_UNREACH
      端口名称  =  NA
    链接故障数  =  6
  (结果个数 = 1)

  ---    END
  ```
- 显示所有PAE告警信息：

  ```
  %%DSP PAEALARMINFO;%%
  RETCODE = 0  操作成功

  结果如下:
  ---------
  微服务类型  微服务实例号                                平面ID  事件名称                        端口名称  链接故障数  

  104         gcp-pod-0172-16-0-83__103__0                0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         udgctrl-pod-0172-16-0-166__103__0           0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         vupctrlds-pod-0172-16-1-121__103__0         0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         vupctrld-pod-0172-16-1-112__103__0          0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         udgctrl-pod-1172-16-0-84__103__0            0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         npmu-pod-0172-16-0-251__103__0              0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         udgspu-pod-1172-16-1-113__103__0            0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         sfm-pod-5fb6fb84cd-v8lqp172-16-0-63__103__0 0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         csdb-pod-0172-16-0-247__103__0              0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         npmu-pod-1172-16-1-122__103__0              0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         sfm-pod-5fb6fb84cd-jqmnv172-16-0-15__103__0 0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  104         sfm-pod-5fb6fb84cd-mvvqf172-16-0-47__103__0 0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         udgspu-pod-0172-16-1-117__103__0            0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        8           
  104         gcp-pod-1172-16-0-165__103__0               0       PAE_ALERT_FABRIC_PLANE_UNREACH  NA        6           
  (结果个数 = 14)

  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释                |
|:--------|:---------------------|
| 微服务类型   | 用于表示上报告警的微服务类型。      |
| 微服务实例号  | 用于表示上报告警的微服务实例号。     |
| 平面ID    | 用于表示上报告警的Fabric平面ID。 |
| 事件名称    | 用于表示上报告警的事件名称。       |
| 端口名称    | 用于表示上报告警的端口名称。       |
| 链接故障数   | 用于表示上报告警的链路故障数量。     |