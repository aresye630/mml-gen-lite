# 查询证书信息(DSP VERIF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询已加载的安全证书信息。

## 注意事项

- 该命令不支持查询“证书类型”为“KEYFILE(密钥文件)”的证书信息。“证书ID”对应的“证书类型”可通过执行**LST VERIF**命令查询。
- 当**SET NEWCERTSWITCH**的参数“证书开关”取值为“OFF（关闭）”时，使用该命令进行查询。**SET NEWCERTSWITCH**的参数“证书开关”取值可通过在“CSP MML命令”界面执行**LST NEWCERTSWITCH**命令查询。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                            |
|:--------|:-------|:----------------------------------------------------------------|
| VERIFID | 证书ID   | 可选必选说明：必选参数。 参数含义：用于指定要查询的已加载的安全证书ID。 取值范围：0～1023。 默认值：无 配置原则：无 |

## 使用实例

1. 查询证书信息，“证书ID”为“1”。

   ```
   DSP VERIF: VERIFID=1;
   ```

   ```
   %%DSP VERIF: VERIFID=1;%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------
    Segregated state  =  Certificate:
       Data:
           Version: 3 (0x2)
           Serial Number: 4616777827669835646 (0x401216f93928ff7e)
           Signature Algorithm: sha256WithRSAEncryption
           Issuer: C = cn, ST = Guangdong, L = ShenZhen, O = Huawei, OU = Wireless, CN = huawei.RootCA, emailAddress = huawei.RootCA@huawei.com
           Validity
               Not Before: Jan 10 07:27:00 2022 GMT
               Not After : Jan 10 07:27:00 2032 GMT
           Subject: C = cn, ST = Guangdong, L = ShenZhen, O = Huawei, OU = Wireless, CN = huawei.RootCA, emailAddress = huawei.RootCA@huawei.com

   (结果个数 = 1)

   ---    END
   ```
2. 查询证书吊销列表文件的信息，“证书ID”为“71”。

   ```
   DSP VERIF: VERIFID=71;
   ```

   ```
   %%DSP VERIF: VERIFID=71;%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------
   Segregated state  =  Certificate Revocation List (CRL):
           Version 2 (0x1)
           Signature Algorithm: sha1WithRSAEncryption
           Issuer: C = CN, O = "Huawei Technologies Co., Ltd.", OU = VPP OpenSSL, CN = localhost2, emailAddress = support@huawei.com
           Last Update: Dec  8 09:03:09 2020 GMT
           Next Update: Jan 16 09:03:09 2025 GMT
           CRL extensions:
               X509v3 CRL Number: 
                   4096

   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令操作成功的提示信息和相关参数，证书信息中常见的字段含义如表1所示。

| 常见字段名称              | 字段解释                   |
|:--------------------|:-----------------------|
| Version             | 用于返回证书的版本号。            |
| Serial Number       | 用于返回证书的序列号。            |
| Signature Algorithm | 用于返回证书的签名算法。           |
| Issuer              | 用于返回证书的颁发者信息。          |
| Validity            | 用于返回证书的有效期。            |
| Subject             | 用于返回证书的使用者信息。          |
| Last Update         | 用于返回证书吊销列表文件最近一次更新的时间。 |
| Next Update         | 用于返回证书吊销列表文件下次需要更新的时间。 |
| CRL extensions      | 用于返回证书吊销列表文件的扩展信息。     |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|    错误码 | 错误码解释        | 原因分析                                        | 处理建议                                                              |
|-------:|:-------------|:--------------------------------------------|:------------------------------------------------------------------|
| 337019 | 指定的证书ID不存在。  | 指定的“证书ID”未在系统中配置。                           | 通过LST VERIF命令查询已加载的“证书ID”并正确填写，然后重新执行本命令。                         |
| 337209 | 不支持查询私钥文件内容。 | 指定的“证书ID”对应的“证书类型”为“密钥文件”，私钥文件涉及敏感信息，不支持查询。 | 通过LST VERIF命令查询“证书ID”对应的“证书类型”，请输入“证书类型”不为“密钥文件”的“证书ID”后，重新执行本命令。 |
| 360015 | 证书文件错误。      | 指定的“证书ID”对应的证书文件错误。                         | 先执行CLR VERIF命令清除对应的证书文件，再执行LOD VERIF命令重新加载证书后，重新执行本命令。            |