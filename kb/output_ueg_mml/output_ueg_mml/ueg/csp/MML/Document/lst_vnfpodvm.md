# 查询网元的POD与虚拟机位置关系（LST VNFPODVM）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

查询网元对应的POD与虚拟机位置关系。

**说明** 

该命令仅在Full-stack虚机场景下支持。

#### 注意事项

无。

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                             |
|:-------|:-------|:-----------------------------------------------------------------|
| VNFID  | 网元ID   | 可选必选说明：必选参数。 参数含义：网元ID，可以通过LST ME获取。 取值范围：0～65535 默认值：无。 配置原则：无。 |

#### 使用实例

查询网元ID为0的POD对应虚拟机位置关系信息。

```
%%LST VNFPODVM: VNFID=0;%%
RETCODE = 0  操作成功

操作结果如下
------------
网元ID 网元类型  Pod ID                                 POD类型             POD所在虚拟机的虚拟机ID               虚拟机类型  POD名称

0      APP       9acfacda-522a-11ea-b3b5-fa163eb9ce89  patchmg             33e683fa-f05d-4fc8-a1ca-fd9da3d00009  APP_A       patchmgr-79bbdcd99d-gvasdsl
0      APP       9ad7c0bb-522a-11ea-b3b5-fa163eb9ce89  patchmg             f8f939d9-4567-45fd-9b30-1adc63616619  APP_A       patchmgr-79bbdcd99d-gvafdsl
0      APP       d7615d4a-522b-11ea-b3b5-fa163eb9ce89  cse-serxxxe-center  c387ae41-d5fc-4655-9d21-63f002684ccb  APP_B       cse-service-center-8867c8f8-512dsfr
0      APP       d76a8b5b-522b-11ea-b3b5-fa163eb9ce89  cse-serxxxe-center  33e683fa-f05d-4fc8-a1ca-fd9da3d00009  APP_A       cse-service-center-8867c8f8-5terv8r
0      APP       d76a7840-522b-11ea-b3b5-fa163eb9ce89  cse-serxxxe-center  f8f939d9-4567-45fd-9b30-1adc63616619  APP_A       cse-service-center-8867c8f8-5tvdf8r
0      APP       baf43e7e-522a-11ea-b3b5-fa163eb9ce89  filetrans           f8f939d9-4567-45fd-9b30-1adc63616619  APP_A       filetransfer-5cb94d646-52saqlg
0      APP       baee0778-522a-11ea-b3b5-fa163eb9ce89  filetrans           33e683fa-f05d-4fc8-a1ca-fd9da3d00009  APP_A       filetransfer-5cb94d646-52qaslg
0      APP       cda377a3-522a-11ea-b3b5-fa163eb9ce89  omce                f8f939d9-4567-45fd-9b30-1adc63616619  APP_A       omce-5cba94d646-52sdqlg
0      APP       102bc6f3-522c-11ea-b3b5-fa163eb9ce89  omce                33e683fa-f05d-4fc8-a1ca-fd9da3d00009  APP_A       omce-5cba94d646-52asqlg

(结果个数 = 9)

---    END
```

#### 输出结果说明

命令执行正常，会返回命令执行成功的提示信息及网元对应POD与虚拟机的位置关系信息，输出结果项信息如表1所示。

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 输出项名称          | 输出项解释                 |
|:---------------|:----------------------|
| 网元ID           | 用于返回查询的网元ID。          |
| 网元类型           | 用于返回查询的网元类型。          |
| Pod ID         | 用于返回查询的容器的ID。         |
| POD类型          | 用于返回查询的容器类型。          |
| POD所在虚拟机的虚拟机ID | 用于返回查询的容器所在虚拟机的虚拟机ID。 |
| 虚拟机类型          | 用于返回查询的虚拟机类型。         |
| POD名称          | 用于返回查询的容器名称。          |

|    错误码 | 错误码解释               | 原因分析                                                              | 处理建议                                    |
|-------:|:--------------------|:------------------------------------------------------------------|:----------------------------------------|
| 150001 | 查询网元信息失败。           | 查询网元信息失败。                                                         | 检查并修改为正确的网元ID。                          |
| 150006 | 查询POD对应虚拟机位置关系信息失败。 | 查询容器对应虚拟机信息失败。                                                    | 请联系华为技术支持。                              |
| 150023 | 查询VNFM获取VM信息失败。     | VNFM系统当前忙，未返回查询结果。                                                | 请间隔1分钟后重新执行该命令，若多次执行后仍无法成功返回，请联系华为技术支持。 |
| 150021 | 当前模式不支持此命令          | 该命令仅在Full-Stack虚机场景下支持，若在Full-Stack裸机及三方CaaS场景下执行该指令，会返回此错误码作为提示。 | 无需处理。                                   |