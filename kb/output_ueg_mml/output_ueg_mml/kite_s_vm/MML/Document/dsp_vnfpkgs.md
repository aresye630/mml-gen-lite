# 显示网元关联的软件包名称（DSP VNFPKGS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询网元关联的软件包名称信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

假如运营商想要查询当前环境已上传的软件包名称，调用以下命令可以查询已上传的软件包名称。

```
%%DSP VNFPKGS:;%%
RETCODE = 0  操作成功

结果如下
--------
软件包名称                                       

t4-device-plugin-fst-manage                      
unc-to-24.1.rc1.b061-tosca-std-edge-arm          
om-service-fst-manage                            
unc-24.1.rc1.b061-tosca-vdm-share-bond-edge-arm  
trm-fst-manage                                   
net-24.1.rc1.b061-tosca-testapp-2u-1822-edge     
unc-24.1.rc1.b084-tosca-ueg-plus-bond-edge-arm   
alarmnotifyservice-fst-manage                    
tosca-csp-network-24.1.rc1.b030-ex               
extension-controller-manager-fst-manage          
unc-24.1.rc1.b061-tosca-ueg-plus-bond-edge-arm   
cfeapiserver-fst-manage                          
tosca-csp-24.1.rc1.b030-ex                       
om-network-service-fst-manage                    
provision-controller-manager-fst-manage          
(结果个数 = 15)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释         |
|:--------|:--------------|
| 软件包名称   | 该参数用于表示软件包名称。 |