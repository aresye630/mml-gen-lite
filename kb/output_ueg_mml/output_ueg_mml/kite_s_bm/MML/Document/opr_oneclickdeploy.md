# 操作服务一键式部署（OPR ONECLICKDEPLOY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

堆栈下线和服务下线功能会将已启用的服务下线，该服务将不会接受相关业务。

该命令用于操作网元一键式部署任务。

## 注意事项

如果命令下发返回超时，请通过**DSP ONECLICKDEPLOYHIST**查询执行结果。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称      | 参数说明                                                                                                                                                                                                                                          |
|:----------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OPRTYPE         | 操作类型      | 可选必选说明：必选参数  参数含义：该参数用于表示一键式部署任务的操作类型。  数据来源：本端规划 取值范围： INDEPSTACKENABLE（独立堆栈服务上线）INDEPSTACKDISABLE（独立堆栈服务下线）FEATUREENABLE（主堆栈服务上线）FEATUREDISABLE（主堆栈服务下线）SCALEOUT（服务扩容）SCALEIN（服务缩容）DELETE（删除）RETRY（重试）ROLLBACK（回退）  默认值：无  配置原则：无           |
| NODETYPELIST    | 节点类型列表    | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"、"INDEPSTACKDISABLE"、"FEATUREENABLE"、"FEATUREDISABLE"、"SCALEOUT"、"SCALEIN"时为条件可选参数。  参数含义：该参数用于表示一键式部署任务的操作的节点信息。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~256。  默认值：无  配置原则：无                                |
| PODTYPELIST     | Pod类型列表   | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"、"FEATUREENABLE"时为条件必选参数。该参数在"OPRTYPE"配置为"SCALEOUT"、"SCALEIN"时为条件可选参数。  参数含义：该参数用于表示一键式部署任务的操作的Pod信息。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~256。输入格式如下："podtype1:podnum1/podtype2:podnum2"。  默认值：无  配置原则：无 |
| FUNCTIONSETNAME | 网络功能集名称   | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"、"FEATUREENABLE"、"FEATUREDISABLE"时为条件必选参数。  参数含义：该参数用于表示一键式部署任务的操作的网络功能集名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~256。  默认值：无  配置原则：无                                                                      |
| VMNAMELIST      | 虚机名称列表    | 可选必选说明：该参数在"OPRTYPE"配置为"DELETE"时为条件必选参数。  参数含义：该参数用于标识需要缩容的虚机名称列表。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~1024。输入格式如下："VmName1/VmName2"。  默认值：无  配置原则：  该参数仅在虚机场景下使用。                                                                                |
| MEID            | 网元ID      | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"、"INDEPSTACKDISABLE"、"FEATUREENABLE"、"FEATUREDISABLE"、"SCALEOUT"、"SCALEIN"、"DELETE"时为条件可选参数。  参数含义：该参数用于表示一键式部署任务的网元标识。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~256。  默认值：无  配置原则：无                          |
| EXTENDEDATTR    | 扩展属性      | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"、"FEATUREENABLE"时为条件可选参数。  参数含义：该参数为预留功能，无需填写。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~256。  默认值：无  配置原则：无                                                                                                   |
| PKGNAME         | 软件包名称     | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"时为条件必选参数。  参数含义：该参数用于表示一键式部署任务的操作的软件包名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~256。该参数可以通过DSP VNFPKGS的返回值中获取。  默认值：无  配置原则：无                                                                               |
| INPUT           | 模板INPUT参数 | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKENABLE"时为条件可选参数。  参数含义：该参数用于表示一键式部署任务的需要更新的模板输入参数。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~512。输入格式如下："key1:value1/key2:value2"。  默认值：无  配置原则：无                                                                     |
| PROCESSTYPE     | 处理方式      | 可选必选说明：该参数在"OPRTYPE"配置为"FEATUREDISABLE"时为条件必选参数。  参数含义：该参数用于指定服务下线方式： 若选择普通下线，内部流程异常时下线任务会终止，修复问题后可以重新下发下线任务； 若选择强制下线，内部流程异常时也会强制将服务下线。强制下线是高危命令，建议操作该动作时，寻求研发工程师支持。  数据来源：本端规划 取值范围： Normal（普通操作）Force（强制操作）  默认值：无  配置原则：无                  |
| STACKNAME       | 堆栈名称      | 可选必选说明：该参数在"OPRTYPE"配置为"INDEPSTACKDISABLE"时为条件必选参数。  参数含义：该参数用于标识堆栈名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~1024。该参数可以通过DSP VNFSTACKNAMES的返回值中获取。  默认值：无  配置原则：无                                                                                   |

## 使用实例

假如运营商需要上线UDG-to堆栈，可以通过调用以下命令进行堆栈上线。

```
%%OPR ONECLICKDEPLOY: OPRTYPE=INDEPSTACKENABLE, PODTYPELIST="to-pod:1/toctrl-pod:1", FUNCTIONSETNAME="UDG-to", PKGNAME="unc-to-24.1.rc1.b061-tosca-std-edge-arm", INPUT="appprogress:false";%%
RETCODE = 0  操作成功

结果如下
--------
接受结果  =  accepted
结果说明  =  NULL
(结果个数 = 1)

---    END
```