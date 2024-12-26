
# `Appium-UI-Testing`

# Overview

This repository demonstrates how to perform UI testing for mobile applications using Appium. It includes a sample test script for automating the login process of a mobile app.

このリポジトリでは、Appiumを使用してモバイルアプリケーションのUIテストを実行する方法を紹介します。サンプルテストスクリプトには、モバイルアプリのログインプロセスの自動化が含まれています。

---
# Features
- Automated UI testing with Appium（Appiumによる自動化UIテスト）
- Supports Android Emulator and physical devices（Androidエミュレーターおよび物理デバイスのサポート）
- Easy configuration of Desired Capabilities（Desired Capabilitiesの簡単な設定）
- Sample script for automating login process（ログインプロセスの自動化サンプルスクリプト）
- Cross-platform testing support (Android/iOS)（クロスプラットフォームテストのサポート（Android/iOS））

 ---
 
# Prerequisites
- Install [Appium](https://appium.io/) and [Python](https://www.python.org/downloads/).( [Appium](https://appium.io/) と [Python](https://www.python.org/downloads/) をインストールしてください.)
- Install the necessary drivers for your target mobile platform (Android/iOS).( 対象のモバイルプラットフォーム（Android/iOS）のドライバをインストールします。)
- Install the required Python packages by running the following command(次のコマンドで必要なPythonパッケージをインストールします。):
    
  ```pip install Appium-Python-Client```

・Make sure you have access to an Android emulator or a physical device for testing.（テストのためにAndroidエミュレータまたは物理デバイスにアクセスできることを確認してください。）
# Setup

**1**.	Clone the repository（リポジトリをクローンします。):

```git clone https://github.com/yourusername/Appium-UI-Testing.git```
```cd Appium-UI-Testing```


**2**.	Start the Appium server (Make sure Appium is installed and running) (Appiumサーバーを起動します（Appiumがインストールされていて動作していることを確認してください.):

```appium```


**3**.	Configure your desired capabilities in the appium_test.py file for your device and app.(デバイスとアプリに応じたdesired capabilitiesをappium_test.pyファイルで設定します。)


---

# Usage

**Step 1**: Configure Desired Capabilities(Capabilities / Desired Capabilitiesの設定)

Edit the desired_caps dictionary in appium_test.py to match your device and application details:
(appium_test.pyのdesired_caps辞書を編集して、デバイスとアプリケーションの詳細に合わせます。)
```
desired_caps = {
   "platformName": "Android",  # Platform name (e.g., Android or iOS)
   "platformVersion": "12.0",  # OS version
   "deviceName": "emulator-5554",  # Emulator or device name
   "app": "/path/to/your/app.apk",  # Path to the application
   "automationName": "UiAutomator2"  # Automation framework for Android
}
```

**Step 2**: Run the test(テストの実行）

Run the test script with the following command（次のコマンドでテストスクリプトを実行します。）:

```python appium_test.py```

For example of how to use this repository,please refer to [example_appium_ui_test.py]

このリポジトリの使用例については、[example_appium_ui_test.py]をご覧ください。

---

# Technologies
- *Python*
- *Appium*
- *Android Emulator*
- *UIAutomator2*
- *JSON*

---
