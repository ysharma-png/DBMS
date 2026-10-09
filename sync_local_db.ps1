Write-Host "Running local MySQL database synchronization for DBMS Lab..." -ForegroundColor Cipher
python "$PSScriptRoot\sync_local_db.py" $args[0]
