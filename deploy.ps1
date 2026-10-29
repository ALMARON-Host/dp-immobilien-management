# Baut die Vorschau und veröffentlicht sie auf GitHub Pages (Branch gh-pages).
# Aufruf:  powershell -ExecutionPolicy Bypass -File .\deploy.ps1
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

# Vorschau: saubere URLs + für Suchmaschinen gesperrt (noindex, robots.txt)
python src\build.py --pretty --noindex
if ($LASTEXITCODE -ne 0) { throw 'Build fehlgeschlagen' }

$remote = git remote get-url origin
Push-Location site
try {
  if (Test-Path .git) { Remove-Item .git -Recurse -Force }
  git init -q -b gh-pages
  git add -A
  git commit -q -m "Deploy $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
  git push -q -f $remote gh-pages
  if ($LASTEXITCODE -ne 0) { throw 'Push fehlgeschlagen' }
  Remove-Item .git -Recurse -Force
}
finally {
  Pop-Location
}
# Lokale Datei-Version wiederherstellen (Doppelklick auf site\index.html)
python src\build.py | Out-Null
Write-Host 'Online in 1-2 Minuten: https://almaron-host.github.io/dp-immobilien-management/'
