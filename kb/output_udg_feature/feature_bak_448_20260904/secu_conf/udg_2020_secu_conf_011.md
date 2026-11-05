# 配置HTTP/RTSP头增强加密策略及防欺诈策略

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

如果需要使用HTTP/RTSP头增强功能，建议使用如下方式进行安全加固，在Web Server/Streaming Server支持加密信息解析的情况下，将用户的IMSI、MSISDN、SGSN-IP等信息加密后添加到报文头传递给Web Server/Streaming Server。同时为了防止用户使用欺诈的头增强信息进行业务，需要配置HTTP/RTSP头增强防欺诈策略。

**说明** 

适用于SGW-U、PGW-U、UPF。

## 必备事项

前提条件

- 请仔细阅读GWFD-110261 HTTP头增强、GWFD-110262 RTSP头增强和HTTP头防欺诈。
- 操作员已经获取到运营商对使用头增强特性的插入字段规划、字段前缀名称规划以及需要头增强信息的Web Server/Streaming Server的URL等信息。

数据

| 类别               | 参数名称                 | 取值样例                                                                               | 获取方法   | 说明                                 |
|:-----------------|:---------------------|:-----------------------------------------------------------------------------------|:-------|:-----------------------------------|
| HTTP/RTSP头增强动作属性 | 头增强名称（HEADERENNAME）  | header_test                                                                        | 本端规划   | ADD HEADEN                         |
| HTTP/RTSP头增强动作属性 | 数据类型（DATATYPE）       | IMSI1MSISDN1SGSNIP1IMEI1SUBPROFILE1CHGCHAR1RAT1ULI1                                | 本端规划   | ADD HEADEN                         |
| HTTP/RTSP头增强动作属性 | 前缀名称（PREFIXNAME）     | X-imsiX-msisdnX-sgsn-ipX-imeiX-subscriber-profileX-charge-characteristicX-ratX-uli | 本端规划   | ADD HEADEN                         |
| HTTP/RTSP头防欺诈    | 加密算法标识（ENCRYALGORI）  | AES256                                                                             | 与对端协商  | 推荐使用AES256加密算法。                    |
| HTTP/RTSP头防欺诈    | 密码（PSWDKEY）          | XXXXXX                                                                             | 本端规划   | 对头增强信息进行加密，配置对应的密钥，且密钥建议使用密文显示。    |
| HTTP/RTSP头防欺诈    | 确认密码（PSWDKEYCONFIRM） | XXXXXX                                                                             | 本端规划   | 对头增强信息进行加密，配置对应的密钥，且密钥建议使用密文显示。    |
| HTTP/RTSP头防欺诈    | 防欺诈标识（ANTIFRAUD）     | ENABLE                                                                             | 本端规划   | 为了防止用户使用欺诈的头增强信息进行业务，建议开启头增强防欺诈功能。 |

## 操作步骤

1. 配置HTTP/RTSP头增强动作及头防欺诈动作。

   头增强的具体配置请参见激活HTTP头增强、激活RTSP头增强；头防欺诈的具体配置请参见激活HTTP头防欺诈。

   **说明** 

   当要在报文头中插入用户的IMSI、MSISDN、SGSN IP等信息时，建议配置为AES256加密方式，配置对应的密钥，且密钥使用密文显示。为了防止用户使用欺诈的头增强信息进行业务，同时开启头防欺诈功能。

   **ADD HEADEN**:HEADERENNAME=头增强名称,DATATYPE=IMSI1,PREFIXNAME=前缀名称,ENCRYALGORI=AES256,PSWDKEY=密码,PSWDKEYCONFIRM=确认密码,ANTIFRAUD=ENABLE;

   **ADD HEADEN**:HEADERENNAME=头增强名称,DATATYPE=MSISDN1,PREFIXNAME=前缀名称,ENCRYALGORI=AES256,PSWDKEY=密码,PSWDKEYCONFIRM=确认密码,ANTIFRAUD=ENABLE;

   **ADD HEADEN**:HEADERENNAME=头增强名称,DATATYPE=SGSNIP1,PREFIXNAME=前缀名称,ENCRYALGORI=AES256,PSWDKEY=密码,PSWDKEYCONFIRM=确认密码,ANTIFRAUD=ENABLE;

   **ADD HEADEN**:HEADERENNAME=头增强名称,DATATYPE=IMEI1,PREFIXNAME=前缀名称,ENCRYALGORI=AES256,PSWDKEY=密码,PSWDKEYCONFIRM=确认密码,ANTIFRAUD=ENABLE;

   **ADD HEADEN**:HEADERENNAME=头增强名称,DATATYPE=SUBPROFILE1,PREFIXNAME=前缀名称,ENCRYALGORI=AES256,PSWDKEY=密码,PSWDKEYCONFIRM=确认密码,ANTIFRAUD=ENABLE;

   **ADD HEADEN**:HEADERENNAME=头增强名称,DATATYPE=CHGCHAR1,PREFIXNAME=前缀名称,ENCRYALGORI=AES256,PSWDKEY=密码,PSWDKEYCONFIRM=确认密码,ANTIFRAUD=ENABLE;

   **ADD HEADEN**:HEADERENNAME=头增强名称,DATATYPE=RAT1,PREFIXNAME=前缀名称,ENCRYALGORI=AES256,PSWDKEY=密码,PSWDKEYCONFIRM=确认密码,ANTIFRAUD=ENABLE;

   **ADD HEADEN**:HEADERENNAME=头增强名称,DATATYPE=ULI1,PREFIXNAME=前缀名称,ENCRYALGORI=AES256,PSWDKEY=密码,PSWDKEYCONFIRM=确认密码,ANTIFRAUD=ENABLE;

## 任务示例

任务描述

UDG将用户发起的上下行报文进行头增强，将用户的IMSI、MSISDN、SGSN IP等字段加密后加入用户报文。

脚本

配置HTTP/RTSP头增强动作属性，使能防欺诈标识。

```
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=IMSI1,PREFIXNAME="X-imsi",ENCRYALGORI=AES256,PSWDKEY="******",PSWDKEYCONFIRM="******",ANTIFRAUD=ENABLE;
```

```
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=MSISDN1,PREFIXNAME="X-msisdn",ENCRYALGORI=AES256,PSWDKEY="******",PSWDKEYCONFIRM="******",ANTIFRAUD=ENABLE;
```

```
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=SGSNIP1,PREFIXNAME="X-sgsn-ip",ENCRYALGORI=AES256,PSWDKEY="******",PSWDKEYCONFIRM="******",ANTIFRAUD=ENABLE;
```

```
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=IMEI1,PREFIXNAME="X-imei",ENCRYALGORI=AES256,PSWDKEY="******",PSWDKEYCONFIRM="******",ANTIFRAUD=ENABLE;
```

```
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=SUBPROFILE1,PREFIXNAME="X-subscriber-profile",ENCRYALGORI=AES256,PSWDKEY="*******",PSWDKEYCONFIRM="*****",ANTIFRAUD=ENABLE;
```

```
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=CHGCHAR1,PREFIXNAME="X-charge-characteristic",ENCRYALGORI=AES256,PSWDKEY="*******",PSWDKEYCONFIRM="*****",ANTIFRAUD=ENABLE;
```

```
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=RAT1,PREFIXNAME="X-rat",ENCRYALGORI=AES256,PSWDKEY="******",PSWDKEYCONFIRM="******",ANTIFRAUD=ENABLE;
```

```
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=ULI1,PREFIXNAME="X-uli",ENCRYALGORI=AES256,PSWDKEY="******",PSWDKEYCONFIRM="******",ANTIFRAUD=ENABLE;
```