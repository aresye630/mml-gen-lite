# 查询LAS TLS协议配置（LST LASTLSCFG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询TLS协议配置信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询TLS协议配置信息。

```
LST LASTLSCFG:;
```

```
%%LST LASTLSCFG:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------
                     协议版本  =  TLS1.2
                   强加密套件  =  TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_RSA_WITH_AES_128_GCM_SHA256&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
                 兼容加密套件  =  NULL
                  TLS配置描述  =  TLS Config
(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见命令**SET LASTLSCFG**的参数说明。