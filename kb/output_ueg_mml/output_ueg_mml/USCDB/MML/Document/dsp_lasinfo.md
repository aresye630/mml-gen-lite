# 显示LAS信息（DSP LASINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询LAS微服务所在的Pod名称和进程ID。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询LAS微服务的Pod名称与进程ID。

```
DSP LASINFO:;
```

```
%%DSP LASINFO:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------
Pod名称和进程ID  
udrlasservice81-0_0      
udrlasservice81-0_5      
udrlasservice81-0_2      
udrlasservice81-0_4      
udrlasservice81-0_3      
udrlasservice81-0_1      
udrlasservice81-1_4      
udrlasservice81-1_1      
udrlasservice81-1_3      
udrlasservice81-1_0      
udrlasservice81-1_5      
udrlasservice81-1_2      
(结果个数 = 12)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见表1中的参数说明。

| 输出项名称      | 输出项解释                      |
|:-----------|:---------------------------|
| Pod名称和进程ID | 用于表示当前LAS微服务所在的Pod名称和进程ID。 |