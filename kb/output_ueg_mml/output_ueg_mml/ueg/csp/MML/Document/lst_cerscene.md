# 查询证书应用场景信息 (LST CERSCENE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询证书应用场景配置信息。

**说明** 

该命令仅在非三方场景下支持。

该命令仅对部分网元生效，不支持的网元执行时会返回“519809 当前网元不支持此操作”错误码。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                  |
|:----------|:-------|:------------------------------------------------------------------------------------------------------|
| MEID      | 网元ID   | 可选必选说明：可选参数。 参数含义：网元ID。 取值范围：5~1023。 默认值：无。 配置原则：无。                                                   |
| SCENENAME | 场景名称   | 可选必选说明：可选参数。 参数含义：证书应用场景名称。 取值范围：长度不超过200个字符，只能包含英文字符、数字、中划线和下划线，且只能以字母开头。 默认值：无。 配置原则：场景名称和证书组一对一绑定。 |

## 使用实例

1. 查询所有证书应用场景数据：

   ```
   LST CERSCENE:;
   ```

   ```
   %%LST CERSCENE:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    网元ID  场景名称         证书组名称       证书组类型  场景描述       

    100     psc_dev          devtest          Device      psc_dev1       
    100     psc_ca           catest           CA          psc_ca1        
    100     testCA           testCA           CA          testCA         
    100     cert-suit-wdl    cert-suit-wdl    CA+Device   cert-suit-wdl  
    100     cert-device-wdl  cert-device-wdl  Device      cert-device-wdl
    100     test             test             CA          test           
    100     zxtest           zz               CA          zzz            
    100     zz               zz               CA          zz             
   (结果个数 = 8)

   ---    END
   ```
2. 查询“网元ID”为“100”的证书应用场景数据：

   ```
   LST CERSCENE: MEID=100;
   ```

   ```
   %%LST CERSCENE: MEID=100;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    网元ID  场景名称         证书组名称       证书组类型  场景描述       

    100     psc_dev          devtest          Device      psc_dev1       
    100     psc_ca           catest           CA          psc_ca1        
    100     testCA           testCA           CA          testCA         
    100     cert-suit-wdl    cert-suit-wdl    CA+Device   cert-suit-wdl  
    100     cert-device-wdl  cert-device-wdl  Device      cert-device-wdl
    100     test             test             CA          test           
    100     zxtest           zz               CA          zzz            
    100     zz               zz               CA          zz             
   (结果个数 = 8)

   ---    END
   ```
3. 查询“网元ID”为“100” “场景名称”为“test”的证书应用场景数据：

   ```
   LST CERSCENE: MEID=100, SCENENAME="test";
   ```

   ```
   %%LST CERSCENE: MEID=100, SCENENAME="test";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
       网元ID  =  100
     场景名称  =  test
   证书组名称  =  test
   证书组类型  =  CA
     场景描述  =  test
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

| 输出项名称   | 输出项解释                |
|:--------|:---------------------|
| 网元ID    | 网元ID。                |
| 场景名称    | 场景名称。场景名称和证书组一对一绑定。  |
| 证书组名称   | 证书组名称。证书组和场景名称一对一绑定。 |
| 证书组类型   | 证书组类型。               |
| 场景描述    | 场景描述。                |