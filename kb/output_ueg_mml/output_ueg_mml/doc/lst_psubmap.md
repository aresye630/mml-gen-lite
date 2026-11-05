# 查询多卡用户所属用户（LST PSUBMAP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用来查询多卡用户从属的从用户。

## 注意事项

无。

## 参数说明

| 参数标识               | 参数名称   | 参数说明                                         |
|:-------------------|:-------|:---------------------------------------------|
| USRTHIRDIDENTIFIER | 多卡用户标识 | 用于标识Multi-SIM用户的标识。 取值范围：长度不超过20的字符串。 默认值：无。 |

## 使用实例

查询用户签约：“多卡用户标识”为“MultiSim01”：

```
LST PSUBMAP: USRTHIRDIDENTIFIER="MultiSim01";
```

输出结果如下：

```
%%LST PSUBMAP: USRTHIRDIDENTIFIER="MultiSim01";%%
RETCODE = 0 Operation succeeded

Common Subscriber ID
Master01Slave01      

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

| 输出项名称                | 输出项解释                                      |
|:---------------------|:-------------------------------------------|
| Common Subscriber ID | 用于标识多卡用户所属的从用户标识。 取值范围：长度不超过20的字符串。 默认值：无。 |