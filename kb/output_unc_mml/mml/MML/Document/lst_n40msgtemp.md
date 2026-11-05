# 查询N40消息属性模板（LST N40MSGTEMP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询N40消息属性模板。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识         | 参数名称       | 参数说明                                                                                           |
|:-------------|:-----------|:-----------------------------------------------------------------------------------------------|
| TEMPLATENAME | N40消息属性模板名 | 可选必选说明：可选参数  参数含义：该参数用于指定N40消息字段模板名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。不区分大小写。  默认值：无  配置原则：无 |

## 使用实例

查询名为“n40attr”的N40消息属性模板：

```
%%LST N40MSGTEMP: TEMPLATENAME="n40attr";%%
RETCODE = 0  操作成功

结果如下
--------
                 N40消息属性模板名  =  n40attr
        RANSecondaryRATUsageReport  =  携带该字段
                        NB扩展属性  =  携带该字段
         QFI容器中的DownLinkVolume  =  携带该字段
            HomeProvidedChargingID  =  携带该字段
               huaweiQBCIndication  =  不携带该字段
applicationserviceProviderIdentity  =  不携带该字段
            roamingChargingProfile  =  携带该字段
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                              | 输出项解释                                                                                                  |
|:-----------------------------------|:-------------------------------------------------------------------------------------------------------|
| N40消息属性模板名                         | 该参数用于指定N40消息字段模板名。                                                                                     |
| RANSecondaryRATUsageReport         | N40消息中是否携带RANSecondaryRATUsageReport。                                                                  |
| NB扩展属性                             | 控制NB-IOT、LTEM接入时N40消息是否携带扩展属性信息，包括APN Rate Control、Serving PLMN Rate Control、CP only indication和PtP隧道。 |
| QFI容器中的DownLinkVolume              | N40消息中MultipleQFIcontainer信元是否携带DownLinkVolume。                                                        |
| HomeProvidedChargingID             | N40消息中是否携带HomeProvidedChargingID。                                                                      |
| huaweiQBCIndication                | QBC计费时N40消息中是否携带huaweiQBCIndication信元。                                                                 |
| applicationserviceProviderIdentity | 该参数用于控制N40消息中是否携带applicationserviceProviderIdentity（应用提供商标识）。                                          |
| 是否支持携带roamingChargingProfile       | 该参数用于控制RCP不协商场景，N40消息中RoamingQBCInformation信元是否携带RoamingChargingProfile。                               |