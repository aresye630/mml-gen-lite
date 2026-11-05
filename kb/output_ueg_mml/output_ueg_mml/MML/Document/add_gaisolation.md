# 增加Ga业务隔离配置（ADD GAISOLATION）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**须知** 

此命令不能动态生效，需要执行RST RU生效。隔离正常运行中的AP模块，需要先执行STP CDRRECEIVE命令停止话单接收。添加隔离配置会导致隔离AP停止接收话单并禁止链路迁入。

**适用NF：NCG**

该命令用于隔离AP模块上的234G话单业务，即禁止Ga接口的接收话单，使得被隔离的AP不生成234G话单文件，并且禁止隔离AP上Ga链路的新建或迁入。

#### 注意事项

- 最多可配置128条记录。
- 运行中的AP模块执行添加Ga业务隔离配置命令之前，需要执行****SET SRVSTH****命令关闭负载均衡开关，通过链路迁移命令，将要隔离AP上的链路均衡迁移到其他234G业务AP上，执行**STP CDRRECEIVE**命令，停止NCG接收话单。
- 当用户增加了Ga隔离配置时，满足输入参数的234G业务AP模块，产生**ALM-82014停止接收话单**告警。
- 若被隔离的AP存在未迁移的Ga链路，相关链路的业务将会切到备NCG并且上游网元会上报“****ALM-81021 CG无响应****”告警。
- 命令操作后，存在隔离配置的234G业务AP禁止Ga链路迁入。
- 命令操作后需要执行**RST RU**命令重启RU生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                                                                                         |
|:--------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| GAISOLATIONID | Ga隔离标识 | 可选必选说明：必选参数 参数含义：话单存储对象标识，全局唯一。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～32。 默认值：无 配置原则：该参数只能由字母、数字、下划线、中划线组成。                                          |
| RUID          | RU的ID  | 可选必选说明：可选参数 参数含义：RU的ID。 数据来源：本端规划 取值范围：整数类型，取值范围为64～4294967294。 默认值：无 配置原则：该值需要执行LST SERVICERUSTATE命令，查询出存在的RU ID进行填写。                       |
| MNAME         | 模块名称   | 可选必选说明：可选参数 参数含义：用于标识一个业务模块对象，全局唯一。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。 默认值：无 配置原则： 该值需要执行LST CPMODULE命令，查询出存在的MNAME进行填写。 不能输入的特殊字符请参考“特殊字符表”。 |

#### 使用实例

增加一个AP65\_1的Ga口接入隔离，示例如下：

- 场景一：扩容RU65后，添加模块AP65\_1前，添加Ga隔离配置。

  ```
  ADD GAISOLATION:GAISOLATIONID="iso1", MNAME="AP65_1";
  ```
- 场景二：运行中的AP65\_1添加Ga隔离配置。
  - 关闭负载均衡开关

    ```
    SET SRVSTH: LINKSWITCH=OFF;
    ```
  - 通过链路迁移命令手动迁出AP65\_1的Ga链路

    ```
    DSP ACTRL:;
    ```

    查询Ga链路状态。

    ```
    DSP RU: SERVICEINSTANCE="CG_VNFC_999";
    ```

    获取RU65的RU名称

    ```
    OPR DBGCMDPRXY: RUNAME="CG_SP_RU2_0065", SGID=1, CMDMSG="crms spu-group", SERVICEINSTANCE="CG_VNFC_999";
    ```

    ```
    RETCODE = 0  操作成功  
    结果如下 
    --------                   
                      RU名称  =  CG_SP_RU2_0065               
                  SG进程ID号  =  1           
              调试命令字符串  =  crms spu-group 
    调试命令执行结果返回信息  =   spu-group 1  
    MasterSlot: 65  
    SlaveSlot: 64   
    Slot No.       Status              ElectionWght         
    - - - - - - - - - - - - - - - - - - - - - - - -  
    64             Normal              Normal               
    65             Normal              Normal                
    (结果个数 = 1)  
    ---    END
    ```

    ```
    OPR DBGCMDPRXY: RUNAME="CG_SP_RU2_0065", SGID=1, CMDMSG="vcg show link 1", SERVICEINSTANCE="CG_VNFC_999";
    ```

    查询RU65上的前100条链路信息，此处的RUNAME为查出的MasterSlot RU编号对应的RU名称。

    ```
    OPR DBGCMDPRXY: RUNAME="CG_SP_RU2_0065", SGID=1, CMDMSG="vcg operate move 1 641", SERVICEINSTANCE="CG_VNFC_999";
    ```

    将AP65\_1上的Link Id为1的链路迁出到234G业务模块AP64\_1上去。若AP65\_1上还存在其它链路，通过该操作将AP65\_1上的其它Ga链路全部迁出。
  - AP65\_1停止接收234G话单

    ```
    STP CDRRECEIVE: MNAME="AP65_1";
    ```
  - AP65\_1添加Ga隔离配置

    ```
    ADD GAISOLATION:GAISOLATIONID="iso1", MNAME="AP65_1";
    ```
  - 执行RST RU重启RU65

    ```
    RST RU: RUNAME="CG_SP_RU2_0065", SERVICEINSTANCE="CG_VNFC_999";
    ```