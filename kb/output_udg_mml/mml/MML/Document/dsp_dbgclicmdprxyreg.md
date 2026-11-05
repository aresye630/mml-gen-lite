# 显示通过命令代理可执行命令行调试命令的白名单（DSP DBGCLICMDPRXYREG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示通过命令代理可执行命令行调试命令的白名单。

#### 注意事项

- 该命令执行后立即生效。
- 该命令用于收集定位信息，需要谨慎执行，请在华为工程师指导下执行。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                         |
|:----------------|:-------|:-------------------------------------------------------------------------------------------------------------|
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### 使用实例

显示通过命令代理可执行命令行调试命令的白名单：

```
DSP DBGCLICMDPRXYREG:SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功  

结果如下: 
--------- 
调试命令类ID  调试命令                                                    调试命令类型    
135356728     clear system cpu statistics                                 2              
137372048     display alarm notification subscription                     1              
135667988     display cli trace                                           1                            
134816092     display system state-trace process                          1              
144843019     display trace trace-server notification subscription        1              
135619073     reset configuration diagnostic-information                  2              
238502008     reset message send-receive-statistic                        2              
163537411     set configuration diagnostic-information max-record-number  2              
238502005     set message send-receive-statistic                          2              
(结果个数 = 9)
--- END
```

#### 输出结果说明

| 输出项名称   | 输出项解释                                    |
|:--------|:-----------------------------------------|
| 调试命令类ID | 用于显示调试命令类ID。                             |
| 调试命令    | 用于显示调试命令。                                |
| 调试命令类型  | 用于显示可以通过命令代理执行的命令行调试命令的类型， 1：查询类。2：非查询类。 |