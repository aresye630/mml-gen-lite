# 查询策略管理服务功能配置(LST PMSFUNC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于查询策略管理服务功能配置信息。

- 若需要查询全部策略管理服务功能的配置信息，请不要输入任何参数。
- 若需要查询特定策略管理服务功能的配置信息，请依据参数说明输入查询的条件。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:-------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE   | 配置类型   | 可选必选说明：可选参数 参数含义：用于标识PMS的配置类型。 取值范围： FtpConfig(FTP-CONFIG)：FTP协议参数配置。WebUI(WEBUI)：WebUI会话锁定自动注销超时时间参数配置。MbeanConfig(MBEAN-CONFIG)：监控信息参数配置。Server(SERVER)：服务器安全认证参数配置。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ITEMN  | 配置项名称  | 可选必选说明：可选参数 参数含义：用于标识PMS配置项的名称。 取值范围： FtpConfig(FTP-CONFIG)mode：FTP协议工作方式。 默认值：无。 WebUI(WEBUI)lockTimeout：会话锁定后被自动注销的超时时长。checkVerifyCode：是否检查PMS登录的验证码。SessionTimeout：会话有效时长。 默认值：无。 MbeanConfig(MBEAN-CONFIG)diskLowValue：标识磁盘空间低位阈值。diskHighValue：标识磁盘空间高位阈值。 默认值：无。 Server(SERVER)sslEnabledProtocols（sslEnabledProtocols）：标识服务器和客户端之间使用的SSL协议版本。 ciphers（ciphers）：标识服务器支持的加密套件列表。cert（cert）：标识PMS所有服务端证书关联的证书对象，仅支持PM接口、UPCF Web UI接入PMS服务。 certForPM（certForPM）：标识PM接口关联的证书对象。 certForSCLI（certForSCLI）：标识SCLI接口关联的证书对象。logFileFormat（logFileFormat）：标识PMS导出的日志格式。xssCheckSwitch（xssCheckSwitch）：标识PMS是否开启可配置输入的规则校验。cliVerifySwitch（cliVerifySwitch）：标识CLI导入时是否开启CLI命令合法性校验。sqlCheckSwitch（sqlCheckSwitch）：标识PMS是否开启SQL注入检查。pmsWebSwitch（pmsWebSwitch）：标识是否关闭PMS WEB、SOAP、REST、4A平台接口功能。certForRest（certForRest）：标识Rest接口关联的证书对象。 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有的策略管理服务功能配置信息。

   ```
   LST PMSFUNC:;
   ```

   ```
   %%LST PMSFUNC:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   配置类型            配置项名称               配置项值                             配置项默认值                         证书应用场景               证书应用默认场景  

   FTP-CONFIG          mode                     PASV                                 PASV                                 NULL                        NULL
   WEBUI               lockTimeout              15                                   15                                   NULL                        NULL
   WEBUI               checkVerifyCode          FALSE                                TRUE                                 NULL                        NULL
   WEBUI               sessionTimeout           480                                  480                                  NULL                        NULL
   MBEAN-CONFIG        diskLowValue             3145728                              3145728                              NULL                        NULL
   MBEAN-CONFIG        diskHighValue            5242880                              5242880                              NULL                        NULL
   SERVER              sslEnabledProtocols      TLSv1.2                              TLSv1.2                              NULL                        NULL
   SERVER              logFileFormat            1                                    1                                    NULL                        NULL
   SERVER              xssCheckSwitch           TRUE                                 TRUE                                 NULL                        NULL
   SERVER              cliVerifySwitch          TRUE                                 TRUE                                 NULL                        NULL
   SERVER              sqlCheckSwitch           1                                    1                                    NULL                        NULL
   SERVER              pmsWebSwitch             1                                    1                                    NULL                        NULL
   SERVER              ciphers                  TLS_DHE_RSA_WITH_AES_256_GCM_SHA384  TLS_DHE_RSA_WITH_AES_256_GCM_SHA384  NULL                        NULL
   SERVER              cert                     NULL                                 NULL                                 UPCF_PMS_Lcert              UPCF_PMS_Lcert
   SERVER              certForPM                NULL                                 NULL                                 NULL                        NULL
   SERVER              certForSCLI              NULL                                 NULL                                 NULL                        NULL 
   SERVER              certForRest              NULL                                 NULL                                 NULL                        NULL 
   (结果个数 = 17)

   ---    END
   ```
2. 查询一个策略管理服务功能的配置信息。“配置类型”为“FtpConfig(FTP-CONFIG)”，“配置项名称”为“mode”。

   ```
   LST PMSFUNC: TYPE=FtpConfig, ITEMN=mode;
   ```

   ```
   %%LST PMSFUNC: TYPE=FtpConfig, ITEMN=mode;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
             配置类型  =  FTP-CONFIG
           配置项名称  =  mode
             配置项值  =  PORT
         配置项默认值  =  PASV
         证书应用场景  =  NULL
     证书应用默认场景  =  NULL
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见参数说明。