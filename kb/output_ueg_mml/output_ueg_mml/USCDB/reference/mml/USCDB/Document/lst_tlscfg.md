# 查询TLS协议配置（LST TLSCFG）

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

| 参数标识    | 参数名称   | 参数说明                                       |
|:--------|:-------|:-------------------------------------------|
| USTYPE  | 用途类型   | 用于指示系统按照哪个用途类型查询TLS协议配置信息；若不输入，则表示所有的用途类型。 |
| INFTYPE | 接口类型   | 用于指示系统按照哪个接口类型查询TLS协议配置信息；若不输入，则表示所有的接口类型。 |

## 使用实例

1. 查询指定接口类型的配置，该“接口类型”为“WEBLMT”。

   ```
   LST TLSCFG: USTYPE=SERVER, INFTYPE=WEBLMT;
   ```

   ```
   %%LST TLSCFG: USTYPE=SERVER, INFTYPE=WEBLMT;%%
   RETCODE = 0  操作成功

   操作结果如下
   ----------
                     用途类型     =  服务端
                     接口类型     =  WEBLMT
                     协议版本     =  TLS1.2
                   强加密套件     =  TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 
                                  =  TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
                                  =  TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
                                  =  TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
                                  =  TLS_DHE_DSS_WITH_AES_128_GCM_SHA256 
                                  =  TLS_DHE_DSS_WITH_AES_256_GCM_SHA384 
                                  =  TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
                                  =  TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
                 兼容加密套件     =  DHE_DSS_AES_256_CBC_SHA256(DHE_DSS_AES_256_CBC_SHA256)
                                  =  DHE_DSS_AES_128_CBC_SHA256(DHE_DSS_AES_128_CBC_SHA256)
                                  =  DHE_DSS_AES_256_CBC_SHA(DHE_DSS_AES_256_CBC_SHA)
                                  =  DHE_DSS_AES_128_CBC_SHA(DHE_DSS_AES_128_CBC_SHA)
                                  =  DHE_RSA_3DES_EDE_CBC_SHA(DHE_RSA_3DES_EDE_CBC_SHA)
                                  =  RSA_3DES_EDE_CBC_SHA(RSA_3DES_EDE_CBC_SHA)
                                  =  DHE_DSS_3DES_EDE_CBC_SHA(DHE_DSS_3DES_EDE_CBC_SHA)
                                  =  RSA_RC4_128_SHA(RSA_RC4_128_SHA)
                                  =  RSA_NULL_SHA256(RSA_NULL_SHA256)
                                  =  RSA_AES_128_CBC_SHA256(RSA_AES_128_CBC_SHA256)
                                  =  RSA_RC4_128_MD5(RSA_RC4_128_MD5)
                                  =  ADH_AES_256_CBC_SHA256(ADH_AES_256_CBC_SHA256)
                                  =  ADH_AES_128_CBC_SHA256(ADH_AES_128_CBC_SHA256)
                                  =  ADH_AES_256_CBC_SHA(ADH_AES_256_CBC_SHA)
                                  =  ADH_AES_128_CBC_SHA(ADH_AES_128_CBC_SHA)
                                  =  ADH_RC4_128_MD5(ADH_RC4_128_MD5)
                                  =  RSA_NULL_SHA(RSA_NULL_SHA)
                                  =  RSA_NULL_MD5(RSA_NULL_MD5)
                                  =  DHE_RSA_AES_256_CBC_SHA256
                                  =  RSA_AES_256_CBC_SHA256 
                                  =  DHE_RSA_AES_128_CBC_SHA256 
                                  =  DHE_RSA_AES_256_CBC_SHA
                                  =  RSA_AES_256_CBC_SHA
                                  =  RSA_AES_128_CBC_SHA 
                                  =  DHE_RSA_AES_128_CBC_SHA
                  TLS配置描述     =  WEBLMT Default Configuration
                  加密套件排序    =  FALSE         
   (结果个数 = 1)

   ---    END
   ```
2. 查询所有接口类型的配置。

   ```
   LST TLSCFG:;
   ```

   ```
   %%LST TLSCFG:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------------------
    用途类型    接口类型        协议版本          强加密套件                                                                    兼容加密套件             TLS配置描述                                   加密套件排序
    服务端      WEBLMT          TLS1.2            TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384  NULL                     WEBLMT Default Configuration For Server       TRUE
    客户端      SOAP            TLS1.2            TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384  NULL                     SOAP Default Configuration For Client         TRUE
    服务端      SOAP            TLS1.2            TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384  NULL                     SOAP Default Configuration For Server         FALSE
    服务端      DMSWEB          TLS1.2            TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384  NULL                     DMSWEB Default Configuration For Server       TRUE

   (结果个数 = 4)

   ---    END
   ```

## 输出结果说明

请参见**SET TLSCFG**命令的参数说明。