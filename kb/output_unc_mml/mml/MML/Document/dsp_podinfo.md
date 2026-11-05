# 显示已部署的Pod实例信息（DSP PODINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

实例化成功之后，执行此命令，用于显示已部署的Pod实例信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                    |
|:-------|:-------|:----------------------------------------------------------------------------------------|
| MEID   | 网元ID   | 可选必选说明：可选参数  参数含义：该参数用于标识Pod所在的网元ID。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~40。  默认值：无  配置原则：无 |

## 使用实例

DSP PODINFO:;

```
%%DSP PODINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
Pod类型        Pod标识                         容器类型               网元ID   GID

sdbsim-pod    sdbsim-pod-1                   CONTAINER_SDRE        0       1044  
sdbsim-pod    sdbsim-pod-1                   ContainerUvcSdbSim    0       1044  
goomtest-pod  goomtest-pod-fbc4b6bf7-7g68q   ContainerAuth         0  	   1029  
goomtest-pod  goomtest-pod-fbc4b6bf7-7g68q   CONTAINER_SDRE        0       1029  
vusn-pod      vusn-pod-1                     CONTAINER_SDRE        0       1032  
vusn-pod      vusn-pod-1                     LINK_SP_RU            0       1032  
httpsim-pod   httpsim-pod-77bc6b8f78-8dk69   ContainerHttpSim      0       1036  
httpsim-pod   httpsim-pod-77bc6b8f78-8dk69   CONTAINER_SDRE        0       1036  
ddbsf-pod     ddbsf-pod-6cf694757d-89p8l     CONTAINER_DDFDDBSF    0       4101  
ddbsf-pod     ddbsf-pod-6cf694757d-89p8l     CONTAINER_SDRE        0       4101  
vusnom-pod    vusnom-pod-0                   CONTAINER_SDRE        0       4114  
vusnom-pod    vusnom-pod-0                   LINK_OM_RU            0       4114  
netcssim-pod  netcssim-pod-79f86d88d-ppvfm   ContainerUvcNetcssim  0       1038  
netcssim-pod  netcssim-pod-79f86d88d-ppvfm   CONTAINER_SDRE        0       1038  
om-scene-pod  om-scene-pod-1                 CONTAINER_DATASHOW    0  	   4115  
om-scene-pod  om-scene-pod-1                 CONTAINER_SDRE        0  	   4115  
om-scene-pod  om-scene-pod-1                 CONTAINER_SERVICECON  0  	   4115  
csdb-pod      csdb-pod-0                     CONTAINER_SDRE        0  	   1035  
csdb-pod      csdb-pod-0                     CSDB_SD_RU            0  	   1035  
omb-pod       omb-pod-54cbdfbccf-qxdq8       CONTAINER_CHR         0  	   4123  
omb-pod       omb-pod-54cbdfbccf-qxdq8       CONTAINER_LICCTRL     0  	   4123  
omb-pod       omb-pod-54cbdfbccf-qxdq8       CONTAINER_MMCS        0  	   4123  
omb-pod       omb-pod-54cbdfbccf-qxdq8       CONTAINER_OMP         0  	   4123  
omb-pod       omb-pod-54cbdfbccf-qxdq8       CONTAINER_SDRE        0  	   4123  
httpsim-pod   httpsim-pod-77bc6b8f78-bfkh7   CONTAINER_SDRE        0  	   1050  
httpsim-pod   httpsim-pod-77bc6b8f78-bfkh7   ContainerHttpSim      0  	   1050  
sfm-pod       sfm-pod-55fd4f7565-476x6       CONTAINER_CPM         0  	   4140  
sfm-pod       sfm-pod-55fd4f7565-476x6       CONTAINER_DCF         0  	   4140  
sfm-pod       sfm-pod-55fd4f7565-476x6       CONTAINER_SCFM        0  	   4140  
sfm-pod       sfm-pod-55fd4f7565-476x6       CONTAINER_SDRE        0       4140  
sfm-pod       sfm-pod-55fd4f7565-476x6       CONTAINER_SFPROXY     0       4140  
sfm-pod       sfm-pod-55fd4f7565-476x6       CONTAINER_TICKSERVER  0       4140  
sfm-pod       sfm-pod-55fd4f7565-476x6       CONTAINER_HAFCTRL     0       4140  
sfm-pod       sfm-pod-55fd4f7565-476x6       CONTAINER_HAFG        0       4140  
sfm-pod       sfm-pod-55fd4f7565-476x6       CONTAINER_RCCTRL      0       4140  
sfm-pod       sfm-pod-55fd4f7565-476x6       CONTAINER_RMFEXEC     0       4140  
sfm-pod       sfm-pod-55fd4f7565-476x6       CONTAINER_SDRC        0       4140  
csdbom-pod    csdbom-pod-0                   CSDB_OM_RU            0       4104  
csdbom-pod    csdbom-pod-0                   CONTAINER_SDRE        0       4104  
csdbom-pod    csdbom-pod-1                   CONTAINER_SDRE        0       4097  
csdbom-pod    csdbom-pod-1                   CSDB_OM_RU            0       4097  
cslbipom-pod  cslbipom-pod-0                 CONTAINER_SDRE        0       4110  
cslbipom-pod  cslbipom-pod-0                 CSLB_OM_RU            0       4110  
cslbipom-pod  cslbipom-pod-0                 VNRS_OM_RU            0       4110  
om-scene-pod  om-scene-pod-0                 CONTAINER_SDRE        0       4108  
om-scene-pod  om-scene-pod-0                 CONTAINER_SERVICECON  0       4108  
om-scene-pod  om-scene-pod-0                 CONTAINER_DATASHOW    0       4108  
sfm-pod       sfm-pod-55fd4f7565-l772t       CONTAINER_CPM         0       4141  
sfm-pod       sfm-pod-55fd4f7565-l772t       CONTAINER_DCF         0       4141  
sfm-pod       sfm-pod-55fd4f7565-l772t       CONTAINER_HAFCTRL     0       4141  
sfm-pod       sfm-pod-55fd4f7565-l772t       CONTAINER_HAFG        0       4141  
sfm-pod       sfm-pod-55fd4f7565-l772t       CONTAINER_RMFEXEC     0       4141  
sfm-pod       sfm-pod-55fd4f7565-l772t       CONTAINER_SCFM        0       4141  
sfm-pod       sfm-pod-55fd4f7565-l772t       CONTAINER_SDRC        0       4141  
sfm-pod       sfm-pod-55fd4f7565-l772t       CONTAINER_SDRE        0       4141  
sfm-pod       sfm-pod-55fd4f7565-l772t       CONTAINER_TICKSERVER  0       4141  
sfm-pod       sfm-pod-55fd4f7565-l772t       CONTAINER_RCCTRL      0       4141  
sfm-pod       sfm-pod-55fd4f7565-l772t       CONTAINER_SFPROXY     0       4141  
appctrl-pod   appctrl-pod-5df9695dd4-zlm8p   CONTAINER_DDFDDB      0       1025  
appctrl-pod   appctrl-pod-5df9695dd4-zlm8p   CONTAINER_IPS         0       1025  
appctrl-pod   appctrl-pod-5df9695dd4-zlm8p   CONTAINER_SDRE        0       1025  
appctrl-pod   appctrl-pod-5df9695dd4-zlm8p   ContainerCtrl         0       1025  
appctrl-pod   appctrl-pod-5df9695dd4-zlm8p   ContainerHttpCtrl     0       1025  
appctrl-pod   appctrl-pod-5df9695dd4-zlm8p   ContainerUvcUpCtrl    0       1025  
cslbipom-pod  cslbipom-pod-1                 CONTAINER_SDRE        0       4111  
cslbipom-pod  cslbipom-pod-1                 CSLB_OM_RU            0       4111  
cslbipom-pod  cslbipom-pod-1                 VNRS_OM_RU            0       4111  
cslbip-pod    cslbip-pod-1                   CSLB_IP_RU2           0       1053  
cslbip-pod    cslbip-pod-1                   VNRS_IP_RU            0       1053  
cslbip-pod    cslbip-pod-1                   CONTAINER_SDRE        0       1053  
appctrl-pod   appctrl-pod-5df9695dd4-jvtrd   ContainerHttpCtrl     0       1045  
appctrl-pod   appctrl-pod-5df9695dd4-jvtrd   ContainerUvcUpCtrl    0       1045  
appctrl-pod   appctrl-pod-5df9695dd4-jvtrd   CONTAINER_DDFDDB      0       1045  
appctrl-pod   appctrl-pod-5df9695dd4-jvtrd   CONTAINER_IPS         0       1045  
appctrl-pod   appctrl-pod-5df9695dd4-jvtrd   CONTAINER_SDRE        0       1045  
appctrl-pod   appctrl-pod-5df9695dd4-jvtrd   ContainerCtrl         0       1045  
gtp-pod       gtp-pod-7f959f4b9f-vl2t6       CONTAINER_SDRE        0       1047  
gtp-pod       gtp-pod-7f959f4b9f-vl2t6       ContainerGtpc         0       1047  
sbim-pod      sbim-pod-779c5446d4-s6wnj      ContainerSbim         0       1051  
sbim-pod      sbim-pod-779c5446d4-s6wnj      CONTAINER_SDRE        0       1051  
netcssim-pod  netcssim-pod-79f86d88d-fzxtp   CONTAINER_SDRE        0       1041  
netcssim-pod  netcssim-pod-79f86d88d-fzxtp   ContainerUvcNetcssim  0       1041  
csdb-pod      csdb-pod-1                     CSDB_SD_RU            0       1028  
csdb-pod      csdb-pod-1                     CONTAINER_SDRE        0       1028  
sbim-pod      sbim-pod-779c5446d4-rzcfx      ContainerSbim         0       1039  
sbim-pod      sbim-pod-779c5446d4-rzcfx      CONTAINER_SDRE        0       1039  
vam-pod       vam-pod-79fbd7474c-kdxrb       CONTAINER_SDRE        0       1024  
vam-pod       vam-pod-79fbd7474c-kdxrb       ContainerSbiLink      0       1024  
vam-pod       vam-pod-79fbd7474c-kdxrb       ContainerSm           0       1024  
vam-pod       vam-pod-79fbd7474c-kdxrb       ContainerTopoSim      0       1024  
vsm-pod       vsm-pod-8694698b5b-lcd8t       ContainerAm           0       1046  
vsm-pod       vsm-pod-8694698b5b-lcd8t       ContainerPlcm         0       1046  
vsm-pod       vsm-pod-8694698b5b-lcd8t       ContainerSecm         0       1046  
vsm-pod       vsm-pod-8694698b5b-lcd8t       CONTAINER_SDRE        0       1046  
vsm-pod       vsm-pod-8694698b5b-lcd8t       ContainerAddr         0       1046  
sdbsim-pod    sdbsim-pod-0                   ContainerUvcSdbSim    0       1026  
sdbsim-pod    sdbsim-pod-0                   CONTAINER_SDRE        0       1026  
cmf-pod       cmf-pod-2                      CONTAINER_CMF         0       4100  
cmf-pod       cmf-pod-2                      CONTAINER_SDRE        0       4100  
comtest-pod   comtest-pod-0                  ContainerDisc         0       1040  
comtest-pod   comtest-pod-0                  CONTAINER_SDRE        0       1040  
ddbsf-pod     ddbsf-pod-6cf694757d-hdp7z     CONTAINER_DDFDDBSF    0       4103  
ddbsf-pod     ddbsf-pod-6cf694757d-hdp7z     CONTAINER_SDRE        0       4103  
omb-pod       omb-pod-54cbdfbccf-t7f64       CONTAINER_LICCTRL     0       4118  
omb-pod       omb-pod-54cbdfbccf-t7f64       CONTAINER_MMCS        0       4118  
omb-pod       omb-pod-54cbdfbccf-t7f64       CONTAINER_OMP         0       4118  
omb-pod       omb-pod-54cbdfbccf-t7f64       CONTAINER_SDRE        0       4118  
omb-pod       omb-pod-54cbdfbccf-t7f64       CONTAINER_CHR         0       4118  
cmf-pod       cmf-pod-1                      CONTAINER_SDRE        0       4106  
cmf-pod       cmf-pod-1                      CONTAINER_CMF         0       4106  
vup-pod       vup-pod-1                      CONTAINER_SDRE        0       1034  
vup-pod       vup-pod-1                      ContainerUvcUp        0       1034  
vsm-pod       vsm-pod-8694698b5b-x9vm9       ContainerPlcm         0       1055  
vsm-pod       vsm-pod-8694698b5b-x9vm9       ContainerSecm         0       1055  
vsm-pod       vsm-pod-8694698b5b-x9vm9       CONTAINER_SDRE        0       1055  
vsm-pod       vsm-pod-8694698b5b-x9vm9       ContainerAddr         0       1055  
vsm-pod       vsm-pod-8694698b5b-x9vm9       ContainerAm           0       1055  
ipctrl-pod    ipctrl-pod-1                   VNRS_IPCTRL_RU        0       4113  
ipctrl-pod    ipctrl-pod-1                   CONTAINER_SDRE        0       4113  
ipctrl-pod    ipctrl-pod-0                   CONTAINER_SDRE        0       4102  
ipctrl-pod    ipctrl-pod-0                   VNRS_IPCTRL_RU        0       4102  
srvcssim-pod  srvcssim-pod-68d86d7c94-vn5tt  ContainerUvcSrvcssim  0       1027  
srvcssim-pod  srvcssim-pod-68d86d7c94-vn5tt  CONTAINER_SDRE        0       1027  
srvcssim-pod  srvcssim-pod-68d86d7c94-vn5tt  ContainerNetm         0       1027  
cslbip-pod    cslbip-pod-0                   CONTAINER_SDRE        0       1048  
cslbip-pod    cslbip-pod-0                   CSLB_IP_RU2           0       1048  
cslbip-pod    cslbip-pod-0                   VNRS_IP_RU            0       1048  
vam-pod       vam-pod-79fbd7474c-zsfw4       ContainerSbiLink      0       1056  
vam-pod       vam-pod-79fbd7474c-zsfw4       ContainerSm           0       1056  
vam-pod       vam-pod-79fbd7474c-zsfw4       ContainerTopoSim      0       1056  
vam-pod       vam-pod-79fbd7474c-zsfw4       CONTAINER_SDRE        0       1056  
vusn-pod      vusn-pod-0                     CONTAINER_SDRE        0       1052  
vusn-pod      vusn-pod-0                     LINK_SP_RU            0       1052  
srvcssim-pod  srvcssim-pod-68d86d7c94-x5cqn  CONTAINER_SDRE        0       1043  
srvcssim-pod  srvcssim-pod-68d86d7c94-x5cqn  ContainerNetm         0       1043  
srvcssim-pod  srvcssim-pod-68d86d7c94-x5cqn  ContainerUvcSrvcssim  0       1043  
vup-pod       vup-pod-0                      CONTAINER_SDRE        0       1031  
vup-pod       vup-pod-0                      ContainerUvcUp        0       1031  
gtp-pod       gtp-pod-7f959f4b9f-tkpn7       ContainerGtpc         0       1037  
gtp-pod       gtp-pod-7f959f4b9f-tkpn7       CONTAINER_SDRE        0       1037  
ddbsf-pod     ddbsf-pod-6cf694757d-zr6lr     CONTAINER_DDFDDBSF    0       4112  
ddbsf-pod     ddbsf-pod-6cf694757d-zr6lr     CONTAINER_SDRE        0       4112  
cmf-pod       cmf-pod-0                      CONTAINER_CMF         0       4105  
cmf-pod       cmf-pod-0                      CONTAINER_SDRE        0       4105  
vusnom-pod    vusnom-pod-1                   CONTAINER_SDRE        0       4116  
vusnom-pod    vusnom-pod-1                   LINK_OM_RU            0       4116  
(Number of results = 150)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                                                      |
|:--------|:-----------------------------------------------------------|
| Pod类型   | 该参数用于表示Pod类型，如sfm-pod，具体类型定义请参考tosca模板中的定义。                |
| Pod标识   | 该参数用于表示Pod标识。                                              |
| 容器类型    | 该参数用于表示容器类型，如ContainerSm、ContainerAm，具体类型定义请参考tosca模板中的定义。 |
| 网元ID    | 该参数用于标识Pod所在的网元ID。                                         |
| GID     | 该参数用于表示Pod的身份标志，由SF-SCF分配。                                 |