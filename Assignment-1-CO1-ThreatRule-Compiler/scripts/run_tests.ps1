$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$build = Join-Path $root 'build'
New-Item -ItemType Directory -Force -Path $build | Out-Null

flex -o (Join-Path $build 'lex.yy.c') (Join-Path $root 'src\threatrule.l')
gcc -std=c11 -Wall -Wextra -O2 (Join-Path $build 'lex.yy.c') -o (Join-Path $build 'threatrule.exe')

& (Join-Path $build 'threatrule.exe') (Join-Path $root 'examples\valid_rules.tr')
if ($LASTEXITCODE -ne 0) { throw 'Valid-rule scan failed.' }

& (Join-Path $build 'threatrule.exe') (Join-Path $root 'examples\live_feed_rules.tr')
if ($LASTEXITCODE -ne 0) { throw 'Live-feed scan failed.' }

& (Join-Path $build 'threatrule.exe') (Join-Path $root 'examples\invalid_rules.tr')
if ($LASTEXITCODE -eq 0) { throw 'Invalid-rule scan unexpectedly succeeded.' }

foreach ($count in 100, 1000, 10000, 100000) {
    $file = Join-Path $build "rules-$count.tr"
    python (Join-Path $root 'scripts\generate_rules.py') $count $file
    $elapsed = Measure-Command { & (Join-Path $build 'threatrule.exe') $file | Out-Null }
    if ($LASTEXITCODE -ne 0) { throw "Generated $count-rule scan failed." }
    [PSCustomObject]@{ Rules = $count; Milliseconds = [math]::Round($elapsed.TotalMilliseconds, 2) }
}
