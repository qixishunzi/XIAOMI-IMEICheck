# 小米设备“查找设备”状态查询工具  
**Mi Device "Find Device" Status Checker**

## 简介 | Introduction
本程序用于通过输入设备 IMEI 号，自动查询该设备是否启用了“小米查找设备”功能。适用于检验设备激活锁状态、售前设备检测等场景。  
This tool allows you to check whether a Xiaomi device has "Find Device" enabled by entering its IMEI number. It's useful for activation lock status checks and pre-sale inspections.

## 适用场景 | Use Cases
- 在二手平台购买小米手机前，查询设备状态，避免购买到“有锁机”；  
  Before buying a Xiaomi phone on a second-hand platform, use this tool to avoid locked devices.  
- 手机维修、翻新前确认设备是否存在账户锁定；  
  For repair or refurbishing, confirm if the device is locked to a Mi account.  
- 做为检测流程的一部分，供商家或个人定期校验设备激活状态。  
  Integrate into a testing flow for regular device checks by individuals or sellers.

## 功能特点 | Features
- 输入 IMEI 后，一键查询设备状态；  
  Enter the IMEI and get the status with one click.  
- 接口调用自小米官网，结果准确可靠；  
  Uses Xiaomi's official API for accurate results.  
- 返回设备是否已开启“查找设备”功能的明确信息；  
  Clearly shows whether "Find Device" is enabled.  
- 自动添加时间戳参数，绕过缓存；  
  Adds timestamp automatically to bypass caching.  
- 请求头与 Cookie 可自定义配置，灵活适配不同环境。  
  Customizable headers and cookies for flexibility.

## 使用方法 | How to Use
1. 运行程序；  
   Run the program.  
2. 根据提示输入需要查询的 IMEI；  
   Enter the IMEI number when prompted.  
3. 等待结果输出，即可查看设备查找状态。  
   Wait for the result to see the device status.

## 注意事项 | Notes
- 请勿频繁请求，以避免被服务器限制；  
  Do not send requests too frequently to avoid being rate-limited.  
- 本工具仅供学习交流使用，严禁用于非法用途。  
  For educational and research use only. Do not use it for illegal purposes.