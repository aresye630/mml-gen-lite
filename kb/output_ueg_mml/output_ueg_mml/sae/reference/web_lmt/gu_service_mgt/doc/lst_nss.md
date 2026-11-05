# 以格式2查询所有补充业务信息(LST NSS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此命令用于查询用户补充业务信息，以指定的格式返回查询结果。

使用场景限于运营商对返回报文格式有特殊适配需求。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数描述                                                            |
|:-------|:-------|:----------------------------------------------------------------|
| IMSI   | IMSI   | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，为6～15位的十进制数。 说明：可选参数。            |
| ISDN   | MSISDN | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，1～15位的十进制数字。 说明：可选参数。          |
| BSG    | 数据业务码  | 该参数用于设置BSG值。 取值范围： TS11TS21TS22 TS62 TSD1 BS26 BS20 BS30 默认值：无。 |

## 使用实例

查询用户补充业务信息，以指定的数据格式返回。命令如下：

```
LST NSS: IMSI="461380000000000";
```

```
%%LST NSS: IMSI="461380000000000";%%
RETCODE = 0 SUCCESS0001:Operation is successful

                SUPPLEMENTARY SERVICES:
                   
                   
    INTERNATIONAL MOBILE SUBSCRIBER IDENTITY ... 461380000000000
    AOC....ADVICE OF CHARGE .................... N
    HOLD...CALL HOLD ........................... N
    CLIP...CALLING LINE ID PRESENTATION ........ N
    CLIR...CALLING LINE ID RESTRICTION ......... N
    COLP...CONNECTED LINE ID PRESENTATION ...... N
    COLR...CONNECTED LINE ID RESTRICTION ....... N
    CT.....CALL TRANSFER ....................... N
    PNI....PRIVATE NUMBERING INDEX ............. 100
    RDI....REDIRECTION DESTINATION INDEX ....... 32
    MPTY...MULTI PARTY SERVICE ................. N
    CHC....CHARGING CLASS ...................... N
    CA.....CHARGING AREA .......................
    HB.....HOT BILLING ......................... N
    UUS1...USER-TO-USER SIGNALLING SERVICE 1 ... N
    UUS2...USER-TO-USER SIGNALLING SERVICE 2 ... N
    UUS3...USER-TO-USER SIGNALLING SERVICE 3 ... N
    DCFC...DENY SENDING OF CFC TO VPLMN ........ N
    BSMS...BAR SMS SENDING WHEN OUTSIDE HPLMN .. N
    FM.....FOLLOW ME ........................... N
    SRBT...SELECTIVE RINGBACK TONE ............. N
    PSS....PLMN SPECIFIC SUPPLEMENTARY SERVICES
                   
   
                LOCATION SERVICES
           
PRIVACY CLASSES
           
    UNIC...UNIVERSAL CLASS .............................. N
           
    CALL UNRELATED CLASS

        EXTERNAL LCS CLIENTS      RESTRICTION        NOTIFIC. AND VERIFICATION

    GMLC LIST

    PLMN CLASS
                                    
        BLOC...BROADCASTING LOCATION ........................ N
        CHPLM..O&M CLIENT IN HPLMN .......................... N
        CVPLM..O&M CLIENT IN VPLMN .......................... N
        ALOC...ANONYMOUS LOCATION ........................... N
        TARG...TARGET MS .................................... N

MOBILE ORIGINATING LOCATION CLASSES
    BSLC...BASIC SELF LOCATION CLASS .................... N
    ASLC...AUTONOMOUS SELF LOCATION CLASS ............... N
    TTPC...TRANSFER TO 3rd PARTY CLASS .................. N
                                
CRNV..CALL RELATED NOTIFICATION AND PRIVACY VERIFICATION .... N
CUNV..CALL UNRELATED NOTIFICATION AND PRIVACY VERIFICATION .. N

   
MOBILE STATION ISDN NUMBER .......................... 461380000000000
BASIC SERVICE CODE .................................. T11
                                             
                CALL RESTRICTION SERVICES:
NAME                                                 PROV    ACT
BAIC..BARRING OF ALL MTC ............................  N      D
BIRO..BARRING OF MTC WHEN ROAMING IN VPLMN COUNTRY ..  N      D
BAOC..BARRING OF ALL MOC ............................  N      D
BOIC..BARRING OF INTERNATIONAL MOC ..................  N      D
BOIH..BARRING OF INT. MOC EXCEPT TO HPLMN COUNTRY ...  N      D
BORO..BARRING OF MOC WHEN ROAMING IN VPLMN COUNTRY ..  N      D
PSW...PASSWORD ......................................  
                                             
                CALL FORWARDING SERVICES:
NAME                                 PROV ACT NPI C-NUMBER          OPTIONS
CFU...CALL FWD UNCONDITIONAL ......... N   D
CFB...CALL FWD ON SUBSCRIBER BUSY .... N   D
CFNR..CALL FWD ON SUBS. NOT REACHABLE  N   D
CFNA..CALL FWD ON NO REPLY ........... N   D
TIME..NO REPLY CONDITION TIME ........
OCCF..OPERATOR CONTROLLED CALL FWD ... N   D  
      SEPARATE IMSI-DETACHED CASE .... N
      DENY SENDING OF OCCF TO VPLMN .. N
PCF...PRIORITY CALL FORWARDING ....... N
CD....CALL DEFLECTION................. N   D
                                             
               CALL COMPLETION SERVICES:
NAME                                                 PROV    ACT
CW....CALL WAITING ................................... N      D
MOBILE STATION ISDN NUMBER .......................... 461380000000111
BASIC SERVICE CODE .................................. B16
                                             
                CALL RESTRICTION SERVICES:
NAME                                                 PROV    ACT
BAIC..BARRING OF ALL MTC ............................  N      D
BIRO..BARRING OF MTC WHEN ROAMING IN VPLMN COUNTRY ..  N      D
BAOC..BARRING OF ALL MOC ............................  N      D
BOIC..BARRING OF INTERNATIONAL MOC ..................  N      D
BOIH..BARRING OF INT. MOC EXCEPT TO HPLMN COUNTRY ...  N      D
BORO..BARRING OF MOC WHEN ROAMING IN VPLMN COUNTRY ..  N      D
PSW...PASSWORD ......................................  
                                             
                CALL FORWARDING SERVICES:
NAME                                 PROV ACT NPI C-NUMBER          OPTIONS
CFU...CALL FWD UNCONDITIONAL ......... N   D
CFB...CALL FWD ON SUBSCRIBER BUSY .... N   D
CFNR..CALL FWD ON SUBS. NOT REACHABLE  N   D
CFNA..CALL FWD ON NO REPLY ........... N   D
TIME..NO REPLY CONDITION TIME ........
OCCF..OPERATOR CONTROLLED CALL FWD ... N   D  
      SEPARATE IMSI-DETACHED CASE .... N
      DENY SENDING OF OCCF TO VPLMN .. N
PCF...PRIORITY CALL FORWARDING ....... N
CD....CALL DEFLECTION................. N   D
                                             
               CALL COMPLETION SERVICES:
NAME                                                 PROV    ACT
CW....CALL WAITING ................................... N      D

         

       

                      
COMMAND EXECUTED

Total count = 103

There is together 1 report

---    END
```