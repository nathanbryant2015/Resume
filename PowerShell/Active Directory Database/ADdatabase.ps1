#1.  Create an Active Directory organizational unit (OU) named “finance.”

New-ADOrganizationalUnit -Name Finance –Path 'DC=domain,DC=com' -ProtectedFromAccidentalDeletion $False

#2.  Import the financePersonnel.csv file (found in the “Requirements2” directory) into your Active Directory domain and directly into the finance OU. Be sure to include the following properties:
#•  First Name
#•  Last Name
#•  Display Name (First Name + Last Name, including a space between)
#•  Postal Code
#• Office Phone
#• Mobile Phone

# use $PSScriptRoot instead of absolute (full) path to file so that the script will work on other systems and locations
$NewAD = Import-CSV $PSScriptRoot\financePersonnel.csv
$Path = "OU=Finance,DC=domain,DC=com"

foreach ($ADuser in $NewAD)
{

$First = $ADUser.First_Name
$Last = $ADUser.Last_Name
$Name = $First + " " + $Last
$SamName = $ADUser.samAccount
$Postal = $ADUser.PostalCode
$Office = $ADUser.OfficePhone
$Mobile = $ADUser.MobilePhone
$Server = "domain.com"

New-ADUser -GivenName $First -Surname $Last -Name $Name -SamAccountName $SamName -DisplayName $Name -PostalCode $Postal -MobilePhone $Mobile -OfficePhone $Office -Path $Path

}

#3.  Create a new database on the ADServer SQL server instance called “ClientDB.”

#Creating Object for the local SQL connection
Import-Module -Name sqlps -DisableNameChecking -Force
$Servername = ".\ADServer"
$Srv = New-Object -TypeName Microsoft.SqlServer.Management.Smo.Server -ArgumentList $Servername
$databasename = "ClientDB"
$db = New-Object -TypeName Microsoft.SqlServer.Management.Smo.Database -ArgumentList $Servername, $databasename
$db.Create()

#4.  Create a new table and name it “Client_A_Contacts.” Add this table to your new database.
Invoke-Sqlcmd -ServerInstance .\ADServer -Database ClientDB -InputFile $PSScriptRoot\NewClientData.sql

$table= 'dbo.Client_A_Contacts'
$db = '\ADServer'

#5.  Insert the data from the attached “NewClientData.csv” file (found in the “Requirements2” folder) into the table created in part B4.

Try
{
    Import-Csv $PSScriptRoot\NewClientData.csv | ForEach-Object {Invoke-Sqlcmd `
    -Database $databasename -ServerInstance $Servername -Query "insert into $table (first_name,Last_name,city,county,zip,officePhone,mobilePhone) VALUES `
    ('$($_.first_name)','$($_.last_name)','$($_.city)','$($_.county)','$($_.zip)','$($_.officePhone)','$($_.mobilePhone)')"}
}
Catch [System.OutOfMemoryException] 
{
	Write-Host "A system out of memeory exception has occured."
}