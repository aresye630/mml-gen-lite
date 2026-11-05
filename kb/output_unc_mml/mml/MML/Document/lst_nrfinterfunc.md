# 查询国际漫游功能参数（LST NRFINTERFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NRF**

此命令用于查询NRF国际漫游功能参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

使用以下命令查询国际漫游功能参数。

```
%%LST NRFINTERFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
        服务发现V-SMF精确匹配开关  =  关闭
    跨PLMN订阅更新是否返回404开关  =  打开
                   故障重选状态码  =  429.500.502.503.504
          HPLMN NRF的标准FQDN开关  =  关闭
              HPLMN NRF的协议模式  =  HTTP
     本NRF是否是国际漫游关口局NRF  =  是
漫游服务发现InterPlmnFqdn过滤开关  =  关闭
                 ProxySMF功能开关  =  关闭
         ProxySMF不匹配时处理策略  =  转发至对端I-NRF
    发现ProxySMF的DNN网络标识列表  =  ims
       漫入SUPI服务发现白名单开关  =  关闭
      允许ProxySMF网内发现开关  =  关闭
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                   | 输出项解释                                                                                                                                                                                                                                                                                |
|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 服务发现V-SMF精确匹配开关         | 该参数用于表示NRF在服务发现过程中是否对vsmf-support-ind进行精确匹配。 开关设置为FUNC_ON时：服务发现过程中，必须严格匹配携带的vsmf-support-ind参数，开关设置为FUNC_OFF时：服务发现过程中，NRF优先使用包含vsmf-support-ind在内的所有属性进行精确匹配，精确匹配有可用NF，就返回满足条件的NF Profile；没有精确匹配到或精确匹配上的NF不可用，就忽略掉该参数，满足其他条件的但没有显式指明V-SMF能力（NF Profile无vsmfSupportInd属性）的NF Profile。 |
| 跨PLMN订阅更新是否返回404开关      | 该参数用于表示国际漫游场景，NRF与NF的路由模式配置更改后，对于存量的跨PLMN订阅记录，是否在下一次收到订阅更新时返回404，用于触发拜访地NF重新发起订阅，刷新路由模式的nfStatusNotificationUri。                                                                                                                                                                     |
| 故障重选状态码                 | 该参数用于表示NRF通过SEPP转发请求时，进行对端NF故障重选的HTTP状态码。当对端NF返回的HTTP状态码在本参数的配置范围内时，NRF会进行故障重选，否则流程失败。                                                                                                                                                                                               |
| HPLMN NRF的标准FQDN开关      | 该参数用于表示本NRF作为拜访地NRF，收到跨PLMN请求时，若没有为目的HPLMN配置分层路由（可通过LST NRFPLMNRT命令查询），NRF是否自动为该HPLMN对应的归属地NRF生成标准FQDN，作为目的NRF的FQDN进行转发。开关设置为FUNC_ON时，允许NRF自动生成FQDN。开关设置为FUNC_OFF时，不自动生成，转发失败。                                                                                                       |
| HPLMN NRF的协议模式          | 该参数用于指定NRF与对端HPLMN NRF的协议模式。NRF和本PLMN的SEPP之间的协议模式不受此参数控制。                                                                                                                                                                                                                            |
| 本NRF是否是国际漫游关口局NRF       | 该参数用于表示本NRF是否为国际漫游关口局NRF。国际漫游关口局NRF用于对接SEPP并通过SEPP与其他HPLMN的NF进行交互。                                                                                                                                                                                                                   |
| 漫游服务发现InterPlmnFqdn过滤开关 | 该参数表示目标NF注册未携带InterPlmnFqdn场景下，漫游服务发现该NF时，NRF是否返回该NF。 开关设置为FUNC_ON时，不返回；开关设置为FUNC_OFF时，正常返回该NF。                                                                                                                                                                                      |
| ProxySMF功能开关            | 该参数用于表示NRF的proxy SMF功能开关。开关为FUNC_ON表示NRF支持处理proxy SMF定制功能，开关为FUNC_OFF表示不支持处理proxy SMF定制功能。                                                                                                                                                                                           |
| ProxySMF不匹配时处理策略        | 该参数表示ProxySMF功能开关开启场景下，NF发起跨PLMN的归属地SMF的服务发现，期望服务发现返回proxy SMF，但本NRF没有匹配的proxy SMF时NRF的处理策略。参数设置为DIRECTRETURN时，NRF直接返回服务发现失败；参数设置为FWD时，NRF继续转发给归属地I-NRF处理，返回归属地I-NRF处理后的最终发现结果。                                                                                                      |
| 发现ProxySMF的DNN网络标识列表    | 该参数表示发现proxy SMF的DNN网络标识列表，当ProxySMF功能开关开启场景下，NF发起跨PLMN的归属地SMF的服务发现，若本参数的DNN网络标识列表包含服务发现携带的dnn参数的网络标识部分，则NRF判断本次请求期望返回proxy SMF，此时没有匹配上proxy SMF，根据“NOSMFFWDPLY”参数指定的处理策略进行进一步的处理，若匹配上proxy SMF，则正常返回proxy SMF。若不包含，则正常转发处理。                                                         |
| 漫入SUPI服务发现白名单开关         | 该参数用于表示针对漫入场景，基于用户SUPI号码或SUPI号段列表（通过ADD ROAMINSUPIWL命令配置）I-NRF是否允许服务发现他网AUSF/UDM。 开关设置为FUNC_ON时，允许服务发现他网AUSF/UDM；开关设置为FUNC_OFF时，则返回服务发现失败。                                                                                                                                           |
| 允许ProxySMF网内发现开关        | 该参数表示ProxySMF功能开关开启场景下，NF发起网内（不跨PLMN）的服务发现SMF时，NRF是否允许proxy SMF被发现的开关。参数设置为FUNC_ON时，通过ADD NRFPROXYSMF命令配置的proxy SMF允许被网内发现；参数设置为FUNC_OFF时，则不允许被网内发现。                                                                                                                                 |