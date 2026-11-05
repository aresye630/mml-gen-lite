# 以格式1查询用户数据(LST ESUB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询用户数据，以指定的格式返回查询结果。

使用场景限于运营商对返回报文有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称        | 参数描述                                                                                                                                                                                                            |
|:------------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI        | 用于标识IMSI号码。 取值范围：E.212格式的编码，6～15位的十进制数字。 默认值：无。                                                                                                                                                                 |
| ISDN        | MSISDN      | 用于标识MSISDN号码。 取值范围：E.164格式的编码，1～15位的十进制数字。 默认值：无。                                                                                                                                                               |
| RECORDCOUNT | 用户个数        | 用于标识查询静态数据的用户数目。 当需要查询连续号码的多个用户的静态数据时配置。配置后，系统将会从已指定的IMSI号码或MSISDN号码开始，查询连续号码的多个用户的静态数据。 取值范围：1～10000 默认值：无。 说明：该参数是对连续号码的多个用户进行静态数据查询，当只有一个用户时，该参数不必配置。当一次查询的用户个数很多时，对系统性能无影响，但查询的用户个数越多，消耗的时间越长，一般从几分钟到几小时不等。 |
| IMSIFILE    | IMSI文件名     | 用于标识IMSI批操作文件。 IMSI批操作文件包含多个不连续的待查询静态数据的用户的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstesub.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见IMSIFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                                   |
| ISDNFILE    | MSISDN文件名   | 用于标识MSISDN批操作文件。 MSISDN批操作文件包含多个不连续的待查询静态数据的用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstesub.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见ISDNFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                             |
| PART_IND    | 显示部分用户数据指示位 | 用于指示系统按照哪种方式查询用户数据。 取值范围： SUBID_INFO：仅显示用户的标识信息。ALL：显示所有用户数据。 默认值：ALL。                                                                                                                                          |

## 使用实例

1. 仅查询用户的状态信息及鉴权数据可用性信息，以特定的数据格式返回。命令如下：

   ```
   LST ESUB: IMSI="460000009123456", PART_IND=SUBID_INFO;
   ```

   ```
   %%LST ESUB: IMSI="460000009123456", PART_IND=SUBID_INFO;%%
   RETCODE = 0 SUCCESS0001:操作成功

   HLR SUBSCRIPTION DATA

   MSISDN           IMSI             STATE          AUTHD
   8613900001234    460000009123456  CONNECTED      AVAILABLE 

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询用户所有数据信息，以特定的数据格式返回。命令如下：

   ```
   LST ESUB: IMSI="46000000012";
   ```

   ```
   %%LST ESUB: IMSI="46000000012";%%
   RETCODE = 0 SUCCESS0001:操作成功

   HLR SUBSCRIBER DATA

   SUBSCRIBER IDENTITY
   MSISDN           IMSI             STATE            AUTHD
   86152000102      46000000012      CONNECTED        AVAILABLE 

   NAM
   0

   PERMANENT SUBSCRIBER DATA
   SUD
   CAT-10	CFB-1	CFNRC-1	CFNRY-1	
   CFU-1	DBSG-1	NAM-0	OFA-0	
   PWD-0000	RSA-0	SCHAR-0-0	SOCFB-1	
   SOCFRC-1	SOCFRY-1	SOCFU-1	TS11-1	
   TS21-1	TS22-1	TS61-1	TS62-1	
   BS21-1	BS22-1	BS23-1	BS24-1	
   BS25-1	BS2F-5	BS26-1	BS2G-1	
   BS31-1	BS32-1	BS33-1	BS34-1	
   BS3G-1	

   AMSISDN             BS       BC
   NONE

   SUPPLEMENTARY SERVICE DATA
   BSG
   TS10
   SS       STATUS        FNUM                 TIME
   CFU      NOT ACTIVE    8613888168860        
   CFB      NOT ACTIVE    8613888168860        
   CFNRY    NOT ACTIVE    8613888168860        10
   CFNRC    NOT ACTIVE    8613888168860        

   BSG
   TS60
   SS       STATUS        FNUM                 TIME
   CFU      NOT ACTIVE    8613888168860        
   CFB      NOT ACTIVE    8613888168860        
   CFNRY    NOT ACTIVE    8613888168860        10
   CFNRC    NOT ACTIVE    8613888168860        

   BSG
   BS20
   SS       STATUS        FNUM                 TIME
   CFU      NOT ACTIVE    8613888168860        
   CFB      NOT ACTIVE    8613888168860        
   CFNRY    NOT ACTIVE    8613888168860        10
   CFNRC    NOT ACTIVE    8613888168860        

   BSG
   BS30
   SS       STATUS        FNUM                 TIME
   CFU      NOT ACTIVE    8613888168860        
   CFB      NOT ACTIVE    8613888168860        
   CFNRY    NOT ACTIVE    8613888168860        10
   CFNRC    NOT ACTIVE    8613888168860        

   LOCATION DATA
   VLR ADDRESS      MSRN             MSC NUMBER       LMSID
   UNKNOWN                                            

   SGSN NUMBER
   UNKNOWN

   PACKET DATA PROTOCOL CONTEXT DATA
   NONE

   Total count = 27

   There is together 1 report

   ---    END
   ```
3. 查询第一个“MSISDN”号码为“13310911001”的连续3个用户的数据。命令如下：

   ```
   LST ESUB: ISDN="13310911001", RECORDCOUNT=3;
   ```

   ```
   %%LST ESUB: ISDN="13310911001", RECORDCOUNT=3;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：11. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```
4. 查询“MSISDN文件名”为“lstesub.txt”的用户数据。命令如下：

   ```
   LST ESUB: ISDNFILE="lstesub.txt";
   ```

   ```
   %%LST ESUB: ISDNFILE="lstesub.txt";%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：268435468. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```