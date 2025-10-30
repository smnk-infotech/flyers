param(
    [string]$ProjectId
)

<#
Improved deploy helper that uses a local/global firebase CLI if available,
otherwise falls back to `npx firebase-tools` or `npm exec --package firebase-tools`.

Usage:
  .\deploy.ps1 -ProjectId your-firebase-project-id

This script will:
 - ensure Node.js/npm are available
 - run an interactive login (using available runner)
 - deploy hosting to the specified project

Notes:
 - This avoids requiring a global `firebase` install (useful on locked machines).
 - If you prefer to install globally, run `npm install -g firebase-tools` in an elevated shell.
#>

function Ensure-Node {
    $node = Get-Command node -ErrorAction SilentlyContinue
    $npm = Get-Command npm -ErrorAction SilentlyContinue
    if (-not $node -or -not $npm) {
        Write-Host "Node.js and npm are required. Install from https://nodejs.org/ and re-run." -ForegroundColor Yellow
        exit 1
    }
}

# Run the firebase command using whatever is available: global firebase, npx, or npm exec.
function Run-Firebase {
    param(
        [Parameter(Mandatory=$true)] [string[]]$Args
    )

    # Try global firebase first
    if (Get-Command firebase -ErrorAction SilentlyContinue) {
        & firebase @Args
        return $LASTEXITCODE
    }

    # Try npx firebase-tools
    if (Get-Command npx -ErrorAction SilentlyContinue) {
        & npx firebase-tools @Args
        return $LASTEXITCODE
    }

    # Fallback to npm exec (works with recent npm)
    if (Get-Command npm -ErrorAction SilentlyContinue) {
        & npm exec --package firebase-tools -- firebase @Args
        return $LASTEXITCODE
    }

    Write-Host "No firebase runner available. Install firebase-tools globally or ensure npm is available." -ForegroundColor Red
    return 1
}

if (-not $ProjectId) {
    $ProjectId = Read-Host "Enter Firebase project id (e.g. my-project-12345)"
}

Ensure-Node

Write-Host "Logging into Firebase (a browser window will open)..." -ForegroundColor Green
if (Run-Firebase -Args @('login') -ne 0) {
    Write-Host "Firebase login failed or was cancelled." -ForegroundColor Red
    exit 1
}

Write-Host "Deploying to Firebase Hosting project: $ProjectId" -ForegroundColor Green
if (Run-Firebase -Args @('deploy', '--only', 'hosting', '--project', $ProjectId) -eq 0) {
    Write-Host "Deployment complete." -ForegroundColor Green
} else {
    Write-Host "Deployment failed. Check the output above for errors." -ForegroundColor Red
    exit 1
}
