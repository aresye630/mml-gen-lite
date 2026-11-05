# 执行DNS配置任务（EXC DNSCFGTASK）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：CloudEPSN**

该命令在对接BLUECAT场景用于进行部署任务、创建缓存、清除缓存等操作。

该命令在对接CloudDNS场景用于进行标识和启动核查任务操作。通过EXC DNSCFGTASK: TASKACT=INIT;命令标识后续执行的DNS配置下发操作需要核查，配置下发完成后通过EXC DNSCFGTASK: TASKACT=DEPLOY;命令启动核查任务，核查下发的配置是否从控制节点到业务节点完成同步且数据一致。

#### 注意事项

- 该命令执行后立即生效。
- 该命令用于多种对接的第三方应用，请根据当前对接的第三方应用参考使用实例。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:-----------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TASKACT    | 执行动作   | 可选必选说明：必选参数 参数含义：该参数表示任务执行的动作。 数据来源：本端规划 取值范围：在枚举类型中选择。 INIT：任务初始化。DEPLOY：部署任务。PRE_VERIFY：预处理。POST_VERIFY：后处理。CLEAR：清除任务状态。QRYCACHE：查询任务缓存。QRYDB：查询DNS数据库。 默认值：无 配置原则： 初始化任务：在用GEN DNSCFGTASK命令生成任务ID之后，需要对该任务ID进行初始化，完成初始化之后，才能进行资源配置操作。部署任务：在完成所有资源配置下发之后，给DNS服务器下发部署任务，使资源配置生效。预处理：操作前任务预处理。后处理：操作完成后任务处理。清除任务状态：任务状态异常的情况下，强制初始化任务状态。查询任务缓存：任务执行结束后，采集最近1小时的运行日志，存储在dns_cache.txt文件中。在CSP界面，依次选择“监控分析 -> 运行日志 -> 服务日志收集”，选择CELLSFMU服务，设置时间段进行日志采集。查询DNS数据库：预留参数，当前不生效。 |
| TASKID     | 任务ID   | 可选必选说明：条件必选参数 前提条件：该参数在“TASKACT”配置为“CLEAR”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“TASKACT”配置为“DEPLOY” 或 “INIT”时为可选参数。 参数含义：该参数表示即将执行命令的任务ID。 数据来源：本端规划 取值范围：0~65535。 默认值：无 配置原则：该参数必须为GEN DNSTASKID命令生成的ID。                                                                                                                                                                                                                                                                        |
| SERVERNAME | 服务器名称  | 可选必选说明：条件可选参数 前提条件：该参数在“TASKACT”配置为“DEPLOY”时为可选参数。 参数含义：该参数表示用于部署的DNS服务器名称。 数据来源：本端规划 取值范围：1~1023位字符。 默认值：无 配置原则：可以指定多个DNS server名称，以空格分开。                                                                                                                                                                                                                                                                                                                                 |

#### 使用实例

- 执行任务初始化操作：

  ```
  %%EXC DNSCFGTASK: TASKACT=INIT, TASKID=1;%%
  RETCODE = 0  操作成功

  进度报文
  ---------------
  上报类型  =  执行DNS配置任务
      状态  =  开始
      进度  =  0%
    会话号  =  10.10.10.10_532
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=INIT, TASKID=1;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  进行中
      进度  =  10%
    会话号  =  10.10.10.10_532
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=INIT, TASKID=1;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  进行中
      进度  =  20%
    会话号  =  10.10.10.10_532
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=INIT, TASKID=1;%%
  RETCODE = 0  操作成功

  会话号 = 10.10.10.10_532

  ---    END

  %%EXC DNSCFGTASK: TASKACT=INIT, TASKID=1;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  成功
    会话号  =  10.10.10.10_532
  (结果个数 = 1)

  共有5个报告
  ---    END
  ```
- 执行DNS配置部署：

  ```
  %%EXC DNSCFGTASK: TASKACT=DEPLOY, TASKID=1, SERVERNAME="DNS-DDS001";%%
  RETCODE = 0  操作成功

  会话号 = 10.10.10.10_2352

  ---    END

  %%EXC DNSCFGTASK: TASKACT=DEPLOY, TASKID=1, SERVERNAME="DNS-DDS001";%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  开始
      进度  =  0%
    会话号  =  10.10.10.10_2352
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=DEPLOY, TASKID=1, SERVERNAME="DNS-DDS001";%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  进行中
      进度  =  10%
    会话号  =  10.10.10.10_2352
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=DEPLOY, TASKID=1, SERVERNAME="DNS-DDS001";%%
  RETCODE = 0  操作成功  

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  成功
    会话号  =  10.10.10.10_2352
  (结果个数 = 1)

  共有4个报告
  ---    END
  ```
- 执行预处理：

  ```
  %%EXC DNSCFGTASK: TASKACT=PRE_VERIFY;%%
  RETCODE = 0  操作成功

  会话号 = 10.10.10.10_537

  ---    END

  %%EXC DNSCFGTASK: TASKACT=PRE_VERIFY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  开始
      进度  =  0%
    会话号  =  10.10.10.10_537
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=PRE_VERIFY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  进行中
      进度  =  10%
    会话号  =  10.10.10.10_537
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=PRE_VERIFY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  进行中
      进度  =  20%
    会话号  =  10.10.10.10_537
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=PRE_VERIFY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  成功
    会话号  =  10.10.10.10_537
  (结果个数 = 1)

  共有5个报告
  ---    END
  ```
- 执行后处理：

  ```
  %%EXC DNSCFGTASK: TASKACT=POST_VERIFY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  开始
      进度  =  0%
    会话号  =  10.10.10.10_538
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=POST_VERIFY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  进行中
      进度  =  10%
    会话号  =  10.10.10.10_538
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=POST_VERIFY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  进行中
      进度  =  20%
    会话号  =  10.10.10.10_538
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=POST_VERIFY;%%
  RETCODE = 0  操作成功

  会话号 = 10.10.10.10_538

  ---    END

  %%EXC DNSCFGTASK: TASKACT=POST_VERIFY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  成功
    会话号  =  10.10.10.10_538
  (结果个数 = 1)

  共有5个报告
  ---    END
  ```
- 执行清除缓存操作：

  ```
  %%EXC DNSCFGTASK: TASKACT=CLEAR, TASKID=1;%%
  RETCODE = 0  操作成功

  会话号 = 10.10.10.10_539

  ---    END

  %%EXC DNSCFGTASK: TASKACT=CLEAR, TASKID=1;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  开始
      进度  =  0%
    会话号  =  10.10.10.10_539
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=CLEAR, TASKID=1;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  成功
    会话号  =  10.10.10.10_539
  (结果个数 = 1)

  共有3个报告
  ---    END
  ```
- 执行查询缓存操作：

  ```
  %%EXC DNSCFGTASK: TASKACT=QRYCACHE;%%
  RETCODE = 0  操作成功

  会话号 = 10.10.10.10_6540

  ---    END

  %%EXC DNSCFGTASK: TASKACT=QRYCACHE;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  开始
      进度  =  0%
    会话号  =  10.10.10.10_6540
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=QRYCACHE;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  成功
    会话号  =  10.10.10.10_6540
  (结果个数 = 1)

  共有3个报告
  ---    END
  ```
- 执行标识配置需要核查操作（对接CloudDNS场景）：

  ```
  %%EXC DNSCFGTASK: TASKACT=INIT;%%
  RETCODE = 0  操作成功

  进度报文
  ---------------
  上报类型  =  执行DNS配置任务
      状态  =  成功
    会话号  =  10.10.10.10_532
  (结果个数 = 1)

  ---    END
  ```
- 执行DNS配置核查任务启动操作（对接CloudDNS场景）：

  ```
  %%EXC DNSCFGTASK: TASKACT=DEPLOY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  进行中
      进度  =  10%
    会话号  =  10.10.10.10_538
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=DEPLOY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  进行中
      进度  =  20%
    会话号  =  10.10.10.10_538
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=DEPLOY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  进行中
      进度  =  50%
    会话号  =  10.10.10.10_538
  (结果个数 = 1)

  ---    END

  %%EXC DNSCFGTASK: TASKACT=DEPLOY;%%
  RETCODE = 0  操作成功

  进度报文
  --------
  上报类型  =  执行DNS配置任务
      状态  =  完成
    会话号  =  10.10.10.10_538
  (结果个数 = 1)

  ---    END
  ```