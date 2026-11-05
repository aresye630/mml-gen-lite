# 查询网元路由模式（LST NFROUTEMODEL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询UDM和NRF之间SCP对接的网元路由模式。

- 若需要查询所有网元路由模式，不输入任何参数。
- 若需要查询某个详细网元路由模式，请输入“路由名称”参数。
- 若需要查询某个网元类型下的网元路由模式，请输入“网元类型”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                 |
|:-------|:-------|:-----------------------------------------------------------------------------------------------------|
| RTNAME | 路由名称   | 可选必选说明：可选参数 参数含义：用于指示系统按照“路由名称”来查询网元路由模式。若不输入，则表示所有的网元路由名称。 取值范围：长度为1~128的字符串。 默认值：无 配置原则：无。         |
| NFTYPE | 网元类型   | 可选必选说明：必选参数 参数含义：用于标识网元实例的类型。 取值范围： AMF(AMF)SMF(SMF)SMSF(SMSF)NEF(NEF)DEFAULT(DEFAULT) 默认值：无 配置原则：无。 |

## 使用实例

1. 查询所有网元路由模式。

   ```
   %%LST NFROUTEMODEL:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   路由名称          网元类型  目标类型    网元实例                                    发现模式    开关    PLMN ID    域名    IP地址    IP地址段起始地址    IP地址段结束地址    域名后缀    
    
   Default_AMF_PLMN  AMF       PLMN        NULL                                        模式B       非使能  Default    NULL    NULL       NULL               NULL                NULL         
   Default_Global    DEFAULT   NULL        NULL                                        模式B       使能    NULL       NULL    NULL       NULL               NULL                NULL         
   Default_SMF_PLMN  SMF       PLMN        NULL                                        模式B       非使能  Default    NULL    NULL       NULL               NULL                NULL         
   4604567890003     AMF       NFINSTANCE  4947a69a-f61b-4bc1-b9da-47c9c5d14b64        模式D       非使能  NULL       NULL    NULL       NULL               NULL                NULL         
   4604567890007     AMF       IPRANGE     NULL                                        模式B       使能    NULL       NULL    NULL       192.168.100.0      192.168.100.100     NULL         
     
   (结果个数 = 5)

   ---    END
   ```
2. 查询网元路由模式，“路由名称”为“4604567890003”，“网元类型”为“AMF(AMF)”

   ```
   LST NFROUTEMODEL: RTNAME="4604567890003", NFTYPE=AMF
   ```

   ```
   %%LST NFROUTEMODEL: RTNAME="4604567890003", NFTYPE=AMF;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
           路由名称  =  4604567890003
           网元类型  =  AMF
           目标类型  =  NFINSTANCE
           网元实例  =  4947a69a-f61b-4bc1-b9da-47c9c5d14b64
           发现模式  =  模式D
               开关  =  非使能
            PLMN ID  =  NULL
               域名  =  NULL
             IP地址  =  NULL
   IP地址段起始地址  =  NULL
   IP地址段结束地址  =  NULL
           域名后缀  =  NULL

   (结果个数 = 1)

   ---    END
   ```
3. 查询网元路由模式，“路由名称”为“4604567890007”：

   ```
   LST NFROUTEMODEL: RTNAME="4604567890007"
   ```

   ```
   %%LST NFROUTEMODEL: RTNAME="4604567890007";%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
           路由名称  =  4604567890007
           网元类型  =  AMF
           目标类型  =  IPRANGE
           网元实例  =  NULL
           发现模式  =  模式B
               开关  =  非使能
            PLMN ID  =  NULL
               域名  =  NULL
             IP地址  =  NULL
   IP地址段起始地址  =  192.168.100.0
   IP地址段结束地址  =  192.168.100.100
           域名后缀  =  NULL

   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD NFROUTEMODEL**命令的参数说明。