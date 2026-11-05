# 查询组件版本号(DSP COMVER)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于请求系统显示指定模块所有组件的版本信息。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                           |
|:-------|:-------|:-------------------------------------------------------------------------------|
| MID    | 模块号    | 用于请求系统显示哪个模块内所有组件的版本信息。模块号是通过ADD MODULE定义，通过LST MODULE可以查询。 取值范围：1～1023 默认值：无。 |

## 使用实例

- 显示组件版本信息，“模块号”为“55”：

  ```
  DSP COMVER: MID=55;
  ```

  ```
  %%DSP COMVER: MID=55;%%
  RETCODE = 0  操作成功

  查询结果如下
  ------------
   模块号  组件类型            组件版本号                                                                       

   55     USC_COMMON_LIB组件  USCDBV100R002C03B010                                                             
   55     USC_DSG_LIB组件     USCDBV100R002C05                                                                        
   55     VPP_LDAP_LIB组件    VPP V300R003C28SPC247B010 (LDAP)                                                     
   (结果个数 = 3)

  ---    END
  ```
- 查询所有的组件版本信息。

  ```
  DSP COMVER:;
  ```

  ```
  %%DSP COMVER:;%%
  RETCODE = 0  操作成功
                                                                      
  查询结果如下
  ------------
   模块号  组件类型            组件版本号                                                              

   54      USC_COMMON_LIB组件  USCDBV100R002C03B010                                                    
   54      VPP_LDAP_LIB组件    VPP V300R003C28SPC247B010 (LDAP)                                        
   54      USC_DSG_LIB组件     USCDBV100R002C05                                                        
   55      VPP_LDAP_LIB组件    VPP V300R003C28SPC247B010 (LDAP)                                        
   55      USC_COMMON_LIB组件  USCDBV100R002C03B010                                                    
   55      USC_DSG_LIB组件     USCDBV100R002C05                                                        
   56      USC_COMMON_LIB组件  USCDBV100R002C03B010                                                    
   56      USC_DSG_LIB组件     USCDBV100R002C05                                                        
   56      VPP_LDAP_LIB组件    VPP V300R003C28SPC247B010 (LDAP)                                        
   201     VPP_DNS_LIB组件     VPP V300R003C21SPC338 (VMS-DNS)            Date:Aug 20 2019 Time:15:10:3
   202     VPP_DNS_LIB组件     VPP V300R003C21SPC338 (VMS-DNS)            Date:Aug 20 2019 Time:15:10:3
   203     VPP_DNS_LIB组件     VPP V300R003C21SPC338 (VMS-DNS)            Date:Aug 20 2019 Time:15:10:3
   204     VPP_DNS_LIB组件     VPP V300R003C21SPC338 (VMS-DNS)            Date:Aug 20 2019 Time:15:10:3
   205     VPP_DNS_LIB组件     VPP V300R003C21SPC338 (VMS-DNS)            Date:Aug 20 2019 Time:15:10:3
   206     VPP_DNS_LIB组件     VPP V300R003C21SPC338 (VMS-DNS)            Date:Aug 20 2019 Time:15:10:3

  (结果个数 = 15)

  ---    END
  ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见本命令的参数说明，表1列出的是未包含在本命令参数说明中的输出项。

| 输出项名称   | 输出项解释             |
|:--------|:------------------|
| 组件类型    | 用于返回本模块所有组件的类型信息。 |
| 组件版本号   | 用于返回本模块所有组件的版本信息。 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|    错误码 | 错误码解释                           | 原因分析                             | 处理建议                                                         |
|-------:|:--------------------------------|:---------------------------------|:-------------------------------------------------------------|
| 335156 | 模块类型不是CCU, BSG, HSF, SPU 或 DSG。 | 执行模块号时“模块号”参数对应的模块是DPU、NSF或者PAU。 | 执行LST MODULE查询模块号对应的ID，重新输入CCU，BSG，HSF，SPU或DSG模块的模块号，再执行该命令。 |