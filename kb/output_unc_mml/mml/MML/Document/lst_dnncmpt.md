# 查询DNN兼容性控制参数（LST DNNCMPT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询AMF与周边NF交互时的DNN相关控制参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询AMF上当前配置的DNN兼容性控制参数，执行如下命令：

```
%%LST DNNCMPT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
          本网用户DNN格式  =  仅网络标识
       LBO漫游用户DNN格式  =  完整DNN
        HR漫游用户DNN格式  =  完整DNN
     AMF间本网用户DNN格式  =  仅网络标识
AMF间LBO漫游会话的DNN格式  =  完整DNN
   AMF间HR漫游会话DNN格式  =  完整DNN
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称             | 输出项解释                                                                                                             |
|:------------------|:------------------------------------------------------------------------------------------------------------------|
| 本网用户DNN格式         | 该参数用于标识AMF针对本网用户，向SMF（包括I-SMF）发送Nsmf_PDUSession_CreateSMContext时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。    |
| LBO漫游用户DNN格式      | 该参数用于标识AMF针对LBO漫游用户，向SMF（包括I-SMF）发送Nsmf_PDUSession_CreateSMContext时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。 |
| HR漫游用户DNN格式       | 该参数用于标识AMF针对HR漫游用户，向V-SMF发送Nsmf_PDUSession_CreateSMContext时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。         |
| AMF间本网用户DNN格式     | 该参数用于标识AMF针对本网用户向新侧AMF发送PDU信息时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。                                      |
| AMF间LBO漫游会话的DNN格式 | 该参数用于标识AMF针对LBO漫游会话向新侧AMF发送PDU信息时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。                                   |
| AMF间HR漫游会话DNN格式   | 该参数用于标识AMF针对HR漫游会话向新侧AMF发送PDU信息时携带的DNN、selectedDnn是否包含OI（Operator Identifier）。                                    |