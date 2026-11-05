# 查询用户数据（LST PSUBDATA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

实时用户数统计操作可能对USRSU虚拟机（对应裸机场景的usrsu-pod）性能产生影响，当任一USRSU虚拟机（对应裸机场景的usrsu-pod）的CPU高于60%时不建议执行本命令。因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于在配置数据库中统计当前全部用户数、动态生成的用户数、在线用户数、从用户数、组用户数、成员用户总数、业务的签约用户数、套餐的签约用户数和子节点用户数。

## 注意事项

- 该操作可能对系统性能产生影响，仅系统管理员级别的操作员有操作权限，请在低业务量的时候进行操作。执行本命令前，在OM Portal“USCDB MML命令”界面执行**DSP NODECPUSTAT**（对应裸机场景DSP PODCPUSTAT）命令，查看虚拟机/裸机Pod的CPU信息，如果所有USRSU类型的虚拟机（对应裸机场景的usrsu-pod）CPU使用率不高于60%，可以直接执行本命令。如果任意一个USRSU虚拟机（对应裸机场景的usrsu-pod）的CPU使用率高于60%，禁止批量执行本命令，必须等上一条命令执行完毕后才能开始执行本命令。如果任意一个USRSU虚拟机（对应裸机场景的usrsu-pod）的CPU使用率高于70%，禁止执行本命令。
- 若存在用户重复订购业务/套餐，则系统查询业务/套餐的签约用户数显示结果为用户订购业务/套餐的记录数，而非实际签约业务/套餐的用户数。
- 若“AllowAdjustService”参数设置为“1”，如果通过该命令查询业务的签约用户数，查询得到的结果可能是业务改造中的过程数据，会存在一定偏差。
- 混合组网场景，5G设备执行本命令查询用户数据，统计时会合并4G设备和5G设备的查询结果返回，不支持分别统计4G设备和5G设备用户数据。4G设备执行本命令只支持统计4G用户数据。
- 混合组网场景，该命令在vSP分区只支持查询本地用户。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                    |
|:-----------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE       | 统计类型   | 用于指示系统需要按照哪种统计类型来查询用户个数。 取值范围：“AllUserNum”：表示统计全部用户数、动态生成的用户数、在线用户数、从用户数、组用户数、成员用户数、子节点用户数。“TotalUserNum”：表示统计全部用户数。“OnlineUserNum”：表示统计在线用户数。“DynamicCreated”：表示统计动态生成的用户数。“SlaveUserNum”：表示统计从用户数。“GroupUserNum”：表示统计组用户数。“MemberUserNum”：表示统计成员用户总数。“ServiceUserNum”：表示业务的签约用户数。“ServicePackageUserNum”：表示套餐的签约用户数。“ChildUserNum”：表示统计子节点用户数。 默认值：无。 |
| SRVNAME    | 业务名称   | 用于指示系统需要按照指定业务名称来查询业务的签约用户数。仅当“统计类型”为“ServiceUserNum”时，该参数显示，且为必选参数。 取值范围：长度不超过64的字符串。 默认值：无。                                                                                                                                                                                                                                                           |
| SRVPKGNAME | 业务套餐名称 | 用于指示系统需要按照指定套餐名称来查询套餐的签约用户数。仅当“统计类型”为“ServicePackageUserNum”时，该参数显示，且为必选参数。 取值范围：长度不超过32的字符串。 默认值：无。                                                                                                                                                                                                                                                    |
| STATUS     | 状态     | 用于指示系统需要按照哪种状态来查询业务/套餐的签约用户数。仅当“统计类型”为“ServiceUserNum”或“ServicePackageUserNum”时，该参数显示，且为必选参数。 取值范围：All：显示所有状态的业务/套餐的签约用户数，包括未过期和已过期的。Valid：显示有效状态的业务/套餐的签约用户数，仅包括未过期的。 默认值：无。                                                                                                                                                                           |

## 使用实例

- 统计所有用户个数。

  ```
  LST PSUBDATA: TYPE=AllUserNum;
  ```

  ```
  %%LST PSUBDATA: TYPE=AllUserNum;%%
  RETCODE = 0 Operation succeeded

                     Total Number of Subscribers = 1000
                    Number of Online Subscribers = 0
           Number of Dynamic Created Subscribers = 0
                     Number of Slave Subscribers = 10
                     Number of Group Subscribers = 1
                    Number of Member Subscribers = 100
                     Number of Child Subscribers = 0
  Total count = 7

  There is together 1 report

  ---    END
  ```
- 查询业务的签约用户数，“业务名称”为“TestService”，“状态”为“All”：

  ```
  LST PSUBDATA: TYPE=ServiceUserNum, SRVNAME="TestService", STATUS=All;
  ```

  ```
  %%LST PSUBDATA: TYPE=ServiceUserNum, SRVNAME="TestService", STATUS=All;%%
  RETCODE = 0 Operation succeeded

                     Service Name = TestService
             Service Package Name = NULL
            Number of Subscribers = 1000
                           Status = All
  Total count = 4

  There is together 1 report

  ---    END
  ```
- 查询套餐的签约用户数，“业务套餐名称”为“TestPackage”，“状态”为“All”：

  ```
  LST PSUBDATA: TYPE=ServicePackageUserNum, SRVPKGNAME="TestPackage", STATUS=All;
  ```

  ```
  %%LST PSUBDATA: TYPE=ServicePackageUserNum, SRVPKGNAME="TestPackage", STATUS=All;%%
  RETCODE = 0 Operation succeeded

                     Service Name = NULL
             Service Package Name = TestPackage
            Number of Subscribers = 100
                           Status = All
  Total count = 4

  There is together 1 report

  ---    END
  ```

## 输出结果说明

| 输出项名称                                 | 输出项解释                                  |
|:--------------------------------------|:---------------------------------------|
| Total Number of Subscribers           | 全部用户数                                  |
| Number of Online Subscribers          | 在线用户数                                  |
| Number of Dynamic Created Subscribers | 动态生成的用户数                               |
| Number of Slave Subscribers           | 从用户数                                   |
| Number of Group Subscribers           | 组用户数                                   |
| Number of Member Subscribers          | 成员用户总数  说明： 一个用户属于几个组，就按几个成员统计。        |
| Service Name                          | 用户签约的业务名称                              |
| Service Package Name                  | 用户签约的套餐名称                              |
| Number of Subscribers                 | 业务/套餐的签约用户数                            |
| Status                                | 用户签约的业务/套餐状态                           |
| Number of Child Subscribers           | 子节点用户数  说明： 一个用户属于几个父节点用户，就按几个子节点用户统计。 |