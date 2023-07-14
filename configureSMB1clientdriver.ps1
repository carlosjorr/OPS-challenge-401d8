# Import the required module
Import-Module SecurityPolicyDsc

# Define the configuration
configuration SMBv1ClientDriverConfiguration {
    param (
        [Parameter(Mandatory = $true)]
        [ValidateSet("Enabled: Disable driver (recommended)", "Enabled: Enable driver", "Disabled")]
        [String]$SMBv1ClientDriver
    )

    # Configuration block
    node localhost {
        SecurityPolicy 'SetSMBv1ClientDriver' {
            Name = 'Configure SMB v1 client driver'
            State = $SMBv1ClientDriver
        }
    }
}

# Set the desired SMBv1 client driver state
$smbv1ClientDriver = "Enabled: Disable driver (recommended)"

# Invoke the configuration
SMBv1ClientDriverConfiguration -SMBv1ClientDriver $smbv1ClientDriver

# Start the configuration
Start-DscConfiguration -Path .\SMBv1ClientDriverConfiguration -Force -Wait

# Check the configuration status
(Get-DscConfigurationStatus).Status