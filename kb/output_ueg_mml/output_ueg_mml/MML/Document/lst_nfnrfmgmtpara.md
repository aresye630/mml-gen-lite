# 查询NF与NRF间的全局管理参数（LST NFNRFMGMTPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF、NEF、NWDAF、SCF、CBCF**

该命令用于查询NF与NRF间的全局管理参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

无

## 使用实例

查询NF与NRF间的全局管理参数。

```
%%LST NFNRFMGMTPARA:;%%
RETCODE = 0 操作成功

结果如下
--------
                  切换主用NRF开关  =  OFF
  订阅通知后触发缓存同步时延 (秒)  =  120
         NFService注册MAP格式开关  =  OFF
     NFService服务发现MAP格式开关  =  OFF
                   NF参数检查开关  =  AMF_TAI&SMF_SNSSAI&SMSF_GROUPID&SMSF_SUPI_OR_GPSI
            AMF向NRF注册的TAI策略  =  取本地配置和无线上报的TAI并集
       注册时BsfInfo的MAP格式开关  =  OFF
               数据校验周期(分钟)  =  0
           参数检查NF直接注册开关  =  OFF
        NF管理类流程NRF故障返回码  =  NULL
      NF服务发现流程NRF故障返回码  =  NULL
         SMSF注册携带SmsfInfo开关  =  OFF
             订阅通知更新缓存开关  =  OFF
           订阅通知中信元长度阈值  =  2
    注册携带PerPlmnSnssaiList开关  =  OFF
              NRF是否支持数据同步  =  支持
       数据校验不一致上报告警开关  =  OFF
      NRF服务发现流控告警上报开关  =  OFF
NRF服务发现流控告警检测周期(分钟)  =  5
(结果个数 = 1)

---- END
```

## 输出结果说明

| 输出项名称                   | 输出项解释                                                                                                                                                                         |
|:------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 切换主用NRF开关               | NRF主备组网情况下，如果当前NF已经注册在备用NRF上，设置该参数为ON可以让NF实时感知主用NRF的状态。主用NRF恢复后，NF将会向主用NRF发起注册，从备用NRF切换到主用NRF。                                                                                |
| 订阅通知后触发缓存同步时延 (秒)       | 该参数用于指定订阅推送后触发缓存同步更新的最大延时时间。实际系统中会在零到最大延时时间中选取随机数作为实际延时时间，以实现对缓存同步更新的离散化。                                                                                                     |
| NFService注册MAP格式开关      | 该参数用于控制NF注册的NF Service是否为MAP格式。  开关值为OFF时，NF注册携带Array格式的NF Service； 开关值为ON时，NF注册携带MAP格式的NF Service。                                                                           |
| NFService服务发现MAP格式开关    | 该参数用于控制NF服务发现请求NRF返回以及创建订阅请求NRF通知的NF Service是否为MAP格式。  开关值为OFF时，NF请求NRF返回的目标NF的NF Service为Array格式； 开关值为ON时，NF请求NRF返回的目标NF的NF Service为MAP格式。                                   |
| NF参数检查开关                | 该参数用于指定在NF注册/更新流程时，是否开启NF参数检查的开关。  当参数中NF的检查开关勾选时，NF注册/更新流程时会进行NF参数检查：如果参数检查失败，NF侧会上报“ALM-100225 NF注册失败”告警，且NF注册到对端的状态设置为Undiscoverable； 当参数中NF的检查开关未勾选时，NF注册/更新流程时不进行NF参数检查。 |
| AMF向NRF注册的TAI策略         | 该参数用于控制AMF向NRF注册的TAI范围的组合方式，即本地配置和无线上报的TAI进行组合的方式，本地配置可以通过ADD TACRANGE、ADD TAIRANGELIST进行配置。                                                                                  |
| 注册时BsfInfo的MAP格式开关      | 该参数用于控制BSF注册的BsfInfo是否为MAP格式。  开关值为OFF时，BSF注册携带Array格式的BsfInfo； 开关值为ON时，BSF注册携带MAP格式的BsfInfo。                                                                                 |
| 数据校验周期(分钟)              | 用于控制NF周期性发起向NRF进行数据校验的时间间隔（分钟），当值为0时表示不开启周期性数据校验。NF向NRF进行数据校验的内容为NF本地配置的NFProfile信息和NRF上存储的该NF的NFProfile信息，如果两者不一致NF会自动触发一次注册，保证NRF上存储的NFProfile信息和本地配置的保持一致。                 |
| 参数检查NF直接注册开关            | 用于控制NF周期性发起向NRF进行数据校验时是否直接发起重注册。  开关值为OFF时，将NF和NRF上的NFProfile数据进行比对，不一致发起重注册，一致则不发起重注册； 开关值为ON时直接发起重注册。                                                                       |
| NF管理类流程NRF故障返回码         | 该参数用于配置本端网元管理类流程NRF故障返回码。                                                                                                                                                     |
| NF服务发现流程NRF故障返回码        | 该参数用于配置本端网元服务发现流程NRF故障返回码。                                                                                                                                                    |
| SMSF注册携带SmsfInfo开关      | 该参数用于控制SMSF向NRF注册时是否携带SmsfInfo。开关值为OFF时，SMSF注册不携带SmsfInfo；开关值为ON时，SMSF注册携带SmsfInfo。                                                                                           |
| 订阅通知更新缓存开关              | 该参数用于控制针对缓存的NF，本端网元是否使用NRF发送的订阅通知中的NfProfile信息更新其缓存信息。                                                                                                                        |
| 订阅通知中信元长度阈值             | 该参数用于指定接收到订阅通知中的信元长度的阈值。当本端网元收到NRF发送的订阅通知时，如NfProfile中的supi、gpsi、tai、dnn的信元长度都小于该参数值时，不使用订阅通知中的NfProfile信息更新其缓存信息，而是后续向NRF服务发现更新缓存。                                           |
| 注册携带PerPlmnSnssaiList开关 | 该参数用于控制本端网元向NRF注册时是否携带PerPlmnSnssaiList。                                                                                                                                      |
| NRF是否支持数据同步             | 该参数用于在NRF主备或NRF双活组网情况下，设置NRF是否有数据同步的功能 。                                                                                                                                      |
| 数据校验不一致上报告警开关           | 该参数用于控制NF向NRF周期性发起数据校验的数据校验结果不一致时是否上报ALM-100225 NF注册失败告警。  开关值为OFF时，数据校验结果不一致时不上报告警； 开关值为ON时，数据校验结果不一致时上报告警。                                                                  |
| NRF服务发现流控告警上报开关         | 该参数用于指定是否上报ALM-100720 NRF服务发现流控告警。                                                                                                                                            |
| NRF服务发现流控告警检测周期(分钟)     | 该参数用于指定ALM-100720 NRF服务发现流控告警的检测周期。在配置的时间周期内每分钟检测一次是否存在流控，检测周期内每分钟都出现流控则上报告警，检测周期内每分钟都没有出现流控则告警恢复。                                                                            |