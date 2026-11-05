# 查询PCRF返回消息属性（LST PCCPCRFMSGATTR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询PCRF返回消息属性的配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询PCRF返回消息属性的配置：

```
LST PCCPCRFMSGATTR:;
```

```
RETCODE = 0  操作成功

PCRF消息属性信息
----------------
基于CCA-U Origin-Host AVP触发PCRF重选  =  禁止
  基于RAR Origin-Host AVP触发PCRF重选  =  禁止
基于CCA-I Origin-Host AVP触发PCRF重选  =  禁止
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET PCCPCRFMSGATTR的参数说明。