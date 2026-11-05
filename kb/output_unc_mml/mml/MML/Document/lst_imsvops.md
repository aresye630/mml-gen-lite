# 查询VoPS配置(LST IMSVOPS)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询SGSN和MME覆盖的RAN对PS域IMS（IP多媒体子系统）语音能力的支持情况，以及IMS语音业务相关的扩展功能。

#### 注意事项

- 此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

执行如下命令查询SGSN和MME侧对PS域IMS语音能力的支持情况:

LST IMSVOPS:;

```
%%LST IMSVOPS:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
            SGSN侧全部支持PS域IMS语音  =  未指定
             MME侧全部支持PS域IMS语音  =  未指定
             支持IMS VoPS的TA获取模式  =  无效
                       跟踪区群组标识  =  NULL
基于语音域优选参数的SRVCC能力判断策略 =  NULL 
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**SET IMSVOPS**的参数说明。