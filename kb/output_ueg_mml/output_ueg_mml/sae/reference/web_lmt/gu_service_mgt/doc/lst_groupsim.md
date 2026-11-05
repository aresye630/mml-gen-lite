# 查询GROUPSIM用户组(LST GROUPSIM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此操作用来查询GROUPSIM用户组信息。通过参数“组IMSI号码”或“组MSISDN号码”来唯一标识一个GROUPSIM用户组。

## 注意事项

无

## 参数说明

| 参数标识   | 参数名称      | 参数说明                                               |
|:-------|:----------|:---------------------------------------------------|
| GIMSI  | 组IMSI号码   | GROUPSIM用户组的IMSI号码。 取值范围：E.212格式的编码，6～15位的十进制数字。   |
| GISDN  | 组MSISDN号码 | GROUPSIM用户组的MSISDN号码。 取值范围：E.164格式的编码，1～15位的十进制数字。 |

## 使用实例

查询GIMSI号码为460000009123456的GROUPSIM用户组信息。

```
LST GROUPSIM: GIMSI="460000009123456";
```

```
%%LST GROUPSIM: GIMSI="460000009123456";%%
RETCODE = 0 SUCCESS0001:操作成功

                         GIMSI = 460000009123456
                         GISDN = 460000009123489
                      MSIMTYPE = Parallel
                      USERTYPE = 254
                      TONETYPE = Intelligent_Tone
                         CFSUP = TRUE
                         PTIME = 0
                    MEMBERISDN = 460000009123488
                         ORDER = 1

Total count = 9

There is together 1 report

---    END
```

## 输出结果说明

输出项的详细说明请参见MOD GROUPSIM、MOD GROUPUSER命令的参数说明。