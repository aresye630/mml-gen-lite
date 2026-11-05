# 卸载IPsec服务（UPF）

- 操作场景
- 必备事项
- 操作步骤

## 操作场景

当运营商不需要IPsec服务或IPsec服务动态上线失败时，可以单独卸载IPsec pod，从而下线IPsec服务。

## 必备事项

前提条件

- 已经完成网络设计，已规划下线IPsec pod的类型和数量。
- 已经规划IPsec pod关联的其他组件的类型和数量，卸载IPsec服务后，请联系华为技术支持工程师缩容关联组件。
- 如果动态下线失败，只能继续重新触发动态下线任务。

数据

| 类别                      | 参数名称                      | 取值样例/说明                                                | 获取方法   |
|:------------------------|:--------------------------|:-------------------------------------------------------|:-------|
| UEG OM Portal帐户         | IP地址                      | 192.168.1.1 操作维护接口IP，即“VNFD模板”中的“MNG_IP”或“MNG_IPv6”参数。 | 本端规划   |
| UEG OM Portal帐户         | 端口号                       | 31943                                                  | 本端规划   |
| UEG OM Portal帐户         | 用户名                       | admin                                                  | 本端规划   |
| UEG OM Portal帐户         | 密码                        | Changeme_123                                           | 本端规划   |
| 特性下线 OPR FEATUREDISABLE | Pod类型列表（PODTYPE）          | ipsecexec-c4-pod/ipsecctl-pod                          | 本端规划   |
| 特性下线 OPR FEATUREDISABLE | 下线方式（DISABLETYPE）         | Normal                                                 | 本端规划   |
| 特性下线 OPR FEATUREDISABLE | FUNCTIONSETNAME （网络功能集名称） | IPsec                                                  | 固定取值   |

## 操作步骤

1. 登录UEG OM Portal。
2. 执行**SET FWSOFTPARA**命令（UEG-M和UEG-L在UEG视图），开启Service Fabric的**DWORD\_521**软参，即系统故障时不触发容灾导致的联动复位。

   ```
   SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=521, DWORDVALUE=1;
   ```

   执行**LST FWSOFTPARA**命令（UEG-M和UEG-L在UEG视图），确认Service Fabric软参值是否为1。

   ```
   LST FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=521;
   ```

   如果软参值为1，请执行后续步骤。如果软参值不是1，请联系华为技术支持。
3. 执行命令（UEG-M和UEG-L在UEG视图），动态下线IPsec pod。

   ```
   OPR FEATUREDISABLE:PODTYPE="ipsecexec-c4-pod/ipsecctl-pod", DISABLETYPE=Normal, FUNCTIONSETNAME="IPsec";
   ```
4. 执行命令（UEG-M和UEG-L在UEG视图），确认已经成功下线IPsec pod。

   ```
   DSP FEATUREOPRHIST:;
   ```

   回显为“处理结果=处理成功”。

   执行命令（UEG-M和UEG-L在CSP视图），确认pod已下线。

   ```
   DSP POD: MEID="网元ID", TYPE=byType, PODTYPE="ipsecctl-pod";
   DSP POD: MEID="网元ID", TYPE=byType, PODTYPE="ipsecexec-c4-pod";
   ```

   回显为“查询Pod不存在”。
5. 执行**SET FWSOFTPARA**命令（UEG-M和UEG-L在UEG视图），关闭Service Fabric的**DWORD\_521**软参，即系统故障时触发容灾导致的联动复位。

   ```
   SET FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=521, DWORDVALUE=0;
   ```

   执行**LST FWSOFTPARA**命令（UEG-M和UEG-L在UEG视图），确认Service Fabric软参值是否为0。

   ```
   LST FWSOFTPARA: PARAMETERSTYPE=DWORD, DWORDINDEX=521;
   ```

   如果软参值为0，请执行后续步骤。如果软参值不是0，请联系华为技术支持。
6. 若动态下线IPsec服务后，不再上线IPsec服务，则需要缩容IPsec自身VM（PBU\_P-I\_C4），释放VM资源。

   若后续还需要上线IPsec服务，则不必缩容IPsec自身VM。

   **缩容VM**：请参见《UEG扩缩容指导书》。