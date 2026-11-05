# 查询HLB TLS协议配置 (LST UDMHLBTLSCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询已配置的HLB TLS协议信息。

- 若需要查询所有配置的HLB TLS协议信息，请不要输入任何参数。
- 若需要查询某个HLB TLS协议信息，请输入“TLS配置ID”或“TLS配置名称”。
- 若需要查询某个协议版本的所有HLB TLS协议信息，请下拉选择“协议版本”。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                                                                                              |
|:------------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TLSCFGID    | TLS配置ID | 可选必选说明：可选参数 参数含义：用于指示系统按照哪个TLS配置ID查询HLB TLS协议配置信息；若不输入，则表示查询所有的TLS配置ID信息。 取值范围：1～128 默认值：无。 配置原则：无。                                                                               |
| TLSCFGNAME  | TLS配置名称 | 可选必选说明：可选参数 参数含义：用于指示系统按照哪个TLS配置名称查询HLB TLS协议配置信息。 取值范围：长度不超过32字节的字符串，只允许输入0～9，a～z，A～Z，“-”和“_”。 默认值：无。 配置原则：无。                                                                    |
| PROTOCOLVER | 协议版本    | 可选必选说明：可选参数 参数含义：用于指定系统按照哪个TLS协议版本查询HLB TLS协议配置信息。 取值范围： TLS1.2(TLS1.2)：支持TLS1.2协议版本。TLS1.3(TLS1.3)：支持TLS1.3协议版本。TLS1.2_TLS1.3(TLS1.2_TLS1.3)：支持TLS1.2和TLS1.3协议版本。 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有的HLB TLS配置信息：

   ```
   LST UDMHLBTLSCFG:;
   ```

   ```
   %%LST UDMHLBTLSCFG:;%%
   RETCODE = 0  操作成功

   TLS配置ID  TLS配置名称  协议版本       TLS1.2加密套件                                                                                                                                                                                                                                                                                                                                                   TLS1.3加密套件                                                                                     TLS配置描述  证书校验  

   1          default      TLS1.2_TLS1.3  TLS_DHE_RSA_WITH_AES_128_GCM_SHA256&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_RSA_WITH_AES_128_CCM&TLS_DHE_RSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM  TLS_AES_128_GCM_SHA256&TLS_AES_256_GCM_SHA384&TLS_CHACHA20_POLY1305_SHA256&TLS_AES_128_CCM_SHA256  default      校验      
   4          add          TLS1.2         TLS_DHE_RSA_WITH_AES_128_GCM_SHA256&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_RSA_WITH_AES_128_CCM&TLS_DHE_RSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM  NULL                                                                                               NULL         校验      
   (结果个数 = 2)

   ---    END
   ```
2. 查询“TLS配置名称”为“add”配置信息：

   ```
   LST UDMHLBTLSCFG: TLSCFGNAME="add";
   ```

   ```
   %%LST UDMHLBTLSCFG: TLSCFGNAME="add";%%
   RETCODE = 0  操作成功

        TLS配置ID  =  4
      TLS配置名称  =  add
         协议版本  =  TLS1.2
   TLS1.2加密套件  =  TLS_DHE_RSA_WITH_AES_128_GCM_SHA256&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384&TLS_DHE_RSA_WITH_AES_128_CCM&TLS_DHE_RSA_WITH_AES_256_CCM&TLS_ECDHE_ECDSA_WITH_AES_128_CCM&TLS_ECDHE_ECDSA_WITH_AES_256_CCM
   TLS1.3加密套件  =  NULL
      TLS配置描述  =  NULL
         证书校验  =  校验
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD UDMHLBTLSCFG**命令的参数说明。