# 查询Token分配信息（DSP UDMHLBTOKENINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询Token分配信息。

- 若需要查询按照类型（服务端Token或客户端Token）查询Token分配信息，请只输入“Token类型”参数进行查询。
- 若需要查询服务端Token或客户端Token中某个微服务实例对应的Token分配信息，请同时输入“Token类型”和“微服务实例ID”参数进行查询。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称    | 参数说明                                                                                                                                               |
|:----------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| TOKENTYPE | Token类型 | 可选必选说明：必选参数 参数含义：用于标识根据哪种配型查询Token分配信息。 取值范围： Client_token(客户端Token)Server_token(服务端Token) 默认值：无。 配置原则：无。                                          |
| INSTID    | 微服务实例ID | 可选必选说明：可选参数 参数含义：用于标识根据哪个微服务实例ID查询Token分配信息。 取值范围：由长度不超过128位的字符串组成。 默认值：无。 配置原则：登录“UDM MML命令”界面，执行DSP UDMSERVICE命令查询各服务信息，报文显示结果“SF实例号”为“微服务实例ID”。 |

## 使用实例

1. 查询客户端Token的分配信息。

   ```
   DSP UDMHLBTOKENINFO: TOKENTYPE=Client_token;
   ```

   ```
   %%DSP UDMHLBTOKENINFO: TOKENTYPE=Client_token;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   微服务实例ID  =  12059636305006266638 
        Pod名称  =  udmall-pod418-676c577889-xzlhl
        Token值  =  32000
   (结果个数 = 1)
   ---    END
   ```
2. 查询“Token类型”为“Client\_token”，“微服务实例ID”为“12059636305006266638”的Token分配信息。

   ```
   DSP UDMHLBTOKENINFO: TOKENTYPE=Client_token, INSTID="12059636305006266638";
   ```

   ```
   %%DSP UDMHLBTOKENINFO: TOKENTYPE=Client_token, INSTID="12059636305006266638";%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   微服务实例ID  =  12059636305006266638 
        Pod名称  =  udmall-pod418-676c577889-xzlhl
        Token值  =  32000
   (结果个数 = 1)
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参考本命令参数说明，表1列出的是未包含在参数说明中的输出项。

| 输出项名称   | 输出项解释        |
|:--------|:-------------|
| Pod名称   | Pod的名称。      |
| Token值  | 分配到的Token的值。 |