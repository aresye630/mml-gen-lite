# 查询服务发现Scheme优选策略（LST NFDISCSCHEMEPLY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG、NEF、NWDAF、SCF**

该命令用于查询服务发现时的Scheme优选策略。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                |
|:---------|:-------|:--------------------------------------------------------------------------------------------------------------------|
| INFOTYPE | 信息类型   | 可选必选说明：可选参数  参数含义：该参数用于指定信息类型。  数据来源：本端规划 取值范围： “BYNFTYPE（使用NF类型）”：输入NF类型“BYNFID（使用NF实例标识）”：输入NF实例标识  默认值：无  配置原则：无 |

## 使用实例

- 查询所有服务发现时的Scheme优选策略。

  ```
  %%LST NFDISCSCHEMEPLY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  信息类型  		NF类型     NF实例标识      服务名称                                    策略      

  使用NF类型		NfUDM      NULL            UDM提供的Nudm_SubscriberDataManagement服务  仅HTTP   
  使用NF实例标识	NfInvalid  smf_instance_0  SMF提供的Nsmf_PDUSession服务                仅HTTPS  
  (结果个数 = 2)

  ---    END
  ```
- 查询所有根据NF类型配置的服务发现时的Scheme优选策略。

  ```
  %%LST NFDISCSCHEMEPLY: INFOTYPE=BYNFTYPE;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
       NF类型  =  NfUDM
  服务名称  =  UDM提供的Nudm_SubscriberDataManagement服务
       策略  =  仅HTTP
  (结果个数 = 1)

  ---    END
  ```
- 查询所有根据NF实例标识配置的服务发现时的Scheme优选策略。

  ```
  %%LST NFDISCSCHEMEPLY: INFOTYPE=BYNFID;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  NF实例标识  =  smf_instance_0
   服务名称  =  SMF提供的Nsmf_PDUSession服务
        策略  =  仅HTTPS
  (结果个数 = 1)

  ---    END
  ```

## 输出结果说明

| 输出项名称   | 输出项解释              |
|:--------|:-------------------|
| NF实例标识  | 该参数用于指定NF实例标识。     |
| 服务名称    | 该参数用于指定服务名称。       |
| 策略      | 该参数用于指定Scheme优选策略。 |
| 信息类型    | 该参数用于指定信息类型。       |
| NF类型    | 该参数用于指定NF类型。       |