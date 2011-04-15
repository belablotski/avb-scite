Oracle Wallet (Secure External Password Store)
http://download.oracle.com/docs/cd/B19306_01/network.102/b14266/cnctslsh.htm

== Steps to configure Oracle Wallet ==
* Create wallet with create_wallet.bat
* Add (modify,delete) credentials with ctrl_cred.bat
* In the client sqlnet.ora file, enter the wallet location:
  WALLET_LOCATION = (SOURCE = (METHOD = FILE) (METHOD_DATA = (DIRECTORY = /xxx/yyy/zzz)))
* In the client sqlnet.ora file:
  SQLNET.WALLET_OVERRIDE = TRUE
