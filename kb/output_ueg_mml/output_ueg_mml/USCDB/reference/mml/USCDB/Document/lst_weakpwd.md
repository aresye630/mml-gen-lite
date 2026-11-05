# 查询弱口令信息（LST WEAKPWD）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询弱口令信息。

- 若要查询指定弱口令信息记录时，请输入“弱口令”参数。
- 若要查询全部弱口令信息记录时，请不要输入“弱口令”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                   |
|:-------|:-------|:-----------------------------------------------------------------------|
| PWD    | 弱口令    | 可选必选说明：可选参数 参数含义：本参数用于指定需要查询的弱口令信息。 取值范围：长度不超过128位的字符串。 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询“弱口令”为“12345”的信息记录：

   ```
   LST WEAKPWD: PWD="*****";
   ```

   ```
   %%LST WEAKPWD: PWD="*****";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   弱口令  =  12345
   (结果个数 = 1)

   ---    END
   ```
2. 查询全部“弱口令”信息记录：

   ```
   LST WEAKPWD:;
   ```

   ```
   %%LST WEAKPWD:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    弱口令            

    !5Hty*@LfMasbIiT  
    Admin_12#         
    CSP@gaussdb@2017  
    Changeme_123      
    Changeme_2021     
    Cspdbg@2017       
    Cspdbr@2017       
    HWps123+          
    Hk%w-!d@8Ve)qH6p  
    Huawei#12         
    Huawei12#@        
    Huawei@123        
    QAZ2wsx@123!      
    SSHAdmin_HW       
    Sysadmin@2009     
    Uscdb_sys0        
    Uscdb_sys1        
    Uscdb_sysAcce1    
    User_hw123        
    cnp200@HW         
    cnp200@HuaWei1    
    data1@HW          
    data2@HW          
    ei*b+@b#6Nh(tS1j  
    grub2020@linux@RD 
    h1+@w(9Ho3b       
    huawei#2013       
    inFTPNe600@HW     
    inFTPadg252@HW    
    inFTPavg2012@HW   
    inFTPbmu600@HW    
    inFTPmt2016@HW    
    inFTPomu600@HW    
    inFTPspider2012@HW
    kafka-1qaz@WSX    
    lem600@HW         
    lgn2020@linux@RD  
    r1+@z(9Ho3b       
    replica0@HW       
    repuser0@HW       
    role#Huawei       
    vrpv8@huawei.com
    pgw#2013
    ab12CD34#56  
   (结果个数 = 44)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，参数含义请参见**ADD WEAKPWD**命令的参数说明。