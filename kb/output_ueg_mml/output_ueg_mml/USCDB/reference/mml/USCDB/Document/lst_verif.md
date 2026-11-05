# 查询证书文件(LST VERIF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询已加载的安全证书文件：

- 若需要查询已加载的全部安全证书文件的信息，请不要输入任何参数。
- 若需要查询某个已加载的安全证书文件的信息，请输入“证书ID”。

## 注意事项

当**SET NEWCERTSWITCH**的参数“证书开关”取值为“OFF（关闭）”时，使用该命令进行查询。**SET NEWCERTSWITCH**的参数“证书开关”取值可通过在“CSP MML命令”界面执行**LST NEWCERTSWITCH**命令查询。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                         |
|:--------|:-------|:---------------------------------------------|
| VERIFID | 证书ID   | 用于指定要查询的已加载的安全证书的ID编号；若不输入，则表示所有的已加载证书的证书ID。 |

## 使用实例

1. 查询证书文件：

   ```
   LST VERIF:;
   ```

   ```
   查询结果如下
   ------------
    证书ID  用途类型  证书类型    证书文件包名称         证书文件名  	    连接类型   业务类型  证书密码

    0       服务端    CA证书      USCDB_WEBLMT.zip       USCDB_WEBLMT_CA       WEBLMT     USCDB     *****   
    1       服务端    设备证书    USCDB_WEBLMT.zip       USCDB_WEBLMT_SERVER   WEBLMT     USCDB     *****   
    2       服务端    密钥文件    USCDB_WEBLMT.zip       USCDB_WEBLMT_KEY      WEBLMT     USCDB     *****   
    3       服务端    CA证书      SUP-FE_SOAP.zip        SUP-FE_SOAP_CA        SOAP       SUP-FE    *****   
    4       服务端    设备证书    SUP-FE_SOAP.zip        SUP-FE_SOAP_SERVER    SOAP       SUP-FE    *****   
    5       服务端    密钥文件    SUP-FE_SOAP.zip        SUP-FE_SOAP_KEY       SOAP       SUP-FE    *****  
    6       服务端    CA证书      SUP-FE_REST.zip        SUP-FE_REST_CA        REST       SUP-FE    *****   
    7       服务端    设备证书    SUP-FE_REST.zip        SUP-FE_REST_SERVER    REST       SUP-FE    *****   
    8       服务端    密钥文件    SUP-FE_REST.zip        SUP-FE_REST_KEY       REST       SUP-FE    ***** 
   (结果个数 = 9)

   ---    END
   ```
2. 查询证书文件，“证书ID”为“4”：

   ```
   LST VERIF: VERIFID=4;
   ```

   ```
   %%LST VERIF: VERIFID=4;%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------

             证书ID  =  4
           用途类型  =  服务端
           证书类型  =  设备证书
     证书文件包名称  =  SUP-FE_SOAP.zip
         证书文件名  =  SUP-FE_SOAP_SERVER
           连接类型  =  SOAP
           业务类型  =  SUP-FE
           证书密码  =  *****
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令操作成功的提示信息和相关参数，各参数含义请参见**LOD VERIF**命令的参数说明。