exit


SETLOCAL
call common.bat

rem Create credential oracle.security.client.connect_string1
mkstore -wrl %ORACLE_WALLET_HOME% -createCredential <db_connect_string> <username> <password>

rem mkstore -wrl %ORACLE_WALLET_HOME% -modifyCredential <db_connect_string> <username> <password>
rem mkstore -wrl %ORACLE_WALLET_HOME% -deleteCredential <db_alias>

ENDLOCAL