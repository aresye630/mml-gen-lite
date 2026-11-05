# 查询FQDN端口策略（LST SBIFQDNPORTPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG、NEF、NWDAF、SCF**

该命令用于显示FQDN使用端口号的策略。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询所有FQDN端口号的策略。

```
%%LST SBIFQDNPORTPLCY:;%%
RETCODE = 0  操作成功

结果如下
--------
场景        范围              对端PLMN  端口策略

TARGETADDR  INTERPLMNDEFAULT  NULL      USEPORT
TARGETADDR  BYPLMN            12303     NOTUSEPORT
(结果个数 = 2)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                 |
|:--------|:----------------------|
| 场景      | 该参数用于指定端口策略适用的场景。     |
| 范围      | 该参数用于指定FQDN端口策略的适用范围。 |
| 对端PLMN  | 该参数用于指定策略适用的对端PLMN。   |
| 端口策略    | 该参数用于指定FQDN使用端口号的策略。  |