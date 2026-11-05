# 查询Pod信息(LST PODINFO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

本命令用于查询CGPLite服务管理下Pod的配置信息。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                       |
|:--------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PODNAME | Pod名称  | 可选必选说明：可选参数。 参数含义：用于指示系统需要查询哪个Pod的数据。 取值范围：长度不超过128的字符串。 默认值：无。 配置原则：该参数的值域范围为：大写字母“A～Z”、小写字母“a～z”、数字“0～9”、特殊字符“-”、“_”、“.”。该参数区分大小写。若不输入，则表示该参数不作为查询的限制条件。 |
| MEID    | 网元ID   | 可选必选说明：可选参数。 参数含义：用于指示系统需要查询哪个网元的Pod的数据。 取值范围：0～1023。 默认值：无。 配置原则：若不输入，则表示该参数不作为查询的限制条件。                                                                   |

## 使用实例

**实例1**

查询CGPLite服务管理下Pod的配置信息。

`LST PODINFO:;`

```
%%LST PODINFO:;%%
RETCODE = 0  操作成功

操作结果如下
------------
 Pod名称    节点名称    应用类型  Base1平面MAC       Base2平面MAC       BASE1 IP     BASE2 IP     FABRIC1 IP   FABRIC2 IP   FABRIC3 IP   FABRIC4 IP   BASE网口个数  FABRIC网口个数  信令网口个数    
VNF ID                            网元ID             架构类型

 cgplite-0  10.16.10.1  OMU       FA:16:3E:18:98:CC  FA:16:3E:18:98:CC  10.16.128.1  10.16.128.1  10.16.144.1  10.16.152.2  NULL         NULL         2             2               0               
98ea39a390c8414fa8a5ab8a6f65b273  0                  X86    
 cgplite-1  10.16.10.1  OMU       FA:16:3E:90:7A:EB  FA:16:3E:90:7A:EB  10.16.128.2  10.16.128.2  10.16.144.2  10.16.152.1  NULL         NULL         2             2               0               
98ea39a390c8414fa8a5ab8a6f65b273  0                  X86
(结果个数 = 2)

---    END
```

**实例2**

查询“Pod名称”为“cgplite-0”的POD的配置信息。

`LST PODINFO: PODNAME="cgplite-0";`

```
%%LST PODINFO: PODNAME="cgplite-0";%%
RETCODE = 0  操作成功

操作结果如下
------------
       Pod名称  =  cgplite-0
      节点名称  =  10.16.10.1
      应用类型  =  OMU
  Base1平面MAC  =  FA:16:3E:18:98:CC
  Base2平面MAC  =  FA:16:3E:18:98:CC
      BASE1 IP  =  10.16.128.1
      BASE2 IP  =  10.16.128.1
    FABRIC1 IP  =  10.16.144.1
    FABRIC2 IP  =  10.16.152.2
    FABRIC3 IP  =  NULL     
    FABRIC4 IP  =  NULL   
  BASE网口个数  =  2 
FABRIC网口个数  =  2   
  信令网口个数  =  0
        VNF ID  =  98ea39a390c8414fa8a5ab8a6f65b273
        网元ID  =  0
      架构类型  =  X86
(结果个数 = 1)

---    END
```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。输出结果说明如表1所示。

命令执行异常，请联系华为技术支持处理。

| 输出项名称      | 输出项解释                 |
|:-----------|:----------------------|
| Pod名称      | 用于返回查询Pod的名称。         |
| 节点名称       | 用于返回查询Pod的节点名称。       |
| 应用类型       | 用于返回查询Pod的应用类型。       |
| Base1平面MAC | 用于返回查询Pod的Base1平面MAC。 |
| Base2平面MAC | 用于返回查询Pod的Base2平面MAC。 |
| BASE1 IP   | 用于返回查询Pod的BASE1 IP。   |
| BASE2 IP   | 用于返回查询Pod的BASE2 IP。   |
| FABRIC1 IP | 用于返回查询Pod的FABRIC1 IP。 |
| FABRIC2 IP | 用于返回查询Pod的FABRIC2 IP。 |
| FABRIC3 IP | 用于返回查询Pod的FABRIC3 IP。 |
| FABRIC4 IP | 用于返回查询Pod的FABRIC4 IP。 |
| BASE网口个数   | 用于返回查询Pod的BASE网口个数。   |
| FABRIC网口个数 | 用于返回查询Pod的FABRIC网口个数。 |
| 信令网口个数     | 用于返回查询Pod的信令网口个数。     |
| VNF ID     | 用于返回查询Pod的VNF ID。     |
| 网元ID       | 用于返回查询Pod所在的网元。       |
| 架构类型       | 用于返回查询Pod的架构类型。       |

## 参考信息

无。