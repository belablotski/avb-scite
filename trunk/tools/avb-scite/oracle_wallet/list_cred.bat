SETLOCAL
call common.bat

rem Create credential oracle.security.client.connect_string1
mkstore -wrl %ORACLE_WALLET_HOME% -listCredential

ENDLOCAL