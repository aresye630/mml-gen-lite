# 显示策略管理服务功能配置(DSP PMSFUNC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于请求系统显示策略管理服务功能配置的状态信息。

- 若需要显示全部策略管理服务功能配置的状态信息，请不要输入任何参数。
- 若需要显示某个策略管理服务功能配置的状态信息，请输入需要显示的参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:-------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE   | 配置类型   | 可选必选说明：可选参数 参数含义：用于标识PMS的配置类型。 取值说明： FtpConfig(FTP-CONFIG)：FTP协议参数配置。WebUI(WEBUI)：WebUI会话锁定自动注销超时时间参数配置。MbeanConfig(MBEAN-CONFIG)：监控信息参数配置。Server(SERVER)：服务器安全认证参数配置。 默认值： 无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ITEMN  | 配置项名称  | 可选必选说明：可选参数 参数含义：用于标识PMS配置项的名称。 取值范围： FtpConfig(FTP-CONFIG)mode：FTP协议工作方式。 默认值：无。 WebUI(WEBUI)lockTimeout：会话锁定后被自动注销的超时时长。checkVerifyCode：是否检查PMS登录的验证码。SessionTimeout：会话有效时长。 默认值：无。 MbeanConfig(MBEAN-CONFIG)diskLowValue：标识磁盘空间低位阈值。diskHighValue：标识磁盘空间高位阈值。 默认值：无。 Server(SERVER)sslEnabledProtocols（sslEnabledProtocols）：标识服务器和客户端之间使用的SSL协议版本。 ciphers（ciphers）：标识服务器支持的加密套件列表。cert（cert）：标识PMS所有服务端证书关联的证书对象，仅支持PM接口、UPCF Web UI接入PMS服务。 certForPM（certForPM）：标识PM接口关联的证书对象。 certForSCLI（certForSCLI）：标识SCLI接口关联的证书对象。logFileFormat（logFileFormat）：标识PMS导出的日志格式。xssCheckSwitch（xssCheckSwitch）：标识PMS是否开启可配置输入的规则校验。cliVerifySwitch（cliVerifySwitch）：标识CLI导入时是否开启CLI命令合法性校验。sqlCheckSwitch（sqlCheckSwitch）：标识PMS是否开启SQL注入检查。pmsWebSwitch（pmsWebSwitch）：标识是否关闭PMS WEB、SOAP、REST、4A平台接口功能。certForRest（certForRest）：标识Rest接口关联的证书对象。 默认值：无。 配置原则：无。 |

## 使用实例

1. 显示所有策略管理服务功能配置的状态信息。

   ```
   DSP PMSFUNC:;
   ```

   ```
   %%DSP PMSFUNC:;%%
   RETCODE = 0    操作成功

   操作结果如下:
   -------------
   配置类型            配置项名称               实例名称         配置项值                             配置实际值                           配置项默认值                         证书应用场景               证书应用默认场景                    配置生效标识  

   SERVER              pmsWebSwitch             pcf-all-pod20-1  1                                    1                                    1                                    NULL                        NULL                                是  
   SERVER              sqlCheckSwitch           pcf-all-pod20-1  1                                    1                                    1                                    NULL                        NULL                                是                           
   SERVER              logFileFormat            pcf-all-pod20-1  1                                    1                                    1                                    NULL                        NULL                                是                           
   FTP-CONFIG          mode                     pcf-all-pod20-1  PASV                                 PASV                                 PASV                                 NULL                        NULL                                是                           
   WEBUI               sessionTimeout           pcf-all-pod20-1  480                                  480                                  480                                  NULL                        NULL                                是                           
   SERVER              sslEnabledProtocols      pcf-all-pod20-1  TLSv1.2                              TLSv1.2                              TLSv1.2                              NULL                        NULL                                是                           
   SERVER              cert                     pcf-all-pod20-1  NULL                                 NULL                                 NULL                                 UPCF_PMS_Lcert              UPCF_PMS_Lcert                      是                           
   SERVER              certForRest              pcf-all-pod20-1  NULL                                 NULL                                 NULL                                 NULL                        NULL                                是                           
   SERVER              ciphers                  pcf-all-pod20-1  TLS_DHE_RSA_WITH_AES_256_GCM_SHA384  TLS_DHE_RSA_WITH_AES_256_GCM_SHA384  TLS_DHE_RSA_WITH_AES_256_GCM_SHA384  NULL                        NULL                                是                           
   WEBUI               lockTimeout              pcf-all-pod20-1  15                                   15                                   15                                   NULL                        NULL                                是                           
   SERVER              cliVerifySwitch          pcf-all-pod20-1  TRUE                                 TRUE                                 TRUE                                 NULL                        NULL                                是                           
   SERVER              certForPM                pcf-all-pod20-1  NULL                                 NULL                                 NULL                                 NULL                        NULL                                是                           
   MBEAN-CONFIG        diskHighValue            pcf-all-pod20-1  5242880                              5242880                              5242880                              NULL                        NULL                                是                           
   WEBUI               checkVerifyCode          pcf-all-pod20-1  FALSE                                FALSE                                TRUE                                 NULL                        NULL                                是                           
   SERVER              certForSCLI              pcf-all-pod20-1  NULL                                 NULL                                 NULL                                 NULL                        NULL                                是                           
   SERVER              xssCheckSwitch           pcf-all-pod20-1  TRUE                                 TRUE                                 TRUE                                 NULL                        NULL                                是                           
   MBEAN-CONFIG        diskLowValue             pcf-all-pod20-1  3145728                              3145728                              3145728                              NULL                        NULL                                是  
   SERVER              pmsWebSwitch             pcf-all-pod20-0  1                                    1                                    1                                    NULL                        NULL                                是                         
   SERVER              sqlCheckSwitch           pcf-all-pod20-0  1                                    1                                    1                                    NULL                        NULL                                是                           
   SERVER              logFileFormat            pcf-all-pod20-0  1                                    1                                    1                                    NULL                        NULL                                是                           
   FTP-CONFIG          mode                     pcf-all-pod20-0  PASV                                 PASV                                 PASV                                 NULL                        NULL                                是                           
   WEBUI               sessionTimeout           pcf-all-pod20-0  480                                  480                                  480                                  NULL                        NULL                                是                           
   SERVER              sslEnabledProtocols      pcf-all-pod20-0  TLSv1.2                              TLSv1.2                              TLSv1.2                              NULL                        NULL                                是                           
   SERVER              cert                     pcf-all-pod20-0  NULL                                 NULL                                 NULL                                 UPCF_PMS_Lcert              UPCF_PMS_Lcert                      是                           
   SERVER              certForRest              pcf-all-pod20-0  NULL                                 NULL                                 NULL                                 NULL                        NULL                                是                           
   SERVER              ciphers                  pcf-all-pod20-0  TLS_DHE_RSA_WITH_AES_256_GCM_SHA384  TLS_DHE_RSA_WITH_AES_256_GCM_SHA384  TLS_DHE_RSA_WITH_AES_256_GCM_SHA384  NULL                        NULL                                是                           
   WEBUI               lockTimeout              pcf-all-pod20-0  15                                   15                                   15                                   NULL                        NULL                                是                           
   SERVER              cliVerifySwitch          pcf-all-pod20-0  TRUE                                 TRUE                                 TRUE                                 NULL                        NULL                                是                           
   SERVER              certForPM                pcf-all-pod20-0  NULL                                 NULL                                 NULL                                 NULL                        NULL                                是                           
   MBEAN-CONFIG        diskHighValue            pcf-all-pod20-0  5242880                              5242880                              5242880                              NULL                        NULL                                是                           
   WEBUI               checkVerifyCode          pcf-all-pod20-0  FALSE                                FALSE                                TRUE                                 NULL                        NULL                                是                           
   SERVER              certForSCLI              pcf-all-pod20-0  NULL                                 NULL                                 NULL                                 NULL                        NULL                                是                           
   SERVER              xssCheckSwitch           pcf-all-pod20-0  TRUE                                 TRUE                                 TRUE                                 NULL                        NULL                                是                           
   MBEAN-CONFIG        diskLowValue             pcf-all-pod20-0  3145728                              3145728                              3145728                              NULL                        NULL                                是 
   (结果个数 = 34)

   ---    END
   ```
2. 显示策略管理服务功能配置的状态信息。“配置类型”为“FtpConfig(FTP-CONFIG)”，“配置项名称”为“mode”。

   ```
   DSP PMSFUNC: TYPE=FtpConfig, ITEMN=mode;
   ```

   ```
   %%DSP PMSFUNC: TYPE=FtpConfig, ITEMN=mode;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
             配置类型  =  FTP-CONFIG
           配置项名称  =  mode
             实例名称  =  pcf-policymanagementa-pod20-6d7cb6dd-t4f98
             配置项值  =  PASV
           配置实际值  =  PASV
         配置项默认值  =  PASV
         证书应用场景  =  NULL
     证书应用默认场景  =  NULL
         配置生效标识  =  是
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义如表1。

| 输出项名称    | 输出项解释                                                                                                                                        |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| 配置类型     | 用于标识PMS的配置类型。具体描述请参见参数说明里的“配置类型”。                                                                                                            |
| 配置项名称    | 用于标识PMS配置项的名称。具体描述请参见参数说明里的“配置项名称”。                                                                                                          |
| 实例名称     | 用于标识配置项的实例名称。 取值范围：长度不超过64的字符串。                                                                                                              |
| 配置项值     | 用于标识配置项的配置值。                                                                                                                                 |
| 配置项实际值   | 用于标识配置项的实际值。                                                                                                                                 |
| 配置项默认值   | 用于标识配置项默认值。                                                                                                                                  |
| 证书应用场景   | 用于标识证书应用场景的实际值。                                                                                                                              |
| 证书应用默认场景 | 用于标识证书应用场景默认值。                                                                                                                               |
| 配置生效标识   | 用于标识该配置是否生效。若配置未生效，需要重启PMS系统： 登录“UPCF MML命令”界面；执行RST MSPROCESS命令重启PMS服务：RST MSPROCESS: PROCOBJECT=PROCNAME, PROCNAME="CELL_PcfPms"; 取值范围： 是否 |