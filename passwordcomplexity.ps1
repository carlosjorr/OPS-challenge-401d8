# Import the required module
Import-Module SecurityPolicyDsc

# Define the configuration
configuration PasswordComplexityConfiguration {
    param (
        [Parameter(Mandatory = $true)]
        [ValidateSet("Enabled", "Disabled")]
        [String]$PasswordComplexity
    )

    # Configuration block
    node localhost {
        SecurityPolicy 'SetPasswordComplexity' {
            Name = 'Password must meet complexity requirements'
            State = $PasswordComplexity
        }
    }
}

# Set the desired password complexity state
$passwordComplexity = "Enabled"

# Invoke the configuration
PasswordComplexityConfiguration -PasswordComplexity $passwordComplexity

# Start the configuration
Start-DscConfiguration -Path .\PasswordComplexityConfiguration -Force -Wait

# Check the configuration status
(Get-DscConfigurationStatus).Status
