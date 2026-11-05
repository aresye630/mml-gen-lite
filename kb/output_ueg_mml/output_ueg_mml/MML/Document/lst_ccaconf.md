# 查询客户端认证断言配置(LST CCACONF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询UDM作为Consumer时是否生成CCA、CCA的有效期以及UDM作为Producer时是否校验CCA。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询UDM作为Consumer和Producer时CCA配置：

```
LST CCACONF:;
```

```
%%LST CCACONF:;%%
RETCODE = 0  操作成功

操作结果如下:
------------
是否生成CCA  =  不生成CCA
CCA的有效期  =  86400
是否检查CCA  =  不校验CCA
(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET CCACONF**命令的参数说明。