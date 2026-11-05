# 异构迁移（ACT MIGRATE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**须知** 

本命令属于高危命令，操作不当可能导致业务受损，请谨慎使用并联系华为支持协助操作。

该命令用于网元由X86单板架构切换至ARM单板架构执行具体迁移子任务。

**说明** 

该命令仅在Full-stack虚机场景下支持。

#### 注意事项

无。

#### 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                                                                          |
|:--------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OPRTYPE | 操作类型   | 可选必选说明：必选参数。 参数含义：异构迁移场景下发操作任务的操作类型。 取值范围： BACKUP（数据导出）SYNCFILE（文件同步）RESTORE（数据恢复）MSWITCH（主备倒换）SWFORBID（主备服务禁止倒换）SWFCANCEL（取消主备服务禁止倒换）DBDATACLR（GAUSSDB数据清除）OMADAPTERDLD（适配包下载）OSPKGDLD（OS包下载） 默认值：无。 配置原则：无。 |
| PARAM1  | 参数1    | 可选必选说明：必选参数。 参数含义：包含网元pod名称、请求body参数，omutype参数。请求body参数表示配置各服务对应数据库无需导出的表名称。 取值范围：字符或字母（a～z或A～Z），不超过2048个字符长度，omutype是枚举类型，枚举值是omu和omu-ex。 默认值：无。 配置原则： “OPRTYPE”参数为“SYNCFILE（文件同步）”，请求body参数中body内容必须为空 。    |

#### 使用实例

执行取消GaussDB主备服务禁止倒换任务。

```
%%ACT MIGRATE: OPRTYPE=SWFCANCEL, PARAM1="{#podname#:#gaussdb-9cbed835-0#& #omutype#:#omu#}", CONFIRM=Y;%%
RETCODE = 0  操作成功
ACT MIGRATE
-----------
操作类型 = SWFCANCEL
参数1    = {#podname#:#gaussdb-Scbed835-0#& #omutype#:#omu#}
状态	 = success
(结果个数 = 1)
---    END
```

执行GaussDB主备倒换任务。

```
%%ACT MIGRATE: OPRTYPE=MSWITCH, PARAM1="{#podname#:#gaussdb-9cbed835-0#& #body#:{#priorityRestoreDb#:#omlbdb& modulekeeperdb& vnfmadaptordb& certmgrdb& userdb& auditdb& netconfgwdb#}& #omutype#:#omu#}", CONFIRM=Y;%%
RETCODE = 0  操作成功
ACT MIGRATE
-----------
操作类型 = MSWITCH
参数1    =  {#podname#:#gaussdb-9cbed835-0#& #body#:{#priorityRestoreDb#:#omlbdb& modulekeeperdb& vnfmadaptordb& certmgrdb& userdb& auditdb& netconfgwdb#}& #omutype#:#omu#}
状态	 = success
(结果个数 = 1)
---    END
```

#### 输出结果说明

命令执行正常，会返回命令操作类型、参数1及执行成功的提示信息，输出结果项信息项目如表1 输出项说明。

命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 输出项名称   | 输出项解释                                      |
|:--------|:-------------------------------------------|
| 操作类型    | 用于返回操作类型。                                  |
| 参数1     | 用于返回参数1的详细信息，包含网元pod名称、请求body参数，omutype参数。 |
| 状态      | 用于返回执行此MML命令成功与否的提示信息。                     |

|    错误码 | 错误码解释           | 原因分析                             | 处理建议       |
|-------:|:----------------|:---------------------------------|:-----------|
| 100031 | 命令下发失败、服务接口调用失败 | 调用服务接口失败。                        | 请联系华为技术支持。 |
| 150002 | MML命令参数校验失败     | MML命令参数校验失败。                     | 请联系华为技术支持。 |
| 150007 | 适配包/OS包下载失败     | 获取SFTP信息失败。输入参数错误。               | 请联系华为技术支持。 |
| 150021 | 当前模式不支持此命令      | 裸机及三方部署场景，不涉及异构迁移，不支持该命令。        | 无需处理。      |
| 150033 | GaussDB任务执行失败   | 没有查询到GAUSSDB实例信息GAUSSDB任务请求下发失败。 | 请联系华为技术支持。 |
| 150034 | GaussDB数据导入失败   | GaussDB接口调用失败。                   | 请联系华为技术支持。 |