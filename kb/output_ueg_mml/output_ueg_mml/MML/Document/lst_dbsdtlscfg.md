# 查询DBS DTLS协议配置(LST DBSDTLSCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询DTLS协议配置信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询DTLS协议配置信息。

```
LST DBSDTLSCFG:;
```

```
%%LST DBSDTLSCFG:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------
    协议版本  =  DTLS1.2
  强加密套件  =  TLS_DHE_DSS_WITH_AES_128_GCM_SHA256&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384&TLS_DHE_RSA_WITH_AES_128_GCM_SHA256&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
兼容加密套件  =  NULL
DTLS配置描述  =  NULL
(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET DBSDTLSCFG**命令的参数说明。