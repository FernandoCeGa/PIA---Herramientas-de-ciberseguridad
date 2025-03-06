function Ver-Reglasblock {
    param([Parameter()] [string] $activo = 'True',
    [Parameter()] [string] $vari = 'Block')
    Get-NetFirewallRule -Enabled $activo -EdgeTraversalPolicy $vari
}

Ver-Reglasblock