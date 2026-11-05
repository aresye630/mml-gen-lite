# 查询AMF与PCF消息交互处理策略（LST AMFPCFPRCSSPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询AMF与PCF之间消息的处理策略。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询AMF与PCF之间消息的处理策略，执行如下命令：

```
%%LST AMFPCFPRCSSPLCY:;%%
RETCODE = 0  操作成功

结果如下
--------
          AMF收到Termination处理策略  =  校验偶联ID
创建AM偶联时收到UpdateNotify处理策略  =  抢占
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                       | 输出项解释                                                                                                 |
|:----------------------------|:------------------------------------------------------------------------------------------------------|
| AMF收到Termination处理策略        | 该参数用于指示AMF创建AM策略偶联后收到AM-PCF发送的Npcf_AMPolicyControl_AmPolicyAssociationTerminateNotify Request消息的处理策略。 |
| 创建AM策略偶联时收到UpdateNotify处理策略 | 该参数用于指示AMF发送Npcf_AMPolicyControl_Create Request消息后收到Npcf_AMPolicyControl_UpdateNotify Request消息的处理策略。 |