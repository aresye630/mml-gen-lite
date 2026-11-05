# 显示5G LAN MAC地址超规格信息（DSP NGLANMACEXINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于显示5G LAN MAC地址超规格信息。

#### 注意事项

此命令每次最多显示10个MAC地址超限的用户信息。清除无效的MAC地址后，如果告警依然存在，请重新执行该命令。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                                                            |
|:-----------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数 参数含义：该参数用于指定5G LAN组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为18～37。VnInstance以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

查询当前超规格MAC信息 ：

```
%%DSP NGLANMACEXINFO: VNINSTANCE="a0000001-460-003-01";
```

```
%%
RETCODE = 0  操作成功

5G LAN MAC地址超规格信息
---------------------------------------------------------
Result  =  

                               UE  =  53456789012342
                      Mac Address  =  76-BB-CC-DD-EE-40
                      Mac Address  =  76-BB-CC-DD-EE-39
                      Mac Address  =  76-BB-CC-DD-EE-38
                      Mac Address  =  76-BB-CC-DD-EE-37
                      Mac Address  =  76-BB-CC-DD-EE-36
                      Mac Address  =  76-BB-CC-DD-EE-35
                      Mac Address  =  76-BB-CC-DD-EE-34
                      Mac Address  =  76-BB-CC-DD-EE-33
                      Mac Address  =  76-BB-CC-DD-EE-32
                      Mac Address  =  76-BB-CC-DD-EE-31
                      Mac Address  =  76-BB-CC-DD-EE-30
                      Mac Address  =  76-BB-CC-DD-EE-29
                      Mac Address  =  76-BB-CC-DD-EE-28
                      Mac Address  =  76-BB-CC-DD-EE-27
                      Mac Address  =  76-BB-CC-DD-EE-26
                      Mac Address  =  76-BB-CC-DD-EE-25
                      Mac Address  =  76-BB-CC-DD-EE-24
                      Mac Address  =  76-BB-CC-DD-EE-23
                      Mac Address  =  76-BB-CC-DD-EE-22
                      Mac Address  =  76-BB-CC-DD-EE-21
(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释                    |
|:--------|:-------------------------|
| Result  | 结果信息，显示超过规格的用户、双发选收结对信息。 |