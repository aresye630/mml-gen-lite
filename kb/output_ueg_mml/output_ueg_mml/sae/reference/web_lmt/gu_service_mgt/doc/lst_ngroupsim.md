# 以格式2查询用户GROUPSIM数据(LST NGROUPSIM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询用户GROUPSIM数据，以指定的格式返回查询结果。

使用场景限于运营商对返回报文有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                  |
|:-------|:-------|:------------------------------------------------------|
| GIMSI  | IMSI   | 此参数用于设置GIMSI号码。 取值范围：E.212格式的编码，6～15位的十进制数字。 说明：可选参数。 |
| GISDN  | MSISDN | 此参数用于设置GISDN号码。 取值范围：E.164格式的编码，1～15位的十进制数字。 说明：可选参数。 |

## 使用实例

查询用户数据，以特定的数据格式返回。命令如下：

```
LST NGROUPSIM: GIMSI="461360000000000";
```

```
%%LST NGROUPSIM: GIMSI="461360000000000";%%
RETCODE = 0 SUCCESS0001:Operation is successful

        GROUP INFORMATION:
        INTERNATIONAL MOBILE SUBSCRIBER IDENTITY ... 461360000000000
        MOBILE STATION ISDN NUMBER ................. 461360000000000
        MOBILE STATION CATEGORY .................... GR
        ACTIVATION STATUS .......................... A
        TYPE OF HUNTING ............................ S
        TYPE OF GROUP USER ......................... MUL
        CALL FORWARDING SUPPRESSION ................ N
        NO ANSWER TIME FOR SEQUENTIAL ALERTING ..... N
        NO ANSWER TIME FOR PARALLEL ALERTING ....... N
        TYPE OF HUNTING FOR DATA CALLS ............. N

        MEMBER ID                      ORDER      PRIMARY
        461360000000001                1          Y
        461360000000002                2          N

                   
        HLRU IDENTITY .............................. 1

Total count = 13

There is together 1 report

---    END
```