# 显示HAFD调试命令结果（DSP DBGHAFD）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于CMF内部功能调试。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                                                        |
|:----------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CELLID    | 进程标识   | 可选必选说明：必选参数  参数含义：该参数是进程唯一的身份标识。通过执行DSP MSPROCESS: PROCOBJECT=PROCNAME, PROCNAME="CELL_CMF";获取CMF进程ID。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~1024。  默认值：无  配置原则：无 |
| DEBUGNAME | 调试命令   | 可选必选说明：必选参数  参数含义：该参数是用户输入的调试命令，例如：cmf agent，用于获取输入命令者所期望获取的查询信息。具体的调试命令请参见“DSP DBGHAFD工程命令”章节。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~1024。  默认值：无  配置原则：无        |

## 使用实例

查询调试命令结果。

```
%%DSP DBGHAFD: CELLID="cmf-pod-2__167__0", DEBUGNAME="cmf agent";%%
RETCODE = 0  操作成功

结果如下
--------
命令查询结果                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

Cell Id                                                         Pod Id                                          Gid             Node Id                         Owner                                           Owner Writer            Registered      EtcdLinkState   HbLinkState     
sfm-pod-5c7bc897dd-pn6nc__103__1                                sfm-pod-5c7bc897dd-pn6nc                        4121            192.168.0.1                     172.22.2.102:37021                              CmfAgent                true            Normal          Normal  
csdbom-pod-0__103__1                                            csdbom-pod-0                                    4107            192.168.0.2                     172.22.2.102:37021                              CmfAgent                true            Normal          Normal                                                                                                                                                                                                                                                                                           
gtp-pod-9c7996fbd-hkxmm__103__1                                 gtp-pod-9c7996fbd-hkxmm                         1033            192.168.0.3                     172.22.2.102:37021                              CmfAgent                true            Normal          Normal                                                                                                                                                                                                                                                                                           
gbimom-pod-0__103__1                                            gbimom-pod-0                                    4098            192.168.0.4                     172.22.2.102:37021                              CmfAgent                true            Normal          Normal                                                                                                                                                                                                                                                                                           
usnom-pod-1__103__1                                             usnom-pod-1                                     4117            192.168.0.5                     172.22.2.102:37021                              CmfAgent                true            Normal          Normal                                                                                                                                                                                                                                                                                           
sbim-pod-6dc4876f4c-cr9kl__103__1                               sbim-pod-6dc4876f4c-cr9kl                       1034            192.168.0.6                     172.22.2.102:37021                              CmfAgent                true            Normal          Normal                                                                                                                                                                                                                                                                                           
appctrl-pod-7cb446d8f4-cqg4m__103__1                            appctrl-pod-7cb446d8f4-cqg4m                    1035            192.168.0.7                     172.22.2.102:37021                              CmfAgent                true            Normal          Normal                                                                                                                                                                                                                                                                                           
gtp-pod-9c7996fbd-qgbj8__103__1                                 gtp-pod-9c7996fbd-qgbj8                         1032            192.168.0.8                     172.22.2.102:37021                              CmfAgent                true            Normal          Normal                                                                                                                                                                                                                                                                                           
(结果个数 = 8)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                                |
|:--------|:-------------------------------------|
| 命令查询结果  | 该参数是由输入的调试命令，调用不同的函数，输出调试命令所期望的查询结果。 |