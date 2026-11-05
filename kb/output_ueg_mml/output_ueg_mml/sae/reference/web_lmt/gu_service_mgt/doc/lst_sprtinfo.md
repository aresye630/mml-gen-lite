# 查询云分区路由数据(LST SPRTINFO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为查询类命令，用于在ATCA平滑演进至CloudDB时查询UDM中配置的云分区路由数据。

- 若需要查询全部的云分区路由数据，请不要输入任何参数。
- 若需要查询某个云分区路由数据，请输入“记录索引”或者“分区ID”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                          |
|:-------|:-------|:------------------------------|
| INDEX  | 记录索引   | 用于指示系统需要按照哪个记录索引来查询云分区路由数据记录。 |
| PID    | 分区ID   | 用于指示系统需要按照哪个分区ID来查询云分区路由数据记录。 |

## 使用实例

- 查询“记录索引”取值为“2”的云分区路由数据。

  ```
  LST SPRTINFO: INDEX=2;
  ```

  ```
  %%LST SPRTINFO: INDEX=2;%%
  RETCODE = 0 SUCCESS0001:Operation is successful 
           
             INDEX = 2
               PID = 20
           HSSNAME = HSS9860
               PRI = 1
             HLRNO = 8613503000
        SAEHSSHOST = SAE-HSS-Host-1
       SAEHSSREALM = hss.huawei.com
        IMSHSSHOST = IMS-HSS-Host-1 
       IMSHSSREALM = s1.huawei.com
        RECORDTYPE = CANCEL
            UDMURI = NULL

  Total count = 11

  There is together 1 report

  ---    END
  ```
- 查询所有的云分区路由数据。

  ```
  LST SPRTINFO:;
  ```

  ```
  %%LST SPRTINFO:;%%
  RETCODE = 0 SUCCESS0001:Operation is successful 
  INDEX    PID   HSSNAME    PRI    HLRNO          SAEHSSHOST          SAEHSSREALM       IMSHSSHOST        IMSHSSREALM     RECORDTYPE      UDMURI
  2        20    HSS9860    1      8613503000     SAE-HSS-Host-1      hss.huawei.com    IMS-HSS-Host-1    s1.huawei.com   NULL            NULL
  13       13    HSS9860    1      8613901000     hss.huawei.com      huawei.com        ims.huawei.com    huawei.com      HYBRID_NETWORK  NULL

  Total count = 2

  There is together 1 report

  ---    END
  ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                         | 处理建议                                     |
|:--------|:--------|:-----------------------------|:-----------------------------------------|
| ERR1004 | 无效的参数值  | 输入的参数值不在其取值范围内或者输入的参数值不符合要求。 | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。         |
| ERR1010 | 参数冲突    | 同时输入了“记录索引”和“分区ID”。          | 不输入任何参数或者仅输入“记录索引”和“分区ID”的其中之一查询云分区路由数据。 |