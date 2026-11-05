# 显示去活操作状态（DSP DEACTIVESTATE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询手动批量去激活命令的执行情况。指定IMSI、MSISDN、或IMEI的用户去激活无法被查询。

执行该命令时，Remain Time (hour)实际时间受CPU占用率影响。CPU占用率越高，实际Remain Time可能会比预期的计算时间长。

#### 注意事项

该命令执行后需要关闭已经创建了数据面跟踪的所有跟踪任务，重新创建新的跟踪任务才能生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

执行DEA SESSION命令后，使用DSP DEACTIVESTATE命令查询执行结果：

```
DSP DEACTIVESTATE:;
```

```
RETCODE = 0 操作成功。

Deactivation Info:
------------------
Result  =  
       Deactivation parameter setting = NF
                      Execution stage = Deleting
            To delete sessions number = 516168
              Deleted sessions number = 516157
                   Remain Time (hour) = 0.1
            Deactivation rate-setting = 2000
(结果个数 = 1)
--- END
```

#### 输出结果说明

| 输出项名称                          | 输出项解释                                             |
|:-------------------------------|:--------------------------------------------------|
| Deactivation parameter setting | DEA SESSION命令的配置参数。                               |
| Execution stage                | DEA SESSION命令的执行阶段。取值为如下几种：正在删除、删除操作执行完成、未执行删除操作。 |
| To delete sessions number      | 预期删除的会话数。                                         |
| Deleted sessions number        | 已删除会话数。                                           |
| Remain Time (hour)             | 系统估计的距离完成删除任务所需的时间。                               |
| Deactivation rate-setting      | SET DEACTIVERATE命令配置的去活速率。取值范围：10～2000。           |