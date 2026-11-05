# 查询基于SA的Intelligence训练参数（LST SAAITRAINPARA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询基于SA的intelligence训练参数。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

如果想查询基于SA的intelligence训练参数，执行以下命令：

```
LST SAAITRAINPARA:;
```

```
RETCODE = 0  操作成功

基于SA的intelligence训练参数
----------------------------
        Intelligence训练阈值  =  9900
        Intelligence训练开关  =  不使能
Intelligence训练周期（分钟）  =  30
      Intelligence训练抽样率  =  0
        SA性能优化库有效时间  =  300
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET SAAITRAINPARA的参数说明。