# 查询GPRS模板(LST GPRSTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来查询GPRS模板的数据。

## 注意事项

- 如果“模板ID”和“接入点名称”没有给出，数据库中的所有GPRS模板ID和相关的数据都将显示出来。
- 如果通过“接入点名称”查询GPRS模板，则需要先将命令**SET MAPCONF**中的参数“是否支持LST GPRSTPL使用APN查询”的值设为“TRUE”。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                         |
|:-------|:-------|:---------------------------------------------|
| HLRSN  | HLR序列号 | HLR序列号，有效值域为1～255，在PGW支持容灾功能或虚拟HLR功能时设置。     |
| TPLID  | 模板ID   | 模板号码，可选参数，取值范围为0～65534。                      |
| APN    | 接入点名称  | APN在GPRS骨干网中用来标识要使用的GGSN，1～63个字符组成的字符串，可选参数。 |

## 使用实例

查询2号GPRS模板中的数据。例如：

```
LST GPRSTPL: HLRSN=1, TPLID=2;
```

```
%%LST GPRSTPL: HLRSN=1, TPLID=2;%%
RETCODE = 0 SUCCESS0001:操作成功

                         HLRSN = 1
                         TPLID = 2
                       TPLNAME = gprstpl
                 CHARGE_GLOBAL = NONE
                        CNTXID = 2
                       PDPTYPE = IPV4
                        ADDIND = DYNAMIC
                        RELCLS = ACKALLPRODT
                      DELAYCLS = DELAY2
                        PRECLS = NORMAL
                       PEAKTHR = 8000 OCT
                       MEANTHR = 200 OCT
                    ARPRIORITY = NORMAL
                        ERRSDU = NODETECT
                      DELIVERY = NO
                    TRAFFICCLS = CONVER
                    MAXSDUSIZE = 10 OCT
                      MAXBRUPL = 1K
                      MAXBRDWL = 1K
                        RESBER = 0.05
                        SDUERR = 0.01
                   TRANSFERDEL = 10MS
                    TRAFFICPRI = PRIORITY1
                     MAXGBRUPL = 1K
                     MAXGBRDWL = 1K
                           APN = APN1
                         VPLMN = TRUE
                        CHARGE = PREPAID
                    APNOITPLID = 1

Total count = 28

There is together 1 report

---    END
```