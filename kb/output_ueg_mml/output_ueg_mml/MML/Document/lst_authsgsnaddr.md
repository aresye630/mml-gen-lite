# 查询向AAA鉴权服务器发送消息中携带的地址信息（LST AUTHSGSNADDR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、SGW-C**

该命令用来查询SPW-C和PGW-C合一形态向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元的配置。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询SPW-C和PGW-C向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元的配置 ：

```
%%LST AUTHSGSNADDR:;%%
RETCODE = 0  操作成功

结果如下
--------
3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元中携带的地址信息  =  Pa接口
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                                               | 输出项解释                                                                               |
|:----------------------------------------------------|:------------------------------------------------------------------------------------|
| 3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元中携带的地址信息 | SPW-C和PGW-C合一形态向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6–Address信元携带的地址信息。 |