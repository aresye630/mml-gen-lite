# 查询SA指纹识别统计结果（DSP FINGIDENSTATIC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用来查询SA指纹识别的统计结果。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

显示SA指纹识别的统计结果：

```
DSP FINGIDENSTATIC:;
```

```
RETCODE = 0  操作成功

指纹识别统计信息
----------------------------------------
统计结果                                                                                                                                                                                                     

Pod Name(ssgpod-0):
StatisticStartTime is 2022-03-18 15:06:00
Protocol            DB counter          FP counter          DB=FP counter       DB<>FP counter
facebook            1000                2000                500                 200                 
youtube             3000                4000                800                 300       
(Statistic-Number = 2)

Pod Name(ssgpod-1):
StatisticStartTime is 2022-03-18 15:06:00
Protocol            DB counter          FP counter          DB=FP counter       DB<>FP counter
facebook            1000                2000                500                 200                 
youtube             3000                4000                800                 300       
(Statistic-Number = 2)

(结果个数 = 2)
---    END
```

#### 输出结果说明

| 输出项名称              | 输出项解释                                         |
|:-------------------|:----------------------------------------------|
| Pod Name           | 该参数用于描述POD的名称。                                |
| StatisticStartTime | 本次统计开始时间。                                     |
| Protocol           | 开启SA指纹识别功能的应用子协议名称。                           |
| DB counter         | 通过传统特征库识别应用协议成功，但指纹识别应用协议失败的次数。               |
| FP counter         | 通过传统特征库识别应用协议失败，但指纹识别应用协议成功的次数。               |
| DB=FP counter      | 通过传统特征库识别应用协议成功，同时指纹识别应用协议也成功，并且两者识别结果相同的次数。  |
| DB<>FP counter     | 通过传统特征库识别应用协议成功，同时指纹识别应用协议也成功，并且两者识别结果不相同的次数。 |