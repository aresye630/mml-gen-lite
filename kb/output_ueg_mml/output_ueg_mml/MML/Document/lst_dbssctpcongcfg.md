# 查询DBS SCTP拥塞控制参数(LST DBSSCTPCONGCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

本命令用于查询DBS SCTP拥塞控制参数的取值。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询DBS SCTP拥塞控制参数的取值。

```
LST DBSSCTPCONGCFG:;
```

```
%%LST DBSSCTPCONGCFG:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------
                  开关  =  ON
      拥塞控制算法类型  =  Congestion control algorithm BBR
      正常消息积压时延  =  50
      过载消息积压时延  =  500
        正常缓存占用率  =  60
        过载缓存占用率  =  80
(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET DBSSCTPCONGCFG**命令的参数说明。

## 参考信息

无。