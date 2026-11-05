# 查询与AUC接口格式(LST AUCFORMAT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询UDM与外置AUC之间的鉴权接口格式数据。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                        |
|:-------|:-------|:------------------------------------------------------------|
| DOMAIN | 域      | 可选必选说明：必选参数 参数含义：用于标识查询哪个域配置的数据。 取值范围： 4GIMS 默认值：无。 配置原则：无。 |

## 使用实例

1. 参数“域”取值为“4G”时，预置的初始数据查询结果如下。本命令查询结果以预置数据为例，不再重复举例。

   ```
   %%LST AUCFORMAT: DOMAIN=4G;%%
   RETCODE = 0 SUCCESS0001:操作成功

                          SUPPAUC = TRUE
                              URI = /nauc-avg/v1/security-information/generate-av
                               AV = authenticationVectors
                             RAND = rand
                             AUTN = autn
                             XRES = xres
                               CK = ck
                               IK = ik
                      REQFORGETAV = {"imsi":"${imsi}","numOfRequestedVectors":${numOfRequestedVectors},"requestingNodeType":"MME"}
                        REQFORSYN = {"imsi":"${imsi}","numOfRequestedVectors":${numOfRequestedVectors},"requestingNodeType":"MME","resynchronizationInfo":{"rand":"${rand}","auts":"${auts}"}}

   Total count = 10

   There is together 1 report

   ---    END
   ```
2. 参数“域”取值为“IMS”时，预置的初始数据查询结果如下：

   ```
   %%LST AUCFORMAT: DOMAIN=IMS;%%
   RETCODE = 0 SUCCESS0001:操作成功

                          SUPPAUC = TRUE
                              URI = /nauc-avg/v1/security-information/generate-av
                               AV = authenticationVectors
                             RAND = rand
                             AUTN = autn
                             XRES = xres
                               CK = ck
                               IK = ik
                      REQFORGETAV = {"imsi":"${imsi}","numOfRequestedVectors":${numOfRequestedVectors},"requestingNodeType":"S_CSCF"}
                        REQFORSYN = {"imsi":"${imsi}","numOfRequestedVectors":${numOfRequestedVectors},"requestingNodeType":"S_CSCF","resynchronizationInfo":{"rand":"${rand}","auts":"${auts}"}}

   Total count = 10

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET AUCFORMAT**命令的参数说明。