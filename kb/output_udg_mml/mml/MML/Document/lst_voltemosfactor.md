# 查询MOS计算值的补偿因子（LST VOLTEMOSFACTOR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询MOS计算值的补偿因子。

#### 注意事项

EVS NB/EVS WB/EVS SWB/EVS FB/EVS AMR-WB IO在未配置时不显示。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询MOS计算值的补偿因子：

```
LST VOLTEMOSFACTOR:;
```

```
RETCODE = 0  操作成功

MOS补偿因子配置
---------------
语音编解码类型    MOS补偿因子1    MOS补偿因子2    MOS补偿因子3    MOS补偿因子4    MOS补偿因子5

AMR NB            0               0                 0               0               0           
AMR WB            0               0                 0               0               0           
G.711             0               0                 0               0               0           
G.722             0               0                 0               0               0           
G.729             0               0                 0               0               0           
EVS NB            0               0                 0               0               0           
EVS WB            0               0                 0               0               0           
EVS SWB           0               0                 0               0               0           
EVS FB            0               0                 0               0               0           
EVS AMR-WB IO     0               0                 0               0               0           
(结果个数 = 10)
---    END
```

#### 输出结果说明

参见SET VOLTEMOSFACTOR的参数说明。