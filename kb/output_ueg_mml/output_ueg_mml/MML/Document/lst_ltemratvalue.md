# 查询LTE-M用户的RAT值（LST LTEMRATVALUE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、SGW-C、SMF**

该命令用于查询终端通过LTE-M接入方式时UNC给周边网元发送消息时RAT信元中携带的值。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询终端通过LTE-M接入方式时，UNC给周边网元发送的消息中RAT信元携带的值：

```
%%LST LTEMRATVALUE:;%%
RETCODE = 0  操作成功

结果如下
--------
                和OCS交互使用的RAT值  =  LTE_M
                和CHF交互使用的RAT值  =  LTE_M
                 和CG交互使用的RAT值  =  LTE_M
      和AAA计费服务器交互使用的RAT值  =  LTE_M
      和AAA鉴权服务器交互使用的RAT值  =  LTE_M
               和PCRF交互使用的RAT值  =  LTE_M
                和PCF交互使用的RAT值  =  LTE_M
UNC作为SGW-C发送给PGW-C时使用的RAT值  =  LTE_M
                和UPF交互使用的RAT值  =  LTE_M
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                      | 输出项解释                                 |
|:---------------------------|:--------------------------------------|
| 和OCS交互使用的RAT值              | 该参数用于指定UNC和OCS交互时使用的RAT值。             |
| 和CHF交互使用的RAT值              | 该参数用于指定UNC和CHF交互时使用的RAT值。             |
| 和CG交互使用的RAT值               | 该参数用于指定UNC和CG交互时使用的RAT值。              |
| 和AAA计费服务器交互使用的RAT值         | 该参数用于指定UNC和AAA计费服务器交互时使用的RAT值。        |
| 和AAA鉴权服务器交互使用的RAT值         | 该参数用于指定UNC作为PGW-C和AAA鉴权服务器交互时使用的RAT值。 |
| 和PCRF交互使用的RAT值             | 该参数用于指定UNC作为PGW-C和PCRF交互时使用的RAT值。     |
| 和PCF交互使用的RAT值              | 该参数用于指定UNC和PCF交互时使用的RAT值。             |
| UNC作为SGW-C发送给PGW-C时使用的RAT值 | 该参数用于指定UNC作为SGW-C和PGW-C交互时使用的RAT值。    |
| 和UPF交互使用的RAT值              | 该参数用于指定UNC和UPF交互时使用的RAT值。             |