# 查询非3GPP信任关系(LST NON3GPPTRS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在配置数据库中查询非3GPP信任关系：

- 若需要查询全部非3GPP信任关系的配置信息，请不要输入任何参数。
- 若需要查询某条非3GPP信任关系的配置信息，请输入“标识”参数和其它参数的组合。

**说明** 

该命令仅在Full-stack虚机场景下支持。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:--------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID      | 标识     | 用于指示系统按照哪个标识来查询非3GPP信任关系信息数据。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| RATTYPE | 接入类型   | 用于指定用户终端（UE）的无线接入技术类型。 取值范围：WLAN(WLAN)：表示RAT的类型为WLAN。VIRTUAL(VIRTUAL)：表示RAT的类型为其他未知类型，详见3GPP TS 29.274。UTRAN(UTRAN)：表示RAT的类型为UTRAN，详见3GPP TS 29.060。GERAN(GERAN)：表示RAT的类型为GERAN，详见3GPP TS 29.060。GAN(GAN)：表示RAT的类型为GAN，详见3GPP TS 29.060和3GPP TS 43.318。HSPA_EVOLUTION(HSPA_EVOLUTION)：表示RAT的类型为HSPA Evolution，详见3GPP TS 29.060。EUTRAN(EUTRAN)：表示RAT的类型为EUTRAN，详见3GPP TS 29.274。CDMA2000_1X(CDMA2000_1X)：表示RAT的类型为CDMA2000 1X，详见3GPP2 X.S001。HRPD(HRPD)：表示RAT的类型为HRPD，详见3GPP2 X.S0011。UMB(UMB)：表示RAT的类型为UMB，详见3GPP2 X.S0011。EHRPD(EHRPD)：表示RAT的类型为eHRPD，详见3GPP2 X.S0057。 默认值：无。 |
| HOST    | 对端主机名  | 用于指定配置Non-3GPP信任关系的对端源主机名。 取值范围：长度不超过127的字符串。 默认值：无。 说明：该参数统一存储为小写字母，支持后向最大匹配。例如：配置了主机名es.huawei.com以及sz.es.huawei.com，用户消息携带的对端主机名为bantian.sz.es.huawei.com，则最大匹配符合sz.es.huawei.com。                                                                                                                                                                                                                                                                                                                                                                                          |
| REL     | 信任关系   | 用于指定用户终端（UE）与对端源主机的信任关系。 取值范围：UNTRUSTED(UNTRUSTED)：非可信接入。TRUSTED(TRUSTED)：可信接入。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## 使用实例

1. 查询所有非3GPP信任关系配置信息，执行命令如下：

   ```
   LST NON3GPPTRS:;
   ```

   返回结果如下：

   ```
   %%LST NON3GPPTRS:;%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------
    标识    接入类型        对端主机名     信任关系 

    0       WLAN            NULL           UNTRUSTED
    1       NULL            NULL           UNTRUSTED
    2       VIRTUAL         NULL           TRUSTED  
    3       NULL            1              UNTRUSTED
    4       NULL            fdsae          TRUSTED  
    5       HSPA_EVOLUTION  NULL           UNTRUSTED
    6       WLAN            es.huawei.com  TRUSTED  
   (结果个数 = 7)

   ---    END
   ```
2. 查询可信接入的对端主机名，“信任关系”为“TRUSTED(TRUSTED)”，执行命令如下：

   ```
   LST NON3GPPTRS: REL=TRUSTED;
   ```

   返回结果如下：

   ```
   %%LST NON3GPPTRS: REL=TRUSTED;%%
   RETCODE = 0  操作成功

   查询结果如下
   ------------
    标识    接入类型  对端主机名     信任关系

    2       VIRTUAL   NULL           TRUSTED 
    4       NULL      fdsae          TRUSTED 
    6       WLAN      es.huawei.com  TRUSTED 
   (结果个数 = 3)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。