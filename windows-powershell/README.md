# verify sha256 checksum

```
PS C:> $hash=$(Get-FileHash -Algorithm SHA256 -Path .\MyFile.ext).Hash
```

# powershell

example 

```
PS C:\> Get-AppPackage -OutVariable foo
PS C:\> Write-Host $foo[0].name
windows.immersivecontrolpanel
PS C:\> $foo[0]


Name              : windows.immersivecontrolpanel
Publisher         : CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
Architecture      : Neutral
ResourceId        : neutral
Version           : 10.0.2.1000
PackageFullName   : windows.immersivecontrolpanel_10.0.2.1000_neutral_neutral_cw5n1h2txyewy
InstallLocation   : C:\Windows\ImmersiveControlPanel
IsFramework       : False
PackageFamilyName : windows.immersivecontrolpanel_cw5n1h2txyewy
PublisherId       : cw5n1h2txyewy
IsResourcePackage : False
IsBundle          : False
IsDevelopmentMode : False
NonRemovable      : True
IsPartiallyStaged : False
SignatureKind     : System
Status            : Ok

PS C:\> $foo[0] | Select-Object "Name"

Name
----
windows.immersivecontrolpanel
```
